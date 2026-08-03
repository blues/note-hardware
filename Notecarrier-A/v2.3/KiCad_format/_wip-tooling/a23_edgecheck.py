import sys
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
for lay, f in [("F.Cu","04-TOP.art"), ("B.Cu","07-BOTTOM.art"), ("In1","05-GND.art"), ("In2","06-POWER.art")]:
    r = parse(f"/scratch/a23-g/{f}", xoff=0.0)
    edge = []
    regs = 0
    for d, x1, y1, x2, y2 in r["draws"]:
        onb = lambda x, y: (abs(x) < 0.2 or abs(x+75) < 0.2 or abs(y) < 0.2 or abs(y-68) < 0.2)
        if onb(x1,y1) and onb(x2,y2):
            w = r["apertures"].get(d, ("?",(0,)))[1]
            edge.append((round(x1,2),round(y1,2),round(x2,2),round(y2,2), w[0] if w else 0))
    inbreg = [reg for reg in r["regions"] if all(-75.6 <= px <= 0.6 and -0.6 <= py <= 68.6 for px, py in reg[:4])]
    print(f"{lay}: boundary-following segments={len(edge)} in-board regions={len(inbreg)}")
    for e in edge[:6]: print("   edge seg", e)
    for reg in inbreg[:8]:
        xs=[p[0] for p in reg]; ys=[p[1] for p in reg]
        print(f"   region n={len(reg)} bbox=({min(xs):.2f},{min(ys):.2f})-({max(xs):.2f},{max(ys):.2f})")
