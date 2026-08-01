#!/usr/bin/env python3
"""Compare a KiCad-exported BOM against the shipped BOM spreadsheet.

Hard gate: the set of reference designators must match exactly, and for each
refdes the value/part name (and MPN where the shipped BOM provides one) must
match. Every board's shipped BOM has a different layout, so the parsing rules
live in boards.yaml (see `bom` section per board).

KiCad side:  kicad-cli sch export bom <sch> -o kicad_bom.csv \
                 --fields "Reference,Value,MPN,DNP" --group-by "" ...
             (run_all.py generates this; one row per refdes)

Usage:
    bom_compare.py --kicad kicad_bom.csv --board <name> --config boards.yaml
                   [--report report.txt]

Exit 0 = exact match (after documented normalizations), 1 = differences.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

import openpyxl
import xlrd
import yaml


def norm(s):
    """Normalize a value string for comparison."""
    if s is None:
        return ""
    if isinstance(s, float) and s.is_integer():
        s = int(s)  # xlrd reads numeric cells as floats ("20404.0")
    s = str(s).strip()
    s = s.replace("µ", "u").replace("μ", "u")  # micro signs -> u
    s = re.sub(r"\s+", " ", s)
    return s.casefold()


def split_refs(cell):
    """'C1, C2 C3' -> ['C1','C2','C3']"""
    return [r for r in re.split(r"[,\s]+", str(cell).strip()) if r]


def load_shipped(cfg, repo=None):
    """Return {refdes: row-dict} from the shipped spreadsheet per board config.

    cfg keys: path, sheet (optional), header_contains (cell text that must
    EQUAL a cell on the header row, default 'Designator'), columns:
    {refs, value, mpn (optional)}, skip_refdes (regex, optional),
    dnp_markers (list, optional).
    """
    path = Path(cfg["path"])
    if not path.is_absolute():
        path = Path(repo) if repo else Path(__file__).resolve().parent.parent.parent
        path = path / cfg["path"]
    if path.suffix.lower() == ".xls":
        book = xlrd.open_workbook(path)
        ws = book.sheet_by_name(cfg["sheet"]) if cfg.get("sheet") else book.sheet_by_index(0)
        rows = [tuple(ws.cell_value(r, c) for c in range(ws.ncols))
                for r in range(ws.nrows)]
    else:
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb[cfg["sheet"]] if cfg.get("sheet") else wb.active
        rows = list(ws.iter_rows(values_only=True))

    marker = cfg.get("header_contains", "Designator")
    header_idx = next((i for i, r in enumerate(rows)
                       if any(marker == str(c).strip() for c in r if c is not None)),
                      None)
    if header_idx is None:
        raise SystemExit(f"no header row in {path.name}: no cell equals "
                         f"{marker!r} (header_contains must match a header "
                         f"cell exactly)")
    header = [str(c).strip() if c is not None else "" for c in rows[header_idx]]
    col = {name: header.index(name) for name in header if name}

    refs_col = col[cfg["columns"]["refs"]]
    value_col = col[cfg["columns"]["value"]]
    mpn_name = cfg["columns"].get("mpn", "")
    if mpn_name and mpn_name not in col:
        # A typo here must not quietly disable the MPN half of the gate: with
        # mpn_col=None every shipped MPN reads as "" and compare() never checks
        # one - the exact silent-degrade this tool was rebuilt to remove.
        raise SystemExit(f"configured mpn column {mpn_name!r} is not in the "
                         f"header of {path.name}: {[h for h in header if h]}")
    mpn_col = col.get(mpn_name, None)
    skip_re = re.compile(cfg["skip_refdes"]) if cfg.get("skip_refdes") else None
    dnp_markers = [norm(m) for m in cfg.get("dnp_markers", [])]
    refdes_map = cfg.get("refdes_map", {})

    shipped = {}
    for r in rows[header_idx + 1:]:
        if r is None or refs_col >= len(r) or r[refs_col] in (None, ""):
            continue
        value = norm(r[value_col]) if value_col < len(r) else ""
        if value in dnp_markers:
            continue
        mpn = norm(r[mpn_col]) if mpn_col is not None and mpn_col < len(r) else ""
        for ref in split_refs(r[refs_col]):
            ref = refdes_map.get(ref, ref)
            if skip_re and skip_re.match(ref):
                continue
            shipped[ref] = {"value": value, "mpn": mpn}
    return shipped


def load_kicad(path, skip_refdes=None):
    """Return {refdes: row-dict} from a kicad-cli BOM CSV (one row per refdes)."""
    skip_re = re.compile(skip_refdes) if skip_refdes else None
    out = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            for ref in split_refs(row.get("Reference", "")):
                if skip_re and skip_re.match(ref):
                    continue
                if norm(row.get("DNP", "")) in ("dnp", "true", "1", "yes"):
                    continue
                out[ref] = {"value": norm(row.get("Value")),
                            "mpn": norm(row.get("MPN"))}
    return out


def compare(kicad, shipped, check_mpn=True, check_value=True):
    """Return (ok, prose_report, problems).

    `problems` is a list of {kind, ref, message}. Callers that need to act on the
    result - the runner, the regression suite - read that rather than parsing the
    prose, so a failure kind they have not enumerated still reaches them.
    """
    lines = [f"KiCad populated refdes:   {len(kicad)}",
             f"Shipped populated refdes: {len(shipped)}", ""]
    only_k = sorted(set(kicad) - set(shipped))
    only_s = sorted(set(shipped) - set(kicad))
    diffs = []
    problems = []

    def fail(kind, ref, message):
        problems.append({"kind": kind, "ref": ref, "message": message})

    for ref in sorted(set(kicad) & set(shipped)):
        k, s = kicad[ref], shipped[ref]
        # A grouped BOM line may list several equivalent value spellings
        # ("1uF/ 16V-X5R, 1uF/ 16V-XR5, 1u/16V-X5R"); accept any of them.
        variants = {v.strip() for v in s["value"].split(",")}
        if check_value and k["value"] != s["value"] and k["value"] not in variants:
            msg = f"{ref}: value KiCad='{k['value']}' shipped='{s['value']}'"
            diffs.append("  " + msg)
            fail("value-mismatch", ref, msg)
        # Value and MPN are checked independently: an `elif` here would hide an
        # MPN mismatch behind a value mismatch on the same refdes.
        if check_mpn and s["mpn"]:
            if not k["mpn"]:
                # A blank KiCad MPN is missing data, not agreement. Treating it
                # as a match let real part numbers silently drop out of a port.
                msg = f"{ref}: MPN missing in KiCad, shipped='{s['mpn']}'"
                diffs.append("  " + msg)
                fail("mpn-missing", ref, msg)
            elif (k["mpn"] != s["mpn"]
                    and k["mpn"] not in {m.strip() for m in s["mpn"].split(",")}):
                msg = f"{ref}: MPN KiCad='{k['mpn']}' shipped='{s['mpn']}'"
                diffs.append("  " + msg)
                fail("mpn-mismatch", ref, msg)
    for r in only_k:
        fail("only-in-kicad", r, f"{r} is fitted in KiCad but absent from the shipped BOM")
    for r in only_s:
        fail("only-in-shipped", r, f"{r} is in the shipped BOM but not fitted in KiCad")
    ok = not problems
    if only_k:
        lines.append(f"Only in KiCad ({len(only_k)}): {only_k}")
    if only_s:
        lines.append(f"Only in shipped BOM ({len(only_s)}): {only_s}")
    if diffs:
        lines.append("Field mismatches:")
        lines.extend(diffs)
    lines.append("")
    lines.append("RESULT: PASS - BOM matches exactly." if ok else "RESULT: FAIL")
    return ok, "\n".join(lines), problems


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kicad", required=True, type=Path)
    ap.add_argument("--board", required=True)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--repo", type=Path,
                    help="repo root for relative shipped-BOM paths "
                         "(default: this script's checkout)")
    ap.add_argument("--report", type=Path)
    ap.add_argument("--json", type=Path,
                    help="write a machine-readable result summary here")
    args = ap.parse_args()

    cfg = yaml.safe_load(args.config.read_text())["boards"][args.board]["bom"]
    try:
        shipped = load_shipped(cfg, repo=args.repo)
        kicad = load_kicad(args.kicad, cfg.get("skip_refdes"))
        # An empty side means the parse went wrong (over-broad skip_refdes,
        # wrong sheet/columns), and {} == {} must not read as a matching BOM.
        if not shipped:
            raise SystemExit("parsed 0 shipped BOM rows - check sheet/columns/"
                             "skip_refdes in boards.yaml")
        if not kicad:
            raise SystemExit(f"parsed 0 KiCad BOM rows from {args.kicad}")
    except SystemExit as e:
        # Still write the JSON summary: a caller must not see a non-zero exit
        # next to a stale bom-compare.json from the last passing run.
        if args.json:
            import json
            args.json.write_text(json.dumps({
                "board": args.board, "result": "FAIL",
                "problems": [{"kind": "config-error", "ref": None,
                              "message": str(e)}],
            }, indent=1, sort_keys=True))
        raise
    ok, report, problems = compare(
        kicad, shipped, check_mpn=cfg.get("check_mpn", True),
        check_value=cfg.get("check_value", True))
    print(report)
    if args.report:
        args.report.write_text(report + "\n")
    if args.json:
        import json
        args.json.write_text(json.dumps({
            "board": args.board,
            "result": "PASS" if ok else "FAIL",
            "problems": problems,
            "summary": {"kicad_refdes": len(kicad), "shipped_refdes": len(shipped)},
        }, indent=1, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
