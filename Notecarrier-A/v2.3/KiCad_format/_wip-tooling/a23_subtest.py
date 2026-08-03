import sys, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse2 import parse
def K(fx, fy): return pcbnew.VECTOR2I(int(round((fx+130.0)*1e6)), int(round((140.0-fy)*1e6)))
def chain(verts):
    # keep every vertex: anti-pad contours legitimately revisit points, and
    # de-duplicating them rewires the shape
    v = list(verts)
    while len(v) > 1 and abs(v[0][0]-v[-1][0]) < 1e-9 and abs(v[0][1]-v[-1][1]) < 1e-9:
        v.pop()
    ch = pcbnew.SHAPE_LINE_CHAIN()
    for x, y in v:
        ch.Append(K(x, y))
    ch.SetClosed(True)
    return ch
r = parse("/scratch/a23-g/07-BOTTOM.art")
dark = [v for pol, v in r["regions"] if pol == "D" and len(v) >= 3 and len(v) > 500]
clear = [v for pol, v in r["regions"] if pol == "C" and len(v) >= 3]
print("dark big:", len(dark), "clear:", len(clear))
pt = K(-17.998, 14.096)
ps = pcbnew.SHAPE_POLY_SET()
ps.AddOutline(chain(dark[0]))
print("after dark add: contains via?", ps.Contains(pt), "outlines", ps.OutlineCount())
for i, v in enumerate(clear):
    c = pcbnew.SHAPE_POLY_SET()
    c.AddOutline(chain(v))
    inside = c.Contains(pt)
    before = ps.Contains(pt)
    ps.BooleanSubtract(c)
    after = ps.Contains(pt)
    xs=[q[0] for q in v]; ys=[q[1] for q in v]
    print(f"  clear[{i}] n={len(v)} bbox=({min(xs):.1f},{min(ys):.1f})-({max(xs):.1f},{max(ys):.1f}) coversPt={inside} -> contains before={before} after={after} outlines={ps.OutlineCount()} holes={sum(ps.HoleCount(j) for j in range(ps.OutlineCount()))}")
