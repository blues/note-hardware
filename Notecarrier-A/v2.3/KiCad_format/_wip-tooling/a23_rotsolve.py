import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PCB)
films = {"F": parse("/scratch/a23-g/04-TOP.art", xoff=0.0), "B": parse("/scratch/a23-g/07-BOTTOM.art", xoff=0.0)}
fl = {s: [(x, y) for d, x, y in r["flashes"]] for s, r in films.items()}
# grid index
grid = {}
for s, pts in fl.items():
    for x, y in pts:
        grid.setdefault((s, int(x//1), int(y//1)), []).append((x, y))
def nearest(s, fx, fy):
    best = 9.9
    for gx in (int(fx//1)-1, int(fx//1), int(fx//1)+1):
        for gy in (int(fy//1)-1, int(fy//1), int(fy//1)+1):
            for x, y in grid.get((s, gx, gy), []):
                d = math.hypot(x-fx, y-fy)
                if d < best: best = d
    return best
def to_film(kx, ky, side):
    return (kx - 130.0 if side == "F" else kx - 55.0), 140.0 - ky
def score(fp):
    side = "B" if fp.IsFlipped() else "F"
    worst = 0.0
    for pad in fp.Pads():
        if not pad.GetNumber(): continue
        p = pad.GetPosition()
        fx, fy = to_film(p.x/1e6, p.y/1e6, side)
        worst = max(worst, nearest(side, fx, fy))
    return worst
TARGETS = ["ANT1","TVS1","J13","J3","DS4","J6","J14","J4","J12","DS5","Q1","ANT2","J9","J7","J8"]
fixed = 0
for fp in b.GetFootprints():
    if fp.GetReference() not in TARGETS: continue
    ref = fp.GetReference()
    base = fp.GetOrientationDegrees()
    cands = []
    for dr in (0, 90, 180, 270):
        fp.SetOrientationDegrees((base + dr) % 360)
        cands.append((score(fp), dr))
    cands.sort()
    bestscore, bestdr = cands[0]
    fp.SetOrientationDegrees((base + bestdr) % 360)
    print(f"{ref:6s} base={base:g} best=+{bestdr:g} -> worst {bestscore:.3f}mm  (was {[f'{s:.2f}@{d}' for s,d in cands]})")
    if bestdr: fixed += 1
print("rotations corrected:", fixed)
pcbnew.SaveBoard(PCB, b)
print("saved")
