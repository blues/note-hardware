#!/usr/bin/env python3
"""Compare a KiCad port's component placement against the shipped pick-and-place file.

Why this gate exists
--------------------
The other gates prove a port is faithful to the *design sources* it was
converted from. The pick-and-place file is different: it is generated from the
**released** design and describes the boards that were actually built, refdes by
refdes, with side, position and rotation. Comparing against it therefore tests
something no other gate does - especially for the Notecarrier-X/-XS/-XM ports,
which were made from the closest available design-house sources rather than the
exact released snapshot.

Two shipped formats are understood:

* the design house's fixed-width ``.pnp``
  (``RefDes  BL Part Number  Value  Footprint  Layer  XPos  YPos  Rot``), and
* Altium's "Pick and Place Locations" text export (``Designator ... Layer ...
  Center-X ... Center-Y ... Rotation``), in mm or mil.

The placement origin used by the assembly file is not KiCad's board origin, so
the comparison solves the constant offset (and a possible y-axis flip) from the
median over all matched parts, then reports the residuals. Rotation and side are
compared directly.

Usage:
  pnp_compare.py --kicad <board.kicad_pcb> --board <name> --config boards.yaml
                 [--report out.txt] [--tolerance 0.05]
"""

import argparse
import math
import re
import sys
from pathlib import Path
from statistics import median

import yaml

MIL = 0.0254
# residuals above this are called out in the report for review
GROSS = 5.0


def read_pnp_fixed(path):
    """Design-house fixed-width .pnp."""
    rows = {}
    for line in Path(path).read_text(errors="replace").splitlines():
        m = re.match(r"^(\S+)\s+(\S+)\s+(.+?)\s{2,}(\S+)\s+(Top|Bottom)\s+"
                     r"([-\d.]+)\s+([-\d.]+)\s+([-\d.]+)\s*$", line)
        if not m:
            continue
        ref = m.group(1)
        # parts the assembler places by hand are bracketed, e.g. !J3! - they are
        # fitted, just not auto-placed, so strip the markers and keep them
        rows[ref.strip("!")] = {
            "side": m.group(5), "x": float(m.group(6)),
            "y": float(m.group(7)), "rot": float(m.group(8)) % 360,
            "hand_placed": ref.startswith("!"),
        }
    return rows


def read_pnp_altium(path):
    """Altium 'Pick and Place Locations' export (mm or mil)."""
    text = Path(path).read_text(errors="replace").splitlines()
    unit = MIL if any("Units used: mil" in ln for ln in text[:40]) else 1.0
    hdr_i = next((i for i, ln in enumerate(text)
                  if ln.startswith("Designator") and "Center-X" in ln), None)
    if hdr_i is None:
        return {}
    hdr = text[hdr_i]
    # fixed-width columns: take each field's start from the header
    names = ["Designator", "Comment", "Layer", "Footprint",
             "Center-X", "Center-Y", "Rotation"]
    starts = [hdr.find(n) for n in names]
    if any(i < 0 for i in starts):
        return {}
    # the Rotation column ends where the next header label begins, otherwise the
    # trailing Description text is swept into the rotation value
    nxt = hdr.find("Description", starts[-1])
    starts.append(nxt if nxt > 0 else len(hdr) + 400)
    rows = {}
    for ln in text[hdr_i + 1:]:
        if not ln.strip():
            continue
        try:
            f = [ln[starts[i]:starts[i + 1]].strip() for i in range(len(names))]
            ref, _, layer, _, cx, cy, rot = f
            if not ref or not cx:
                continue
            rows[ref] = {
                "side": "Bottom" if layer.lower().startswith("bottom") else "Top",
                "x": float(cx) * unit, "y": float(cy) * unit,
                "rot": float(rot) % 360, "hand_placed": False,
            }
        except (ValueError, IndexError):
            continue
    return rows


