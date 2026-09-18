#!/usr/bin/env python3
"""Notecarrier-F v1.3: post-process the importer's board with the KiCad Python API.

  * inner copper layer names Mid Layer 3/4 -> Mid Layer 1/2 (match G1/G2 gerbers)
  * MOD1L/MOD1R -> MODL1/MODR1
  * 48 nameless free-hole footprints -> H1..H48, board-only, no BOM / no PnP
  * fiducials board-only + no BOM; MOD2 no BOM / no PnP; J11/R11/R12 DNP
  * every footprint re-pointed at Notecarrier-F-altium-import:<name> and the
    footprints saved into that .pretty (bottom parts flipped back to front)
  * imported GND pours: clearance 0.5 -> 0.1499 (fills are NOT recomputed)

Run with KiCad's bundled python:  <kicad-python> f13_pcb.py <in.kicad_pcb> <work-dir>
"""
import sys, collections
from pathlib import Path
import pcbnew

SRC, DST = Path(sys.argv[1]), Path(sys.argv[2])
LIB = "Notecarrier-F-altium-import"
REF_RENAME = {"MOD1L": "MODL1", "MOD1R": "MODR1"}
DNP = {"J11", "R11", "R12"}

b = pcbnew.LoadBoard(str(SRC))

# layer names
b.SetLayerName(pcbnew.In1_Cu, "Mid Layer 1")
b.SetLayerName(pcbnew.In2_Cu, "Mid Layer 2")

fps = list(b.GetFootprints())
# free holes: name by position (top-left first), so the numbering is reproducible
holes = sorted((f for f in fps if f.GetReference() == ""), key=lambda f: (f.GetPosition().y, f.GetPosition().x))
for i, f in enumerate(holes, 1):
    drills = {round(p.GetDrillSize().x / 1e6, 2) for p in f.Pads()}
    d = drills.pop() if len(drills) == 1 else 0
    name = "NPTH_free_hole" if d == 0.8 else f"NPTH_free_hole_{d:g}mm"
    f.SetReference(f"H{i}")
    f.SetValue(name)
    f.Reference().SetVisible(False)
    f.Value().SetVisible(False)
    f.SetFPID(pcbnew.LIB_ID(LIB, name))
    f.SetAttributes(pcbnew.FP_BOARD_ONLY | pcbnew.FP_EXCLUDE_FROM_POS_FILES | pcbnew.FP_EXCLUDE_FROM_BOM)
print(f"free holes named: {len(holes)}", collections.Counter(f.GetValue() for f in holes))

for f in fps:
    r = f.GetReference()
    if r in REF_RENAME:
        f.SetReference(REF_RENAME[r]); r = f.GetReference()
    a = f.GetAttributes()
    if r.startswith("FD") and r[2:].isdigit():
        a = pcbnew.FP_SMD | pcbnew.FP_BOARD_ONLY | pcbnew.FP_EXCLUDE_FROM_BOM
    elif r == "MOD2":
        a = pcbnew.FP_THROUGH_HOLE | pcbnew.FP_EXCLUDE_FROM_BOM | pcbnew.FP_EXCLUDE_FROM_POS_FILES
    elif r in DNP:
        a |= pcbnew.FP_DNP
        if any(p.GetAttribute() == pcbnew.PAD_ATTRIB_PTH for p in f.Pads()):
            a |= pcbnew.FP_THROUGH_HOLE
    f.SetAttributes(a)
    if not r.startswith("H"):
        bare = f.GetFPID().GetLibItemName().wx_str() if hasattr(f.GetFPID().GetLibItemName(), "wx_str") else str(f.GetFPID().GetLibItemName())
        f.SetFPID(pcbnew.LIB_ID(LIB, bare))

# collision check: same bare footprint name from different Altium libs with different pads
sig = {}
for f in fps:
    name = str(f.GetFPID().GetLibItemName())
    pads = tuple(sorted((p.GetNumber(), round(p.GetSize()[0] if False else p.GetSizeX()/1e6, 3)) for p in f.Pads())) if False else \
           tuple(sorted((p.GetNumber(), p.GetAttribute(), round(p.GetDrillSize().x/1e6, 3)) for p in f.Pads()))
    sig.setdefault(name, set()).add(pads)
coll = {k: len(v) for k, v in sig.items() if len(v) > 1}
print("footprint names:", len(sig), "pad-signature collisions:", coll)

