import re, uuid

P = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
s = open(P).read()

def balanced_end(text, start):
    depth = 0; i = start
    while i < len(text):
        if text[i] == '(': depth += 1
        elif text[i] == ')':
            depth -= 1
            if depth == 0: return i + 1
        i += 1
    raise ValueError

def remove_block(s, start):
    end = balanced_end(s, start)
    # eat leading whitespace/newline
    a = start
    while a > 0 and s[a-1] in ' \t': a -= 1
    if a > 0 and s[a-1] == '\n': a -= 1
    return s[:a] + s[end:]

def find_symbol_block(s, ref):
    i = s.find(f'"Reference" "{ref}"')
    assert i >= 0, ref
    j = s.rfind('\t(symbol', 0, i)
    return j

# ---------- 1. delete symbols: J2, old J11, #PWR046, #PWR047 ----------
for ref in ("J2", "J11", "#PWR046", "#PWR047"):
    s = remove_block(s, find_symbol_block(s, ref))
    print("removed symbol", ref)

# ---------- 2. delete wires ----------
KILL_WIRES = [((127.0,209.55),(144.78,209.55), False),  # keep! marker False = keep
]
kill = [((119.38,224.79),(119.38,227.33)), ((119.38,227.33),(140.97,227.33)), ((140.97,227.33),(140.97,237.49)),
        ((116.84,224.79),(116.84,227.33)), ((111.76,227.33),(116.84,227.33)), ((111.76,227.33),(111.76,237.49)),
        ((132.08,254.0),(142.24,254.0)), ((132.08,259.08),(138.43,259.08)), ((132.08,261.62),(138.43,261.62)),
        ((140.97,273.05),(124.46,273.05)), ((124.46,273.05),(124.46,269.24)),
        ((121.92,269.24),(121.92,273.05)), ((121.92,273.05),(111.76,273.05)),
        ((140.97,274.32),(140.97,273.05)),
        ((125.73,237.49),(140.97,237.49))]
def canon(p1, p2): return (min(p1,p2), max(p1,p2))
killset = {canon(a,b) for a,b in kill}
out = []
removed_w = 0
pos = 0
for m in re.finditer(r'\t\(wire\s*\n\s*\(pts\s*\n\s*\(xy ([\d.\-]+) ([\d.\-]+)\) \(xy ([\d.\-]+) ([\d.\-]+)\)', s):
    x1,y1,x2,y2 = (float(v) for v in m.groups())
    if canon((x1,y1),(x2,y2)) in killset:
        end = balanced_end(s, m.start()+1)
        out.append((m.start(), end))
        removed_w += 1
for a, e in reversed(out):
    aa = a
    if aa > 0 and s[aa-1] == '\n': aa -= 0
    s = s[:a] + s[e+1 if s[e:e+1]=='\n' else e:] + ''
print("removed wires:", removed_w)

# ---------- 3. delete ncs, labels, junction ----------
for x, y in [(127.0,219.71), (132.08,264.16)]:
    m = re.search(r'\t\(no_connect\s*\n\s*\(at %s %s\)' % (re.escape(f"{x:g}"), re.escape(f"{y:g}")), s)
    assert m, (x,y)
    s = remove_block(s, m.start()+1)
print("removed 2 ncs")
for x, y, name in [(138.43,259.08,"USB_DP"), (138.43,261.62,"USB_DM")]:
    m = re.search(r'\t\(global_label "%s"[\s\S]{0,400}?\(at %s %s' % (name, f"{x:g}", f"{y:g}"), s)
    if not m:
        m = re.search(r'\t\(label "%s"[\s\S]{0,200}?\(at %s %s' % (name, f"{x:g}", f"{y:g}"), s)
    assert m, name
    s = remove_block(s, m.start()+1)
print("removed 2 labels")
m = re.search(r'\t\(junction\s*\n\s*\(at 111.76 273.05\)', s)
assert m
s = remove_block(s, m.start()+1)
print("removed 1 junction")

