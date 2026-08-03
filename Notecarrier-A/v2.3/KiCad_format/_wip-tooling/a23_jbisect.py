import re, subprocess, json, shutil
SRC = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
s0 = open(SRC).read()
exec(open("/scratch/kd/a23_classes.py").read().split("spans = top_spans(s0)")[0].replace('print(tag, "-> fails" if bad else "-> PASSES")', 'pass'))
spans = top_spans(s0)
jns = [(a,e) for a,e,k in spans if k == "junction"]
def fails_with_removed(rem):
    return check(build_without(s0, rem), "probe")
# find minimal blocking junction: binary search over which junction's REMOVAL fixes it
# removal of all passes; find single junction j st removing ONLY j passes
lo, hi = 0, len(jns)
work = list(jns)
# try removing one at a time via bisection: find subset S of junctions st removing S passes and S minimal
# first: does removing half pass?
cur = list(work)
removedset = None
while len(cur) > 1:
    half1 = cur[:len(cur)//2]
    if not check(build_without(s0, half1), f"remove {len(half1)} (first half)"):
        cur = half1
    else:
        half2 = cur[len(cur)//2:]
        if not check(build_without(s0, half2), f"remove {len(half2)} (second half)"):
            cur = half2
        else:
            print("no single-half fix; multiple blockers")
            break
if len(cur) == 1:
    a, e = cur[0]
    print("BLOCKING JUNCTION:", s0[a:e])
