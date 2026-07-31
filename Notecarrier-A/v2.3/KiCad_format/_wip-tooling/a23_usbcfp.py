import sys, re
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
# J11 v20 place: (71.04, 13.7603) rot -90 TOP -> film center (-71.04, 13.7603)
CX, CY = -71.04, 13.7603
top = parse("/scratch/a23-g/04-TOP.art", xoff=0.0)
print("== TOP flashes within 6mm of J11 center (rel coords, film frame):")
for d, x, y in top["flashes"]:
    if abs(x-CX) < 6 and abs(y-CY) < 6:
        ap = top["apertures"].get(d)
        print(f"   {ap} rel=({x-CX:+.4f},{y-CY:+.4f})")
print("== plated drill holes near J11:")
sec = 0
sizes = []
for line in open("/scratch/a23-g/20210324_notecarrier-m2-al_v20-1-4.drl"):
    line = line.strip()
    if line.startswith(";   Holesize"):
        sizes.append(line)
    if line == "M00": sec += 1
    if line.startswith("X"):
        xs, ys = line[1:].split("Y")
        hx, hy = float(xs)/1e5, float(ys)/1e5
        if abs(hx-CX) < 6 and abs(hy-CY) < 6:
            print(f"   hole sec{sec} rel=({hx-CX:+.4f},{hy-CY:+.4f})")
for s_ in sizes: print("  ", s_)
