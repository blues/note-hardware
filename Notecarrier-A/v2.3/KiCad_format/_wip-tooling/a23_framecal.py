"""Validate the film frame per layer using the v2.0 port's own copper
(the port is validated against v16, so its tracks must lie on the v16 films)."""
import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.0/KiCad_format/Notecarrier-A.kicad_pcb")
films = {"F.Cu": "/scratch/a16-g/TOP.art", "B.Cu": "/scratch/a16-g/BOTTOM.art",
         "In1.Cu": "/scratch/a16-g/GND.art", "In2.Cu": "/scratch/a16-g/POWER.art"}
for lay, path in films.items():
    r = parse(path, xoff=0.0)
    segs = set()
    for d, x1, y1, x2, y2 in r["draws"]:
        segs.add(((round(x1,2), round(y1,2)), (round(x2,2), round(y2,2))))
        segs.add(((round(x2,2), round(y2,2)), (round(x1,2), round(y1,2))))
    tracks = [t for t in b.GetTracks() if t.GetClass() == "PCB_TRACK" and t.GetLayerName() == lay]
    for tag, ox in [("x-130", -130.0), ("x-55", -55.0)]:
        hit = 0
        for t in tracks:
            s = (round(t.GetStart().x/1e6 + ox, 2), round(140.0 - t.GetStart().y/1e6, 2))
            e = (round(t.GetEnd().x/1e6 + ox, 2), round(140.0 - t.GetEnd().y/1e6, 2))
            if (s, e) in segs: hit += 1
        print(f"{lay:7s} {tag}: {hit}/{len(tracks)} tracks match a film segment exactly")
