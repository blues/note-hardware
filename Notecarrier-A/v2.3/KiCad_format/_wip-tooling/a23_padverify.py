import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
films = {"F": parse("/scratch/a23-g/04-TOP.art", xoff=0.0), "B": parse("/scratch/a23-g/07-BOTTOM.art", xoff=0.0)}
flashes = {}
for side, r in films.items():
    fl = []
    for d, x, y in r["flashes"]:
        ap = r["apertures"].get(d)
        if not ap: continue
        fl.append((x, y, ap))
    flashes[side] = fl
# board->film: film_x = kicad_x - 130 ... check both conventions on TOP
def to_film(kx, ky, side):
    # top: film x = kx - 130, y = 140 - ky ; bottom: film x = kx - 55 ... test
    if side == "F": return kx - 130.0, 140.0 - ky
    return kx - 55.0, 140.0 - ky
bad = ok = 0
report = []
for fp in b.GetFootprints():
    ref = fp.GetReference()
    side = "B" if fp.IsFlipped() else "F"
    worst = 0.0
    n = 0
    for pad in fp.Pads():
        if not pad.GetNumber(): continue
        p = pad.GetPosition()
        fx, fy = to_film(p.x/1e6, p.y/1e6, side)
        # nearest flash
        best = 9.9
        for x, y, ap in flashes[side]:
            d = math.hypot(x-fx, y-fy)
            if d < best: best = d
        worst = max(worst, best); n += 1
    if n:
        if worst > 0.12: bad += 1; report.append((ref, side, round(worst,3), n))
        else: ok += 1
print(f"footprints pad-exact: {ok}, off: {bad}")
for r in sorted(report, key=lambda t: -t[2])[:25]:
    print("  ", r)
