import pcbnew, os
LIB = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A-local.pretty"
os.makedirs(LIB, exist_ok=True)
fp = pcbnew.FOOTPRINT(None)
fp.SetFPID(pcbnew.LIB_ID("", "AMPHENOL_12402012E212A"))
fp.Reference().SetText("REF**")
fp.Reference().SetVisible(False)
fp.Value().SetText("12402012E212A")
fp.Value().SetLayer(pcbnew.F_Fab)
def mk(num, lx, ly, sx, sy, kind="smd", drillx=0, drilly=0, shape=None):
    p = pcbnew.PAD(fp)
    p.SetNumber(num)
    p.SetPosition(pcbnew.VECTOR2I(int(lx*1e6), int(ly*1e6)))
    p.SetSize(pcbnew.F_Cu, pcbnew.VECTOR2I(int(sx*1e6), int(sy*1e6)))
    if kind == "smd":
        p.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        p.SetLayerSet(pcbnew.PAD.SMDMask())
        p.SetShape(pcbnew.F_Cu, shape or pcbnew.PAD_SHAPE_RECT)
    elif kind == "pth":
        p.SetAttribute(pcbnew.PAD_ATTRIB_PTH)
        p.SetLayerSet(pcbnew.PAD.PTHMask())
        p.SetShape(pcbnew.F_Cu, shape or pcbnew.PAD_SHAPE_OVAL)
        p.SetDrillShape(pcbnew.PAD_DRILL_SHAPE_OBLONG if drilly != drillx else pcbnew.PAD_DRILL_SHAPE_CIRCLE)
        p.SetDrillSize(pcbnew.VECTOR2I(int(drillx*1e6), int(drilly*1e6)))
    elif kind == "npth":
        p.SetAttribute(pcbnew.PAD_ATTRIB_NPTH)
        p.SetLayerSet(pcbnew.PAD.UnplatedHoleMask())
        p.SetShape(pcbnew.F_Cu, pcbnew.PAD_SHAPE_CIRCLE)
        p.SetDrillShape(pcbnew.PAD_DRILL_SHAPE_CIRCLE)
        p.SetDrillSize(pcbnew.VECTOR2I(int(drillx*1e6), int(drillx*1e6)))
        p.SetNumber("")
    fp.Add(p)
    return p
# signal pads: local=(-rel, -3.39); wide 0.6 -> local size (0.6,1.14); narrow 0.3 -> (0.3,1.14)
# Pad naming derived from the published v20 films' own connectivity (a USB-C
# receptacle is rotationally symmetric, so the contact row reads B-side first
# in this orientation): CC2->R32 at film y 12.01, the D pairs at 13.01/13.51
# (B6/B7) and 14.01/14.51 (A6/A7), CC1->R33 at 15.01, SBU1/SBU2 unrouted.
SIG = [("B1_A12", -3.2, 0.6), ("B4_A9", -2.4, 0.6), ("B5", -1.75, 0.3), ("B8", -1.25, 0.3),
       ("B6", -0.75, 0.3), ("B7", -0.25, 0.3), ("A6", 0.25, 0.3), ("A7", 0.75, 0.3),
       ("A5", 1.25, 0.3), ("A8", 1.75, 0.3), ("A4_B9", 2.4, 0.6), ("A1_B12", 3.2, 0.6)]
for num, rel, w in SIG:
    mk(num, -rel, -3.39, w, 1.14)
# shield PTH oval slots: legs A (film rel -1.36,±4.32): local (∓4.32, +1.36), pad (0.9,1.8), slot (0.6,1.4)
mk("S1", -4.32, 1.36, 0.9, 1.8, "pth", 0.6, 1.4)
mk("S2",  4.32, 1.36, 0.9, 1.8, "pth", 0.6, 1.4)
# legs B (film rel +2.82,±4.32): local (∓4.32, -2.82), pad (1.05,2.1), slot (0.6,1.7)
mk("S3", -4.32, -2.82, 1.05, 2.1, "pth", 0.6, 1.7)
mk("S4",  4.32, -2.82, 1.05, 2.1, "pth", 0.6, 1.7)
# NPTH pegs 0.65 at local (∓2.89, -2.32)
mk("", -2.89, -2.32, 0.65, 0.65, "npth", 0.65)
mk("",  2.89, -2.32, 0.65, 0.65, "npth", 0.65)
# fab outline (body approx 9.3 x 7.4, mouth toward +y local? edge toward local +y since abs edge x=+75 -> absdelta +x from fp -> local -y?? edge at kicad x 55-side... skip precision: simple body rect)
r = pcbnew.PCB_SHAPE(fp)
r.SetShape(pcbnew.SHAPE_T_RECTANGLE)
r.SetStart(pcbnew.VECTOR2I(int(-4.7e6), int(-3.6e6)))
r.SetEnd(pcbnew.VECTOR2I(int(4.7e6), int(3.6e6)))
r.SetLayer(pcbnew.F_Fab)
r.SetWidth(int(0.1e6))
fp.Add(r)
io = pcbnew.PCB_IO_KICAD_SEXPR()
io.FootprintSave(LIB, fp)
print("footprint written:", os.listdir(LIB))
