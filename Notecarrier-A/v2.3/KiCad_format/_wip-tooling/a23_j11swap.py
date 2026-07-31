"""Reload J11's footprint from the corrected local library, preserving pose."""
import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
LIB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A-local.pretty"
b = pcbnew.LoadBoard(PATH)
IO = pcbnew.PCB_IO_KICAD_SEXPR()
old = next(fp for fp in b.GetFootprints() if fp.GetReference() == "J11")
nets = {p.GetNumber(): p.GetNetCode() for p in old.Pads() if p.GetNumber()}
pos, rot, flip = old.GetPosition(), old.GetOrientation(), old.IsFlipped()
val = old.GetValue()
new = IO.FootprintLoad(LIB, "AMPHENOL_12402012E212A")
new.SetReference("J11"); new.SetValue(val)
new.SetPosition(pos); new.SetOrientation(rot)
if new.IsFlipped() != flip: new.Flip(pos, False)
new.SetFPID(pcbnew.LIB_ID("Notecarrier-A-local", "AMPHENOL_12402012E212A"))
for p in new.Pads():
    n = p.GetNumber()
    if n in nets: p.SetNetCode(nets[n])
b.Remove(old); b.Add(new)
print("J11 reloaded with corrected pad order")
for p in sorted(new.Pads(), key=lambda p: p.GetPosition().x):
    if p.GetNumber():
        print(f"   {p.GetNumber():8s} {p.GetNetname():22s} film=({p.GetPosition().x/1e6-130:.3f},{140-p.GetPosition().y/1e6:.3f})")
pcbnew.SaveBoard(PATH, b)
