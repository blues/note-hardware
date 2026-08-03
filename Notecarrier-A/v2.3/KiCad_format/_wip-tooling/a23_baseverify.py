import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
# v2.0 port vs v16 film -> what was already "off" before my delta
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.0/KiCad_format/Notecarrier-A.kicad_pcb")
films = {"F": parse("/scratch/a16-g/TOP.art", xoff=0.0), "B": parse("/scratch/a16-g/BOTTOM.art", xoff=0.0)}
grid = {}
for s_, r in films.items():
    for d, x, y in r["flashes"]:
        grid.setdefault((s_, int(x//1), int(y//1)), []).append((x, y))
def nearest(s_, fx, fy):
    best = 9.9
    for gx in (int(fx//1)-1, int(fx//1), int(fx//1)+1):
        for gy in (int(fy//1)-1, int(fy//1), int(fy//1)+1):
            for x, y in grid.get((s_, gx, gy), []):
                d = math.hypot(x-fx, y-fy)
                if d < best: best = d
    return best
out = {}
for fp in b.GetFootprints():
    side = "B" if fp.IsFlipped() else "F"
    worst = 0.0; n = 0
    for pad in fp.Pads():
        if not pad.GetNumber(): continue
        p = pad.GetPosition()
        fx = p.x/1e6 - (130.0 if side == "F" else 55.0)
        fy = 140.0 - p.y/1e6
        worst = max(worst, nearest(side, fx, fy)); n += 1
    if n: out[fp.GetReference()] = round(worst, 3)
print("v2.0 port vs v16 film — parts NOT pad-exact (pre-existing):")
for ref, w in sorted(out.items(), key=lambda t: -t[1]):
    if w > 0.12: print(f"   {ref:6s} {w}")
