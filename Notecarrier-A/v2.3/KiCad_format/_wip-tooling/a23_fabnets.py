"""Trace the published v20 films into connected copper islands, then
  (a) name every island from the port pads that touch it,
  (b) assign those names to board tracks/vias that still have no net,
  (c) report islands whose pads disagree (real shorts or mis-wiring).

Frame: film_x = kicad_x - 130, film_y = 140 - kicad_y (validated).
"""
import sys, math, json, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse

TOL = 0.02
PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
LAYERS = [("F", "04-TOP.art"), ("B", "07-BOTTOM.art"), ("G", "05-GND.art"), ("P", "06-POWER.art")]

def inb(x, y): return -75.6 <= x <= 0.6 and -0.6 <= y <= 68.6

class UF:
    def __init__(s): s.p = {}
    def find(s, a):
        r = a
        while s.p.setdefault(r, r) != r: r = s.p[r]
        while s.p[a] != r: s.p[a], a = r, s.p[a]
        return r
    def join(s, a, b): s.p[s.find(a)] = s.find(b)

def d_pt_seg(px, py, x1, y1, x2, y2):
    dx, dy = x2-x1, y2-y1
    L2 = dx*dx + dy*dy
    if L2 < 1e-12: return math.hypot(px-x1, py-y1)
    t = max(0.0, min(1.0, ((px-x1)*dx + (py-y1)*dy)/L2))
    return math.hypot(px-(x1+t*dx), py-(y1+t*dy))

def segs_cross(a, b):
    x1,y1,x2,y2 = a[:4]; x3,y3,x4,y4 = b[:4]
    d1 = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1); d2 = (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
    d3 = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3); d4 = (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
    if ((d1>0)!=(d2>0)) and ((d3>0)!=(d4>0)): return 0.0
    return min(d_pt_seg(x1,y1,x3,y3,x4,y4), d_pt_seg(x2,y2,x3,y3,x4,y4),
               d_pt_seg(x3,y3,x1,y1,x2,y2), d_pt_seg(x4,y4,x1,y1,x2,y2))

def in_poly(px, py, poly):
    n = len(poly); c = False
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i+1) % n]
        if ((y1 > py) != (y2 > py)) and (px < (x2-x1)*(py-y1)/(y2-y1) + x1): c = not c
    return c

def near_edge(px, py, poly, rad):
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i+1) % n]
        if d_pt_seg(px, py, x1, y1, x2, y2) <= rad: return True
    return False

