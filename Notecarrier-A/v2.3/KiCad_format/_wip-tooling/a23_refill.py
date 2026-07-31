import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
print("zones:", len([z for z in b.Zones()]))
filler = pcbnew.ZONE_FILLER(b)
filler.Fill(b.Zones())
pcbnew.SaveBoard(PATH, b)
b.BuildConnectivity()
print("unconnected after refill:", b.GetConnectivity().GetUnconnectedCount(True))
