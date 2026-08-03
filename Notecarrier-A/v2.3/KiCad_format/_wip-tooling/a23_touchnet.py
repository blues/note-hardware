"""Last resort for still-net-0 copper: adopt the net of copper it physically
touches on the same layer (fab geometry is the authority)."""
import math, pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
def seg(t):
    return (t.GetStart().x/1e6, t.GetStart().y/1e6, t.GetEnd().x/1e6, t.GetEnd().y/1e6, t.GetWidth()/1e6)
def d_pt_seg(px, py, x1, y1, x2, y2):
    dx, dy = x2-x1, y2-y1
    L2 = dx*dx+dy*dy
    if L2 < 1e-12: return math.hypot(px-x1, py-y1)
    t = max(0.0, min(1.0, ((px-x1)*dx+(py-y1)*dy)/L2))
    return math.hypot(px-(x1+t*dx), py-(y1+t*dy))
for _ in range(8):
    tracks = [t for t in b.GetTracks()]
    known = [t for t in tracks if t.GetNetCode() != 0]
    n0 = [t for t in tracks if t.GetNetCode() == 0]
    if not n0: break
    got = 0
    for t in n0:
        lays = set(t.GetLayerSet().Seq())
        a = seg(t)
        best = None
        for k in known:
            if not (set(k.GetLayerSet().Seq()) & lays): continue
            bb = seg(k)
            d = min(d_pt_seg(a[0], a[1], bb[0], bb[1], bb[2], bb[3]),
                    d_pt_seg(a[2], a[3], bb[0], bb[1], bb[2], bb[3]),
                    d_pt_seg(bb[0], bb[1], a[0], a[1], a[2], a[3]),
                    d_pt_seg(bb[2], bb[3], a[0], a[1], a[2], a[3]))
            if d <= (a[4]+bb[4])/2 + 0.005:
                best = k.GetNetCode(); break
        if best:
            t.SetNetCode(best); got += 1
    print(f"  touch pass: {got} assigned")
    if got == 0: break
left = [t for t in b.GetTracks() if t.GetNetCode() == 0]
print("still net-0:", len(left))
for t in left[:8]:
    print("   ", t.GetClass(), t.GetLayerName(), round(t.GetStart().x/1e6-130,2), round(140-t.GetStart().y/1e6,2))
pcbnew.SaveBoard(PATH, b)
b2 = pcbnew.LoadBoard(PATH); b2.BuildConnectivity()
print("unconnected:", b2.GetConnectivity().GetUnconnectedCount(True))
