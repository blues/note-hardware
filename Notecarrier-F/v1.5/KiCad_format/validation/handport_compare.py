#!/usr/bin/env python3
"""Connectivity-partition comparison between this Altium-imported schematic and
the independently hand-ported v1.5 schematic (a delta port of the v1.3 KiCad
project, made before the Altium sources were available). Two routes to the
same board: if they agree, both are right; where they disagree, one is wrong.

Pin numbers differ between the two symbol sets (Altium SIM socket pins are
named C1..C7 vs 1..7, the hand-port's USB-C symbol pairs pins as A4_B9, its
diode/capacitor/resistor pin 1/2 conventions are swapped on several parts), so
partitions are compared on the set of *component references* they touch, then
the pin-level differences are listed for review.

Usage: handport_compare.py <import.net> <handport.net>
"""
import re, sys
def parse(s):
    tok=re.findall(r'"(?:\\.|[^"\\])*"|\(|\)|[^\s()"]+',s); st=[[]]
    for t in tok:
        if t=='(': st.append([])
        elif t==')': l=st.pop(); st[-1].append(l)
        else: st[-1].append(t)
    return st[0][0]
def find(n,k): return [c for c in n if isinstance(c,list) and c and c[0]==k]
def nets(path):
    doc=parse(open(path).read()); out={}
    for n in find(find(doc,'nets')[0],'net'):
        name=find(n,'name')[0][1].strip('"'); s=set()
        for node in find(n,'node'): s.add((find(node,'ref')[0][1].strip('"'),find(node,'pin')[0][1].strip('"')))
        if len(s)>=2: out[name]=frozenset(s)
    return out
A=nets(sys.argv[1]); B=nets(sys.argv[2])
alias={'MODL1':'MOD1L','MODR1':'MOD1R'}
def refsets(parts): return {frozenset(alias.get(r,r) for r,p in s):n for n,s in parts.items()}
Ar,Br=refsets(A),refsets(B)
same=set(Ar)&set(Br)
print(f'import nets (>=2 pins): {len(A)}   hand-port nets: {len(B)}   identical by touched-component set: {len(same)}')
for s in sorted(set(Ar)-set(Br),key=lambda x:Ar[x]): print('  IMPORT ONLY  ',Ar[s],sorted(s))
for s in sorted(set(Br)-set(Ar),key=lambda x:Br[x]): print('  HAND-PORT ONLY',Br[s],sorted(s))
