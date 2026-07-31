import subprocess, json, uuid, shutil
SRC = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
s = open(SRC).read()
tail = s.rstrip()
close = tail.rfind('\n)')
probe = f'''	(wire
		(pts
			(xy 127 209.55) (xy 127 205.74)
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{uuid.uuid4()}")
	)
	(global_label "PROBE1"
		(shape bidirectional)
		(at 127 205.74 90)
		(effects
			(font
				(size 1.27 1.27)
			)
			(justify left)
		)
		(uuid "{uuid.uuid4()}")
	)
'''
out = tail[:close] + "\n" + probe.rstrip("\n") + tail[close:] + "\n"
open("/tmp/probe_power.kicad_sch", "w").write(out)
shutil.copy("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_sch", "/tmp/probe_root.kicad_sch")
shutil.copy("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Connector.kicad_sch", "/tmp/probe_conn.kicad_sch")
r = open("/tmp/probe_root.kicad_sch").read()
r = r.replace('Notecarrier-A_Power.kicad_sch', 'probe_power.kicad_sch').replace('Notecarrier-A_Connector.kicad_sch', 'probe_conn.kicad_sch')
open("/tmp/probe_root.kicad_sch", "w").write(r)
subprocess.run(["kicad-cli","sch","export","netlist","--format","kicadsexpr","-o","/tmp/probe.net","/tmp/probe_root.kicad_sch"], capture_output=True)
import re
n = open("/tmp/probe.net").read()
for m in re.finditer(r'\(net \(code "\d+"\) \(name "([^"]+)"\)(.*?)(?=\(net |\Z)', n, re.S):
    if 'PROBE1' in m.group(1) or 'B4_A9' in m.group(2):
        pins = re.findall(r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"\)', m.group(2))
        print(m.group(1), '->', pins)
