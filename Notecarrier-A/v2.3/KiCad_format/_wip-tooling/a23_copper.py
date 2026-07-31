"""Compute and apply the v16 -> v20 copper delta on all four layers.

Segments are keyed at 2-decimal precision for matching, then written back at
full film precision. Vias are round flashes present on both outer films at the
same coordinate whose drill appears in the plated drill file.
"""
import sys, json, math
sys.path.insert(0, "/scratch/kd")
from gerbparse import parse

LAYERS = [("F.Cu", "TOP.art", "04-TOP.art"), ("B.Cu", "BOTTOM.art", "07-BOTTOM.art"),
          ("In1.Cu", "GND.art", "05-GND.art"), ("In2.Cu", "POWER.art", "06-POWER.art")]

def inb(x, y):
    return -75.6 <= x <= 0.6 and -0.6 <= y <= 68.6

def segs_of(path):
    r = parse(path, xoff=0.0)
    out = {}
    for d, x1, y1, x2, y2 in r["draws"]:
        if not (inb(x1, y1) and inb(x2, y2)): continue
        ap = r["apertures"].get(d)
        if not ap or ap[0] != "C" or not ap[1]: continue
        w = ap[1][0]
        p1 = (round(x1, 2), round(y1, 2)); p2 = (round(x2, 2), round(y2, 2))
        if p1 == p2: continue
        key = (min(p1, p2), max(p1, p2), round(w, 3))
        out[key] = ((x1, y1), (x2, y2), w) if p1 <= p2 else ((x2, y2), (x1, y1), w)
    return out, r

delta = {}
for lay, f16, f20 in LAYERS:
    a, _ = segs_of(f"/scratch/a16-g/{f16}")
    c, r20 = segs_of(f"/scratch/a23-g/{f20}")
    add = {k: c[k] for k in c if k not in a}
    rem = [k for k in a if k not in c]
    delta[lay] = {"add": add, "rem": rem}
    print(f"{lay:7s} v16 {len(a):5d}  v20 {len(c):5d}  ->  add {len(add):5d}  remove {len(rem):5d}")

# vias: round flashes on both outer films at the same spot, with a plated hole
def flashes(path, lo=0.3, hi=1.2):
    r = parse(path, xoff=0.0)
    out = {}
    for d, x, y in r["flashes"]:
        ap = r["apertures"].get(d)
        if ap and ap[0] == "C" and ap[1] and lo <= ap[1][0] <= hi and inb(x, y):
            out[(round(x, 2), round(y, 2))] = ap[1][0]
    return out

def holes(path):
    out = []
    sec = 0
    plated = 0
    sizes = []
    for line in open(path):
        line = line.strip()
        if line.startswith(";   Holesize"):
            sizes.append(("PLATED" in line, float(line.split("=")[1].split()[0])))
        if line == "M00": sec += 1
        elif line.startswith("X"):
            xs, ys = line[1:].split("Y")
            if sec < len(sizes) and sizes[sec][0]:
                out.append((round(float(xs)/1e5, 2), round(float(ys)/1e5, 2), sizes[sec][1]))
    return out

def viaset(root, top, bot, drl):
    t, b_ = flashes(f"/scratch/{root}/{top}"), flashes(f"/scratch/{root}/{bot}")
    hs = {(x, y): d for x, y, d in holes(f"/scratch/{root}/{drl}")}
    out = {}
    for k, w in t.items():
        if k in b_ and k in hs:
            out[k] = (w, hs[k])
    return out

v16v = viaset("a16-g", "TOP.art", "BOTTOM.art", "20210324_notecarrier-m2-al_v16-1-4.drl")
v20v = viaset("a23-g", "04-TOP.art", "07-BOTTOM.art", "20210324_notecarrier-m2-al_v20-1-4.drl")
def near(k, dd):
    return any(abs(k[0]-x) <= 0.06 and abs(k[1]-y) <= 0.06 for x, y in dd)
addv = {k: v for k, v in v20v.items() if not near(k, v16v)}
remv = [k for k in v16v if not near(k, v20v)]
print(f"vias   v16 {len(v16v):5d}  v20 {len(v20v):5d}  ->  add {len(addv):5d}  remove {len(remv):5d}")

json.dump({"layers": {lay: {"add": [[list(k[0]), list(k[1]), k[2], list(v[0]), list(v[1])]
                                    for k, v in d["add"].items()],
                            "rem": [[list(k[0]), list(k[1]), k[2]] for k in d["rem"]]}
                      for lay, d in delta.items()},
           "vias": {"add": [[k[0], k[1], v[0], v[1]] for k, v in addv.items()],
                    "rem": [[k[0], k[1]] for k in remv]}},
          open("/scratch/a23-refpack/copper-delta.json", "w"))
print("delta saved to /scratch/a23-refpack/copper-delta.json")
