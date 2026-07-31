import sys, math, pcbnew
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse
for name, f in [("v20 TOP", "/scratch/a23-g/04-TOP.art"), ("v20 BOT", "/scratch/a23-g/07-BOTTOM.art"),
                ("v20 GND", "/scratch/a23-g/05-GND.art"), ("v20 PWR", "/scratch/a23-g/06-POWER.art")]:
    r = parse(f, xoff=0.0)
    xs = [x for d,x,y in r["flashes"]]; ys = [y for d,x,y in r["flashes"]]
    print(f"{name}: flashes n={len(xs)} x {min(xs):.1f}..{max(xs):.1f}  y {min(ys):.1f}..{max(ys):.1f}")
# THT pads exist on both films at identical raw coords (Pi lesson) -> use them to calibrate
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
top = parse("/scratch/a23-g/04-TOP.art", xoff=0.0)
bot = parse("/scratch/a23-g/07-BOTTOM.art", xoff=0.0)
tset = {(round(x,3), round(y,3)) for d,x,y in top["flashes"]}
bset = {(round(x,3), round(y,3)) for d,x,y in bot["flashes"]}
common = tset & bset
print("flashes at identical coords on BOTH films:", len(common))
# J9 is a THT header (44 pads) - compare its kicad pads to those common coords
for fp in b.GetFootprints():
    if fp.GetReference() != "J9": continue
    pads = [(p.GetPosition().x/1e6, p.GetPosition().y/1e6) for p in fp.Pads() if p.GetNumber()]
    print("J9 pads:", len(pads), "example kicad", [(round(x,2), round(y,2)) for x,y in pads[:3]])
    for tag, ox in [("x-130", -130.0), ("x-55", -55.0)]:
        best = 0
        for kx, ky in pads:
            fx, fy = kx + ox, 140.0 - ky
            if any(abs(fx-cx) < 0.08 and abs(fy-cy) < 0.08 for cx, cy in common): best += 1
        print(f"   convention {tag}: {best}/{len(pads)} pads hit a both-films flash")
