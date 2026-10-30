"""Headless Altium PcbDoc -> .kicad_pcb (KiCad 9 bundled python).
usage: pcb_import.py <in.PcbDoc> <out.kicad_pcb>"""
import sys

# No wx.App here: with one, wx collects the importer's warnings (font
# substitutions, unmapped layers) and shows them in a modal dialog at exit,
# which blocks a headless run forever. Without one they go to stderr.
import pcbnew

src, dst = sys.argv[1], sys.argv[2]
b = pcbnew.PCB_IO_MGR.Load(pcbnew.PCB_IO_MGR.ALTIUM_DESIGNER, src)
b.BuildConnectivity()
# aSkipSettings: the imported board has no project; saving project settings
# segfaults in SETTINGS_MANAGER::SaveProjectAs after the board is written.
if not pcbnew.SaveBoard(dst, b, True):
    sys.exit(f"SaveBoard failed for {dst}")
print("footprints", len(b.GetFootprints()), "nets", b.GetNetCount(),
      "tracks", len(b.GetTracks()), "zones", b.GetAreaCount())
