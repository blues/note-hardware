"""Resolve the net-less pour fragments: adopt the net of the copper they
overlap; if genuinely isolated, keep them net-less but exclude them from the
shorting check by leaving them as plain graphics (fab-accurate isolated copper)."""
import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
CU = {"F.Cu", "B.Cu", "In1.Cu", "In2.Cu"}
frag = [d for d in b.GetDrawings()
        if d.GetClass() == "PCB_SHAPE" and d.GetLayerName() in CU
        and d.ShowShape() == "Polygon" and d.GetNetCode() == 0]
print("net-less fragments:", len(frag))
resolved = 0
for d in frag:
    lid = d.GetLayer()
    poly = d.GetPolyShape()
    votes = {}
    for t in b.GetTracks():
        if t.GetNetCode() == 0: continue
        if t.GetClass() == "PCB_VIA":
            if not t.IsOnLayer(lid): continue
            pts = [t.GetStart()]
        elif t.GetLayer() == lid:
            pts = [t.GetStart(), t.GetEnd()]
        else:
            continue
        if any(poly.Contains(p) for p in pts):
            votes[t.GetNetCode()] = votes.get(t.GetNetCode(), 0) + 1
    if not votes:
        for fp in b.GetFootprints():
            for pad in fp.Pads():
                if pad.GetNetCode() == 0 or not pad.IsOnLayer(lid): continue
                if poly.Contains(pad.GetPosition()):
                    votes[pad.GetNetCode()] = votes.get(pad.GetNetCode(), 0) + 3
    if votes:
        nc = max(votes.items(), key=lambda kv: kv[1])[0]
        d.SetNetCode(nc)
        resolved += 1
        bb = d.GetBoundingBox()
        print(f"   fragment on {d.GetLayerName()} -> {d.GetNetname()}")
print(f"resolved {resolved}, still net-less {len(frag)-resolved} (fab-accurate isolated copper)")
pcbnew.SaveBoard(PATH, b)
