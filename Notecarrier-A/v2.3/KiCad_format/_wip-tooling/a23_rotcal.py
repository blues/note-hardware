import re, pcbnew
b = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb")
def place(path):
    out = {}
    for line in open(path, errors="replace"):
        m = re.match(r"^(\S+)\s+([\-\d.]+)\s+([\-\d.]+)\s+([\-\d.]+)\s+(\S+)", line)
        if m: out[m.group(1)] = (float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5))
    return out
S = "/scratch/a16-g"
pt = place(f"{S}/PLACETOP.txt"); pb = place(f"{S}/PLACEBOTTOM.txt")
print("ref | side | place(px,py,rot) | kicad(x,y,rot,flip)")
for fp in b.GetFootprints():
    ref = fp.GetReference()
    src = pt.get(ref); side = "T"
    if src is None: src = pb.get(ref); side = "B"
    if src is None: continue
    p = fp.GetPosition()
    kx, ky, kr = p.x/1e6, p.y/1e6, fp.GetOrientationDegrees()
    px, py, pr, _ = src
    if side == "T":
        ex, ey = 130-px, 140-py
    else:
        ex, ey = 55+px, 140-py
    ok = abs(kx-ex) < 0.05 and abs(ky-ey) < 0.05
    if ref in ("R1","C5","J9","J13","J14","DS2","TVS1","J5","J6","OBJ1","FID2","FID4","C7","R8","Q1","RR1","U1","J11"):
        print(f"{ref:5s} {side} place=({px:.2f},{py:.2f},{pr:g}) kicad=({kx:.2f},{ky:.2f},{kr:g}) flip={fp.IsFlipped()} posmatch={ok}")
