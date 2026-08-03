"""Rebuild the v20 pours honouring gerber polarity.

The films draw each pour as dark (%LPD) region fragments with the clearances
and thermal reliefs cut back in as clear (%LPC) regions. Ignoring polarity fills
those cutouts with copper - which is what produced ~900 spurious clearance and
hole-clearance violations. Here the clear regions are subtracted from the dark
ones with SHAPE_POLY_SET booleans before the copper is emitted.
"""
import sys, re, pcbnew
sys.path.insert(0, "/scratch/kd")

PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
FILMS = [("F.Cu", "04-TOP.art"), ("B.Cu", "07-BOTTOM.art"),
         ("In1.Cu", "05-GND.art"), ("In2.Cu", "06-POWER.art")]

def inb(x, y): return -75.6 <= x <= 0.6 and -0.6 <= y <= 68.6
def K(fx, fy): return pcbnew.VECTOR2I(int(round((fx+130.0)*1e6)), int(round((140.0-fy)*1e6)))

from gerbparse2 import parse as parse2

def regions_by_polarity(path):
    """[(polarity, [(x,y), ...]), ...] in file order, from the proven parser"""
    return parse2(path)["regions"]


def split_keyhole(verts):
    """Allegro writes a pour with holes as ONE contour that walks into each hole
    and back out along a zero-width bridge, so a vertex repeats where a hole
    loop closes. Split the contour at repeated vertices into separate closed
    loops, then classify them as outers or holes by containment."""
    pts = [(round(x, 4), round(y, 4)) for x, y in verts]
    loops, stack, seen = [], [], {}
    for pt in pts:
        if pt in seen:
            i = seen[pt]
            loop = stack[i:]
            if len(loop) >= 3:
                loops.append(loop)
            for q in stack[i:]:
                seen.pop(q, None)
            del stack[i:]
            stack.append(pt); seen[pt] = len(stack) - 1
        else:
            stack.append(pt); seen[pt] = len(stack) - 1
    if len(stack) >= 3:
        loops.append(list(stack))
    return loops

def area(loop):
    a = 0.0
    for i in range(len(loop)):
        x1, y1 = loop[i]; x2, y2 = loop[(i+1) % len(loop)]
        a += x1*y2 - x2*y1
    return abs(a)/2.0

def pt_in(loop, pt):
    px, py = pt; c = False
    for i in range(len(loop)):
        x1, y1 = loop[i]; x2, y2 = loop[(i+1) % len(loop)]
        if ((y1 > py) != (y2 > py)) and (px < (x2-x1)*(py-y1)/(y2-y1) + x1): c = not c
    return c

def chain_of(loop):
    ch = pcbnew.SHAPE_LINE_CHAIN()
    for x, y in loop:
        ch.Append(K(x, y))
    ch.SetClosed(True)
    return ch

def to_polyset(verts):
    ch = pcbnew.SHAPE_LINE_CHAIN()
    seen = set()
    for x, y in verts:
        k = (round(x, 4), round(y, 4))
        if k in seen: continue
        seen.add(k)
        ch.Append(K(x, y))
    ch.SetClosed(True)
    loops = split_keyhole(verts)
    ps = pcbnew.SHAPE_POLY_SET()
    if len(loops) <= 1:
        ps.AddOutline(ch)
        return ps
    loops.sort(key=area, reverse=True)
    outers = []
    for lp in loops:
        probe = lp[0]
        parent = None
        for oi, (olp, _) in enumerate(outers):
            if pt_in(olp, probe):
                parent = oi
        if parent is None:
            outers.append((lp, []))
        else:
            outers[parent][1].append(lp)
    for olp, holes in outers:
        idx = ps.AddOutline(chain_of(olp))
        for h in holes:
            ps.AddHole(chain_of(h), idx)
    return ps

b = pcbnew.LoadBoard(PCB)
CU = {"F.Cu", "B.Cu", "In1.Cu", "In2.Cu"}
old = [d for d in b.GetDrawings()
       if d.GetClass() == "PCB_SHAPE" and d.GetLayerName() in CU and d.ShowShape() == "Polygon"]
for d in old:
    b.Remove(d)
print(f"removed {len(old)} polarity-blind pour polygons")

# net lookup sources
def net_sources(lid):
    pads, items = [], []
    for fp in b.GetFootprints():
        for p in fp.Pads():
            if p.GetNumber() and p.GetNetCode() and p.IsOnLayer(lid):
                pads.append((p.GetPosition(), p.GetNetCode(), p.GetNetname()))
    for t in b.GetTracks():
        if not t.GetNetCode(): continue
        if t.GetClass() == "PCB_VIA":
            if t.IsOnLayer(lid): items.append((t.GetStart(), t.GetNetCode(), t.GetNetname()))
        elif t.GetLayer() == lid:
            items.append((t.GetStart(), t.GetNetCode(), t.GetNetname()))
            items.append((t.GetEnd(), t.GetNetCode(), t.GetNetname()))
    return pads, items

from collections import Counter
total = named = anon = 0
for lay, fname in FILMS:
    lid = b.GetLayerID(lay)
    regs = regions_by_polarity(f"/scratch/a23-g/{fname}")
    inboard = [(pol, v) for pol, v in regs if len(v) >= 3 and all(inb(x, y) for x, y in v)]
    dark = [v for pol, v in inboard if pol == "D"]
    clear = [v for pol, v in inboard if pol == "C"]
    acc = pcbnew.SHAPE_POLY_SET()
    for pol, v in inboard:          # film order: dark adds copper, clear cuts it
        if pol == "D": acc.BooleanAdd(to_polyset(v))
        else: acc.BooleanSubtract(to_polyset(v))
    acc.Simplify()
    try:
        acc.Unfracture(pcbnew.SHAPE_POLY_SET.PM_STRICTLY_SIMPLE)
    except Exception:
        pass
    pads, items = net_sources(lid)
    n_out = 0
    for i in range(acc.OutlineCount()):
        one = pcbnew.SHAPE_POLY_SET()
        one.AddOutline(acc.Outline(i))
        for h in range(acc.HoleCount(i)):
            one.AddHole(acc.Hole(i, h))
        votes = Counter()
        for pos, nc, nn in pads:
            if one.Contains(pos): votes[(nc, nn)] += 3
        if not votes:
            for pos, nc, nn in items:
                if one.Contains(pos): votes[(nc, nn)] += 1
        sh = pcbnew.PCB_SHAPE(b)
        sh.SetShape(pcbnew.SHAPE_T_POLY)
        sh.SetPolyShape(one)
        sh.SetFilled(True)
        sh.SetWidth(0)
        sh.SetLayer(lid)
        if votes:
            (nc, nn), _ = votes.most_common(1)[0]
            sh.SetNetCode(nc); named += 1
        else:
            anon += 1
        b.Add(sh)
        n_out += 1
        total += 1
    print(f"{lay:7s}: {len(dark)} dark + {len(clear)} clear fragments -> {n_out} copper areas")
print(f"total {total}: {named} net-assigned, {anon} isolated")
pcbnew.SaveBoard(PCB, b)
b2 = pcbnew.LoadBoard(PCB)
b2.BuildConnectivity()
print("unconnected:", b2.GetConnectivity().GetUnconnectedCount(True))
