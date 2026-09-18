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

# zones: importer carries Altium's 0.5 mm pour clearance parameter; the fabricated
# pours were poured at the board minimum (mirrors the v1.5 port). Fills untouched.
zc = collections.Counter()
for z in b.Zones():
    if z.GetIsRuleArea():
        continue
    zc[round(z.GetLocalClearance() / 1e6, 4)] += 1
    if z.GetLocalClearance() > pcbnew.FromMM(0.15):
        z.SetLocalClearance(pcbnew.FromMM(0.1499))
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

pcbnew.SaveBoard(str(DST / "Notecarrier-F.kicad_pcb"), b)
print("board saved")
