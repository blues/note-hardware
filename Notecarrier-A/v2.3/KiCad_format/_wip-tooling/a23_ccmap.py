import sys
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
top = parse("/scratch/a23-g/04-TOP.art", xoff=0.0)
# signal pads at film x = -71.04+3.39 = -67.65, y = 13.7603 + k*0.5...
# R33 at px 64.7 -> film -64.7, R32 at -65.9, y 7.8 +/- pads
print("== draws near the CC/R32/R33 corridor (film frame, x -69..-63, y 6..15) ==")
for d, x1, y1, x2, y2 in top["draws"]:
    if -69.5 <= x1 <= -63 and 6 <= y1 <= 15.6:
        w = top["apertures"].get(d, ("?", (0,)))[1]
        print(f"  w={w[0] if w else 0:.2f} ({x1:.3f},{y1:.3f})->({x2:.3f},{y2:.3f})")
