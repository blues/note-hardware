import re, uuid
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
TARGETS = [((144.78,209.55),(127,209.55)), ((127,214.63),(147.32,214.63)), ((127,217.17),(147.32,217.17)),
           ((144.78,209.55),(144.78,207.01)), ((144.78,228.6),(144.78,209.55)), ((144.78,209.55),(185.42,209.55))]
def canon(a,b): return (min(a,b), max(a,b))
tset = {canon(a,b) for a,b in TARGETS}
removed = []
out = s
while True:
    found = False
    for m in re.finditer(r'\t\(wire\s*\n\s*\(pts\s*\n\s*\(xy ([\d.\-]+) ([\d.\-]+)\) \(xy ([\d.\-]+) ([\d.\-]+)\)', out):
        x1,y1,x2,y2 = (float(v) for v in m.groups())
        if canon((x1,y1),(x2,y2)) in tset:
            e = balanced_end(out, m.start()+1)
            removed.append(((x1,y1),(x2,y2)))
            out = out[:m.start()] + out[e+1 if out[e:e+1]=='\n' else e:]
            found = True
            break
    if not found: break
print("removed:", removed)
tail = out.rstrip()
close = tail.rfind('\n)')
blocks = ""
for (a, b) in removed:
    blocks += f'''	(wire
		(pts
			(xy {a[0]:g} {a[1]:g}) (xy {b[0]:g} {b[1]:g})
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{uuid.uuid4()}")
	)
'''
out = tail[:close] + "\n" + blocks.rstrip("\n") + tail[close:] + "\n"
open(P, "w").write(out)
print("re-added", len(removed), "fresh wires")
