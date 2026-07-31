import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
print("footprints:", len(b.GetFootprints()), "tracks:", len(b.GetTracks()), "zones:", b.Zones().size() if hasattr(b.Zones(),'size') else len(list(b.Zones())))
pcbnew.SaveBoard(PATH, b)
print("saved (KiCad 9 format)")
