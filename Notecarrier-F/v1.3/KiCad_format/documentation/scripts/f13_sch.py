#!/usr/bin/env python3
"""Notecarrier-F v1.3: post-process the KiCad Altium-importer output (schematic side).

Text-level, mirrors what the v1.5 port did:
  * rename project + sheet files to Notecarrier-F / Notecarrier-F_<Sheet>
  * drop the non-electrical cover + block-diagram sheets from the root
  * (project ...) instance blocks -> "Notecarrier-F"
  * sheet symbols get the Altium sheet titles
  * title blocks: rev 11 (v1.3), 2023-07-10, BOM 3000-653-002
  * annotate the importer's #PWR? power symbols
  * MOD1L/MOD1R -> MODL1/MODR1 (KiCad cannot annotate refs ending in a letter)
  * production variant: J11/R11/R12 DNP, MOD2 out of BOM, ASS1 off board
  * promote Altium's (globally scoped) net labels to global labels where they
    span sheets or share a name with a power net
  * footprint fields -> Notecarrier-F-altium-import:<name>
  * merged project symbol library from the embedded lib_symbols
  * sym-lib-table / fp-lib-table / .kicad_pro settings (rules from v1.5)

usage: f13_sch.py <importer-out-dir> <work-dir> <v1.5-kicad_pro>
"""
import json, re, shutil, sys, uuid
from pathlib import Path

SRC, DST, V15_PRO = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
OLD_PROJECT = "100275_NOTECARRIER-F"
PROJECT = "Notecarrier-F"
LIB = "Notecarrier-F-altium-import"
SHEETS = {  # importer file -> (new file, sheet name)
    "03_NOTECARD-CONNECTION.kicad_sch": ("Notecarrier-F_Notecard-Connection.kicad_sch", "Notecard Connection"),
    "04_FEATHER-CONNECTION.kicad_sch": ("Notecarrier-F_Feather-Connection.kicad_sch", "Feather Connection"),
    "05_IO.kicad_sch": ("Notecarrier-F_IO.kicad_sch", "IO"),
    "06_POWER-INPUT.kicad_sch": ("Notecarrier-F_Power-Input.kicad_sch", "Power Input"),
    "07_POWER-RAILS.kicad_sch": ("Notecarrier-F_Power-Rails.kicad_sch", "Power Rails"),
}
DROPPED = {"01_COVER.kicad_sch", "02_BLOCK-DIAGRAM.kicad_sch"}
REF_RENAME = {"MOD1L": "MODL1", "MOD1R": "MODR1"}
DNP = {"J11", "R11", "R12"}          # PrjPCB Production variant, Kind=1 (P1 has no symbol)
NOT_IN_BOM = {"MOD2"}                 # Feather outline graphic (variant Kind=1, not a part)
NOT_ON_BOARD = {"ASS1"}               # M2.5 screw: BOM line, no footprint
TITLE_BLOCK = """	(title_block
		(title "Notecarrier-F")
		(date "2023-07-10")
		(rev "11 (v1.3)")
		(company "Byte Lab Grupa d.o.o.")
		(comment 1 "Blues Inc")
		(comment 2 "Ported from Altium Designer sources (100275_NOTECARRIER-F Rev 11, BOM 3000-653-002)")
	)
"""
TEXT_VARS = {
    "AUTHOR": "M. Hamin", "ACCEPTOR": "T. Zvonc",
    "PCB_AUTHOR": "M. Hamin", "PCB_ACCEPTOR": "T. Zvonc",
    "ADDRESS1": "Medarska 69/1, 10000 Zagreb, Croatia", "WEB": "www.byte-lab.com",
    "HW_E_DOC_NUM": "100275", "MODULE_NAME": "Notecarier F",
    "PCB_NUM": "2200-814", "PCBA_BOM_NUM": "3000-653-002", "SHEETTOTAL": "6",
}


