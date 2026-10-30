"""Regenerate a published X-series port board from the Rev-11 Altium import.

The published port was built from a post-v1.2 development-state PcbDoc. Its
schematic is substantively identical to Rev-11 (checked record by record), and
every footprint except the one jumper that moved is byte-identical between the
two raw imports. So: keep the port's file (header, setup, title block, text
variables, net table, footprints with all schematic metadata, embedded models)
and replace only the geometry with the Rev-11 import's:

  - segments / arcs / vias / zones (incl. their filled polygons - never refilled)
  - board-level graphics and dimensions (Edge.Cuts stroke width re-set to the
    port convention; port-added castellation join rects kept)
  - the moved footprint(s): 3-way merge base=dev-state raw, ours=port,
    theirs=Rev-11 raw
  - footprint 3D-model sub-blocks that differ between the two raw imports

Nets in transplanted items are renumbered by name, mapping raw net names to the
port's (schematic-derived) names through pad correspondence; any unmapped name
is a hard error. Plain python3 plus git (for `git merge-file`).

usage: transplant.py <port.kicad_pcb> <dev_raw.kicad_pcb> <rev11_raw.kicad_pcb> <out.kicad_pcb>
                     --moved R4 [--models P1,P2] [--edge-width 0.199898] [--pour-clearance 0.1499]
                     [--check-exclusions Notecarrier-XM.kicad_pro]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import uuid
from collections import Counter


PROPS = re.compile(r'\(property (?:"([^"]+)"|([^\s")]+))')


def blocks(t):
    """Top-level child blocks of the root s-expression: list of [start, end) spans."""
    i = t.index("(") + 1
    depth, start, out, j, n = 0, None, [], i, len(t)
    while j < n:
        c = t[j]
        if c == '"':
            j += 1
            while t[j] != '"':
                j += 2 if t[j] == "\\" else 1
        elif c == "(":
            if depth == 0:
                start = j
            depth += 1
        elif c == ")":
            if depth == 0:
                break
            depth -= 1
            if depth == 0:
                out.append((start, j + 1))
        j += 1
    return out


def kind(b):
    return re.match(r"\((\S+)", b).group(1)


def sub_blocks(b, head):
    """Spans of nested blocks starting with '(head ' at any depth (non-overlapping, outermost)."""
    out, i = [], 0
    pat = re.compile(r"\(" + re.escape(head) + r"[\s)]")
    while True:
        m = pat.search(b, i)
        if not m:
            return out
        s = m.start()
        d, j = 0, s
        while True:
            c = b[j]
            if c == '"':
                j += 1
                while b[j] != '"':
                    j += 2 if b[j] == "\\" else 1
            elif c == "(":
                d += 1
            elif c == ")":
                d -= 1
                if d == 0:
                    break
            j += 1
        out.append((s, j + 1))
        i = j + 1


def fp_ref(b):
    return re.search(r'\(property "Reference" "([^"]*)"', b).group(1)


def fp_at(b):
    return re.search(r"\n\t\t\(at ([^)]*)\)", b).group(1)


def fp_key(b):
    ref = fp_ref(b)
    return ref if ref else "@" + fp_at(b)


def pads(b):
    out = []
    for s, e in sub_blocks(b, "pad"):
        p = b[s:e]
        num = re.match(r'\(pad "([^"]*)"', p).group(1)
        at = re.search(r"\(at ([^)]*)\)", p).group(1)
        m = re.search(r'\(net (\d+) "((?:[^"\\]|\\.)*)"\)', p)
        out.append((num, at, m.group(2) if m else "", (s, e)))
    return out


def net_table(bl, t):
    tab = {}
    for s, e in bl:
        b = t[s:e]
        if kind(b) == "net":
            m = re.match(r'\(net (\d+) "((?:[^"\\]|\\.)*)"\)', b)
            tab[int(m.group(1))] = m.group(2)
    return tab


def zone_key(b):
    """Identity of a zone that survives re-import: pours by net/layers/priority,
    rule areas by layers, keepout flags and exact outline."""
    layers = re.search(r'\n\t\t\(layers? ([^)]*)\)', b).group(1)
    if "(keepout" in b:
        flags = re.sub(r"\s+", " ", b[slice(*sub_blocks(b, "keepout")[0])])
        outline = re.sub(r"\s+", " ", b[slice(*sub_blocks(b, "polygon")[0])])
        return ("rule-area", layers, flags, outline)
    net = re.search(r'\(net_name "((?:[^"\\]|\\.)*)"\)', b).group(1)
    prio = re.search(r"\n\t\t\(priority (\d+)\)", b)
    return ("pour", net, layers, prio.group(1) if prio else "0")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("port")
    ap.add_argument("raw469")
    ap.add_argument("raw11")
    ap.add_argument("out")
    ap.add_argument("--moved", default="")
    ap.add_argument("--models", default="")
    ap.add_argument("--edge-width", default="0.199898")
    ap.add_argument("--pour-clearance", default="0.1499")
    ap.add_argument("--check-exclusions", metavar="KICAD_PRO",
                    help="fail if a DRC exclusion in this project references a UUID the output lacks")
    a = ap.parse_args()
    moved = [x for x in a.moved.split(",") if x]
    model_refs = [x for x in a.models.split(",") if x]

    P = open(a.port, encoding="utf-8").read()
    B = open(a.raw469, encoding="utf-8").read()
    R = open(a.raw11, encoding="utf-8").read()
    pbl, bbl, rbl = blocks(P), blocks(B), blocks(R)

    # --- sanity: board-level sections the port inherited must not differ between raw imports
    def section(t, bl, k):
        return [re.sub(r'\(uuid "[^"]+"\)', "", t[s:e]) for s, e in bl if kind(t[s:e]) == k]
    for k in ("general", "layers", "setup", "paper"):
        if section(B, bbl, k) != section(R, rbl, k):
            print(f"WARNING: raw imports differ in ({k}) - port keeps its own", file=sys.stderr)

    pnet = net_table(pbl, P)
    pnum = {v: k for k, v in pnet.items()}
    rnet = net_table(rbl, R)

    pf = {fp_key(P[s:e]): P[s:e] for s, e in pbl if kind(P[s:e]) == "footprint"}
    rf = {fp_key(R[s:e]): R[s:e] for s, e in rbl if kind(R[s:e]) == "footprint"}
    bf = {fp_key(B[s:e]): B[s:e] for s, e in bbl if kind(B[s:e]) == "footprint"}
    if set(pf) != set(rf):
        sys.exit(f"footprint sets differ: port-only {set(pf)-set(rf)} raw-only {set(rf)-set(pf)}")

    # --- raw net name -> port net name, via pad correspondence
    name_map, conflicts = {"": ""}, []
    for key, rb in rf.items():
        if key.startswith("@"):
            continue
        ppads = pads(pf[key])
        for num, at, rn, _ in pads(rb):
            if not rn:
                continue
            cand = [pn for (pn_num, pat, pn, _) in ppads if pn_num == num and (key in moved or pat == at)]
            if len(set(cand)) != 1:
                conflicts.append((key, num, at, rn, cand))
                continue
            pn = cand[0]
            if name_map.setdefault(rn, pn) != pn:
                conflicts.append((key, num, rn, name_map[rn], pn))
    if conflicts:
        sys.exit(f"net mapping conflicts: {conflicts[:10]}")
    inv = Counter(name_map.values())
    dup = [n for n, c in inv.items() if c > 1 and n]
    if dup:
        sys.exit(f"two raw nets map to one port net: {dup}")

    def renum(text):
        """Rewrite (net N) / (net N "x") / (net_name "x") in a raw block to port numbering."""
        def m_net(m):
            raw_name = rnet[int(m.group(1))]
            if raw_name not in name_map:
                raise SystemExit(f"raw net {raw_name!r} has no port equivalent")
            pn = name_map[raw_name]
            num = pnum[pn] if pn else 0
            return f"(net {num}" + (f' "{pn}")' if m.group(2) is not None else ")")
        text = re.sub(r'\(net (\d+)(?: ("(?:[^"\\]|\\.)*"))?\)', m_net, text)

        def m_nn(m):
            return f'(net_name "{name_map[m.group(1)]}")'
        return re.sub(r'\(net_name "((?:[^"\\]|\\.)*)"\)', m_nn, text)

    # --- 3-way merge for moved footprints
    def norm(b):
        b = re.sub(r'\(uuid "[^"]+"\)', '(uuid "@@")', b)
        return re.sub(r'\(net \d+ "', '(net "', b)

    def merge(key):
        base, ours, theirs = norm(bf[key]), norm(pf[key]), norm(rf[key])
        # The lib-id line and schematic linkage always come from the port: each raw
        # import carries its own random path, and the lib id sits next to the layer
        # line that the move changes (adjacent edits conflict in a line merge).
        head = ours.split("\n", 1)[0]
        base, ours, theirs = (x.split("\n", 1)[1] for x in (base, ours, theirs))
        link = re.compile(r'\n\t\t\((path|sheetname|sheetfile) "[^"]*"\)')
        base_link = "".join(m.group(0) for m in link.finditer(base))
        theirs = link.sub("", theirs)
        anchor = re.search(r"\n\t\t\(fp_|\n\t\t\(pad ", theirs).start()
        theirs = theirs[:anchor] + base_link + theirs[anchor:]
        with tempfile.TemporaryDirectory() as d:
            paths = []
            for nm, txt in (("ours", ours), ("base", base), ("theirs", theirs)):
                p = os.path.join(d, nm)
                open(p, "w", encoding="utf-8").write(txt + "\n")
                paths.append(p)
            r = subprocess.run(["git", "merge-file", "-p", *paths], capture_output=True, text=True)
        merged = r.stdout
        if r.returncode != 0:
            # Adjacent edits (port changed a field's text, the move changed the
            # field's position line) are reported as conflicts. Resolve only
            # equal-length hunks, line by line: property value lines from the port,
            # everything else (geometry) from the Rev-11 import.
            hunk = re.compile(r"<<<<<<< [^\n]*\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n", re.S)

            def res(hm):
                o, th = hm.group(1).splitlines(True), hm.group(2).splitlines(True)
                if len(o) != len(th):
                    sys.exit(f"unresolvable conflict in {key}:\n{hm.group(0)}")
                return "".join(ol if ol.lstrip().startswith("(property ") else tl for ol, tl in zip(o, th))
            merged = hunk.sub(res, merged)
            if "<<<<<<<" in merged:
                sys.exit(f"merge conflict left in {key}")
            print(f"{key}: resolved {len(hunk.findall(r.stdout))} adjacent-edit hunks", file=sys.stderr)
        m = head + "\n" + merged.rstrip("\n")
        # restore uuids from the port block in order (same structure), else fresh
        puu = re.findall(r'\(uuid "([^"]+)"\)', pf[key])
        n_slots = m.count('(uuid "@@")')
        it = iter(puu if len(puu) == n_slots else [str(uuid.uuid4()) for _ in range(n_slots)])
        m = re.sub(r'\(uuid "@@"\)', lambda _: f'(uuid "{next(it)}")', m)
        # pad nets: port names -> port numbers
        m = re.sub(r'\(net "((?:[^"\\]|\\.)*)"\)', lambda x: f'(net {pnum[x.group(1)]} "{x.group(1)}")', m)
        # hidden schematic fields the port added on the old side follow the part to its new side
        # (and to its new rotation: field angles are stored absolute, so take the
        # angle the importer gave the untouched Datasheet field on each side)
        side = re.search(r'\n\t\t\(layer "([FB])\.Cu"\)', m).group(1)
        old = re.search(r'\n\t\t\(layer "([FB])\.Cu"\)', pf[key]).group(1)
        ang = re.compile(r'\(property "Datasheet" ""\s*\(at 0 0 (-?[0-9.]+)\)')
        a_old, a_new = ang.search(pf[key]).group(1), ang.search(m).group(1)
        if side != old or a_old != a_new:
            added = ({x or y for x, y in PROPS.findall(pf[key])}
                     - {x or y for x, y in PROPS.findall(bf[key])})

            def fix(blk):
                nm = next(x for x in PROPS.match(blk).groups() if x)
                if nm not in added:
                    return blk
                blk = blk.replace(f'(layer "{old}.Fab")', f'(layer "{side}.Fab")')
                if side == "F":
                    blk = re.sub(r"\n\t+\(justify mirror\)", "", blk)
                return blk.replace(f"(at 0 0 {a_old})", f"(at 0 0 {a_new})")
            out, last = [], 0
            for s, e in sub_blocks(m, "property"):
                out.append(m[last:s])
                out.append(fix(m[s:e]))
                last = e
            out.append(m[last:])
            m = "".join(out)
        print(f"merged {key}: side {old}->{side}, uuids {'port' if len(puu) == n_slots else 'fresh'}", file=sys.stderr)
        return m

    def swap_models(key):
        ob = pf[key]
        om = sub_blocks(ob, "model")
        rm = sub_blocks(rf[key], "model")
        if len(om) != len(rm):
            sys.exit(f"{key}: model count differs {len(om)} vs {len(rm)}")
        out, last = [], 0
        for (s, e), (rs, re_) in zip(om, rm):
            out.append(ob[last:s])
            out.append(rf[key][rs:re_])
            last = e
        out.append(ob[last:])
        return "".join(out)

    # --- assemble
    GEOM = {"segment", "arc", "via", "zone", "gr_line", "gr_arc", "gr_circle", "gr_poly", "gr_text",
            "gr_text_box", "gr_curve", "gr_bbox", "dimension", "image", "group", "target"}
    # Zones keep the port's UUID when they correspond unambiguously: DRC
    # exclusions in the .kicad_pro name zones by UUID, and the importer mints
    # fresh ones on every run.
    port_zones = {}
    for s, e in pbl:
        if kind(P[s:e]) == "zone":
            port_zones.setdefault(zone_key(P[s:e]), []).append(
                re.search(r'\(uuid "([^"]+)"\)', P[s:e]).group(1))
    zone_uuid_kept = zone_uuid_fresh = 0
    new_zone_keys = {}

    items = []
    inserted = False
    kept_rects = 0
    for s, e in pbl:
        b = P[s:e]
        k = kind(b)
        if k == "footprint":
            key = fp_key(b)
            if key in moved:
                b = merge(key)
            elif key in model_refs:
                b = swap_models(key)
            items.append(b)
        elif k == "gr_rect":
            kept_rects += 1          # port-added castellation joins (net-assigned copper)
            items.append(b)
        elif k in GEOM:
            if inserted:
                continue
            inserted = True
            for rs, re_ in rbl:
                rb = R[rs:re_]
                rk = kind(rb)
                if rk not in GEOM:
                    continue
                if rk == "gr_rect":
                    sys.exit("raw import unexpectedly has gr_rect")
                rb = renum(rb)
                if '(face "KiCad Font")' in rb:
                    # KiCad 9.0.9 drops a TrueType face (and converts its size
                    # as stroke text) when the PcbDoc's font-name padding is not
                    # valid UTF-16 - import a sanitize_fonts.py copy instead.
                    sys.exit("TrueType text fell back to the stroke font - import the sanitized PcbDoc")
                if rk.startswith("gr_") and '(layer "Edge.Cuts")' in rb:
                    rb = re.sub(r"\(width [0-9.]+\)", f"(width {a.edge_width})", rb, count=1)
                if rk == "zone" and "(keepout" not in rb:
                    rb, n = re.subn(r"(\(connect_pads[^\n]*\n\t+)\(clearance [0-9.]+\)",
                                    rf"\g<1>(clearance {a.pour_clearance})", rb)
                    if n != 1:
                        sys.exit("pour zone without a connect_pads clearance")
                if rk == "zone":
                    zk = zone_key(rb)
                    cand = port_zones.get(zk, [])
                    if len(cand) == 1:
                        zid = cand.pop()
                        zone_uuid_kept += 1
                    else:
                        # a zone the port lacks: derive the UUID from its identity
                        # so every regeneration produces the same one
                        n = new_zone_keys[zk] = new_zone_keys.get(zk, -1) + 1
                        zid = str(uuid.uuid5(uuid.NAMESPACE_URL, f"kicad-zone:{zk!r}:{n}"))
                        zone_uuid_fresh += 1
                    rb = re.sub(r'\(uuid "[^"]+"\)', f'(uuid "{zid}")', rb, count=1)
                items.append(rb)
        else:
            items.append(b)
    text = P[:pbl[0][0]] + "\n\t".join(items) + P[pbl[-1][1]:]
    # KiCad writes a dimension's embedded text with the dimension's own UUID,
    # so count each UUID once per dimension block.
    seen = Counter()
    for s, e in blocks(text):
        ids = re.findall(r'\(uuid "([^"]+)"\)', text[s:e])
        seen.update(set(ids) if kind(text[s:e]) == "dimension" else ids)
    dup = [u for u, c in seen.items() if c > 1]
    if dup:
        sys.exit(f"duplicate UUIDs in the output: {dup[:5]}")
    if a.check_exclusions:
        pro = json.load(open(a.check_exclusions, encoding="utf-8"))
        missing = []
        for ex in pro["board"]["design_settings"].get("drc_exclusions", []):
            key = ex[0] if isinstance(ex, list) else ex
            for u in re.findall(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", key):
                if u != "00000000-0000-0000-0000-000000000000" and f'(uuid "{u}")' not in text:
                    missing.append(key)
        if missing:
            sys.exit(f"DRC exclusions reference UUIDs absent from the output: {missing}")
    open(a.out, "w", encoding="utf-8").write(text)
    print(f"zones: {zone_uuid_kept} kept the port's UUID, {zone_uuid_fresh} new (deterministic)", file=sys.stderr)
    print(f"wrote {a.out}: kept {kept_rects} port gr_rect, mapped {len(name_map)-1} nets", file=sys.stderr)


if __name__ == "__main__":
    main()
