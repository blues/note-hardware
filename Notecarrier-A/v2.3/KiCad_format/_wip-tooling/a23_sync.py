"""Scripted 'Update PCB from Schematic' for the A v2.3 delta.

Re-link by reference ON, replace footprints OFF (house convention). Handles the
three things the delta changes: J2 removed, R32/R33 added, J11's footprint
swapped to the USB-C part with a new pad-name set.
"""
import re, subprocess, pcbnew

PCB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_pcb"
SCH = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A.kicad_sch"
LIB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A-local.pretty"

subprocess.run(["kicad-cli", "sch", "export", "netlist", "--format", "kicadsexpr",
                "-o", "/tmp/a23sync.net", SCH], capture_output=True)
net = open("/tmp/a23sync.net").read()

# refdes -> {pad: net}, and refdes -> footprint lib id
pad_nets, fps_sch = {}, {}
for m in re.finditer(r'\(comp \(ref "([^"]+)"\)(.*?)(?=\(comp |\Z)', net, re.S):
    ref, body = m.group(1), m.group(2)
    fpm = re.search(r'\(footprint "([^"]+)"\)', body)
    if fpm: fps_sch[ref] = fpm.group(1)
for m in re.finditer(r'\(net \(code "\d+"\) \(name "([^"]+)"\)(.*?)(?=\(net |\Z)', net, re.S):
    nname = m.group(1)
    for ref, pin in re.findall(r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"\)', m.group(2)):
        pad_nets.setdefault(ref, {})[pin] = nname

b = pcbnew.LoadBoard(PCB)
board_refs = {fp.GetReference(): fp for fp in b.GetFootprints()}

def fpid_str(fp):
    try:
        return fp.GetFPIDAsString()
    except AttributeError:
        return str(fp.GetFPID().Format())

IO = pcbnew.PCB_IO_KICAD_SEXPR()
def load_fp(libpath, fpname):
    return IO.FootprintLoad(libpath, fpname)

def netcode(name):
    ni = b.FindNet(name)
    if ni is None:
        ni = pcbnew.NETINFO_ITEM(b, name)
        b.Add(ni)
    return ni.GetNetCode()

# ---- 1. remove footprints absent from the schematic ----
sch_refs = set(fps_sch)
for ref, fp in list(board_refs.items()):
    if ref not in sch_refs and not ref.startswith(("H", "FID", "PAD", "ANT", "OBJ", "BAT", "CS")):
        print(f"removing footprint {ref}")
        b.Remove(fp)
        del board_refs[ref]

# ---- 2. swap J11's footprint ----
want = fps_sch.get("J11")
old = board_refs.get("J11")
if old and want and fpid_str(old) != want:
    libname, fpname = want.split(":")
    libpath = LIB if libname.endswith("local") else "/blues/blues-kicad-lib/blues-kicad-lib.pretty"
    newfp = load_fp(libpath, fpname)
    assert newfp, want
    newfp.SetReference("J11")
    newfp.SetValue(old.GetValue())
    newfp.SetPosition(old.GetPosition())
    newfp.SetOrientation(old.GetOrientation())
    if old.IsFlipped() != newfp.IsFlipped():
        newfp.Flip(newfp.GetPosition(), False)
    newfp.SetFPID(pcbnew.LIB_ID(libname, fpname))
    b.Remove(old)
    b.Add(newfp)
    board_refs["J11"] = newfp
    print(f"J11 footprint -> {want}")

# ---- 3. add missing footprints ----
for ref in sorted(sch_refs - set(board_refs)):
    lid = fps_sch[ref]
    libname, fpname = lid.split(":")
    libpath = LIB if libname.endswith("local") else "/blues/blues-kicad-lib/blues-kicad-lib.pretty"
    fp = load_fp(libpath, fpname)
    if not fp:
        print(f"!! cannot load {lid} for {ref}")
        continue
    fp.SetReference(ref)
    fp.SetFPID(pcbnew.LIB_ID(libname, fpname))
    fp.SetPosition(pcbnew.VECTOR2I(int(60e6), int(150e6)))
    b.Add(fp)
    board_refs[ref] = fp
    print(f"added footprint {ref} ({lid})")

# ---- 4. reassign pad nets from the schematic ----
changed = 0
for ref, fp in board_refs.items():
    want_nets = pad_nets.get(ref)
    if not want_nets: continue
    for pad in fp.Pads():
        num = pad.GetNumber()
        if not num: continue
        nn = want_nets.get(num)
        if nn is None:
            if pad.GetNetCode() != 0:
                pad.SetNetCode(0); changed += 1
            continue
        if pad.GetNetname() != nn:
            pad.SetNetCode(netcode(nn)); changed += 1
print(f"pad net assignments changed: {changed}")

pcbnew.SaveBoard(PCB, b)
b2 = pcbnew.LoadBoard(PCB)
b2.BuildConnectivity()
print("unconnected after sync:", b2.GetConnectivity().GetUnconnectedCount(True))