def block_end(text, start):
    """index just past the s-expr that opens at text[start] == '('; quote-aware."""
    depth, i, n, in_str = 0, start, len(text), False
    while i < n:
        c = text[i]
        if in_str:
            if c == "\\":
                i += 1
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced")


def top_blocks(text, token, indent="\t"):
    """yield (start, end) of every `\n<indent>(<token>` block."""
    pat = re.compile(r"\n" + re.escape(indent) + r"\(" + re.escape(token) + r"(?=[\s\n\"])")
    pos = 0
    while True:
        m = pat.search(text, pos)
        if not m:
            return
        s = m.start() + 1
        e = block_end(text, s)
        yield s, e
        pos = e


def prop(blk, name):
    m = re.search(r'\(property "%s" "((?:[^"\\]|\\.)*)"' % re.escape(name), blk)
    return m.group(1) if m else None


def set_prop(blk, name, value):
    return re.sub(r'(\(property "%s" ")(?:[^"\\]|\\.)*(")' % re.escape(name),
                  lambda m: m.group(1) + value + m.group(2), blk, count=1)


# ---------------------------------------------------------------- collect
sheets_text = {}
for f in list(SHEETS) + [OLD_PROJECT + ".kicad_sch"]:
    sheets_text[f] = (SRC / f).read_text()

label_sheets, power_names = {}, set()
for f in SHEETS:
    t = sheets_text[f]
    for s, e in top_blocks(t, "label"):
        name = re.match(r'\t\(label "((?:[^"\\]|\\.)*)"', t[s:e]).group(1)
        label_sheets.setdefault(name, set()).add(f)
    for s, e in top_blocks(t, "symbol"):
        blk = t[s:e]
        if (prop(blk, "Reference") or "").startswith("#PWR"):
            power_names.add(prop(blk, "Value"))
promote = {n for n, ss in label_sheets.items() if len(ss) >= 2} | (set(label_sheets) & power_names)
print(f"labels: {len(label_sheets)} names; promoting {len(promote)} to global: {sorted(promote)}")

# ---------------------------------------------------------------- per sheet
pwr_counter = 0
lib_symbols = {}          # bare name -> (full name, body)
fp_names = set()

