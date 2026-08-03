import sys, math, json
sys.path.insert(0, "/scratch/kd")
src = open("/scratch/kd/a23_copper.py").read()
exec(src[:src.index("v16v = viaset")])
v16v = viaset("a16-g", "TOP.art", "BOTTOM.art", "20210324_notecarrier-m2-al_v16-1-4.drl")
v20v = viaset("a23-g", "04-TOP.art", "07-BOTTOM.art", "20210324_notecarrier-m2-al_v20-1-4.drl")
print("v16 vias", len(v16v), "v20 vias", len(v20v))
print("sample v16:", sorted(v16v.items())[:4])
print("sample v20:", sorted(v20v.items())[:4])
un = []
for k in v20v:
    d = min((math.hypot(k[0]-x, k[1]-y) for x, y in v16v), default=99)
    if d > 0.06: un.append((round(d,3), k))
un.sort()
print("unmatched v20 vias:", len(un), "nearest-dist histogram sample:", un[:8], "...", un[-4:])
# also compare with port vias
import pcbnew
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.0/KiCad_format/Notecarrier-A.kicad_pcb")
pv = [( round(t.GetStart().x/1e6-130.0,2), round(140.0-t.GetStart().y/1e6,2)) for t in b.GetTracks() if t.GetClass()=="PCB_VIA"]
print("v2.0 port vias:", len(pv))
hit = sum(1 for k in pv if any(abs(k[0]-x)<=0.06 and abs(k[1]-y)<=0.06 for x,y in v16v))
print(f"port vias matching my v16 via set: {hit}/{len(pv)}")
