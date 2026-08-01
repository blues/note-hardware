#!/usr/bin/env python3
"""Regression tests for the gerber gate's ability to FAIL.

Every check here exists because the gate once passed the situation it describes.
The gate's job is not to measure a difference, it is to exit non-zero when the
port and the shipped fab package disagree - so each test introduces a specific
defect and asserts the gate catches it.

Usage:  .venv/bin/python test_gerber_diff.py [--board scoop]
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PY = str(HERE / ".venv" / "bin" / "python")
KICAD_CLI = os.environ.get(
    "KICAD_CLI",
    str(Path.home() / "Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"))


def export_gerbers(pcb, out):
    subprocess.run([KICAD_CLI, "pcb", "export", "gerbers", "--no-x2",
                    "--subtract-soldermask", "-o", str(out) + "/", str(pcb)],
                   capture_output=True, check=True)


def run_gate(board, cfg_gerbers, kicad_dir):
    with tempfile.TemporaryDirectory() as td:
        cfgp = Path(td) / "b.yaml"
        cfgp.write_text(yaml.safe_dump({"boards": {board: {"gerbers": cfg_gerbers}}}))
        r = subprocess.run([PY, HERE / "gerber_diff.py", "--board", board,
                            "--config", str(cfgp), "--kicad-dir", str(kicad_dir),
                            "--repo", str(REPO), "--out", td + "/out"],
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr


def blank_layer(path):
    """Strip every drawing command, leaving a structurally valid but empty file."""
    text = Path(path).read_text(errors="replace")
    kept = [ln for ln in text.splitlines()
            if not re.match(r"^[XYIJ][-\d]", ln) and not re.match(r"^G0[123]", ln)]
    Path(path).write_text("\n".join(kept) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board", default="scoop")
    args = ap.parse_args()

    cfg = yaml.safe_load((HERE / "boards.yaml").read_text())["boards"][args.board]
    gcfg = cfg["gerbers"]
    failures = []

    with tempfile.TemporaryDirectory() as work:
        base = Path(work) / "clean"
        base.mkdir()
        export_gerbers(REPO / cfg["kicad"]["pcb"], base)

        # 1. the unmodified port must pass, or the rest proves nothing
        rc, out = run_gate(args.board, gcfg, base)
        print(f"[1] unmodified port                  -> rc={rc}")
        if rc != 0:
            failures.append("the unmodified port does not pass; "
                            "the negative tests below are meaningless\n" + out)

        # Which layers actually carry content? A layer that is empty on both
        # sides to begin with (Scoop has no bottom-side paste, and the shipped
        # .GBP holds only its caption glyphs) cannot be emptied any further, so
        # blanking it is a no-op and proves nothing.
        inked = {}
        for ln in out.splitlines():
            m = re.match(r"\s+(\w+): rendered.*ink KiCad ([\d.]+)", ln)
            if m:
                inked[m.group(1)] = float(m.group(2))
        sparse = [l for l, v in inked.items()
                  if 0 < v < 0.10 and ("Paste" in l or "Mask" in l)]
        print(f"    layers with sparse content: {sparse or 'none'}")

        # 2. an entirely absent sparse layer must FAIL.
        #    This is the case that used to pass: the layer render included the
        #    board outline, so ink never reached zero, and an absolute mean
        #    difference over the whole canvas stayed under the threshold because
        #    paste covers ~1% of the board.
        for layer in sparse:
            if layer not in gcfg["layers"]:
                continue
            trial = Path(work) / f"missing-{layer}"
            subprocess.run(["cp", "-r", str(base), str(trial)], check=True)
            import glob
            hits = glob.glob(str(trial / gcfg["layers"][layer]["kicad"]))
            if not hits:
                failures.append(f"could not find the {layer} gerber to blank")
                continue
            blank_layer(hits[0])
            rc, out = run_gate(args.board, gcfg, trial)
            caught = "draws NOTHING" in out or rc != 0
            print(f"[2] {layer} emptied{'':<{max(0, 21 - len(layer))}}-> rc={rc} {'CAUGHT' if caught else 'MISSED'}")
            if not caught:
                failures.append(f"an entirely missing {layer} layer still passed:\n{out}")

        # 3. a shifted layer must FAIL: copy another layer over the top one so
        #    the copper is real but wrong.
        if "F_Cu" in gcfg["layers"] and "B_Cu" in gcfg["layers"]:
            import glob
            trial = Path(work) / "swapped"
            subprocess.run(["cp", "-r", str(base), str(trial)], check=True)
            f = glob.glob(str(trial / gcfg["layers"]["F_Cu"]["kicad"]))
            b = glob.glob(str(trial / gcfg["layers"]["B_Cu"]["kicad"]))
            if f and b:
                Path(f[0]).write_text(Path(b[0]).read_text(errors="replace"))
                rc, out = run_gate(args.board, gcfg, trial)
                print(f"[3] F_Cu replaced by B_Cu           -> rc={rc} "
                      f"{'CAUGHT' if rc != 0 else 'MISSED'}")
                if rc == 0:
                    failures.append(f"wrong copper on F_Cu still passed:\n{out}")

    print()
    if failures:
        print(f"RESULT: FAIL - {len(failures)} regression(s)")
        for f in failures:
            print("  - " + f.split("\n")[0])
        return 1
    print("RESULT: PASS - the gate fails on every defect it is supposed to catch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
