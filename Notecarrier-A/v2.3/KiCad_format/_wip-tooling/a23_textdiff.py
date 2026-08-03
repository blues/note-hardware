import sys
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
def strokes(path, x0, y0, x1, y1):
    r = parse(path, xoff=0.0)
    out = []
    for d, a, b_, c, e in r["draws"]:
        if x0 <= a <= x1 and y0 <= b_ <= y1:
            w = r["apertures"].get(d, ("?", (0,)))[1]
            out.append((round(a,3), round(b_,3), round(c,3), round(e,3), w[0] if w else 0))
    return set(out)
W = (-6.0, 44.0, 0.6, 52.0)
s16 = strokes("/scratch/a16-g/BOTTOM.art", *W)
s20 = strokes("/scratch/a23-g/07-BOTTOM.art", *W)
print(f"v16 strokes in doc-text box: {len(s16)}  v20: {len(s20)}")
print(f"identical: {len(s16 & s20)}  only-v16: {len(s16 - s20)}  only-v20: {len(s20 - s16)}")
for s_ in sorted(s16 - s20)[:8]: print("   v16-only", s_)
for s_ in sorted(s20 - s16)[:8]: print("   v20-only", s_)
