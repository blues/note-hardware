"""Reproduce the v20 pours exactly, as net-assigned filled copper polygons.

Allegro emits each pour as a set of G36 region fragments that already have all
clearances and thermal reliefs cut in. Importing those fragments verbatim as
filled copper shapes reproduces the fabricated copper exactly - far more
faithful than trying to recover a zone outline and letting KiCad re-pour. This
matches the house convention on the existing ports ("zone fills preserved from
the import - do not refill").

Net for each fragment comes from the copper it contains: pads first, then
tracks/vias. Fragments with nothing in them stay net-less (fab-accurate
isolated copper).
"""
import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse

PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
FILMS = [("F.Cu", "04-TOP.art"), ("B.Cu", "07-BOTTOM.art"),
         ("In1.Cu", "05-GND.art"), ("In2.Cu", "06-POWER.art")]

def inb(x, y): return -75.6 <= x <= 0.6 and -0.6 <= y <= 68.6
def K(fx, fy): return pcbnew.VECTOR2I(int(round((fx+130.0)*1e6)), int(round((140.0-fy)*1e6)))

def in_poly(px, py, poly):
    n = len(poly); c = False
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i+1) % n]
        if ((y1 > py) != (y2 > py)) and (px < (x2-x1)*(py-y1)/(y2-y1) + x1): c = not c
    return c

b = pcbnew.LoadBoard(PCB)

# ---- drop the inherited v16 zones; the fab fragments replace them ----
zones = [z for z in b.Zones() if not z.GetIsRuleArea()]
for z in zones:
    b.Remove(z)
print(f"removed {len(zones)} inherited pour zones (rule areas kept)")

# board items indexed by layer for net lookup
pads_by_layer = {}
items_by_layer = {}
for lay, _ in FILMS:
    lid = b.GetLayerID(lay)
    pl = []
    for fp in b.GetFootprints():
        for p in fp.Pads():
            if not p.GetNumber() or p.GetNetCode() == 0: continue
            if not p.IsOnLayer(lid): continue
            pl.append((p.GetPosition().x/1e6-130.0, 140.0-p.GetPosition().y/1e6, p.GetNetCode(), p.GetNetname()))
    pads_by_layer[lay] = pl
    il = []
    for t in b.GetTracks():
        if t.GetNetCode() == 0: continue
        if t.GetClass() == "PCB_VIA":
            if not t.IsOnLayer(lid): continue
            il.append((t.GetStart().x/1e6-130.0, 140.0-t.GetStart().y/1e6, t.GetNetCode(), t.GetNetname()))
        elif t.GetLayer() == lid:
            il.append((t.GetStart().x/1e6-130.0, 140.0-t.GetStart().y/1e6, t.GetNetCode(), t.GetNetname()))
            il.append((t.GetEnd().x/1e6-130.0, 140.0-t.GetEnd().y/1e6, t.GetNetCode(), t.GetNetname()))
    items_by_layer[lay] = il

total = named = anon = 0
from collections import Counter
per_net = Counter()
for lay, fname in FILMS:
    r = parse(f"/scratch/a23-g/{fname}", xoff=0.0)
    lid = b.GetLayerID(lay)
    regs = [reg for reg in r["regions"] if len(reg) >= 3 and all(inb(px, py) for px, py in reg)]
    for reg in regs:
        xs = [p[0] for p in reg]; ys = [p[1] for p in reg]
        bbox = (min(xs), min(ys), max(xs), max(ys))
        cand = Counter()
        for px, py, nc, nn in pads_by_layer[lay]:
            if bbox[0] <= px <= bbox[2] and bbox[1] <= py <= bbox[3] and in_poly(px, py, reg):
                cand[(nc, nn)] += 3
        if not cand:
            for px, py, nc, nn in items_by_layer[lay]:
                if bbox[0] <= px <= bbox[2] and bbox[1] <= py <= bbox[3] and in_poly(px, py, reg):
                    cand[(nc, nn)] += 1
        sh = pcbnew.PCB_SHAPE(b)
        sh.SetShape(pcbnew.SHAPE_T_POLY)
        chain = pcbnew.SHAPE_LINE_CHAIN()
        seen = set()
        for px, py in reg:
            k = (round(px, 4), round(py, 4))
            if k in seen: continue
            seen.add(k)
            chain.Append(K(px, py))
        chain.SetClosed(True)
        poly = pcbnew.SHAPE_POLY_SET()
        poly.AddOutline(chain)
        sh.SetPolyShape(poly)
        sh.SetFilled(True)
        sh.SetWidth(0)
        sh.SetLayer(lid)
        if cand:
            (nc, nn), _ = cand.most_common(1)[0]
            sh.SetNetCode(nc)
            per_net[nn] += 1
            named += 1
        else:
            anon += 1
        b.Add(sh)
        total += 1
    print(f"{lay:7s}: {len(regs)} fab pour fragments imported")
print(f"total {total} fragments: {named} net-assigned, {anon} left net-less")
print("largest nets by fragment count:", per_net.most_common(8))
pcbnew.SaveBoard(PCB, b)
b2 = pcbnew.LoadBoard(PCB)
b2.BuildConnectivity()
print("unconnected after pour import:", b2.GetConnectivity().GetUnconnectedCount(True))
