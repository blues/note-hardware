import sys, math
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
import pcbnew
bot = parse("/scratch/a23-g/07-BOTTOM.art", xoff=0.0)
# chain-follow from each via
def follow(start, maxhop=60):
    segs = [(x1,y1,x2,y2) for d,x1,y1,x2,y2 in bot["draws"]]
    path = [start]
    cur = start
    used = set()
    for _ in range(maxhop):
        found = None
        for i,(x1,y1,x2,y2) in enumerate(segs):
            if i in used: continue
            if math.hypot(x1-cur[0], y1-cur[1]) < 0.12: found = (i,(x2,y2)); break
            if math.hypot(x2-cur[0], y2-cur[1]) < 0.12: found = (i,(x1,y1)); break
        if not found: break
        used.add(found[0])
        cur = found[1]
        path.append(cur)
    return path
for name, v in [("viaA(pad rel -0.75)", (-69.7688, 12.9286)), ("viaB(pad rel -0.25)", (-69.733, 13.633))]:
    p = follow(v)
    print(name, "->", [(round(a,2), round(b,2)) for a,b in p[-3:]], f"({len(p)} pts)")
# J6 pins 7/9 fab positions: from port J6 pad offsets + v20 place (31.9481,14.2254,180)
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
for fp in b.GetFootprints():
    if fp.GetReference() == "J6":
        for pad in fp.Pads():
            if pad.GetNumber() in ("7","9","13"):
                p = pad.GetPosition()
                print("current-port J6." + pad.GetNumber(), pad.GetNetname(), "kicad", round(p.x/1e6,2), round(p.y/1e6,2))
