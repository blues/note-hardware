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
m = re.search(r'\t\(wire\s*\n\s*\(pts\s*\n\s*\(xy 144.78 209.55\) \(xy 127 209.55\)', s)
e = balanced_end(s, m.start()+1)
repl = ""
for (a, b) in [((127,209.55),(128.27,209.55)), ((128.27,209.55),(144.78,209.55))]:
    repl += f'''	(wire
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
s = s[:m.start()] + repl.rstrip("\n") + s[e:]
open(P, "w").write(s)
print("wire split at junction")