def process_sheet(t, is_root):
    global pwr_counter
    t = t.replace(f'(project "{OLD_PROJECT}"', f'(project "{PROJECT}"')
    # title block
    tb = list(top_blocks(t, "title_block"))
    if tb:
        s, e = tb[0]
        t = t[:s] + TITLE_BLOCK.rstrip("\n") + t[e:]
    else:
        t = t.replace('\t(paper "A4")\n', '\t(paper "A4")\n' + TITLE_BLOCK, 1)
    # symbols (walk back-to-front so slicing stays valid)
    for s, e in reversed(list(top_blocks(t, "symbol"))):
        blk = t[s:e]
        ref = prop(blk, "Reference")
        if ref is None:
            continue
        if ref.startswith("#PWR"):
            pwr_counter += 1
            new = f"#PWR{pwr_counter:03d}"
            blk = set_prop(blk, "Reference", new)
            blk = re.sub(r'\(reference "#PWR\?"\)', f'(reference "{new}")', blk)
        elif ref in REF_RENAME:
            new = REF_RENAME[ref]
            blk = set_prop(blk, "Reference", new)
            blk = blk.replace(f'(reference "{ref}")', f'(reference "{new}")')
        if ref in DNP:
            blk = blk.replace("\t\t(dnp no)", "\t\t(dnp yes)", 1)
        if ref in NOT_IN_BOM:
            blk = blk.replace("\t\t(in_bom yes)", "\t\t(in_bom no)", 1)
        if ref in NOT_ON_BOARD:
            blk = blk.replace("\t\t(on_board yes)", "\t\t(on_board no)", 1)
        fp = prop(blk, "Footprint")
        if fp:
            bare = fp.split(":", 1)[-1]
            fp_names.add(bare)
            blk = set_prop(blk, "Footprint", f"{LIB}:{bare}")
        t = t[:s] + blk + t[e:]
    # labels -> global labels
    for s, e in reversed(list(top_blocks(t, "label"))):
        blk = t[s:e]
        name = re.match(r'\t\(label "((?:[^"\\]|\\.)*)"', blk).group(1)
        if name not in promote:
            continue
        blk = blk.replace('\t(label "', '\t(global_label "', 1)
        blk = re.sub(r'(\n\t\t\(at [^)]*\))', r'\n\t\t(shape input)\1', blk, count=1)
        isr = ('\n\t\t(property "Intersheetrefs" "${INTERSHEET_REFS}"\n\t\t\t(at 0 0 0)\n'
               '\t\t\t(effects\n\t\t\t\t(font\n\t\t\t\t\t(size 1.27 1.27)\n\t\t\t\t)\n'
               '\t\t\t\t(hide yes)\n\t\t\t)\n\t\t)')
        blk = blk[:-2].rstrip("\n") + isr + "\n\t)"
        t = t[:s] + blk + t[e:]
    # embedded lib_symbols -> collect + re-point footprint fields
    lb = list(top_blocks(t, "lib_symbols"))
    if lb:
        s, e = lb[0]
        lib = t[s:e]
        for ss, ee in reversed(list(top_blocks(lib, "symbol", indent="\t\t"))):
            sym = lib[ss:ee]
            full = re.match(r'\t\t\(symbol "((?:[^"\\]|\\.)*)"', sym).group(1)
            bare = full.split(":", 1)[-1]
            fp = prop(sym, "Footprint")
            if fp:
                sym = set_prop(sym, "Footprint", f"{LIB}:{fp.split(':', 1)[-1]}")
            lib = lib[:ss] + sym + lib[ee:]
            body = sym.replace(f'(symbol "{full}"', f'(symbol "{bare}"', 1)
            body = re.sub(r"^\t", "", body, flags=re.M)  # de-indent one level
            if bare in lib_symbols and lib_symbols[bare][0] != full:
                a = re.sub(r'\(uuid "[^"]*"\)', "", lib_symbols[bare][1])
                b = re.sub(r'\(uuid "[^"]*"\)', "", body)
                if a != b:
                    print(f"WARNING symbol name collision with differing bodies: {bare} ({lib_symbols[bare][0]} vs {full})")
            lib_symbols.setdefault(bare, (full, body))
        t = t[:s] + lib + t[e:]
    return t


for f, (newf, name) in SHEETS.items():
    (DST / newf).write_text(process_sheet(sheets_text[f], False))

# root sheet
root = process_sheet(sheets_text[OLD_PROJECT + ".kicad_sch"], True)
for s, e in reversed(list(top_blocks(root, "sheet"))):
    blk = root[s:e]
    sf = prop(blk, "Sheetfile")
    if sf in DROPPED:
        root = root[:s] + root[e:].lstrip("\n") if root[e:e+1] == "\n" else root[:s] + root[e:]
        continue
    newf, name = SHEETS[sf]
    blk = set_prop(blk, "Sheetfile", newf)
    blk = set_prop(blk, "Sheetname", name)
    root = root[:s] + blk + root[e:]
root = re.sub(r"\n{3,}", "\n\n", root)
(DST / f"{PROJECT}.kicad_sch").write_text(root)
print(f"root sheets kept: {len(list(top_blocks(root, 'sheet')))}; #PWR annotated: {pwr_counter}")

# merged symbol library
out = ['(kicad_symbol_lib', '\t(version 20241209)', '\t(generator "kicad_symbol_editor")', '\t(generator_version "9.0")']
for bare in sorted(lib_symbols):
    out.append(lib_symbols[bare][1])
out.append(")\n")
(DST / f"{LIB}.kicad_sym").write_text("\n".join(out))
print(f"merged library: {len(lib_symbols)} symbols; footprint names referenced: {len(fp_names)}")

