import re, subprocess, json, shutil
SRC = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
s0 = open(SRC).read()
def balanced_end(text, start):
    d=0; j=start
    while True:
        if text[j]=='(':d+=1
        elif text[j]==')':
            d-=1
            if d==0: return j+1
        j+=1
def top_spans(s):
    spans = []
    i = 0; depth = 0
    while i < len(s):
        c = s[i]
        if c == '"':
            i = s.index('"', i+1) + 1
            continue
        if c == '(':
            if depth == 1:
                m = re.match(r'\(([a-z_0-9]+)', s[i:])
                kind = m.group(1) if m else '?'
                e = balanced_end(s, i)
                spans.append((i, e, kind))
                i = e
                continue
            depth += 1
        elif c == ')':
            depth -= 1
        i += 1
    return spans
def build_without(s, remove_spans):
    out = []
    last = 0
    for a, e in sorted(remove_spans):
        out.append(s[last:a])
        last = e
    out.append(s[last:])
    return "".join(out)
def check(txt, tag):
    open("/tmp/cls_power.kicad_sch", "w").write(txt)
    r = open("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_sch").read()
    r = r.replace('Notecarrier-A_Power.kicad_sch', 'cls_power.kicad_sch').replace('Notecarrier-A_Connector.kicad_sch', 'cls_conn.kicad_sch')
    open("/tmp/cls_root.kicad_sch", "w").write(r)
    shutil.copy("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Connector.kicad_sch", "/tmp/cls_conn.kicad_sch")
    subprocess.run(["kicad-cli","sch","erc","--format","json","--output","/tmp/cls-erc.json","--severity-error","/tmp/cls_root.kicad_sch"], capture_output=True)
    d = json.load(open("/tmp/cls-erc.json"))
    bad = any("B4_A9" in json.dumps(v) for sh in d.get("sheets",[]) for v in sh.get("violations",[]))
    print(tag, "-> fails" if bad else "-> PASSES")
    return bad

spans = top_spans(s0)
# remove all symbols except J11
sym_spans = []
for a,e,k in spans:
    if k == "symbol" and '"Reference" "J11"' not in s0[a:e]:
        sym_spans.append((a,e))
check(build_without(s0, sym_spans), f"without {len(sym_spans)} other symbols")
# remove all labels
lbl = [(a,e) for a,e,k in spans if k in ("label","global_label","hierarchical_label")]
check(build_without(s0, lbl), f"without {len(lbl)} labels")
# remove all texts
txts = [(a,e) for a,e,k in spans if k in ("text","text_box")]
check(build_without(s0, txts), f"without {len(txts)} texts")
# remove all junctions
jns = [(a,e) for a,e,k in spans if k == "junction"]
check(build_without(s0, jns), f"without {len(jns)} junctions")
# remove all other wires except the rail cluster
keepw = {"(xy 144.78 209.55) (xy 127 209.55)"}
wr = [(a,e) for a,e,k in spans if k == "wire" and "(xy 144.78 209.55) (xy 127 209.55)" not in s0[a:e]]
check(build_without(s0, wr), f"without {len(wr)} other wires")
