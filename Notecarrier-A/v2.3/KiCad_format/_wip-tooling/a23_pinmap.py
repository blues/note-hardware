import re, math
P = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
s = open(P).read()
def balanced_end(text, start):
    d=0; j=start
    while True:
        if text[j]=='(':d+=1
        elif text[j]==')':
            d-=1
            if d==0: return j+1
        j+=1
# lib pin maps
i_lib = s.index('\t(lib_symbols')
lib_end = balanced_end(s, i_lib+1)
lib = s[i_lib:lib_end]
pins_by_lib = {}
for m in re.finditer(r'\(symbol "([^"]+:[^"]+)"', lib):
    name = m.group(1)
    blk = lib[m.start():balanced_end(lib, m.start())]
    pins = []
    for pm in re.finditer(r'\(pin \w+ \w+\s*\n\s*\(at ([\-\d.]+) ([\-\d.]+) (\d+)\)[\s\S]{0,500}?\(number "([^"]*)"', blk):
        pins.append((float(pm.group(1)), float(pm.group(2)), pm.group(4)))
    pins_by_lib[name] = pins
# instances
body = s[lib_end:]
hits = []
for m in re.finditer(r'\(symbol\s*\n\s*\(lib_id "([^"]+)"\)\s*\n\s*\(at ([\-\d.]+) ([\-\d.]+) ([\-\d.]+)\)\s*\n(\s*\(mirror ([xy])\)\s*\n)?', body):
    lid, X, Y, R = m.group(1), float(m.group(2)), float(m.group(3)), float(m.group(4))
    mir = m.group(6)
    tail = body[m.end():m.end()+1200]
    ref = re.search(r'"Reference" "([^"]+)"', tail)
    ref = ref.group(1) if ref else "?"
    for dx, dy, num in pins_by_lib.get(lid, []):
        # apply mirror then rotation (KiCad order: mirror about axis, then rotate)
        px, py = dx, dy
        if mir == "x": py = -py
        elif mir == "y": px = -px
        a = math.radians(R)
        rx = px*math.cos(a) - py*math.sin(a)
        ry = px*math.sin(a) + py*math.cos(a)
        ax, ay = X + rx, Y - ry
        if abs(ax-127.0) < 0.01 and abs(ay-209.55) < 0.01:
            hits.append((ref, lid, num, X, Y, R, mir))
print("pins at (127,209.55):")
for h in hits: print("  ", h)