uf = UF()
layer_data = {}
for tag, fname in LAYERS:
    r = parse(f"/scratch/a23-g/{fname}", xoff=0.0)
    segs, fls, regs = [], [], []
    for d, x1, y1, x2, y2 in r["draws"]:
        ap = r["apertures"].get(d)
        if not ap or not ap[1]: continue
        w = ap[1][0]
        if w < 0.05 or not (inb(x1, y1) and inb(x2, y2)): continue
        segs.append((x1, y1, x2, y2, w))
    for d, x, y in r["flashes"]:
        ap = r["apertures"].get(d)
        if not ap or not inb(x, y): continue
        shp, prm = ap
        rr = prm[0]/2 if shp == "C" else min(prm[0], prm[1])/2 if len(prm) > 1 else prm[0]/2
        fls.append((x, y, rr))
    # Allegro emits one pour as many G36 fragments; treating each as a filled
    # polygon merges everything through clearance channels, so regions are
    # excluded from the connectivity trace (traces/flashes/holes only).
    for reg in r["regions"]:
        if False: regs.append(reg)
    # grid index for same-layer contact
    grid = {}
    items = {}
    def put(key, x1, y1, x2, y2, pad=0.7):
        for gx in range(int((min(x1,x2)-pad)//2), int((max(x1,x2)+pad)//2)+1):
            for gy in range(int((min(y1,y2)-pad)//2), int((max(y1,y2)+pad)//2)+1):
                grid.setdefault((gx, gy), []).append(key)
    for i, s in enumerate(segs):
        k = (tag, "s", i); items[k] = s; uf.find(k); put(k, s[0], s[1], s[2], s[3])
    for i, f in enumerate(fls):
        k = (tag, "f", i); items[k] = f; uf.find(k); put(k, f[0], f[1], f[0], f[1])
    checked = set()
    for cell, ks in grid.items():
        for i in range(len(ks)):
            for j in range(i+1, len(ks)):
                a, b_ = ks[i], ks[j]
                pair = (a, b_) if a < b_ else (b_, a)
                if pair in checked: continue
                checked.add(pair)
                ia, ib = items[a], items[b_]
                ta, tb = a[1], b_[1]
                if ta == "s" and tb == "s":
                    if segs_cross(ia, ib) <= (ia[4]+ib[4])/2 + TOL: uf.join(a, b_)
                elif ta == "s" and tb == "f":
                    # a trace joins a pad when the trace END lies in the pad, or
                    # the pad centre lies under the trace - not when a wide trace
                    # merely reaches past a neighbouring pad
                    if (min(math.hypot(ib[0]-ia[0], ib[1]-ia[1]),
                            math.hypot(ib[0]-ia[2], ib[1]-ia[3])) <= ib[2] + TOL
                        or d_pt_seg(ib[0], ib[1], ia[0], ia[1], ia[2], ia[3]) <= ia[4]/2 + TOL): uf.join(a, b_)
                elif ta == "f" and tb == "s":
                    if (min(math.hypot(ia[0]-ib[0], ia[1]-ib[1]),
                            math.hypot(ia[0]-ib[2], ia[1]-ib[3])) <= ia[2] + TOL
                        or d_pt_seg(ia[0], ia[1], ib[0], ib[1], ib[2], ib[3]) <= ib[4]/2 + TOL): uf.join(a, b_)
                else:
                    if math.hypot(ia[0]-ib[0], ia[1]-ib[1]) <= ia[2] + ib[2] + TOL: uf.join(a, b_)
    for ri, reg in enumerate(regs):
        rk = (tag, "r", ri); uf.find(rk)
        for k, it in items.items():
            if k[1] == "s":
                if (in_poly(it[0], it[1], reg) or in_poly(it[2], it[3], reg)
                        or near_edge(it[0], it[1], reg, it[4]/2+TOL) or near_edge(it[2], it[3], reg, it[4]/2+TOL)):
                    uf.join(rk, k)
            else:
                if in_poly(it[0], it[1], reg) or near_edge(it[0], it[1], reg, it[2]+TOL):
                    uf.join(rk, k)
        step = max(1, len(reg)//10)
        for rj in range(ri):
            if any(in_poly(px, py, regs[rj]) for px, py in reg[::step]): uf.join(rk, (tag, "r", rj))
    layer_data[tag] = (segs, fls, regs, items)
    print(f"{tag}: segs {len(segs)} flashes {len(fls)} regions {len(regs)}")

# plated holes join all layers
def plated_holes(path):
    sizes, out, sec = [], [], 0
    for line in open(path):
        line = line.strip()
        if line.startswith(";   Holesize"):
            sizes.append(("PLATED" in line and "NON_PLATED" not in line, float(line.split("=")[1].split()[0])))
        if line == "M00": sec += 1
        elif line.startswith("X"):
            xs, ys = line[1:].split("Y")
            if sec < len(sizes) and sizes[sec][0]:
                out.append((float(xs)/1e5, float(ys)/1e5, sizes[sec][1]))
    return out

holes = [h for h in plated_holes("/scratch/a23-g/20210324_notecarrier-m2-al_v20-1-4.drl") if inb(h[0], h[1])]
for hi, (hx, hy, dr) in enumerate(holes):
    hk = ("H", hi); uf.find(hk)
    hr = dr/2
    for tag, (segs, fls, regs, items) in layer_data.items():
        for k, it in items.items():
            if k[1] == "s":
                if d_pt_seg(hx, hy, it[0], it[1], it[2], it[3]) <= it[4]/2 + TOL: uf.join(hk, k)
            else:
                if math.hypot(hx-it[0], hy-it[1]) <= it[2] + TOL: uf.join(hk, k)
        for ri, reg in enumerate(regs):
            if in_poly(hx, hy, reg): uf.join(hk, (tag, "r", ri))
print(f"plated holes: {len(holes)}")

HOLE_AT = {}
for hi, (hx, hy, dr) in enumerate(holes):
    HOLE_AT[(round(hx, 2), round(hy, 2))] = hi

def hole_island(fx, fy, tol=0.06):
    for (hx, hy), hi in HOLE_AT.items():
        if abs(hx-fx) < tol and abs(hy-fy) < tol:
            return uf.find(("H", hi))
    return None

b = pcbnew.LoadBoard(PCB)
def to_film(p): return p.x/1e6 - 130.0, 140.0 - p.y/1e6

def locate(fx, fy, tags, rad=0.0):
    """island key nearest to a point on any of the given layers"""
    best = (9.9, None)
    for tag in tags:
        segs, fls, regs, items = layer_data[tag]
        for k, it in items.items():
            if k[1] == "s":
                d = d_pt_seg(fx, fy, it[0], it[1], it[2], it[3]) - it[4]/2
            else:
                d = math.hypot(fx-it[0], fy-it[1]) - it[2]
            if d < best[0]: best = (d, k)
        for ri, reg in enumerate(regs):
            if in_poly(fx, fy, reg): return (0.0, (tag, "r", ri))
    return best

# island -> nets from pads
isl_nets = {}
pads_seen = 0
for fp in b.GetFootprints():
    for pad in fp.Pads():
        if not pad.GetNumber() or not pad.GetNetname(): continue
        fx, fy = to_film(pad.GetPosition())
        if not inb(fx, fy): continue
        att = pad.GetAttribute()
        root = None
        if att in (pcbnew.PAD_ATTRIB_PTH,):
            # plated holes are exact in the drill file - use them as the anchor
            root = hole_island(fx, fy)
        if root is None:
            tags = ["F"] if pad.IsOnLayer(b.GetLayerID("F.Cu")) else ["B"]
            d, k = locate(fx, fy, tags)
            # the pad must genuinely sit on the copper, not merely near it
            if k is None or d > 0.02: continue
            root = uf.find(k)
        isl_nets.setdefault(root, {}).setdefault(pad.GetNetname(), []).append(f"{fp.GetReference()}.{pad.GetNumber()}")
        pads_seen += 1
print(f"pads mapped to islands: {pads_seen}")

conflicts = [(sorted(v), root) for root, v in isl_nets.items() if len(v) > 1]
print(f"islands with conflicting nets: {len(conflicts)}")
for nets, root in conflicts[:20]:
    print("   nets:", nets, "| pads:", [p for n in nets for p in isl_nets[root][n]][:10])

# assign nets to net-0 board items
nets_by_name = {}
def netcode(name):
    ni = b.FindNet(name)
    return ni.GetNetCode() if ni else 0
assigned = unresolved = 0
for t in b.GetTracks():
    if t.GetNetCode() != 0: continue
    root = None
    if t.GetClass() == "PCB_VIA":
        fx, fy = to_film(t.GetStart())
        root = hole_island(fx, fy)
    else:
        fx, fy = to_film(t.GetStart())
        tags = {"F.Cu": ["F"], "B.Cu": ["B"], "In1.Cu": ["G"], "In2.Cu": ["P"]}[t.GetLayerName()]
        d, k = locate(fx, fy, tags)
        if k is not None and d <= 0.02: root = uf.find(k)
    cand = isl_nets.get(root)
    if cand and len(cand) == 1:
        nc = netcode(list(cand)[0])
        if nc:
            t.SetNetCode(nc); assigned += 1
            continue
    unresolved += 1
print(f"net-0 items assigned from fab islands: {assigned}, unresolved: {unresolved}")
pcbnew.SaveBoard(PCB, b)
b2 = pcbnew.LoadBoard(PCB)
b2.BuildConnectivity()
print("unconnected after assignment:", b2.GetConnectivity().GetUnconnectedCount(True))
