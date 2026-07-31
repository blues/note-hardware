import sys
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
for f in ("a23-g/04-TOP.art", "a16-g/TOP.art"):
    r = parse(f"/scratch/{f}", xoff=0.0)
    xs = [x for d,x,y in r["flashes"]]; ys = [y for d,x,y in r["flashes"]]
    print(f, "flash extents x", round(min(xs),1), round(max(xs),1), "y", round(min(ys),1), round(max(ys),1), "n", len(xs))
# port board coordinate frame
import pcbnew
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
bb = b.GetBoardEdgesBoundingBox()
print("port Edge.Cuts bbox:", bb.GetX()/1e6, (140-(bb.GetY()+bb.GetHeight())/1e6), "-", (bb.GetX()+bb.GetWidth())/1e6, 140-bb.GetY()/1e6, "size", bb.GetWidth()/1e6, bb.GetHeight()/1e6)
# a known unchanged part: R1 place v16 (51.34,17.29) -> find its kicad pos
for fp in b.GetFootprints():
    if fp.GetReference() in ("R1","J9","PAD1","PAD2","FID1"):
        p = fp.GetPosition()
        print(fp.GetReference(), "kicad", p.x/1e6, p.y/1e6)
