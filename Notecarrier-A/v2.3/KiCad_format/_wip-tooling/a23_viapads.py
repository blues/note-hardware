import sys, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
# Allegro suppresses unused pads on inner layers; reproduce that on the vias
n = 0
for t in b.GetTracks():
    if t.GetClass() == "PCB_VIA":
        t.SetRemoveUnconnected(True)
        t.SetKeepStartEnd(True)
        n += 1
print(f"inner-layer unused-pad suppression set on {n} vias")
# copper doc-number text: v20 artwork
r = parse("/scratch/a23-g/07-BOTTOM.art", xoff=0.0)
gl = [(a, b_, c, e) for d, a, b_, c, e in r["draws"]
      if (r["apertures"].get(d) or ("", (0,)))[1][0] == 0.127
      and -6.0 <= a <= 0.6 and 44.0 <= b_ <= 52.0]
xs = [v for g in gl for v in (g[0], g[2])]
ys = [v for g in gl for v in (g[1], g[3])]
cx, cy = (min(xs)+max(xs))/2, (min(ys)+max(ys))/2
print(f"v20 doc-text glyph bbox: ({min(xs):.3f},{min(ys):.3f})-({max(xs):.3f},{max(ys):.3f}) centre ({cx:.3f},{cy:.3f})")
for d in b.GetDrawings():
    if d.GetClass() == "PCB_TEXT" and d.GetLayerName() == "B.Cu":
        old = d.GetText()
        d.SetText("2017-3047_V20")
        d.SetPosition(pcbnew.VECTOR2I(int(round((cx+130.0)*1e6)), int(round((140.0-cy)*1e6))))
        print(f"copper text {old!r} -> {d.GetText()!r} at film ({cx:.3f},{cy:.3f})")
pcbnew.SaveBoard(PATH, b)
print("saved")
