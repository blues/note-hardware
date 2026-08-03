import re, subprocess, json, shutil
SRC = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
TMP = "/tmp/rectest_power.kicad_sch"
s = open(SRC).read()
def balanced_end(text, start):
    d=0; j=start
    while True:
        if text[j]=='(':d+=1
        elif text[j]==')':
            d-=1
            if d==0: return j+1
        j+=1
out = s
removed = 0
while True:
    m = re.search(r'\t\(rectangle\s*\n', out)
    if not m: break
    e = balanced_end(out, m.start()+1)
    out = out[:m.start()] + out[e+1 if out[e:e+1]=='\n' else e:]
    removed += 1
print("rectangles removed:", removed)
open(TMP, "w").write(out)
# build a root that references this copy: copy root + connector to /tmp
shutil.copy("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_sch", "/tmp/rectest_root.kicad_sch")
shutil.copy("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Connector.kicad_sch", "/tmp/rectest_conn.kicad_sch")
r = open("/tmp/rectest_root.kicad_sch").read()
r = r.replace('Notecarrier-A_Power.kicad_sch', 'rectest_power.kicad_sch').replace('Notecarrier-A_Connector.kicad_sch', 'rectest_conn.kicad_sch')
open("/tmp/rectest_root.kicad_sch", "w").write(r)
subprocess.run(["kicad-cli","sch","erc","--format","json","--output","/tmp/r-erc.json","--severity-error","/tmp/rectest_root.kicad_sch"], capture_output=True)
d = json.load(open("/tmp/r-erc.json"))
for sh in d.get("sheets", []):
    for v in sh.get("violations", []):
        print(v["type"], "|", " ~ ".join(i["description"][:55] for i in v["items"]))
