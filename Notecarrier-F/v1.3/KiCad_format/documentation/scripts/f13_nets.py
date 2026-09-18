#!/usr/bin/env python3
"""Rename the board's Altium auto-named / sheet-local nets to the KiCad schematic's
net names by matching every pad against the exported netlist, and report anything
that does not line up (a board net spanning two schematic nets, or a schematic-
connected pad the board leaves netless).

usage: f13_nets.py <netlist.net> <board.kicad_pcb> [--apply]
Plain python3 (text level).
"""
import re, sys, collections
from pathlib import Path

NET, PCB = Path(sys.argv[1]), Path(sys.argv[2])
APPLY = "--apply" in sys.argv


def block_end(text, start):
    depth, i, in_str = 0, start, False
    while i < len(text):
        c = text[i]
        if in_str:
            if c == "\\": i += 1
            elif c == '"': in_str = False
        elif c == '"': in_str = True
        elif c == "(": depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0: return i + 1
        i += 1
    raise ValueError


# schematic: pad -> net name
nl = NET.read_text()
sch = {}
pos = 0
while True:
    m = re.search(r'\(net \(code "\d+"\) \(name "((?:[^"\\]|\\.)*)"\)', nl[pos:])
    if not m: break
    s = pos + m.start(); e = block_end(nl, s)
    name = m.group(1)
    for ref, pin in re.findall(r'\(node \(ref "([^"]*)"\) \(pin "([^"]*)"\)', nl[s:e]):
        sch[f"{ref}.{pin}"] = name
    pos = e
print(f"schematic netlist: {len(sch)} pins, {len(set(sch.values()))} nets")

# board: pad -> net (code, name)
t = PCB.read_text()
nets = dict(re.findall(r'^\t\(net (\d+) "((?:[^"\\]|\\.)*)"\)', t, re.M))
brd = {}
pos = 0
while True:
    m = re.search(r'\n\t\(footprint ', t[pos:])
    if not m: break
    s = pos + m.start() + 1; e = block_end(t, s)
    fp = t[s:e]
    ref = re.search(r'\(property "Reference" "([^"]*)"', fp)
    ref = ref.group(1) if ref else ""
    pp = 0
    while True:
        pm = re.search(r'\n\t\t\(pad "((?:[^"\\]|\\.)*)"', fp[pp:])
        if not pm: break
        ps = pp + pm.start() + 1; pe = block_end(fp, ps)
        nm = re.search(r'\(net (\d+) "((?:[^"\\]|\\.)*)"\)', fp[ps:pe])
        brd[f"{ref}.{pm.group(1)}"] = (nm.group(1), nm.group(2)) if nm else (None, "")
        pp = pe
    pos = e
print(f"board: {len(brd)} pads, {len(nets)} nets")

# per board net: which schematic nets do its pads carry?
by_code = collections.defaultdict(collections.Counter)
netless_but_connected = []
unknown_pads = []
for pad, (code, bname) in brd.items():
    sname = sch.get(pad)
    if code is None:
        if sname and not sname.startswith("unconnected-"):
            netless_but_connected.append((pad, sname))
        continue
    if sname is None:
        unknown_pads.append((pad, bname)); continue
    by_code[code][sname] += 1

rename, conflicts = {}, {}
for code, names in nets.items():
    c = by_code.get(code)
    if not c: continue
    real = [n for n in c if not n.startswith("unconnected-")]
    if len(real) == 1:
        if real[0] != names: rename[code] = (names, real[0])
    elif len(real) > 1:
        conflicts[code] = (names, dict(c))
print(f"renames: {len(rename)}   conflicts (board net spans >1 schematic nets): {len(conflicts)}")
for code, (old, cnt) in sorted(conflicts.items(), key=lambda x: int(x[0])):
    print(f"  CONFLICT net {code} {old!r}: {cnt}")
print(f"schematic-connected pads left netless on board: {len(netless_but_connected)}")
for p in netless_but_connected[:40]: print("  ", p)
print(f"board pads absent from schematic netlist: {len(unknown_pads)}", collections.Counter(p.split('.')[0] for p, _ in unknown_pads))

# schematic nets never seen on the board (should only be unconnected- stubs)
seen = {n for c in by_code.values() for n in c}
missing = sorted(n for n in set(sch.values()) - seen if not n.startswith("unconnected-"))
print(f"schematic nets with no board pad: {len(missing)}", missing[:30])

if APPLY:
    for code, (old, new) in rename.items():
        t = t.replace(f'(net {code} "{old}")', f'(net {code} "{new}")')
    PCB.write_text(t)
    print("applied", len(rename), "renames")
    for code, (old, new) in sorted(rename.items(), key=lambda x: int(x[0])):
        print(f"  {old} -> {new}")
