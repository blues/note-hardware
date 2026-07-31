"""The films draw the copper doc-number as strokes; the port carries it as a
PCB_TEXT object, so the imported strokes are duplicate copper - drop them."""
import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
kill = []
for t in b.GetTracks():
    if t.GetClass() != "PCB_TRACK" or t.GetNetCode() != 0: continue
    fx = t.GetStart().x/1e6 - 130.0
    fy = 140.0 - t.GetStart().y/1e6
    w = t.GetWidth()/1e6
    if t.GetLayerName() == "B.Cu" and abs(w - 0.127) < 0.01 and -3.2 <= fx <= -1.4 and 32.0 <= fy <= 49.0:
        kill.append(t)
for t in kill: b.Remove(t)
print(f"removed {len(kill)} duplicate copper-text stroke tracks")
left = [t for t in b.GetTracks() if t.GetNetCode() == 0]
print("net-0 remaining:", len(left))
for t in left:
    print(f"   {t.GetClass()} {t.GetLayerName()} w={t.GetWidth()/1e6:.3f} film=({t.GetStart().x/1e6-130:.2f},{140-t.GetStart().y/1e6:.2f})->({t.GetEnd().x/1e6-130:.2f},{140-t.GetEnd().y/1e6:.2f})")
pcbnew.SaveBoard(PATH, b)
