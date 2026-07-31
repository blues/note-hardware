"""Derive per-part anchor offsets from the v2.0 port (= Allegro v16) and
re-apply them to the v20 placements.

The KiCad footprint origin and the Allegro place origin do not always coincide.
For every part present in both revisions, the v2.0 port gives us the true
offset: delta = actual_v20port_position - transform(v16 place row). Expressed
in the footprint's LOCAL frame it survives a rotation change between the
revisions, so it can be re-applied on top of the v20 place row.
"""
import re, math, pcbnew

V20PORT = "/blues/note-hardware/Notecarrier-A/v2.0/KiCad_format/Notecarrier-A.kicad_pcb"
PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"

def place(path):
    out = {}
    for line in open(path, errors="replace"):
        m = re.match(r"^(\S+)\s+([\-\d.]+)\s+([\-\d.]+)\s+([\-\d.]+)\s+(\S+)", line)
        if m and not line.startswith(";"):
            out[m.group(1)] = (float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5))
    return out

def rows(root):
    t, bt = place(f"{root}/PLACETOP.txt"), place(f"{root}/PLACEBOTTOM.txt")
    out = {}
    for r, v in t.items(): out[r] = ("T",) + v
    for r, v in bt.items(): out[r] = ("B",) + v
    return out

def xform(side, px, py, pr):
    if side == "T":
        return 130.0 - px, 140.0 - py, pr % 360.0
    return 55.0 + px, 140.0 - py, (-pr) % 360.0

v16 = rows("/scratch/a16-g")
v20 = rows("/scratch/a23-g")

old = pcbnew.LoadBoard(V20PORT)
deltas = {}
for fp in old.GetFootprints():
    ref = fp.GetReference()
    if ref not in v16: continue
    side, px, py, pr, pkg = v16[ref]
    ex, ey, er = xform(side, px, py, pr)
    p = fp.GetPosition()
    dx, dy = p.x/1e6 - ex, p.y/1e6 - ey
    rot = fp.GetOrientationDegrees()
    # express the offset in the footprint's local frame
    a = math.radians(rot)
    lx = dx*math.cos(a) + dy*math.sin(a)
    ly = -dx*math.sin(a) + dy*math.cos(a)
    drot = (rot - er) % 360.0
    if ref == "J11":
        # v2.3 replaces J11's footprint; the new USB-C footprint is built
        # directly on the Allegro place origin, so the old part's anchor
        # offset must not carry over.
        lx = ly = 0.0
    deltas[ref] = (lx, ly, drot, side)
    if abs(lx) > 0.005 or abs(ly) > 0.005 or min(drot, 360-drot) > 0.01:
        print(f"  {ref:6s} anchor local=({lx:+.4f},{ly:+.4f}) rotdelta={drot:g}")
print(f"anchor offsets derived for {len(deltas)} parts "
      f"({sum(1 for v in deltas.values() if abs(v[0])>0.005 or abs(v[1])>0.005 or min(v[2],360-v[2])>0.01)} non-zero)")

b = pcbnew.LoadBoard(PCB)
applied = 0
for fp in b.GetFootprints():
    ref = fp.GetReference()
    if ref not in v20: continue
    side, px, py, pr, pkg = v20[ref]
    bx, by, br = xform(side, px, py, pr)
    lx, ly, drot, oldside = deltas.get(ref, (0.0, 0.0, 0.0, side))
    rot = (br + drot) % 360.0
    a = math.radians(rot)
    dx = lx*math.cos(a) - ly*math.sin(a)
    dy = lx*math.sin(a) + ly*math.cos(a)
    kx, ky = bx + dx, by + dy
    want_flip = (side == "B")
    if fp.IsFlipped() != want_flip:
        fp.Flip(fp.GetPosition(), False)
    cur = fp.GetPosition()
    moved = (abs(cur.x/1e6 - kx) > 0.002 or abs(cur.y/1e6 - ky) > 0.002
             or min((fp.GetOrientationDegrees()-rot) % 360, (rot-fp.GetOrientationDegrees()) % 360) > 0.01)
    fp.SetPosition(pcbnew.VECTOR2I(int(round(kx*1e6)), int(round(ky*1e6))))
    fp.SetOrientationDegrees(rot)
    if moved: applied += 1
print(f"placements re-applied with anchors: {applied}")
pcbnew.SaveBoard(PCB, b)
print("saved")
