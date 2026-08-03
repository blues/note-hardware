import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse2 import parse
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
via = next(t for t in b.GetTracks() if t.m_Uuid.AsString().startswith("4ae4a38c"))
p = via.GetStart()
fx, fy = p.x/1e6-130.0, 140.0-p.y/1e6
print(f"via VIO at film ({fx:.3f},{fy:.3f}) width={via.GetWidth()/1e6:.3f} drill={via.GetDrillValue()/1e6:.3f}")
# what does the fab B film have there?
r = parse("/scratch/a23-g/07-BOTTOM.art")
near_f = [(d, x, y) for d, x, y in r["flashes"] if abs(x-fx) < 1.0 and abs(y-fy) < 1.0]
print("B film flashes within 1mm:", [(r["apertures"].get(d), round(x,3), round(y,3)) for d, x, y in near_f])
# is the point inside the dark pour region and inside any clear region?
def pt_in(loop, px, py):
    c = False
    for i in range(len(loop)):
        x1, y1 = loop[i]; x2, y2 = loop[(i+1) % len(loop)]
        if ((y1 > py) != (y2 > py)) and (px < (x2-x1)*(py-y1)/(y2-y1) + x1): c = not c
    return c
for pol, v in r["regions"]:
    if len(v) < 3: continue
    if pt_in(v, fx, fy):
        xs=[q[0] for q in v]; ys=[q[1] for q in v]
        print(f"   point is INSIDE a {pol} region (n={len(v)} bbox=({min(xs):.1f},{min(ys):.1f})-({max(xs):.1f},{max(ys):.1f}))")
# and does the port's polygon contain it?
for d in b.GetDrawings():
    if d.GetClass()=="PCB_SHAPE" and d.ShowShape()=="Polygon" and d.GetLayerName()=="B.Cu":
        if d.GetPolyShape().Contains(p):
            print("   port B.Cu polygon CONTAINS the via centre -> copper where fab has none")