# ---------- 4. lib_symbol for the USB-C ----------
PINS_R = [("B4_A9","VBUS",5.08), ("A4_B9","VBUS",2.54), ("A6","D1+",0.0), ("A7","D1-",-2.54),
          ("B6","D2+",-5.08), ("B7","D2-",-7.62), ("A5","CC1",-10.16), ("B5","CC2",-12.7),
          ("A8","SBU1",-15.24), ("B8","SBU2",-17.78), ("A1_B12","GND",-20.32), ("B1_A12","GND",-22.86)]
PINS_L = [("S1","SHIELD",-10.16), ("S2","SHIELD",-12.7), ("S3","SHIELD",-15.24), ("S4","SHIELD",-17.78)]
pins = ""
for num, name, dy in PINS_R:
    pins += f'''
			(pin passive line
				(at 7.62 {dy:g} 180)
				(length 1.27)
				(name "{name}"
					(effects
						(font
							(size 1.27 1.27)
						)
					)
				)
				(number "{num}"
					(effects
						(font
							(size 1.27 1.27)
						)
					)
				)
			)'''
for num, name, dy in PINS_L:
    pins += f'''
			(pin passive line
				(at -7.62 {dy:g} 0)
				(length 1.27)
				(name "{name}"
					(effects
						(font
							(size 1.27 1.27)
						)
					)
				)
				(number "{num}"
					(effects
						(font
							(size 1.27 1.27)
						)
					)
				)
			)'''
libsym = f'''	(symbol "Notecarrier-A-local:12402012E212A"
		(pin_names
			(offset 1.016)
		)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(property "Reference" "J"
			(at 0 7.62 0)
			(effects
				(font
					(size 1.27 1.27)
				)
			)
		)
		(property "Value" "12402012E212A"
			(at 0 -26.67 0)
			(effects
				(font
					(size 1.27 1.27)
				)
			)
		)
		(property "Footprint" ""
			(at 0 0 0)
			(effects
				(font
					(size 1.27 1.27)
				)
				(hide yes)
			)
		)
		(property "Datasheet" ""
			(at 0 0 0)
			(effects
				(font
					(size 1.27 1.27)
				)
				(hide yes)
			)
		)
		(symbol "12402012E212A_0_1"
			(rectangle
				(start -6.35 6.35)
				(end 6.35 -24.13)
				(stroke
					(width 0.254)
					(type default)
				)
				(fill
					(type background)
				)
			)
		)
		(symbol "12402012E212A_1_1"{pins}
		)
	)
'''
i = s.index('(lib_symbols')
insert_at = s.index('\n', i) + 1
s = s[:insert_at] + libsym + s[insert_at:]
print("lib_symbol added")

# ---------- 5. new symbol instances ----------
SHEET_PATH = "/5050c972-9893-4dc9-ac8b-afa1eb9e3ab8/03718417-b36a-4e5d-916f-df242c9477be"
def prop(name, val, x, y, hide=True, justify=None):
    j = f"\n\t\t\t\t(justify {justify})" if justify else ""
    h = "\n\t\t\t\t(hide yes)" if hide else ""
    return f'''
		(property "{name}" "{val}"
			(at {x:g} {y:g} 0)
			(effects
				(font
					(size 1.27 1.27)
				){j}{h}
			)
		)'''