# library tables
nicks = sorted({m for t in sheets_text.values() for m in re.findall(r'\(lib_id "([^:"]+):', t)} | {LIB})
slt = ['(sym_lib_table', '  (version 7)',
       '  (lib (name "blues-kicad-lib")(type "KiCad")(uri "${BLUES_KICAD_LIB_DIR}/blues-kicad-lib.kicad_sym")(options "")(descr ""))']
for n in nicks:
    slt.append(f'  (lib (name "{n}")(type "KiCad")(uri "${{KIPRJMOD}}/{LIB}.kicad_sym")(options "")(descr "Symbols captured during the Altium import"))')
slt.append(")\n")
(DST / "sym-lib-table").write_text("\n".join(slt))
(DST / "fp-lib-table").write_text(
    '(fp_lib_table\n  (version 7)\n'
    '  (lib (name "blues-kicad-lib")(type "KiCad")(uri "${BLUES_KICAD_LIB_DIR}/blues-kicad-lib.pretty")(options "")(descr ""))\n'
    f'  (lib (name "{LIB}")(type "KiCad")(uri "${{KIPRJMOD}}/{LIB}.pretty")(options "")(descr "Footprints captured during the Altium import"))\n)\n')

# project file: importer's, with v1.5 rules/severities/netclasses and our text vars
pro = json.loads((SRC / f"{OLD_PROJECT}.kicad_pro").read_text())
v15 = json.loads(V15_PRO.read_text())
pro["meta"]["filename"] = f"{PROJECT}.kicad_pro"
pro["text_variables"] = TEXT_VARS
rules = dict(v15["board"]["design_settings"]["rules"])
# v1.3 was routed to the board's own Altium rule set (read from the .PcbDoc Rules6
# stream): clearance 0.1 mm, track 0.1 mm, hole-to-hole 0.2 mm - a hair under each.
rules.update({"min_clearance": 0.0999, "min_track_width": 0.0999,
              "min_hole_clearance": 0.0999, "min_hole_to_hole": 0.1999})
pro["board"]["design_settings"]["rules"] = rules
pro["board"]["design_settings"]["rule_severities"] = v15["board"]["design_settings"]["rule_severities"]
pro["board"]["design_settings"]["drc_exclusions"] = []
pro["net_settings"] = json.loads(json.dumps(v15["net_settings"]))
for nc in pro["net_settings"]["classes"]:
    nc["clearance"], nc["track_width"] = 0.0999, 0.1
pro["erc"] = v15["erc"]
pro.pop("sheets", None)
for k in ("pinned_symbol_libs", "pinned_footprint_libs"):
    pro.setdefault("libraries", {})[k] = []
(DST / f"{PROJECT}.kicad_pro").write_text(json.dumps(pro, indent=2))
if (SRC / f"{OLD_PROJECT}.kicad_prl").exists():
    shutil.copy(SRC / f"{OLD_PROJECT}.kicad_prl", DST / f"{PROJECT}.kicad_prl")

# Graphic-only symbols (the Feather outline MOD2) have passive pins with nothing
# attached; ERC flags each as pin_not_connected. Their embedded lib symbol - in
# the sheet and in the merged library - gets no_connect-type pins instead.
NO_CONNECT_PINS = {"MOD2"}
for newf, _ in SHEETS.values():
    t = (DST / newf).read_text()
    for s, e in top_blocks(t, "symbol"):
        blk = t[s:e]
        if prop(blk, "Reference") in NO_CONNECT_PINS:
            lib_id = re.search(r'\(lib_id "([^"]*)"', blk).group(1)
            for path, name in ((DST / newf, lib_id), (DST / f"{LIB}.kicad_sym", lib_id.split(":", 1)[-1])):
                txt = path.read_text()
                i = txt.find(f'(symbol "{name}"')
                j = block_end(txt, i)
                n = txt[i:j].count("(pin passive")
                path.write_text(txt[:i] + txt[i:j].replace("(pin passive", "(pin no_connect") + txt[j:])
                print(f"{path.name}: {name}: {n} pins -> no_connect")
            break
print("done")
