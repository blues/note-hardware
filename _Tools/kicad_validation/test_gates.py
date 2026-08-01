#!/usr/bin/env python3
"""Regression tests for the BOM and placement gates' ability to FAIL.

Companion to test_gerber_diff.py, written for the same reason: a gate that
measures a defect but does not act on it is not a gate, and a suite that infers
the result from printed text silently ignores failure kinds it never enumerated.
Both gates now emit a structured --json summary, so each test here injects one
specific defect and asserts the gate reports the expected *kind* for the
expected refdes.

Usage:  .venv/bin/python test_gates.py [--board mojo]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PY = str(HERE / ".venv" / "bin" / "python")
KICAD_CLI = os.environ.get(
    "KICAD_CLI",
    str(Path.home() / "Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"))


def export_bom(sch, mpn_field, out):
    subprocess.run([KICAD_CLI, "sch", "export", "bom", "-o", str(out),
                    "--fields", f"Reference,Value,{mpn_field},${{DNP}}",
                    "--labels", "Reference,Value,MPN,DNP", str(sch)],
                   capture_output=True, check=True)


def run_bom(board, csv_path):
    with tempfile.TemporaryDirectory() as td:
        jp = Path(td) / "r.json"
        r = subprocess.run([PY, HERE / "bom_compare.py", "--kicad", str(csv_path),
                            "--board", board, "--config", HERE / "boards.yaml",
                            "--json", str(jp)], capture_output=True, text=True)
        problems = json.loads(jp.read_text())["problems"] if jp.exists() else []
        return r.returncode, problems


def run_pnp(board, pcb, baseline):
    with tempfile.TemporaryDirectory() as td:
        jp = Path(td) / "r.json"
        r = subprocess.run([PY, HERE / "pnp_compare.py", "--kicad", str(pcb),
                            "--board", board, "--config", HERE / "boards.yaml",
                            "--repo", str(REPO), "--baseline", str(baseline),
                            "--json", str(jp)], capture_output=True, text=True)
        problems = json.loads(jp.read_text())["problems"] if jp.exists() else []
        return r.returncode, problems


def kinds_for(problems, ref=None):
    return sorted({p["kind"] for p in problems
                   if ref is None or p.get("ref") == ref})


def footprint_blocks(text):
    """Yield (start, end, refdes) for each footprint in a .kicad_pcb."""
    for m in re.finditer(r"\n[\t ]+\(footprint ", text):
        depth, j = 0, text.index("(", m.start())
        start = j
        while j < len(text):
            c = text[j]
            if c == '"':
                j = text.find('"', j + 1)
                if j < 0:
                    return
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        blk = text[start:j + 1]
        rm = (re.search(r'\(property "Reference" "([^"]+)"', blk)
              or re.search(r'\(fp_text reference "([^"]+)"', blk))
        if rm:
            yield start, j + 1, rm.group(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board", default="mojo")
    args = ap.parse_args()
    cfg = yaml.safe_load((HERE / "boards.yaml").read_text())["boards"][args.board]
    failures = []

    def check(label, rc, problems, want_kind, want_ref):
        got = kinds_for(problems, want_ref)
        ok = rc != 0 and want_kind in got
        print(f"  [{'OK  ' if ok else 'MISS'}] {label:38s} rc={rc} "
              f"{want_ref}: {got or 'nothing reported'}")
        if not ok:
            failures.append(f"{label}: expected {want_kind} on {want_ref}, got {got}")

    # ---------------- BOM gate ----------------
    if "bom" in cfg:
        with tempfile.TemporaryDirectory() as td:
            base = Path(td) / "bom.csv"
            export_bom(REPO / cfg["kicad"]["sch"],
                       cfg["bom"].get("kicad_mpn_field", "MPN"), base)
            rows = base.read_text(encoding="utf-8-sig").splitlines()
            hdr, body = rows[0], rows[1:]
            rc, probs = run_bom(args.board, base)
            print(f"  [{'OK  ' if rc == 0 else 'MISS'}] unmodified BOM"
                  f"{'':<24}rc={rc}")
            if rc != 0:
                failures.append("the unmodified BOM does not pass; "
                                f"the rest proves nothing: {probs[:2]}")

            # Pick a refdes carrying an MPN on BOTH sides. The gate only compares
            # MPNs where the shipped BOM supplies one, so choosing a part the
            # shipped BOM leaves blank would make the MPN cases untestable and
            # look like a gate failure - which is exactly what it did at first.
            import bom_compare as _bc
            shipped = _bc.load_shipped(cfg["bom"])
            def _row_ref(l):
                return l.split('","')[0].strip('"')
            target = next(
                (i for i, l in enumerate(body)
                 if len(l.split('","')) > 2 and l.split('","')[2].strip('"')
                 and shipped.get(_row_ref(l), {}).get("mpn")),
                None)
            if target is None:
                print("  (no refdes has an MPN on both sides; skipping MPN cases)")
                target = 0
                mpn_testable = False
            else:
                mpn_testable = True
            ref = _row_ref(body[target])

            def write(mod_body, name):
                p = Path(td) / name
                p.write_text("\n".join([hdr] + mod_body) + "\n")
                return p

            # a part dropped from the port
            check("refdes removed from KiCad",
                  *run_bom(args.board, write(body[:target] + body[target + 1:], "a.csv")),
                  "only-in-shipped", ref)
            # a part the shipped BOM does not have
            extra = body[target].replace(f'"{ref}"', '"ZZ99"', 1)
            check("extra refdes in KiCad",
                  *run_bom(args.board, write(body + [extra], "b.csv")),
                  "only-in-kicad", "ZZ99")
            f = body[target].split('","')
            if mpn_testable:
                # MPN blanked
                blanked = '","'.join(f[:2] + [""] + f[3:])
                check("MPN blanked",
                      *run_bom(args.board, write(body[:target] + [blanked] + body[target + 1:], "c.csv")),
                      "mpn-missing", ref)
                # MPN wrong
                wrong = '","'.join(f[:2] + ["WRONG-MPN-0000"] + f[3:])
                check("MPN replaced",
                      *run_bom(args.board, write(body[:target] + [wrong] + body[target + 1:], "d.csv")),
                      "mpn-mismatch", ref)
            # value wrong (only meaningful where the board checks values)
            if cfg["bom"].get("check_value", True):
                badval = '","'.join([f[0], "NOT-A-REAL-VALUE"] + f[2:])
                check("value replaced",
                      *run_bom(args.board, write(body[:target] + [badval] + body[target + 1:], "e.csv")),
                      "value-mismatch", ref)
    else:
        print("  (board has no BOM gate configured)")

    # ---------------- placement gate ----------------
    if "pnp" in cfg and cfg["kicad"].get("pcb"):
        pcb_src = REPO / cfg["kicad"]["pcb"]
        baseline = pcb_src.parent / "validation" / "placement-baseline.yaml"
        text = pcb_src.read_text(errors="replace")
        blocks = [b for b in footprint_blocks(text) if not b[2].startswith("#")]
        # a small two-pad part, so a 1 mm move cannot be mistaken for an origin offset
        pick = next((b for b in blocks if re.match(r"^[RC]\d+$", b[2])), blocks[0])
        s, e, ref = pick
        blk = text[s:e]

        with tempfile.TemporaryDirectory() as td:
            def variant(new_blk, name, drop=False):
                p = Path(td) / name
                p.write_text(text[:s] + ("" if drop else new_blk) + text[e:])
                return p

            rc, probs = run_pnp(args.board, pcb_src, baseline)
            print(f"  [{'OK  ' if rc == 0 else 'MISS'}] unmodified board"
                  f"{'':<22}rc={rc}")
            if rc != 0:
                failures.append(f"the unmodified board does not pass: {probs[:2]}")

            at = re.search(r'\(at ([-\d.]+) ([-\d.]+)(?: ([-\d.]+))?\)', blk)
            x, y, rot = float(at.group(1)), float(at.group(2)), float(at.group(3) or 0)
            moved = blk[:at.start()] + f"(at {x + 1.0:.4f} {y:.4f} {rot:g})" + blk[at.end():]
            check("footprint moved 1 mm",
                  *run_pnp(args.board, variant(moved, "moved.kicad_pcb"), baseline),
                  "displaced", ref)

            turned = blk[:at.start()] + f"(at {x:.4f} {y:.4f} {(rot + 90) % 360:g})" + blk[at.end():]
            check("footprint rotated 90 deg",
                  *run_pnp(args.board, variant(turned, "rot.kicad_pcb"), baseline),
                  "rotation", ref)

            lay = re.search(r'\(layer "([FB])\.Cu"\)', blk)
            if lay:
                other = "B" if lay.group(1) == "F" else "F"
                flipped = blk[:lay.start()] + f'(layer "{other}.Cu")' + blk[lay.end():]
                check("footprint moved to the other side",
                      *run_pnp(args.board, variant(flipped, "side.kicad_pcb"), baseline),
                      "side", ref)

            check("footprint deleted",
                  *run_pnp(args.board, variant("", "gone.kicad_pcb", drop=True), baseline),
                  "missing-refdes", ref)
    else:
        print("  (board has no placement gate configured)")

    print()
    if failures:
        print(f"RESULT: FAIL - {len(failures)} regression(s)")
        for f in failures:
            print("  - " + f)
        return 1
    print("RESULT: PASS - both gates fail on every defect they are supposed to catch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
