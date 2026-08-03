import re, subprocess, json

SRC = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
s = open(SRC).read()
def balanced_end(text, start):
    d=0; j=start
    while True:
        if text[j]=='(':d+=1
        elif text[j]==')':
            d-=1
            if d==0: return j+1
        j+=1
def grab(pat):
    m = re.search(pat, s)
    st = s.rfind('\t(', 0, m.start()) if not s[m.start()-2:m.start()] == '\n\t' else m.start()
    return None
# header pieces
i_lib = s.index('\t(lib_symbols')
header = s[:i_lib]
lib_block = s[i_lib:balanced_end(s, i_lib+1)]
i_j11 = s.index('"Reference" "J11"')
i_sym = s.rfind('\t(symbol', 0, i_j11)
j11_block = s[i_sym:balanced_end(s, i_sym+1)]
i_w = s.index("(xy 144.78 209.55) (xy 127 209.55)")
i_wire = s.rfind('\t(wire', 0, i_w)
wire_block = s[i_wire:balanced_end(s, i_wire+1)]


si_block = ""

def fails(txt, tag):
    open("/tmp/b2.kicad_sch", "w").write(txt)
    subprocess.run(["kicad-cli","sch","erc","--format","json","--output","/tmp/b2-erc.json","--severity-error","/tmp/b2.kicad_sch"], capture_output=True)
    d = json.load(open("/tmp/b2-erc.json"))
    bad = any("B4_A9" in json.dumps(v) for sh in d.get("sheets",[]) for v in sh.get("violations",[]))
    print(tag, "-> fails" if bad else "-> PASSES")
    return bad

skeleton = header + lib_block + "\n" + j11_block + "\n" + wire_block + "\n" + "\t" + si_block + "\n)\n"
fails(skeleton, "skeleton (real header+libs+J11+wire)")

# swap lib_symbols with ONLY my def
i_my = lib_block.index('(symbol "Notecarrier-A-local:12402012E212A"')
my_def = lib_block[i_my:balanced_end(lib_block, i_my)]
small_lib = "\t(lib_symbols\n\t" + my_def + "\n\t)\n"
fails(header + small_lib + "\n" + j11_block + "\n" + wire_block + "\n" + "\t" + si_block + "\n)\n", "skeleton with ONLY my lib def")

# swap header with the minimal test header
test_header = '''(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "aaaaaaaa-0000-0000-0000-000000000001")
	(paper "A4")
'''
fails(test_header + lib_block + "\n" + j11_block + "\n" + wire_block + "\n" + "\t" + si_block + "\n)\n", "minimal header + real libs")

# cross-swaps with the passing test pieces
test_wire = """	(wire
		(pts
			(xy 127 209.55) (xy 144.78 209.55)
		)
		(stroke (width 0) (type default))
		(uuid "dddddddd-0000-0000-0000-000000000004")
	)
"""
test_inst = """	(symbol
		(lib_id "Notecarrier-A-local:12402012E212A")
		(at 119.38 214.63 0)
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "bbbbbbbb-0000-0000-0000-000000000002")
		(property "Reference" "J11"
			(at 112 205 0)
			(effects (font (size 1.27 1.27)))
		)
		(property "Value" "test"
			(at 112 207 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Footprint" ""
			(at 0 0 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(property "Datasheet" ""
			(at 0 0 0)
			(effects (font (size 1.27 1.27)) (hide yes))
		)
		(pin "B4_A9" (uuid "cccccccc-0000-0000-0000-000000000003"))
		(instances
			(project "Notecarrier-A"
				(path "/5050c972-9893-4dc9-ac8b-afa1eb9e3ab8/03718417-b36a-4e5d-916f-df242c9477be"
					(reference "J11")
					(unit 1)
				)
			)
		)
	)
"""
fails(header + lib_block + "\n" + test_inst + "\n" + wire_block + "\n)\n", "real libs + TEST inst + real wire")
fails(header + lib_block + "\n" + j11_block + "\n" + test_wire + "\n)\n", "real libs + real inst + TEST wire")
fails(header + lib_block + "\n" + test_inst + "\n" + test_wire + "\n)\n", "real libs + TEST inst + TEST wire")

tail_blocks = """	(sheet_instances
		(path "/"
			(page "1")
		)
	)
	(embedded_fonts no)
"""
fails(header + lib_block + "\n" + test_inst + "\n" + test_wire + "\n" + tail_blocks + ")\n", "real hdr+libs + TEST inst/wire + TAIL")
fails(header + lib_block + "\n" + j11_block + "\n" + wire_block + "\n" + tail_blocks + ")\n", "real everything + TAIL")