# zones: the importer carries Altium's 0.5 mm zone *parameter*; the pours were
# actually poured to the board's "Clearance Polygon" rule (0.2 mm, read from the
# .PcbDoc Rules6 stream) - set a hair under that. Fills untouched.
zc = collections.Counter()
for z in b.Zones():
    if z.GetIsRuleArea():
        continue
    zc[round(z.GetLocalClearance() / 1e6, 4)] += 1
    if z.GetLocalClearance() > pcbnew.FromMM(0.2):
        z.SetLocalClearance(pcbnew.FromMM(0.1999))
print("copper zone clearances before:", dict(zc))

# save footprints into the project library
lib = DST / f"{LIB}.pretty"
lib.mkdir(exist_ok=True)
io = pcbnew.PCB_IO_MGR.PluginFind(pcbnew.PCB_IO_MGR.KICAD_SEXP)
saved = set()
for f in sorted(fps, key=lambda f: f.GetReference()):
    name = str(f.GetFPID().GetLibItemName())
    if name in saved:
        continue
    c = pcbnew.FOOTPRINT(f)
    if c.IsFlipped():
        c.Flip(c.GetPosition(), False)
    c.SetOrientationDegrees(0)
    c.SetPosition(pcbnew.VECTOR2I(0, 0))
    c.SetReference("REF**")
    c.Reference().SetVisible(True)
    for p in c.Pads():
        p.SetNet(None) if hasattr(p, "SetNet") else None
    io.FootprintSave(str(lib), c)
    saved.add(name)
print(f"saved {len(saved)} footprints into {lib.name}")

out = DST / "Notecarrier-F.kicad_pcb"
pcbnew.SaveBoard(str(out), b)
print("board saved")

# ---- text-level passes on the saved board -------------------------------------
import re, glob


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


def blocks(text, opener):
    pos = 0
    while True:
        i = text.find(opener, pos)
        if i < 0: return
        e = block_end(text, i); yield i, e; pos = e


# 1. the importer leaves every footprint's Value empty; fill it from the
#    schematic (schematic parity otherwise reports a mismatch per part)
vals = {}
for f in glob.glob(str(DST / "Notecarrier-F_*.kicad_sch")):
    s = open(f).read()
    for i, e in blocks(s, "\n\t(symbol\n"):
        blk = s[i:e]
        r = re.search(r'\(property "Reference" "([^"]*)"', blk)
        v = re.search(r'\(property "Value" "((?:[^"\\]|\\.)*)"', blk)
        if r and v and not r.group(1).startswith("#"):
            vals.setdefault(r.group(1), v.group(1))
t = open(out).read(); parts = []; pos = 0; filled = 0
for i, e in blocks(t, "\n\t(footprint "):
    blk = t[i:e]
    r = re.search(r'\(property "Reference" "([^"]*)"', blk)
    if r and r.group(1) in vals:
        new = re.sub(r'(\(property "Value" ")(?:[^"\\]|\\.)*(")',
                     lambda m: m.group(1) + vals[r.group(1)] + m.group(2), blk, count=1)
        filled += new != blk; blk = new
    parts += [t[pos:i], blk]; pos = e
parts.append(t[pos:]); t = "".join(parts)
print(f"footprint Values filled from schematic: {filled}")

# 2. OBJ1 mounting hole: Altium's pad stack is 6 mm outer / 1.524 mm inner around a
#    3.7 mm hole (no inner copper survives drilling); KiCad flags the negative
#    annulus, so give the inner layers the smallest legal ring (drill + 0.1) and
#    let KiCad drop the unused inner layers.
i = t.find('(property "Reference" "OBJ1"')
k = t.find('(pad "1" thru_hole circle', i)
seg_end = block_end(t, k)
seg = t[k:seg_end]
drill = float(re.search(r"\(drill ([0-9.]+)\)", seg).group(1))
inner = re.search(r'\(layer "Inner"\n\t*\(shape circle\)\n\t*\(size ([0-9.]+) [0-9.]+\)', seg)
if inner and float(inner.group(1)) < drill:
    seg = seg.replace(inner.group(0), inner.group(0).replace(f"(size {inner.group(1)} {inner.group(1)})",
                                                             f"(size {drill + 0.1:g} {drill + 0.1:g})"))
    seg = seg.replace("(remove_unused_layers no)", "(remove_unused_layers yes)\n\t\t\t(keep_end_layers yes)", 1)
    t = t[:k] + seg + t[seg_end:]
    print(f"OBJ1 pad 1: inner size {inner.group(1)} -> {drill + 0.1:g} mm, unused inner layers removed")
open(out, "w").write(t)