def read_pnp_csv(path):
    """Altium CSV export: quoted, column order varies, names carry the unit."""
    import csv
    lines = Path(path).read_text(errors="replace").splitlines()
    hdr_i = next((i for i, ln in enumerate(lines)
                  if "Designator" in ln and "Center-X" in ln), None)
    if hdr_i is None:
        return {}
    rows = {}
    for rec in csv.DictReader(lines[hdr_i:]):
        keys = {k.split("(")[0].strip(): k for k in rec if k}
        try:
            ref = rec[keys["Designator"]].strip()
            layer = rec[keys["Layer"]].strip()
            unit = MIL if "mil" in keys.get("Center-X", "").lower() else 1.0
            rows[ref] = {
                "side": "Bottom" if layer.lower().startswith("bottom") else "Top",
                "x": float(rec[keys["Center-X"]]) * unit,
                "y": float(rec[keys["Center-Y"]]) * unit,
                "rot": float(rec[keys["Rotation"]]) % 360, "hand_placed": False,
            }
        except (KeyError, ValueError, TypeError):
            continue
    return rows


def read_pnp(path):
    head = Path(path).read_text(errors="replace")[:600]
    if '"Designator"' in head or (path.suffix.lower() == ".csv" and "Designator" in head):
        return read_pnp_csv(path)
    if "Pick and Place Locations" in head:
        return read_pnp_altium(path)
    return read_pnp_fixed(path)


def read_board_footprints(path):
    """Footprint reference -> side/position/rotation, read straight from the
    .kicad_pcb. Parsing the file rather than going through pcbnew keeps this
    gate runnable in the harness venv, with no KiCad install needed."""
    text = Path(path).read_text(errors="replace")
    out = {}
    # KiCad 9 indents footprints with a tab, KiCad 7 with two spaces
    starts = [m.start() for m in re.finditer(r"\n[\t ]+\(footprint ", text)]
    for i in starts:
        # walk to the end of this footprint block
        depth, j = 0, text.index("(", i)
        start = j
        while j < len(text):
            c = text[j]
            if c == '"':
                k = text.find('"', j + 1)
                if k < 0:
                    break
                j = k
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        blk = text[start:j + 1]
        # KiCad 9 stores the reference as a property, KiCad 7 as fp_text
        m_ref = (re.search(r'\(property "Reference" "([^"]+)"', blk)
                 or re.search(r'\(fp_text reference "([^"]+)"', blk))
        m_at = re.search(r'\(at ([-\d.]+) ([-\d.]+)(?: ([-\d.]+))?\)', blk)
        m_lay = re.search(r'\(layer "([^"]+)"\)', blk)
        if not (m_ref and m_at and m_lay):
            continue
        m_fp = re.search(r'\(footprint "([^"]+)"', blk)
        # Pad extent, measured in the footprint's own frame. This bounds how far
        # the footprint origin can legitimately sit from the body centre that a
        # pick-and-place file reports: the origin is a point on the part, so it
        # cannot be further from the centre than the part's own half-size.
        xs, ys = [], []
        for px, py, pw, ph in re.findall(
                r'\(pad\s+"[^"]*"\s+\S+\s+\S+\s*\(at\s+([-\d.]+)\s+([-\d.]+)'
                r'(?:\s+[-\d.]+)?\)\s*\(size\s+([-\d.]+)\s+([-\d.]+)\)', blk):
            px, py, pw, ph = float(px), float(py), float(pw), float(ph)
            xs += [px - pw / 2, px + pw / 2]
            ys += [py - ph / 2, py + ph / 2]
        out[m_ref.group(1)] = {
            "x": float(m_at.group(1)), "y": float(m_at.group(2)),
            "rot": float(m_at.group(3) or 0) % 360,
            "side": "Bottom" if m_lay.group(1).startswith("B.") else "Top",
            "fp": m_fp.group(1) if m_fp else "?",
            # Centre of the pad bounding box, in the footprint's own frame. A
            # pick-and-place file reports the body centre while KiCad measures
            # from the footprint origin, so this is the offset between them -
            # which makes each part's expected residual predictable instead of
            # merely "some fixed per-footprint value we cannot check".
            "cx": (min(xs) + max(xs)) / 2 if xs else None,
            "cy": (min(ys) + max(ys)) / 2 if ys else None,
        }
    return out


