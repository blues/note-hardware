"""RS-274X parser for Allegro .art films, polarity-aware.

Same as gerbparse but keeps %LPD/%LPC so pour cutouts (clear regions) can be
told from pour copper (dark regions). Regions are returned as (polarity, pts).
"""
import re

def parse(path, xoff=0.0):
    """Returns dict: apertures {d: (shape, dims_mm)}, flashes [(d,x,y)], draws [(d,x1,y1,x2,y2)],
       arcs [(d,x1,y1,x2,y2,i,j,cw)], regions [ [pts...] ]. Coords mm, xoff added to x."""
    txt = open(path, errors="replace").read()
    fs = re.search(r'%FS([LT])([AI])X(\d)(\d)Y(\d)(\d)\*', txt)
    xi, xd = int(fs.group(3)), int(fs.group(4))
    scale = 10 ** xd
    unit = 25.4 if "%MOIN" in txt else 1.0
    if "%MOMM" in txt: unit = 1.0
    apertures = {}
    for m in re.finditer(r'%ADD(\d+)([CROP]),([\d.X]+)\*', txt):
        d = int(m.group(1)); shape = m.group(2)
        dims = tuple(float(v) * unit for v in m.group(3).split("X") if v)
        apertures[d] = (shape, dims)
    flashes, draws, arcs, regions = [], [], [], []
    cur = None; x = y = 0.0; mode = 1; inreg = False; regpts = []; polarity = "D"
    body = txt.split("%")[-1] if False else txt
    # keep polarity, strip the other extended commands
    body = re.sub(r'%LP([CD])\*%', r'LP\1*', txt)
    body = re.sub(r'%(?!LP)[^%]*%', '', body)
    for cmd in body.split("*"):
        cmd = cmd.strip().replace("\n", "").replace("\r", "")
        if not cmd: continue
        if cmd.startswith("G04"): continue
        if cmd in ("LPD", "LPC"): polarity = cmd[2]; continue
        if cmd == "G36": inreg = True; regpts = []; continue
        if cmd == "G37":
            inreg = False
            if regpts: regions.append((polarity, regpts))
            continue
        m = re.match(r'^(?:G0?([123]))?(?:X(-?\d+))?(?:Y(-?\d+))?(?:I(-?\d+))?(?:J(-?\d+))?(?:D0?([123]))?$', cmd)
        if not m:
            dm = re.match(r'^(?:G54)?D(\d\d+)$', cmd)
            if dm: cur = int(dm.group(1))
            continue
        g, xs, ys, is_, js, dcode = m.groups()
        if g: mode = int(g)
        nx = (int(xs) / scale * unit + xoff) if xs else x
        ny = (int(ys) / scale * unit) if ys else y
        i = int(is_) / scale * unit if is_ else 0.0
        j = int(js) / scale * unit if js else 0.0
        if dcode == "3":
            flashes.append((cur, nx, ny))
        elif dcode == "1":
            if inreg:
                regpts.append((nx, ny))
            elif mode == 1:
                draws.append((cur, x, y, nx, ny))
            else:
                arcs.append((cur, x, y, nx, ny, x + i, y + j, mode == 2))
        elif dcode == "2":
            if inreg:
                if regpts: regions.append((polarity, regpts))
                regpts = [(nx, ny)]
        x, y = nx, ny
    return {"apertures": apertures, "flashes": flashes, "draws": draws, "arcs": arcs, "regions": regions}

if __name__ == "__main__":
    import sys, json
    r = parse(sys.argv[1], xoff=float(sys.argv[2]) if len(sys.argv) > 2 else 0.0)
    print("apertures:", len(r["apertures"]), "flashes:", len(r["flashes"]),
          "draws:", len(r["draws"]), "arcs:", len(r["arcs"]), "regions:", len(r["regions"]))
