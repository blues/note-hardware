import sys, math
sys.path.insert(0, "/scratch/kd")
src = open("/scratch/kd/a23_fabnets.py").read()
exec(src[:src.index("b = pcbnew.LoadBoard(PCB)")])
from collections import Counter, defaultdict
sizes = Counter()
members = defaultdict(list)
for tag, (segs, fls, regs, items) in layer_data.items():
    for k in items:
        r = uf.find(k); sizes[r] += 1; members[r].append(k)
for hi in range(len(holes)):
    r = uf.find(("H", hi)); sizes[r] += 1; members[r].append(("H", hi))
top5 = sizes.most_common(5)
print("largest islands:", [(n) for _, n in top5])
big = top5[0][0]
ms = members[big]
print("biggest island item count:", len(ms))
print("by layer:", Counter(m[0] for m in ms))
# widest segments and biggest flashes in it
segsin = [(layer_data[m[0]][0][m[2]], m) for m in ms if m[1] == "s"]
flsin = [(layer_data[m[0]][1][m[2]], m) for m in ms if m[1] == "f"]
segsin.sort(key=lambda t: -t[0][4])
flsin.sort(key=lambda t: -t[0][2])
print("widest segments:")
for s_, m in segsin[:6]:
    print(f"   {m[0]} w={s_[4]:.2f} ({s_[0]:.2f},{s_[1]:.2f})->({s_[2]:.2f},{s_[3]:.2f})")
print("biggest flashes:")
for f_, m in flsin[:8]:
    print(f"   {m[0]} r={f_[2]:.3f} at ({f_[0]:.2f},{f_[1]:.2f})")
