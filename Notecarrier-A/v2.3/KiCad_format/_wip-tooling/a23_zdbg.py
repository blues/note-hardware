import pcbnew
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
via = None
for t in b.GetTracks():
    if t.GetClass() == "PCB_VIA" and t.GetNetCode() == 0:
        via = t; break
p = via.GetStart()
print("via at kicad", p.x/1e6, p.y/1e6, "film", p.x/1e6-130, 140-p.y/1e6)
print("via layers:", [b.GetLayerName(l) for l in via.GetLayerSet().Seq()])
for z in b.Zones():
    if z.GetIsRuleArea(): continue
    zl = [b.GetLayerName(l) for l in z.GetLayerSet().Seq()]
    for lname in zl:
        lid = b.GetLayerID(lname)
        poly = z.GetFilledPolysList(lid)
        try:
            n = poly.OutlineCount()
        except Exception as e:
            print("  poly err", e); n = -1
        if n and n > 0:
            inside = poly.Contains(pcbnew.VECTOR2I(p.x, p.y))
            if inside:
                print(f"  INSIDE zone net={z.GetNetname()} layer={lname} outlines={n}")
    # also test the raw outline
print("--- zone summary ---")
from collections import Counter
c = Counter()
for z in b.Zones():
    if z.GetIsRuleArea(): c["ruleArea"] += 1; continue
    for l in z.GetLayerSet().Seq():
        lid = l
        poly = z.GetFilledPolysList(lid)
        c[(z.GetNetname(), b.GetLayerName(l), poly.OutlineCount() if poly else 0)] += 1
for k, v in list(c.items())[:20]: print("  ", k, v)