def sym_instance(lib_id, ref, x, y, rot, props, pin_nums):
    u = str(uuid.uuid4())
    pp = "".join(props)
    pins_s = "".join(f'\n\t\t(pin "{n}"\n\t\t\t(uuid "{uuid.uuid4()}")\n\t\t)' for n in pin_nums)
    return f'''	(symbol
		(lib_id "{lib_id}")
		(at {x:g} {y:g} {rot})
		(unit 1)
		(exclude_from_sim no)
		(in_bom yes)
		(on_board yes)
		(dnp no)
		(uuid "{u}"){pp}{pins_s}
		(instances
			(project "Notecarrier-A"
				(path "{SHEET_PATH}"
					(reference "{ref}")
					(unit 1)
				)
			)
		)
	)
'''
new_syms = []
jx, jy = 119.38, 214.63
new_syms.append(sym_instance("Notecarrier-A-local:12402012E212A", "J11", jx, jy, 0, [
    prop("Reference", "J11", jx-6.35, jy-8.89, hide=False, justify="left"),
    prop("Value", "12402012E212A", jx-6.35, jy-6.35, hide=True, justify="left"),
    prop("Footprint", "Notecarrier-A-local:AMPHENOL_12402012E212A", jx, jy),
    prop("Datasheet", "~", jx, jy),
    prop("Description", "CONN. USB 3.0 F/90° TIPO C C.S. 12402012E212A AMPHENOL", jx, jy),
    prop("Temperature", "-40°..+85°", jx, jy),
    prop("MPN", "12402012E212A", jx, jy),
    prop("Pkg Type", "SMD", jx, jy),
    prop("Distributor", "FAE", jx, jy),
], [n for n,_,_ in PINS_R] + [n for n,_,_ in PINS_L]))
for ref, ry in [("R33", 224.79), ("R32", 227.33)]:
    rx = 135.89
    new_syms.append(sym_instance("Device:R", ref, rx, ry, 90, [
        prop("Reference", ref, rx, ry-2.54, hide=False),
        prop("Value", "5.1k", rx, ry+2.54, hide=False),
        prop("Footprint", "blues-kicad-lib:RS-0402", rx, ry),
        prop("Datasheet", "~", rx, ry),
        prop("Description", "CHIP RES. 5K1 0402 1/16W 1%", rx, ry),
        prop("Temperature", "-55°..+155°", rx, ry),
        prop("MPN", "", rx, ry),
        prop("Pkg Type", "SMD", rx, ry),
        prop("Distributor", "FAE", rx, ry),
    ], ["1", "2"]))

# ---------- 6. new wires / junctions / ncs ----------
W = [
    # A4_B9 VBUS join
    ((127,212.09),(128.27,212.09)), ((128.27,212.09),(128.27,209.55)),
    # D2+ / D2- ties
    ((127,219.71),(129.54,219.71)), ((129.54,219.71),(129.54,214.63)),
    ((127,222.25),(130.81,222.25)), ((130.81,222.25),(130.81,217.17)),
    # CC1 - R33 - GND drop
    ((127,224.79),(132.08,224.79)), ((139.7,224.79),(140.97,224.79)),
    # CC2 - R32
    ((127,227.33),(132.08,227.33)), ((139.7,227.33),(140.97,227.33)),
    # GND drop x140.97 (segmented at joins)
    ((140.97,224.79),(140.97,227.33)), ((140.97,227.33),(140.97,234.95)), ((140.97,234.95),(140.97,237.49)),
    # A1_B12 GND
    ((127,234.95),(140.97,234.95)),
    # B1_A12 into split C11 wire
    ((125.73,237.49),(127,237.49)), ((127,237.49),(140.97,237.49)),
    # shield bus segments up to S pins
    ((111.76,224.79),(111.76,227.33)), ((111.76,227.33),(111.76,229.87)),
    ((111.76,229.87),(111.76,232.41)), ((111.76,232.41),(111.76,237.49)),
]
J = [(128.27,209.55),(129.54,214.63),(130.81,217.17),(140.97,227.33),(140.97,234.95),(127,237.49),
     (111.76,227.33),(111.76,229.87),(111.76,232.41)]
NC = [(127,229.87),(127,232.41)]
blocks = ""
for (x1,y1),(x2,y2) in W:
    blocks += f'''	(wire
		(pts
			(xy {x1:g} {y1:g}) (xy {x2:g} {y2:g})
		)
		(stroke
			(width 0)
			(type default)
		)
		(uuid "{uuid.uuid4()}")
	)
'''
for x, y in J:
    blocks += f'''	(junction
		(at {x:g} {y:g})
		(diameter 0)
		(color 0 0 0 0)
		(uuid "{uuid.uuid4()}")
	)
'''
for x, y in NC:
    blocks += f'''	(no_connect
		(at {x:g} {y:g})
		(uuid "{uuid.uuid4()}")
	)
'''
# insert everything before the trailing ')' of the file... find last sheet_instances or append before final close
tail = s.rstrip()
assert tail.endswith(')')
close = tail.rfind('\n)')
s = tail[:close] + "\n" + "".join(new_syms) + blocks.rstrip("\n") + tail[close:] + "\n"
print("added", len(new_syms), "symbols,", len(W), "wires,", len(J), "junctions,", len(NC), "ncs")

open(P, "w").write(s)
print("saved")
