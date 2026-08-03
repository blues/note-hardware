"""Add the vias the first pass missed: every plated hole that is not a
component pad becomes a via, taking its annular ring from whichever outer film
flashes it (falling back to the port's default via size)."""
import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
def inb(x, y): return -75.6 <= x <= 0.6 and -0.6 <= y <= 68.6
def K(fx, fy): return pcbnew.VECTOR2I(int(round((fx+130.0)*1e6)), int(round((140.0-fy)*1e6)))
def flashes(path):
    r = parse(path, xoff=0.0)
    out = []
    for d, x, y in r["flashes"]:
        ap = r["apertures"].get(d)
        if ap and ap[0] == "C" and ap[1] and inb(x, y):
            out.append((x, y, ap[1][0]))
    return out
def plated(path):
    sizes, out, sec = [], [], 0
    for line in open(path):
        line = line.strip()
        if line.startswith(";   Holesize"):
            sizes.append(("PLATED" in line and "NON_PLATED" not in line, float(line.split("=")[1].split()[0])))
        if line == "M00": sec += 1
        elif line.startswith("X"):
            xs, ys = line[1:].split("Y")
            if sec < len(sizes) and sizes[sec][0]: out.append((float(xs)/1e5, float(ys)/1e5, sizes[sec][1]))
    return out
top, bot = flashes("/scratch/a23-g/04-TOP.art"), flashes("/scratch/a23-g/07-BOTTOM.art")
holes = [h for h in plated("/scratch/a23-g/20210324_notecarrier-m2-al_v20-1-4.drl") if inb(h[0], h[1])]
padpos = []
for fp in b.GetFootprints():
    for p in fp.Pads():
        if p.GetAttribute() in (pcbnew.PAD_ATTRIB_PTH, pcbnew.PAD_ATTRIB_NPTH):
            padpos.append((p.GetPosition().x/1e6-130.0, 140.0-p.GetPosition().y/1e6))
existing = [(t.GetStart().x/1e6-130.0, 140.0-t.GetStart().y/1e6) for t in b.GetTracks() if t.GetClass() == "PCB_VIA"]
def near(x, y, lst, tol): return any(abs(x-a) < tol and abs(y-c) < tol for a, c in lst)
added = 0
for hx, hy, dr in holes:
    if near(hx, hy, padpos, 0.10): continue
    if near(hx, hy, existing, 0.06): continue
    ring = None
    for fx, fy, w in top + bot:
        if abs(fx-hx) < 0.06 and abs(fy-hy) < 0.06 and w > dr:
            ring = w if ring is None else min(ring, w)
    if ring is None: ring = dr + 0.25
    v = pcbnew.PCB_VIA(b)
    v.SetPosition(K(hx, hy)); v.SetWidth(int(round(ring*1e6))); v.SetDrill(int(round(dr*1e6)))
    v.SetViaType(pcbnew.VIATYPE_THROUGH)
    v.SetLayerPair(b.GetLayerID("F.Cu"), b.GetLayerID("B.Cu"))
    b.Add(v); added += 1
print(f"vias added in second pass: {added}")
print("total vias now:", sum(1 for t in b.GetTracks() if t.GetClass() == "PCB_VIA"))
pcbnew.SaveBoard(PATH, b)
