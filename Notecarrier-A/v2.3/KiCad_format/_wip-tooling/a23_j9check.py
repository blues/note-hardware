import math, pcbnew
def plated(path):
    sizes, out, sec = [], [], 0
    for line in open(path):
        line = line.strip()
        if line.startswith(";   Holesize"):
            sizes.append((("PLATED" in line and "NON_PLATED" not in line), float(line.split("=")[1].split()[0])))
        if line == "M00": sec += 1
        elif line.startswith("X"):
            xs, ys = line[1:].split("Y")
            if sec < len(sizes): out.append((float(xs)/1e5, float(ys)/1e5, sizes[sec][1], sizes[sec][0]))
    return out
h20 = plated("/scratch/a23-g/20210324_notecarrier-m2-al_v20-1-4.drl")
for ref in ("J9", "J6"):
    for board, tag in [("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb", "v2.3"),
                       ("/blues/note-hardware/Notecarrier-A/v2.0/KiCad_format/Notecarrier-A.kicad_pcb", "v2.0")]:
        b = pcbnew.LoadBoard(board)
        fp = next((f for f in b.GetFootprints() if f.GetReference() == ref), None)
        if not fp: continue
        worst = 0.0; n = 0; hits = 0
        for p in fp.Pads():
            if not p.GetNumber(): continue
            if p.GetAttribute() not in (pcbnew.PAD_ATTRIB_PTH, pcbnew.PAD_ATTRIB_NPTH): continue
            fx, fy = p.GetPosition().x/1e6 - 130.0, 140.0 - p.GetPosition().y/1e6
            d = min((math.hypot(fx-hx, fy-hy) for hx, hy, dr, pl in h20), default=9.9)
            worst = max(worst, d); n += 1
            if d < 0.05: hits += 1
        print(f"{ref} ({tag}): {hits}/{n} THT pads coincide with a v20 drill hole, worst {worst:.3f}mm")
