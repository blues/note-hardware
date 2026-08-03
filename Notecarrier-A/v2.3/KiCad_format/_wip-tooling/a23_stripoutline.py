import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
# the films draw the board outline on every copper layer; those strokes are not
# traces. They run along x=-75/0 or y=0/68 in film coords (kicad x 55/130, y 72/140).
OUTLINE = [((-70.0, 68.0), (-5.0, 68.0)), ((0.0, 63.0), (0.0, 20.4)),
           ((0.0, 18.2), (0.0, 5.0)), ((-5.0, 0.0), (-70.0, 0.0)),
           ((-75.0, 5.0), (-75.0, 63.0))]
def canon(a, b_): return (min(a, b_), max(a, b_))
kill = {canon(a, b_) for a, b_ in OUTLINE}
removed = []
for t in list(b.GetTracks()):
    if t.GetClass() != "PCB_TRACK": continue
    s = (round(t.GetStart().x/1e6 - 130.0, 2), round(140.0 - t.GetStart().y/1e6, 2))
    e = (round(t.GetEnd().x/1e6 - 130.0, 2), round(140.0 - t.GetEnd().y/1e6, 2))
    if canon(s, e) in kill:
        removed.append((t.GetLayerName(), s, e))
        b.Remove(t)
print(f"removed {len(removed)} outline strokes from copper layers")
from collections import Counter
print(Counter(r[0] for r in removed))
# arcs on the films are chorded into many short segments; nothing to do.
pcbnew.SaveBoard(PATH, b)
print("saved")
