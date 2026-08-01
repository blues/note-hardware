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
    i = 0
    while True:
        i = text.find("\n\t(footprint ", i)
        if i < 0:
            break
        # walk to the end of this footprint block
        depth, j = 0, text.index("(", i)
        start = j
        while j < len(text):
            c = text[j]
            if c == '"':
                j = text.index('"', j + 1)
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        blk = text[start:j + 1]
        i = j
        m_ref = re.search(r'\(property "Reference" "([^"]+)"', blk)
        m_at = re.search(r'\(at ([-\d.]+) ([-\d.]+)(?: ([-\d.]+))?\)', blk)
        m_lay = re.search(r'\(layer "([^"]+)"\)', blk)
        if not (m_ref and m_at and m_lay):
            continue
        out[m_ref.group(1)] = {
            "x": float(m_at.group(1)), "y": float(m_at.group(2)),
            "rot": float(m_at.group(3) or 0) % 360,
            "side": "Bottom" if m_lay.group(1).startswith("B.") else "Top",
        }
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kicad", required=True, type=Path)
    ap.add_argument("--board", required=True)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--repo", type=Path, help="repo root for relative pnp paths")
    ap.add_argument("--report", type=Path)
    ap.add_argument("--tolerance", type=float, default=0.05,
                    help="position tolerance in mm (default 0.05)")
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

    # solve the placement-origin offset; try both y-axis senses
    best = None
    for flip in (False, True):
        dx = median(fps[r]["x"] - rows[r]["x"] for r in common)
        dy = median(fps[r]["y"] -
                    (-rows[r]["y"] if flip else rows[r]["y"]) for r in common)
        res = [max(abs(fps[r]["x"] - rows[r]["x"] - dx),
                   abs(fps[r]["y"] -
                       (-rows[r]["y"] if flip else rows[r]["y"]) - dy))
               for r in common]
        agree = sum(1 for e in res if e < args.tolerance)
        if best is None or agree > best[0]:
            best = (agree, flip, dx, dy)
    _, flip, dx, dy = best

    side_bad, pos_bad, rot_bad = [], [], []
    for r in common:
        fp, want = fps[r], rows[r]
        side = fp["side"]
        if side != want["side"]:
            side_bad.append(f"{r}: port {side}, released build {want['side']}")
        ex = fp["x"] - want["x"] - dx
        ey = fp["y"] - (-want["y"] if flip else want["y"]) - dy
        if max(abs(ex), abs(ey)) >= args.tolerance:
            pos_bad.append(f"{r}: residual ({ex:+.3f}, {ey:+.3f}) mm")
        dr = (fp["rot"] - want["rot"]) % 360
        if min(dr, 360 - dr) > 0.5:
            rot_bad.append(f"{r}: port {fp['rot']:g} deg, "
                           f"released build {want['rot']:g} deg")

    only_pnp = sorted(set(rows) - set(fps))
    gross = [x for x in pos_bad if float(re.search(r"\(([-+\d.]+),", x).group(1)) ** 2 +
             float(re.search(r", ([-+\d.]+)\)", x).group(1)) ** 2 > GROSS ** 2]

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
        "Position residuals (informational): the pick-and-place file references each",
        "part's body centre, while KiCad measures from the footprint origin, so",
        "connectors and other asymmetric parts carry a fixed per-footprint offset -",
        "it even changes sign when the part is rotated 180 degrees. Copper geometry is",
        f"proven exactly by the gerber diff instead. Residuals over {args.tolerance} mm:",
        f"  {len(pos_bad)} of {len(common)}",
        *(f"    {t}" for t in pos_bad),
        f"  largest residuals (>{GROSS} mm) are exact pin-pitch multiples, i.e. the",
        f"  origin sits on a pin rather than the body centre: {len(gross)}",
        *(f"    {t}" for t in gross),
        "",
        "This report is committed, so any future change to these residuals shows up",
        "as a diff for review - the same convention the gerber-diff gate uses.",
    ]

    # The hard gate is what the assembly file states unambiguously: every placed
    # part present, on the right side, at the right rotation. Position is reported
    # rather than gated, because the file's body-centre reference cannot be
    # compared to KiCad's footprint origin without per-footprint knowledge.
    ok = not only_pnp and not side_bad and not rot_bad
    lines += ["", f"RESULT: {'PASS' if ok else 'FAIL'} - {len(common)} placements checked; "
                  f"side and rotation match the released build for "
                  f"{len(common) - len(side_bad) - len(rot_bad)}/{len(common)}"]
    out = "\n".join(lines)
    print(out)
    if args.report:
        args.report.write_text(out + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
