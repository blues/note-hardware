"""Adopt nets onto still-net-0 copper from the net-assigned fab pour areas."""
import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
CU = {"F.Cu", "B.Cu", "In1.Cu", "In2.Cu"}
polys = [(d.GetLayer(), d.GetPolyShape(), d.GetNetCode(), d.GetNetname())
         for d in b.GetDrawings()
         if d.GetClass() == "PCB_SHAPE" and d.GetLayerName() in CU
         and d.ShowShape() == "Polygon" and d.GetNetCode() != 0]
print("net-assigned fab copper areas:", len(polys))
n0 = [t for t in b.GetTracks() if t.GetNetCode() == 0]
print("net-0 copper items:", len(n0))
assigned = 0
from collections import Counter
per = Counter()
for t in n0:
    if t.GetClass() == "PCB_VIA":
        pts = [t.GetStart()]
        lays = [l for l in t.GetLayerSet().Seq()]
    else:
        pts = [t.GetStart(), t.GetEnd()]
        lays = [t.GetLayer()]
    hit = None
    for lid, poly, nc, nn in polys:
        if lid not in lays: continue
        if any(poly.Contains(p) for p in pts):
            hit = (nc, nn); break
    if hit:
        t.SetNetCode(hit[0]); assigned += 1; per[hit[1]] += 1
print(f"assigned from fab copper areas: {assigned}")
print("by net:", per.most_common(8))
left = [t for t in b.GetTracks() if t.GetNetCode() == 0]
print("still net-0:", len(left))
pcbnew.SaveBoard(PATH, b)
b2 = pcbnew.LoadBoard(PATH); b2.BuildConnectivity()
print("unconnected:", b2.GetConnectivity().GetUnconnectedCount(True))
