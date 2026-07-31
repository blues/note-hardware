import re, subprocess, json

def balanced_end(text, start):
    d=0; j=start
    while True:
        if text[j]=='(':d+=1
        elif text[j]==')':
            d-=1
            if d==0: return j+1
        j+=1

test = open("/scratch/kd/usbc-test.kicad_sch").read()
real = open("/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch").read()

def fails(txt, tag):
    open("/tmp/b3.kicad_sch", "w").write(txt)
    r = subprocess.run(["kicad-cli","sch","erc","--format","json","--output","/tmp/b3-erc.json","--severity-all","/tmp/b3.kicad_sch"], capture_output=True, text=True)
    try:
        d = json.load(open("/tmp/b3-erc.json"))
    except Exception:
        print(tag, "-> ERC ERROR:", r.stderr[-200:])
        return None
    bad = any("B4_A9" in json.dumps(v) for sh in d.get("sheets",[]) for v in sh.get("violations",[]))
    print(tag, "-> fails(B4_A9)" if bad else "-> PASSES")
    return bad

fails(test, "original test")
# swap 1: header (kicad_sch..paper + uuid/title_block)
i_t = test.index('\t(lib_symbols')
i_r = real.index('\t(lib_symbols')
fails(real[:i_r] + test[i_t:], "REAL header + test rest")
# swap 2: replace test's instance with the real J11 instance block
i_j = real.index('"Reference" "J11"')
i_sym = real.rfind('\t(symbol', 0, i_j)
j11_real = real[i_sym:balanced_end(real, i_sym+1)]
i_tj = test.index('"Reference" "J1"')
i_tsym = test.rfind('\t(symbol', 0, i_tj)
t_end = balanced_end(test, i_tsym+1)
fails(test[:i_tsym] + j11_real + test[t_end:], "test + REAL J11 instance")
# swap 3: test wire -> real wire block
i_w = real.index("(xy 144.78 209.55) (xy 127 209.55)")
i_wire = real.rfind('\t(wire', 0, i_w)
wire_real = real[i_wire:balanced_end(real, i_wire+1)]
i_tw = test.index('\t(wire')
tw_end = balanced_end(test, i_tw+1)
fails(test[:i_tw] + wire_real + test[tw_end:], "test + REAL wire")
