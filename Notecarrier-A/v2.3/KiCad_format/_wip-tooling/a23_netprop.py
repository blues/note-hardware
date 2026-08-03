import pcbnew
PATH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PATH)
for _pass in range(12):
    b.BuildConnectivity()
    conn = b.GetConnectivity()
    changed = 0
    for t in b.GetTracks():
        if t.GetNetCode() != 0: continue
        nc = 0
        for p in conn.GetConnectedPads(t):
            if p.GetNetCode() != 0: nc = p.GetNetCode(); break
        if not nc:
            for tt in conn.GetConnectedTracks(t):
                if tt.GetNetCode() != 0: nc = tt.GetNetCode(); break
        if nc:
            t.SetNetCode(nc); changed += 1
    print(f"pass {_pass}: assigned {changed}")
    if changed == 0: break
left = [t for t in b.GetTracks() if t.GetNetCode() == 0]
print("still net-0:", len(left))
from collections import Counter
print(Counter(t.GetLayerName() for t in left))
for t in left[:12]:
    s = (round(t.GetStart().x/1e6-130,2), round(140-t.GetStart().y/1e6,2))
    print("  net0", t.GetClass(), t.GetLayerName(), s)
b.BuildConnectivity()
print("ratsnest unconnected:", b.GetConnectivity().GetUnconnectedCount(True))
pcbnew.SaveBoard(PATH, b)
print("saved")
