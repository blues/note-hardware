import pcbnew
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
CU = {"F.Cu", "B.Cu", "In1.Cu", "In2.Cu"}
from collections import Counter
c = Counter()
for d in b.GetDrawings():
    lay = d.GetLayerName()
    if lay not in CU: continue
    cls = d.GetClass()
    shp = d.ShowShape() if hasattr(d, "ShowShape") else ""
    c[(lay, cls, shp, d.GetNetname() if hasattr(d, "GetNetname") else "")] += 1
for k, v in sorted(c.items()): print(f"  {v:4d}  {k}")
print("--- texts on copper ---")
for d in b.GetDrawings():
    if d.GetLayerName() in CU and d.GetClass() == "PCB_TEXT":
        p = d.GetPosition()
        print(f"   {d.GetLayerName()} {repr(d.GetText())} at film=({p.x/1e6-130:.2f},{140-p.y/1e6:.2f}) mirrored={d.IsMirrored()}")
print("--- non-poly shapes on copper (v2.0 leftovers) ---")
n = 0
for d in b.GetDrawings():
    if d.GetLayerName() in CU and d.GetClass() == "PCB_SHAPE" and d.ShowShape() != "Polygon":
        bb = d.GetBoundingBox()
        print(f"   {d.GetLayerName()} {d.ShowShape()} bbox=({bb.GetX()/1e6-130:.2f},{140-(bb.GetY()+bb.GetHeight())/1e6:.2f})-({(bb.GetX()+bb.GetWidth())/1e6-130:.2f},{140-bb.GetY()/1e6:.2f})")
        n += 1
        if n > 12: break
