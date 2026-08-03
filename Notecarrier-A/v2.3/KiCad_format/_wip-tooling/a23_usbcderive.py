"""Derive the USB-C pad naming from the fab's own connectivity.

For each of the 12 signal-pad positions, find which island the fab puts it in,
then look up which other component pads share that island.
"""
import sys, math
sys.path.insert(0, "/scratch/kd")
src = open("/scratch/kd/a23_fabnets.py").read()
exec(src[:src.index("b = pcbnew.LoadBoard(PCB)")])
import pcbnew
b = pcbnew.LoadBoard(PCB)
def to_film(p): return p.x/1e6 - 130.0, 140.0 - p.y/1e6
def locate(fx, fy, tags):
    best = (9.9, None)
    for tag in tags:
        segs, fls, regs, items = layer_data[tag]
        for k, it in items.items():
            d = (d_pt_seg(fx, fy, it[0], it[1], it[2], it[3]) - it[4]/2) if k[1] == "s" \
                else (math.hypot(fx-it[0], fy-it[1]) - it[2])
            if d < best[0]: best = (d, k)
    return best
# every non-J11 pad -> island
isl_pads = {}
for fp in b.GetFootprints():
    if fp.GetReference() == "J11": continue
    for pad in fp.Pads():
        if not pad.GetNumber(): continue
        fx, fy = to_film(pad.GetPosition())
        if not inb(fx, fy): continue
        att = pad.GetAttribute()
        tags = ["F","B","G","P"] if att == pcbnew.PAD_ATTRIB_PTH else (["F"] if pad.IsOnLayer(0) else ["B"])
        d, k = locate(fx, fy, tags)
        if k is None or d > 0.12: continue
        isl_pads.setdefault(uf.find(k), []).append(f"{fp.GetReference()}.{pad.GetNumber()}={pad.GetNetname()}")
# the 12 signal positions from the film: x=-67.65, y = 13.7603 + offsets
CX, CY = -71.04, 13.7603
OFF = [-3.2, -2.4, -1.75, -1.25, -0.75, -0.25, 0.25, 0.75, 1.25, 1.75, 2.4, 3.2]
print("pos  film_y    island contents (other components)")
for i, o in enumerate(OFF, 1):
    fx, fy = CX + 3.39, CY + o
    d, k = locate(fx, fy, ["F"])
    root = uf.find(k) if k else None
    others = isl_pads.get(root, [])
    print(f"{i:3d}  {fy:7.3f}  d={d:.3f}  {others[:6]}")
