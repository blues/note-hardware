"""Rebuild the A v2.3 copper wholesale from the published v20 films.

v20 is a re-layout rather than a tweak (51 parts moved, ~75% of vias differ),
so reconstructing every trace and via from the films is both simpler and more
verifiable than applying a delta - there is no possibility of stale v16 copper
surviving.

Frame (validated against the v2.0 port vs the v16 films, 701/717 tracks):
    film_x = kicad_x - 130      film_y = 140 - kicad_y
"""
import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse

PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
FILMS = [("F.Cu", "04-TOP.art"), ("B.Cu", "07-BOTTOM.art"),
         ("In1.Cu", "05-GND.art"), ("In2.Cu", "06-POWER.art")]

def K(fx, fy):
    return pcbnew.VECTOR2I(int(round((fx + 130.0) * 1e6)), int(round((140.0 - fy) * 1e6)))

def inb(x, y):
    return -75.6 <= x <= 0.6 and -0.6 <= y <= 68.6

b = pcbnew.LoadBoard(PCB)

# ---- clear existing copper tracks/vias ----
old = [t for t in b.GetTracks()]
n_tr = sum(1 for t in old if t.GetClass() == "PCB_TRACK")
n_vi = sum(1 for t in old if t.GetClass() == "PCB_VIA")
for t in old:
    b.Remove(t)
print(f"removed {n_tr} tracks and {n_vi} vias from the v2.0 layout")

# ---- add v20 traces ----
added = 0
for lay, fname in FILMS:
    r = parse(f"/scratch/a23-g/{fname}", xoff=0.0)
    lid = b.GetLayerID(lay)
    n = 0
    for d, x1, y1, x2, y2 in r["draws"]:
        ap = r["apertures"].get(d)
        if not ap or ap[0] != "C" or not ap[1]: continue
        if not (inb(x1, y1) and inb(x2, y2)): continue
        w = ap[1][0]
        if abs(x1-x2) < 1e-9 and abs(y1-y2) < 1e-9:
            continue  # zero-length dots handled separately below
        tr = pcbnew.PCB_TRACK(b)
        tr.SetStart(K(x1, y1)); tr.SetEnd(K(x2, y2))
        tr.SetWidth(int(round(w * 1e6)))
        tr.SetLayer(lid)
        b.Add(tr)
        n += 1
    # zero-length film dots are real copper (Pi lesson) - keep as zero-length
    for d, x1, y1, x2, y2 in r["draws"]:
        ap = r["apertures"].get(d)
        if not ap or ap[0] != "C" or not ap[1]: continue
        if not inb(x1, y1): continue
        if abs(x1-x2) < 1e-9 and abs(y1-y2) < 1e-9:
            tr = pcbnew.PCB_TRACK(b)
            tr.SetStart(K(x1, y1)); tr.SetEnd(K(x1, y1))
            tr.SetWidth(int(round(ap[1][0] * 1e6)))
            tr.SetLayer(lid)
            b.Add(tr)
            n += 1
    print(f"{lay:7s}: {n} traces")
    added += n

# ---- vias: round flashes on both outer films with a plated hole ----
def flashes(path, lo, hi):
    r = parse(path, xoff=0.0)
    out = {}
    for d, x, y in r["flashes"]:
        ap = r["apertures"].get(d)
        if ap and ap[0] == "C" and ap[1] and lo <= ap[1][0] <= hi and inb(x, y):
            out[(round(x, 3), round(y, 3))] = ap[1][0]
    return out

def plated_holes(path):
    sizes, out, sec = [], [], 0
    for line in open(path):
        line = line.strip()
        if line.startswith(";   Holesize"):
            sizes.append(("PLATED" in line and "NON_PLATED" not in line,
                          float(line.split("=")[1].split()[0])))
        if line == "M00": sec += 1
        elif line.startswith("X"):
            xs, ys = line[1:].split("Y")
            if sec < len(sizes) and sizes[sec][0]:
                out.append((float(xs)/1e5, float(ys)/1e5, sizes[sec][1]))
    return out

top = flashes("/scratch/a23-g/04-TOP.art", 0.25, 1.3)
bot = flashes("/scratch/a23-g/07-BOTTOM.art", 0.25, 1.3)
holes = plated_holes("/scratch/a23-g/20210324_notecarrier-m2-al_v20-1-4.drl")
# pad positions to exclude (a via is not a component pad)
padpos = []
for fp in b.GetFootprints():
    for p in fp.Pads():
        padpos.append((p.GetPosition().x/1e6 - 130.0, 140.0 - p.GetPosition().y/1e6))
def is_pad(x, y):
    return any(abs(x-px) < 0.08 and abs(y-py) < 0.08 for px, py in padpos)

nv = 0
for hx, hy, drill in holes:
    if not inb(hx, hy): continue
    if is_pad(hx, hy): continue
    key = None
    for k in top:
        if abs(k[0]-hx) < 0.06 and abs(k[1]-hy) < 0.06: key = k; break
    if key is None: continue
    if not any(abs(k2[0]-hx) < 0.06 and abs(k2[1]-hy) < 0.06 for k2 in bot): continue
    v = pcbnew.PCB_VIA(b)
    v.SetPosition(K(hx, hy))
    v.SetWidth(int(round(top[key] * 1e6)))
    v.SetDrill(int(round(drill * 1e6)))
    v.SetViaType(pcbnew.VIATYPE_THROUGH)
    v.SetLayerPair(b.GetLayerID("F.Cu"), b.GetLayerID("B.Cu"))
    b.Add(v)
    nv += 1
print(f"vias: {nv}")
print(f"total copper items added: {added + nv}")
pcbnew.SaveBoard(PCB, b)
print("saved")
