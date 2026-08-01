#!/usr/bin/env python3
"""Run the full validation battery for one ported board.

Gates (hard — any FAIL means the port must be fixed or dropped, per the NO-GO
policy). A gate that cannot run is NOT a pass: it fails unless the board records
why under `skip_gates.<GATE>` in boards.yaml, which keeps the justification
machine-readable and reviewable instead of relying on someone remembering a
--skip flag. --skip is likewise refused for any gate with no declared reason.

  1. ERC          kicad-cli sch erc --exit-code-violations
  2. DRC          kicad-cli pcb drc --exit-code-violations
  3. BOM          bom_compare.py vs shipped spreadsheet
  4. NETLIST      netlist_compare.py vs shipped ODB++ (when the board has one)
  5. GERBER-DIFF  gerber_diff.py vs shipped fab package (human reviews PNGs)
  5b. PNP         pnp_compare.py vs the shipped pick-and-place file - the only
                  gate that checks the port against the *released build* rather
                  than against the design sources it was converted from
  6. KICANVAS     kicanvas_check/render_check.py on every sch sheet + pcb
  7. RAG          extract_for_rag/extract.py parses the new sheets

Reports and artifacts land in <product>/KiCad_format/validation/.

Usage: run_all.py <board-name> [--repo <path>] [--skip GATE ...]
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PY = str(HERE / ".venv" / "bin" / "python")
KICAD_CLI = os.environ.get(
    "KICAD_CLI",
    str(Path.home() / "Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"))
BLUES_LIB = os.environ.get(
    "BLUES_KICAD_LIB_DIR",
    str(Path.home() / "Documents/GitHub/blues/blues-kicad-lib"))


def run(cmd, **kw):
    print(f"    $ {' '.join(str(c) for c in cmd)}")
    env = {**os.environ, "BLUES_KICAD_LIB_DIR": BLUES_LIB}
    return subprocess.run([str(c) for c in cmd], env=env, **kw)


class Gates:
    def __init__(self, repo, name, cfg):
        self.repo, self.name, self.cfg = repo, name, cfg
        self.sch = repo / cfg["kicad"]["sch"]
        self.pcb = repo / cfg["kicad"]["pcb"] if cfg["kicad"].get("pcb") else None
        self.val_dir = self.sch.parent / "validation"
        self.val_dir.mkdir(exist_ok=True)
        self.results = {}

    def gate(self, gid, fn):
        print(f"\n== {gid} ==")
        try:
            ok = fn()
        except SkipGate as e:
            # A gate that cannot run is not a gate that passed. Skipping is
            # allowed only where the board declares why, in boards.yaml, so the
            # justification is reviewable and travels with the config instead of
            # living in a command line somebody has to remember.
            why = (self.cfg.get("skip_gates") or {}).get(gid)
            if why:
                print(f"  SKIPPED: {e}\n  justified: {why}")
                self.results[gid] = "SKIP"
            else:
                print(f"  FAIL: {e}\n  This gate is required. Either configure "
                      f"it, or record a justification under skip_gates.{gid} "
                      f"in boards.yaml.")
                self.results[gid] = "FAIL"
            return
        self.results[gid] = "PASS" if ok else "FAIL"
        print(f"  {self.results[gid]}")

    def erc(self):
        # full report (all severities) archived for human review ...
        run([KICAD_CLI, "sch", "erc", "--severity-all",
             "-o", self.val_dir / "erc.rpt", self.sch])
        # ... but the hard gate is error-severity only; warnings are reviewed
        # and documented in Porting-Notes (house convention, cf. the
        # Notecarrier-A port's rule_severities).
        r = run([KICAD_CLI, "sch", "erc", "--exit-code-violations",
                 "--severity-error", "-o", self.val_dir / "erc-errors.rpt",
                 self.sch])
        return r.returncode == 0

    def drc(self):
        if not self.pcb:
            raise SkipGate("no pcb configured")
        run([KICAD_CLI, "pcb", "drc", "--severity-all", "--schematic-parity",
             "-o", self.val_dir / "drc.rpt", self.pcb])
        r = run([KICAD_CLI, "pcb", "drc", "--exit-code-violations",
                 "--severity-error", "--schematic-parity",
                 "-o", self.val_dir / "drc-errors.rpt", self.pcb])
        return r.returncode == 0

    def bom(self):
        if "bom" not in self.cfg:
            raise SkipGate("no bom config")
        kicad_csv = self.val_dir / "bom-kicad.csv"
        mpn_field = self.cfg["bom"].get("kicad_mpn_field", "MPN")
        r = run([KICAD_CLI, "sch", "export", "bom", "-o", kicad_csv,
                 "--fields", f"Reference,Value,{mpn_field},${{DNP}}",
                 "--labels", "Reference,Value,MPN,DNP", self.sch])
        if r.returncode != 0:
            return False
        r = run([PY, HERE / "bom_compare.py", "--kicad", kicad_csv,
                 "--board", self.name, "--config", HERE / "boards.yaml",
                 "--report", self.val_dir / "bom-compare.txt"])
        return r.returncode == 0

    def netlist(self):
        if "odb" not in self.cfg:
            raise SkipGate("no shipped ODB++ for this board")
        net = self.val_dir / "netlist-kicad.net"
        r = run([KICAD_CLI, "sch", "export", "netlist",
                 "--format", "kicadsexpr", "-o", net, self.sch])
        if r.returncode != 0:
            return False
        r = run([PY, HERE / "netlist_compare.py", "--kicad", net,
                 "--odb", self.repo / self.cfg["odb"]["root"],
                 "--step", self.cfg["odb"].get("step", "pcb"),
                 "--report", self.val_dir / "netlist-compare.txt"])
        return r.returncode == 0

    def gerber(self):
        if "gerbers" not in self.cfg or not self.pcb:
            raise SkipGate("no gerber config")
        with tempfile.TemporaryDirectory() as td:
            r = run([KICAD_CLI, "pcb", "export", "gerbers", "--no-x2",
                     "--subtract-soldermask", "-o", td + "/", self.pcb])
            if r.returncode != 0:
                return False
            cfg_g = dict(self.cfg["gerbers"])
            tmp_cfg = Path(td) / "boards-abs.yaml"
            tmp_cfg.write_text(yaml.safe_dump(
                {"boards": {self.name: {"gerbers": cfg_g}}}))
            # gerber_diff resolves original_zip / a relative original_dir
            # against --repo, so nothing here depends on a local scratch dir.
            r = run([PY, HERE / "gerber_diff.py", "--board", self.name,
                     "--config", tmp_cfg, "--kicad-dir", td,
                     "--repo", self.repo, "--out", self.val_dir])
            return r.returncode == 0

    def pnp(self):
        if "pnp" not in self.cfg or not self.pcb:
            raise SkipGate("no shipped pick-and-place file configured")
        r = run([PY, HERE / "pnp_compare.py", "--kicad", self.pcb,
                 "--board", self.name, "--config", HERE / "boards.yaml",
                 "--repo", self.repo,
                 "--baseline", self.val_dir / "placement-baseline.yaml",
                 "--report", self.val_dir / "pnp-compare.txt"])
        return r.returncode == 0

    def kicanvas(self):
        sheets = sorted(self.sch.parent.glob("*.kicad_sch"))
        files = sheets + ([self.pcb] if self.pcb else [])
        r = run([PY, HERE / "kicanvas_check" / "render_check.py",
                 "--out", self.val_dir / "kicanvas", *files])
        return r.returncode == 0

    def rag(self):
        extract = self.repo / "_Tools" / "extract_for_rag" / "extract.py"
        rag_py = self.repo / "_Tools" / "extract_for_rag" / ".venv" / "bin" / "python"
        if not rag_py.exists():
            raise SkipGate("extract_for_rag venv not present")
        with tempfile.TemporaryDirectory() as td:
            changed = [str(p.relative_to(self.repo))
                       for p in self.sch.parent.glob("*.kicad_sch")]
            changed_file = Path(td) / "changed.txt"
            changed_file.write_text("\n".join(changed) + "\n")
            r = run([rag_py, extract, "--no-vlm", "--only", "kicad",
                     "--out", td, "--changed-from", changed_file],
                    text=True, cwd=self.repo, capture_output=True)
            print((r.stdout or "")[-1500:])
            print((r.stderr or "")[-500:])
            return r.returncode == 0


class SkipGate(Exception):
    pass


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("board")
    ap.add_argument("--repo", type=Path,
                    default=HERE.parent.parent)
    ap.add_argument("--skip", nargs="*", default=[],
                    help="gate ids to skip (must be justified in Porting-Notes)")
    args = ap.parse_args()

    cfg = yaml.safe_load((HERE / "boards.yaml").read_text())["boards"][args.board]
    g = Gates(args.repo.resolve(), args.board, cfg)

    for gid, fn in [("ERC", g.erc), ("DRC", g.drc), ("BOM", g.bom),
                    ("NETLIST", g.netlist), ("GERBER-DIFF", g.gerber),
                    ("PNP", g.pnp), ("KICANVAS", g.kicanvas), ("RAG", g.rag)]:
        if gid in args.skip:
            why = (cfg.get("skip_gates") or {}).get(gid)
            if not why:
                print(f"\n== {gid} ==\n  FAIL: --skip {gid} was requested but "
                      f"boards.yaml records no justification under "
                      f"skip_gates.{gid}.")
                g.results[gid] = "FAIL"
                continue
            print(f"\n== {gid} ==\n  SKIPPED (--skip)\n  justified: {why}")
            g.results[gid] = "SKIP"
            continue
        g.gate(gid, fn)

    print("\n===== SUMMARY:", args.board, "=====")
    for gid, res in g.results.items():
        print(f"  {gid:12s} {res}")
    hard_fail = any(v == "FAIL" for v in g.results.values())
    sys.exit(1 if hard_fail else 0)


if __name__ == "__main__":
    main()
