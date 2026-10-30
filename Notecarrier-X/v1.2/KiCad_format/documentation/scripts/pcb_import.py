"""Headless Altium PcbDoc -> .kicad_pcb (KiCad 9 bundled python).
usage: pcb_import.py <in.PcbDoc> <out.kicad_pcb>"""
import sys
import wx
app = wx.App(False)  # the importer reaches wx paths/logging; avoid the missing-wxApp assert
import pcbnew

src, dst = sys.argv[1], sys.argv[2]
b = pcbnew.PCB_IO_MGR.Load(pcbnew.PCB_IO_MGR.ALTIUM_DESIGNER, src)
b.BuildConnectivity()
pcbnew.SaveBoard(dst, b)
print("footprints", len(b.GetFootprints()), "nets", b.GetNetCount(),
      "tracks", len(b.GetTracks()), "zones", b.GetAreaCount())
