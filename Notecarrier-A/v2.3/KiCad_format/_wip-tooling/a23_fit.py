"""Fit the remaining off-placement parts directly to the v20 film flashes.

For each part, search rotation x translation for the pose whose pads best
coincide with film flashes. Only applied when the fit is unambiguous (worst
pad error under 0.06 mm) - otherwise reported for review.
"""
import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse

PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PCB)
films = {"F": parse("/scratch/a23-g/04-TOP.art", xoff=0.0),
         "B": parse("/scratch/a23-g/07-BOTTOM.art", xoff=0.0)}
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

def worst_at(fp, side, dx, dy):
    w = 0.0
    for pad in fp.Pads():
        if not pad.GetNumber(): continue
        p = pad.GetPosition()
        fx = p.x/1e6 + dx - 130.0
        fy = 140.0 - (p.y/1e6 + dy)
        w = max(w, nearest(side, fx, fy))
        if w > 5: return w
    return w

TARGETS = ["Q1", "J8", "ANT2", "J9"]
for fp in b.GetFootprints():
    ref = fp.GetReference()
    if ref not in TARGETS: continue
    side = "B" if fp.IsFlipped() else "F"
    base_rot = fp.GetOrientationDegrees()
    base_pos = fp.GetPosition()
    best = (worst_at(fp, side, 0, 0), 0.0, 0.0, base_rot)
    for dr in (0, 90, 180, 270):
        fp.SetOrientationDegrees((base_rot + dr) % 360)
        # coarse then fine translation search
        span, step = 3.0, 0.25
        cx = cy = 0.0
        for _ in range(3):
            n = int(span/step)
            local = None
            for i in range(-n, n+1):
                for j in range(-n, n+1):
                    dx, dy = cx + i*step, cy + j*step
                    w = worst_at(fp, side, dx, dy)
                    if local is None or w < local[0]:
                        local = (w, dx, dy)
            cx, cy = local[1], local[2]
            span, step = step*1.5, step/5
            if local[0] < best[0]:
                best = (local[0], local[1], local[2], (base_rot + dr) % 360)
    fp.SetOrientationDegrees(base_rot)
    w, dx, dy, rot = best
    print(f"{ref:6s} best fit: worst={w:.4f}mm  translate=({dx:+.4f},{dy:+.4f}) rot={rot:g} (was {base_rot:g})")
    if w < 0.06 and (abs(dx) > 0.002 or abs(dy) > 0.002 or rot != base_rot):
        fp.SetOrientationDegrees(rot)
        fp.SetPosition(pcbnew.VECTOR2I(int(round((base_pos.x/1e6 + dx)*1e6)),
                                       int(round((base_pos.y/1e6 + dy)*1e6))))
        print(f"       -> applied")
    elif w >= 0.06:
        print(f"       -> NOT applied (ambiguous / pads not flashed in film)")
pcbnew.SaveBoard(PCB, b)
print("saved")