def predict(fp, rot_sign=1):
    """Where the body centre sits relative to the footprint origin, in board
    coordinates, for a footprint placed at its recorded rotation."""
    if fp["cx"] is None:
        return None
    th = math.radians(fp["rot"] * rot_sign)
    cx, cy = fp["cx"], fp["cy"]
    return (cx * math.cos(th) - cy * math.sin(th),
            cx * math.sin(th) + cy * math.cos(th))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kicad", required=True, type=Path)
    ap.add_argument("--board", required=True)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--repo", type=Path, help="repo root for relative pnp paths")
    ap.add_argument("--report", type=Path)
    ap.add_argument("--json", type=Path,
                    help="write a machine-readable result summary here")
    ap.add_argument("--tolerance", type=float, default=0.05,
                    help="position tolerance in mm (default 0.05)")
    ap.add_argument("--position-tolerance", type=float, default=0.3,
                    help="how far a part may sit from its predicted body "
                         "centre before it counts as displaced (default 0.3mm; "
                         "the pad bounding box only approximates the body)")
    ap.add_argument("--baseline", type=Path,
                    help="committed YAML of reviewed residuals the "
                         "body-centre prediction cannot explain")
    ap.add_argument("--update-baseline", action="store_true",
                    help="rewrite the baseline file (review every entry)")
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())["boards"][args.board]
    if "pnp" not in cfg:
        print("no pnp config for this board", file=sys.stderr)
        return 2
    pnp_path = Path(cfg["pnp"]["path"])
    if not pnp_path.is_absolute():
        root = args.repo or args.config.resolve().parent.parent.parent
        pnp_path = root / pnp_path
    skip = re.compile(cfg["pnp"].get("skip_refdes", r"^$"))

    fps = read_board_footprints(args.kicad)
    rows = {r: v for r, v in read_pnp(pnp_path).items() if not skip.match(r)}
    if not rows:
        print(f"could not parse any placements from {pnp_path}", file=sys.stderr)
        return 1

    common = sorted(set(rows) & set(fps))
    if not common:
        print("no refdes in common", file=sys.stderr)
        return 1

    # Solve the placement-origin offset. Each part's expected body-centre offset
    # is predicted from its own pad geometry, so what is left over is real
    # displacement rather than an unexplained per-footprint constant.
    best = None
    for flip in (False, True):
        for sign in (1, -1):
          for psign in (1, -1):
            pred = {r: tuple(psign * v for v in (predict(fps[r], sign) or (0.0, 0.0)))
                    for r in common}
            dx = median(fps[r]["x"] - rows[r]["x"] - pred[r][0] for r in common)
            dy = median(fps[r]["y"] - (-rows[r]["y"] if flip else rows[r]["y"])
                        - pred[r][1] for r in common)
            res = [math.hypot(
                fps[r]["x"] - rows[r]["x"] - pred[r][0] - dx,
                fps[r]["y"] - (-rows[r]["y"] if flip else rows[r]["y"])
                - pred[r][1] - dy) for r in common]
            agree = sum(1 for e in res if e < args.tolerance)
            if best is None or agree > best[0]:
                best = (agree, flip, sign, psign, dx, dy)
    _, flip, rot_sign, pred_sign, dx, dy = best

    baseline_path = Path(args.baseline) if args.baseline else None
    baseline = {}
    if baseline_path and baseline_path.exists():
        baseline = yaml.safe_load(baseline_path.read_text()) or {}

    structured = []

    def fail(kind, ref, message):
        """Record a hard failure in machine-readable form; see bom_compare for
        why callers must not have to parse the prose report."""
        structured.append({"kind": kind, "ref": ref, "message": message})

    side_bad, rot_bad = [], []
    explained, accepted, unexplained, measured = [], [], [], {}
    for r in common:
        fp, want = fps[r], rows[r]
        if fp["side"] != want["side"]:
            msg = f"{r}: port {fp['side']}, released build {want['side']}"
            side_bad.append(msg)
            fail("side", r, msg)
        px, py = (lambda v: (pred_sign * v[0], pred_sign * v[1]))(
            predict(fp, rot_sign) or (0.0, 0.0))
        ex = fp["x"] - want["x"] - px - dx
        ey = fp["y"] - (-want["y"] if flip else want["y"]) - py - dy
        err = math.hypot(ex, ey)
        measured[r] = [round(ex, 3), round(ey, 3)]
        if err < args.position_tolerance:
            explained.append(r)
        elif r in baseline and math.hypot(ex - baseline[r][0],
                                          ey - baseline[r][1]) < args.position_tolerance:
            # A reviewed, committed exception. It is frozen, so any future drift
            # in this part's placement fails the gate.
            accepted.append(f"{r}: ({ex:+.3f}, {ey:+.3f}) mm, matches baseline")
        else:
            was = (f", baseline says ({baseline[r][0]:+.3f}, {baseline[r][1]:+.3f})"
                   if r in baseline else ", not in the baseline")
            msg = (f"{r}: ({ex:+.3f}, {ey:+.3f}) mm from the body "
                   f"centre predicted by {fp['fp']}{was}")
            unexplained.append(msg)
            fail("displaced", r, msg)
        dr = (fp["rot"] - want["rot"]) % 360
        if min(dr, 360 - dr) > 0.5:
            msg = (f"{r}: port {fp['rot']:g} deg, "
                   f"released build {want['rot']:g} deg")
            rot_bad.append(msg)
            fail("rotation", r, msg)

    only_pnp = sorted(set(rows) - set(fps))
    for r in only_pnp:
        fail("missing-refdes", r,
             f"{r} is placed in the released build but absent from the port")

    if args.update_baseline and baseline_path:
        keep = {r: measured[r] for r in common
                if math.hypot(*measured[r]) >= args.position_tolerance}
        baseline_path.write_text(
            "# Placement residuals that the body-centre prediction does not\n"
            "# explain, frozen after review. Regenerate only with\n"
            "# --update-baseline, and re-review every entry when you do.\n"
            + yaml.safe_dump(keep, sort_keys=True))
        print(f"wrote {len(keep)} baseline entries to {baseline_path}")

    lines = [
        "Placement comparison vs the shipped pick-and-place file",
        f"  board:      {args.board}",
        f"  pnp file:   {pnp_path.name}",
        f"  placements: {len(rows)} in the file, {len(common)} matched in the port",
        f"  fitted origin offset ({dx:.3f}, {dy:.3f}) mm, y-flip={flip}",
        "",
        "Hard checks (unambiguous in the assembly file):",
        f"  refdes in the file but missing from the port: {len(only_pnp)}"
        + (f" -> {', '.join(only_pnp)}" if only_pnp else ""),
        f"  board-side mismatches: {len(side_bad)}",
        *(f"    {t}" for t in side_bad),
        f"  rotation mismatches:   {len(rot_bad)}",
        *(f"    {t}" for t in rot_bad),
        "",
        "",
        "Position (gated). Each part's expected residual is predicted from its own",
        "pad bounding box, because the assembly file references the body centre",
        "while KiCad measures from the footprint origin. What is left after that",
        "prediction is real displacement, not a per-footprint constant.",
        f"  explained by the body-centre prediction: {len(explained)} of {len(common)}",
        f"  accepted against the committed baseline:  {len(accepted)}",
        *(f"    {t}" for t in accepted),
        f"  UNEXPLAINED:                              {len(unexplained)}",
        *(f"    {t}" for t in unexplained),
        "",
        "This report is committed, so any future change to these residuals shows up",
        "as a diff for review - the same convention the gerber-diff gate uses.",
    ]

    # Every placed part present, on the right side, at the right rotation, and
    # not displaced beyond what a footprint-origin difference can explain.
    ok = not only_pnp and not side_bad and not rot_bad and not unexplained
    lines += ["", f"RESULT: {'PASS' if ok else 'FAIL'} - {len(common)} placements checked; "
                  f"side and rotation match the released build for "
                  f"{len(common) - len(side_bad) - len(rot_bad)}/{len(common)}; "
                  f"{len(unexplained)} unexplained displacement(s)"]
    out = "\n".join(lines)
    print(out)
    if args.report:
        args.report.write_text(out + "\n")
    if args.json:
        import json
        args.json.write_text(json.dumps({
            "board": args.board,
            "result": "PASS" if ok else "FAIL",
            "problems": structured,
            "summary": {"placements": len(rows), "matched": len(common),
                        "explained": len(explained), "accepted": len(accepted)},
            "measured": measured,
        }, indent=1, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
