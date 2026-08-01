#!/usr/bin/env python3
"""Compare a KiCad schematic netlist against an ODB++ netlist (ground truth).

The comparison is by connectivity *partition*, not by net name: two netlists
are equivalent when they group the same set of (refdes, pin) nodes into the
same clusters. Net names are used only for reporting.

KiCad side:   kicad-cli sch export netlist --format kicadsexpr <sch> -o out.net
ODB++ side:   the `steps/<step>/layers/comp_+_top|bot/components` files map
              refdes+pin -> net number; `steps/<step>/netlists/cadnet/netlist`
              maps net number -> net name.

Usage:
    netlist_compare.py --kicad out.net --odb <extracted-odb-root> [--step pcb]
                       [--ignore-refdes REGEX] [--report report.txt]

Exit code 0 = partitions match (after documented normalizations), 1 = mismatch.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------- s-expressions

def parse_sexpr(text: str):
    """Minimal s-expression parser (sufficient for kicad netlist files)."""
    tokens = re.findall(r'"(?:[^"\\]|\\.)*"|[()]|[^\s()"]+', text)
    pos = 0

    def parse():
        nonlocal pos
        tok = tokens[pos]
        pos += 1
        if tok == '(':
            lst = []
            while tokens[pos] != ')':
                lst.append(parse())
            pos += 1
            return lst
        if tok.startswith('"'):
            return tok[1:-1].replace('\\"', '"').replace('\\\\', '\\')
        return tok

    return parse()


def kicad_nodes(netlist_path: Path):
    """Return {netname: set((refdes, pin))} from a kicadsexpr netlist."""
    tree = parse_sexpr(netlist_path.read_text(errors="replace"))
    nets = {}
    nets_section = next(x for x in tree if isinstance(x, list) and x and x[0] == "nets")
    for net in nets_section[1:]:
        if not (isinstance(net, list) and net and net[0] == "net"):
            continue
        name = next(x[1] for x in net if isinstance(x, list) and x[0] == "name")
        nodes = set()
        for node in net:
            if isinstance(node, list) and node and node[0] == "node":
                ref = next(x[1] for x in node if isinstance(x, list) and x[0] == "ref")
                pin = next(x[1] for x in node if isinstance(x, list) and x[0] == "pin")
                nodes.add((str(ref), str(pin)))
        if nodes:
            if str(name) == "$NONE$":
                continue  # ODB bucket for unassigned/unconnected pins
            nets[str(name)] = nodes
    return nets


# ---------------------------------------------------------------------- ODB++

def odb_net_names(odb_root: Path, step: str):
    """Return {net_number: net_name} from the cadnet netlist ($n lines)."""
    names = {}
    netlist = odb_root / "steps" / step / "netlists" / "cadnet" / "netlist"
    for line in netlist.read_text(errors="replace").splitlines():
        m = re.match(r"^\$(\d+)\s+(\S+)", line)
        if m:
            names[int(m.group(1))] = m.group(2)
    return names


def odb_nodes(odb_root: Path, step: str):
    """Return {net_name: set((refdes, pin))} from ODB components files.

    components file format (per record):
        CMP <pkg> <x> <y> <rot> <mirror> <refdes> <part> ;attrs
        TOP <pin_index> <x> <y> <rot> <mirror> <net_num> <subnet> <pin_name>
    """
    names = odb_net_names(odb_root, step)
    nets = defaultdict(set)
    for side in ("comp_+_top", "comp_+_bot"):
        comp_file = odb_root / "steps" / step / "layers" / side / "components"
        if not comp_file.exists():
            continue
        refdes = None
        for line in comp_file.read_text(errors="replace").splitlines():
            if line.startswith("CMP "):
                refdes = line.split()[6]
            elif line.startswith("TOP ") and refdes is not None:
                f = line.split()
                net_num, pin_name = int(f[6]), f[8]
                name = names.get(net_num, f"$NET{net_num}")
                if name == "$NONE$":
                    continue  # ODB bucket for unassigned/unconnected pins
                nets[name].add((refdes, pin_name))
    return dict(nets)


# ----------------------------------------------------------------- comparison

def partitions(nets, ignore_re=None, min_nodes=2):
    """Convert {name: nodes} into a canonical set of frozensets.

    Single-node nets are dropped (unconnected pins are represented
    inconsistently between tools); ignored refdes are filtered out first.
    """
    parts = {}
    for name, nodes in nets.items():
        if ignore_re:
            nodes = {n for n in nodes if not ignore_re.match(n[0])}
        if len(nodes) >= min_nodes:
            parts[frozenset(nodes)] = name
    return parts


def compare(kicad, odb, ignore_re):
    k = partitions(kicad, ignore_re)
    o = partitions(odb, ignore_re)
    matched = set(k) & set(o)
    only_k = {s: k[s] for s in set(k) - matched}
    only_o = {s: o[s] for s in set(o) - matched}

    lines = [
        f"KiCad nets (>=2 nodes): {len(k)}",
        f"ODB++ nets (>=2 nodes): {len(o)}",
        f"Matched partitions:     {len(matched)}",
        "",
    ]
    ok = not only_k and not only_o
    if ok:
        lines.append("RESULT: PASS - connectivity partitions are identical.")
    else:
        lines.append("RESULT: FAIL - partition differences below.")
        # Pair up near-misses by best node overlap for a readable report.
        for s, name in sorted(only_k.items(), key=lambda x: x[1]):
            best = max(only_o, key=lambda t: len(s & t), default=None)
            lines.append(f"\nKiCad net '{name}' ({len(s)} nodes) has no exact ODB match.")
            if best and s & best:
                lines.append(f"  Closest ODB net '{only_o[best]}':")
                lines.append(f"    only in KiCad: {sorted(s - best)}")
                lines.append(f"    only in ODB:   {sorted(best - s)}")
        for s, name in sorted(only_o.items(), key=lambda x: x[1]):
            best = max(only_k, key=lambda t: len(s & t), default=None)
            if best and len(s & best) == 0:
                best = None
            if best is None:
                lines.append(f"\nODB net '{name}' ({len(s)} nodes) has no overlapping KiCad net: {sorted(s)}")
    return ok, "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kicad", required=True, type=Path, help="kicadsexpr netlist file")
    ap.add_argument("--odb", required=True, type=Path, help="extracted ODB++ root (dir containing steps/)")
    ap.add_argument("--step", default="pcb", help="ODB step name (default: pcb)")
    ap.add_argument("--ignore-refdes", default=r"^(TP|FID|MH|LOGO|H)\d*$",
                    help="regex of refdes to ignore on both sides")
    ap.add_argument("--report", type=Path, help="write full report here")
    args = ap.parse_args()

    ignore_re = re.compile(args.ignore_refdes) if args.ignore_refdes else None
    ok, report = compare(kicad_nodes(args.kicad), odb_nodes(args.odb, args.step), ignore_re)
    print(report)
    if args.report:
        args.report.write_text(report + "\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
