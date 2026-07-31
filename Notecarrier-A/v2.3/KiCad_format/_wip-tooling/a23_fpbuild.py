import pcbnew, math, os
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
# rotation convention from TVS1 (rot -90)
for fp in b.GetFootprints():
    if fp.GetReference() == "TVS1":
        print("TVS1 rot", fp.GetOrientationDegrees())
        for p in fp.Pads():
            rel = p.GetFPRelativePosition()
            ab = p.GetPosition()
            fpp = fp.GetPosition()
            print(f"  pad {p.GetNumber()}: local=({rel.x/1e6:.3f},{rel.y/1e6:.3f}) absdelta=({(ab.x-fpp.x)/1e6:.3f},{(ab.y-fpp.y)/1e6:.3f})")
