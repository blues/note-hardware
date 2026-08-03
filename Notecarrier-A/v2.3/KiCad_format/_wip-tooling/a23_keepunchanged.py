"""Parts whose v16 and v20 place rows are identical keep the validated v2.0
port's exact pose - no re-derivation, no drift."""
import re, pcbnew
def place(path):
    out = {}
    for line in open(path, errors="replace"):
        m = re.match(r"^(\S+)\s+([\-\d.]+)\s+([\-\d.]+)\s+([\-\d.]+)\s+(\S+)", line)
        if m and not line.startswith(";"):
            out[m.group(1)] = (float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5))
    return out
def rows(root):
    t, bt = place(f"{root}/PLACETOP.txt"), place(f"{root}/PLACEBOTTOM.txt")
    return {**{r: ("T",) + v for r, v in t.items()}, **{r: ("B",) + v for r, v in bt.items()}}
v16, v20 = rows("/scratch/a16-g"), rows("/scratch/a23-g")
unchanged = {r for r in set(v16) & set(v20) if v16[r] == v20[r]}
print(f"unchanged parts: {len(unchanged)}")
old = pcbnew.LoadBoard("/blues/note-hardware/Notecarrier-A/v2.0/KiCad_format/Notecarrier-A.kicad_pcb")
pose = {}
for fp in old.GetFootprints():
    pose[fp.GetReference()] = (fp.GetPosition(), fp.GetOrientationDegrees(), fp.IsFlipped())
PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
b = pcbnew.LoadBoard(PCB)
restored = 0
for fp in b.GetFootprints():
    ref = fp.GetReference()
    if ref not in unchanged or ref not in pose: continue
    p, rot, flip = pose[ref]
    if fp.IsFlipped() != flip:
        fp.Flip(fp.GetPosition(), False)
    moved = (fp.GetPosition() != p) or abs(fp.GetOrientationDegrees() - rot) > 0.001
    fp.SetPosition(p)
    fp.SetOrientationDegrees(rot)
    if moved:
        restored += 1
        print(f"  {ref} restored to v2.0 pose")
print(f"restored: {restored}")
pcbnew.SaveBoard(PCB, b)
print("saved")
