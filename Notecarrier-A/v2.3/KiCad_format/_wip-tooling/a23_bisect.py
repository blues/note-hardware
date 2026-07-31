import re, subprocess, json, shutil

SRC = "/blues/note-hardware/Notecarrier-A/v2.3/KiCad_format/Notecarrier-A_Power.kicad_sch"
TST = "/tmp/bisect.kicad_sch"

def balanced_end(text, start):
    d=0; j=start
    while True:
        if text[j]=='(':d+=1
        elif text[j]==')':
            d-=1
            if d==0: return j+1
        j+=1

def fails(txt):
    open(TST, "w").write(txt)
    subprocess.run(["kicad-cli","sch","erc","--format","json","--output","/tmp/b-erc.json","--severity-error",TST],
                   capture_output=True)
    d = json.load(open("/tmp/b-erc.json"))
    for sh in d.get("sheets", []):
        for v in sh.get("violations", []):
            if "B4_A9" in json.dumps(v): return True
    return False

s = open(SRC).read()
print("full file fails:", fails(s))
# find all top-level element spans except lib_symbols, and the J11 symbol + its wires must stay
spans = []
i = 0
depth = 0
while i < len(s):
    c = s[i]
    if c == '"':
        i = s.index('"', i+1) + 1
        continue
    if c == '(':
        if depth == 1:
            m = re.match(r'\(([a-z_0-9]+)', s[i:])
            kind = m.group(1) if m else '?'
            end = balanced_end(s, i)
            spans.append((i, end, kind))
            i = end
            continue
        depth += 1
    elif c == ')':
        depth -= 1
    i += 1
print("top-level elements:", len(spans))
from collections import Counter
print(Counter(k for _,_,k in spans))
# keep-list: lib_symbols, the J11 instance, the VBUS wire, sheet_instances, paper/version etc (non-symbol scalars are part of header)
keep_always = set()
for a,e,k in spans:
    blk = s[a:e]
    if k in ("lib_symbols","sheet_instances","embedded_fonts","title_block","paper","version","generator","generator_version","uuid"):
        keep_always.add((a,e))
    elif k == "symbol" and '"Reference" "J11"' in blk:
        keep_always.add((a,e))
    elif k == "wire" and "(xy 144.78 209.55) (xy 127 209.55)" in blk:
        keep_always.add((a,e))
candidates = [(a,e,k) for a,e,k in spans if (a,e) not in keep_always]
print("candidates:", len(candidates))
# binary search: find minimal removal set that makes it PASS
def build(removed):
    out = []
    last = 0
    for a,e in sorted(removed):
        out.append(s[:a] if not out else s[last:a])
        last = e
    out.append(s[last:])
    return "".join(out)
# first check: removing ALL candidates -> passes?
allrem = {(a,e) for a,e,k in candidates}
print("all-removed fails:", fails(build(allrem)))
# bisect: find the single element whose PRESENCE causes failure
lo_set = []   # keep-side that still passes
active = sorted(allrem)
# iterative: add halves back while it passes
import sys
kept_back = set()
def test_with(back):
    return fails(build(allrem - set(back)))
# grow kept_back: binary search for a minimal blocking element
work = list(active)
blockers = []
while True:
    # try adding all remaining back
    if not test_with(kept_back | set(work)):
        kept_back |= set(work)
        break
    # find one blocker among work by bisection
    lo, hi = 0, len(work)
    cur = list(work)
    while len(cur) > 1:
        half = cur[:len(cur)//2]
        if test_with(kept_back | set(half)):
            cur = half
        else:
            kept_back |= set(half)
            cur = cur[len(cur)//2:]
    b = cur[0]
    blockers.append(b)
    work = [w for w in work if w != b and w not in kept_back]
    if len(blockers) > 4: break
for a,e in blockers:
    print("BLOCKER:", s[a:min(e,a+400)][:400])
