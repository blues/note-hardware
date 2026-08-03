import re, pcbnew

PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PCB)

def place(path):
    out = {}
    for line in open(path, errors="replace"):
        m = re.match(r"^(\S+)\s+([\-\d.]+)\s+([\-\d.]+)\s+([\-\d.]+)\s+(\S+)", line)
        if m and not line.startswith(";"):
            out[m.group(1)] = (float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5))
    return out

G = "/scratch/a23-g"
pt, pb = place(f"{G}/PLACETOP.txt"), place(f"{G}/PLACEBOTTOM.txt")

def target(ref):
    if ref in pt: return "T", pt[ref]
    if ref in pb: return "B", pb[ref]
    return None, None

moved = skipped = 0
for fp in b.GetFootprints():
    ref = fp.GetReference()
    side, rec = target(ref)
    if rec is None:
        print(f"  (no place row for {ref})")
        skipped += 1
        continue
    px, py, pr, pkg = rec
    if side == "T":
        kx, ky = 130.0 - px, 140.0 - py
        want_flip = False
        kr = pr
    else:
        kx, ky = 55.0 + px, 140.0 - py
        want_flip = True
        kr = -pr
    kr = kr % 360.0
    cur = fp.GetPosition()
    dpos = ((cur.x/1e6 - kx)**2 + (cur.y/1e6 - ky)**2) ** 0.5
    drot = (fp.GetOrientationDegrees() - kr) % 360
    if fp.IsFlipped() != want_flip:
        fp.Flip(fp.GetPosition(), False)
        print(f"  {ref}: side flipped -> {'B' if want_flip else 'T'}")
    if dpos > 0.005 or min(drot, 360-drot) > 0.01:
        fp.SetPosition(pcbnew.VECTOR2I(int(round(kx*1e6)), int(round(ky*1e6))))
        fp.SetOrientationDegrees(kr)
        moved += 1
        print(f"  {ref}: -> ({kx:.4f},{ky:.4f}) rot {kr:g}  (was d={dpos:.3f}mm, drot={drot:g})")
print(f"moved/rotated: {moved}, no-place-row: {skipped}")
pcbnew.SaveBoard(PCB, b)
print("saved")
