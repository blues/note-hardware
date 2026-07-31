"""Assign nets to still-net-0 items by the zone fill they sit inside."""
import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
zones = [z for z in b.Zones() if not z.GetIsRuleArea() and z.GetNetCode() != 0]
assigned = 0
left = []
for t in b.GetTracks():
    if t.GetNetCode() != 0: continue
    pts = [t.GetStart()] if t.GetClass() == "PCB_VIA" else [t.GetStart(), t.GetEnd()]
    lays = [b.GetLayerName(l) for l in t.GetLayerSet().Seq()] if t.GetClass() == "PCB_VIA" else [t.GetLayerName()]
    hit = None
    for z in zones:
        zl = [b.GetLayerName(l) for l in z.GetLayerSet().Seq()]
        common = set(zl) & set(lays)
        if not common: continue
        for lname in common:
            lid = b.GetLayerID(lname)
            poly = z.GetFilledPolysList(lid)
            if poly and any(poly.Contains(p) for p in pts):
                hit = z; break
        if hit: break
    if hit:
        t.SetNetCode(hit.GetNetCode()); assigned += 1
    else:
        left.append(t)
print(f"assigned by zone containment: {assigned}, still net-0: {len(left)}")
from collections import Counter
print(Counter((t.GetClass(), t.GetLayerName()) for t in left))
for t in left[:15]:
    s = (round(t.GetStart().x/1e6-130,2), round(140-t.GetStart().y/1e6,2))
    print("  ", t.GetClass(), t.GetLayerName(), s)
pcbnew.SaveBoard(PATH, b)
b2 = pcbnew.LoadBoard(PATH)
b2.BuildConnectivity()
print("unconnected:", b2.GetConnectivity().GetUnconnectedCount(True))
