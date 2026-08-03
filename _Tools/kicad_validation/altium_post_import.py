#!/usr/bin/env python3
"""Post-process a KiCad schematic produced by the Altium project importer.

The GUI importer (KiCad 9, File > Import Non-KiCad Project) wraps a flat
Altium project in a virtual root sheet that is never written to disk when the
project name collides with a design sheet name. Sheets saved that way carry
EMPTY `(instances)` blocks, which silently excludes every symbol from the
connectivity graph: pins never bind to wires, wire-only nets vanish from
netlists, and ERC reports the wires as dangling. (Diagnosed on the Mojo v1.1
pilot port, 2026-07-28.)

Fixes applied, in order:
  1. populate empty `(instances)` blocks with this file as the root sheet
     (project name + root uuid + Reference/unit from the symbol properties);
  2. normalize every symbol lib nickname (`TBL Connectors:`, `Altium Content
     Vault:`, `*:`, ...) to a single project-import nickname so the
     sym-lib-table can resolve all of them;
  3. strip stale `(render_cache ...)` blocks (glyphs baked with substituted
     fonts on the import machine);
  4. regenerate `<nickname>.kicad_sym` from the schematic's embedded
     lib_symbols so the external library matches the embedded copies exactly.

Usage:
    altium_post_import.py <schematic.kicad_sch> --project <name>
                          [--nickname <lib-nickname>] [--no-symlib]
"""

import argparse
import re
import sys
from pathlib import Path


def balanced_block(text, start):
    """Return end index (inclusive) of the s-expr starting at `start`."""
    depth, p = 0, start
    while p < len(text):
        if text[p] == "(":
            depth += 1
        elif text[p] == ")":
            depth -= 1
            if depth == 0:
                return p
        p += 1
    raise ValueError("unbalanced s-expression")


def strip_blocks(text, token):
    out, i, removed = [], 0, 0
    tok = "(" + token
    while True:
        j = text.find(tok, i)
        if j == -1:
            out.append(text[i:])
            break
        k = j + len(tok)
        if k < len(text) and text[k] not in " \t\n(":
            out.append(text[i:k])
            i = k
            continue
        out.append(text[i:j].rstrip("\t "))
        p = balanced_block(text, j)
        i = p + 1
        if i < len(text) and text[i] == "\n":
            i += 1
        removed += 1
    return "".join(out), removed


def fix_instances(text, project, root_uuid):
    blocks = text.split("\n\t(symbol\n")
    out, fixed = [blocks[0]], 0
    for b in blocks[1:]:
        if "(instances)" in b:
            ref = re.search(r'\(property "Reference" "([^"]+)"', b)
            unit = re.search(r"^\t\t\(unit (\d+)\)", b, re.M)
            refv = ref.group(1) if ref else "U?"
            unitv = unit.group(1) if unit else "1"
            inst = (
                f'(instances\n\t\t\t(project "{project}"\n'
                f'\t\t\t\t(path "/{root_uuid}"\n'
                f'\t\t\t\t\t(reference "{refv}")\n\t\t\t\t\t(unit {unitv})\n'
                f"\t\t\t\t)\n\t\t\t)\n\t\t)"
            )
            b = b.replace("(instances)", inst, 1)
            fixed += 1
        out.append(b)
    return "\n\t(symbol\n".join(out), fixed


def normalize_nicknames(text, nickname):
    """Rewrite `<anything>:<name>` lib ids/names to `<nickname>:<name>`."""
    names = set(re.findall(r'\n\t\t\(symbol "([^"]+)"', text))
    mapping = {}
    for full in names:
        if ":" in full:
            suffix = full.split(":", 1)[1]
        else:
            suffix = full
        target = f"{nickname}:{suffix}"
        if full != target:
            mapping[full] = target
    # collision check
    targets = list(mapping.values())
    if len(set(targets)) != len(targets):
        raise SystemExit("nickname normalization would collide; aborting")
    for old, new in mapping.items():
        text = text.replace(f'(symbol "{old}"', f'(symbol "{new}"')
        text = text.replace(f'(lib_id "{old}")', f'(lib_id "{new}")')
    return text, len(mapping)


def extract_symlib(text, nickname, generator_version="9.0"):
    """Build a .kicad_sym file from the schematic's embedded lib_symbols."""
    i = text.find("\t(lib_symbols")
    if i == -1:
        return None
    p = balanced_block(text, i + 1)
    body = text[i + len("\t(lib_symbols"): p].rstrip()
    # strip the nickname prefix from symbol names (library files use bare names)
    body = body.replace(f'(symbol "{nickname}:', '(symbol "')
    return (
        "(kicad_symbol_lib\n"
        "\t(version 20241209)\n"
        '\t(generator "kicad_symbol_editor")\n'
        f'\t(generator_version "{generator_version}")\n'
        f"{body}\n)\n"
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("schematic", type=Path)
    ap.add_argument("--project", required=True)
    ap.add_argument("--nickname", default=None,
                    help="lib nickname (default: <project>-altium-import)")
    ap.add_argument("--no-symlib", action="store_true")
    args = ap.parse_args()
    nickname = args.nickname or f"{args.project}-altium-import"

    text = args.schematic.read_text()
    root_uuid = re.search(
        r'\(kicad_sch\n\t\(version[^\n]*\n\t\(generator[^\n]*\n'
        r'\t\(generator_version[^\n]*\n\t\(uuid "([^"]+)"', text).group(1)

    text, n_inst = fix_instances(text, args.project, root_uuid)
    text, n_nick = normalize_nicknames(text, nickname)
    text, n_rc = strip_blocks(text, "render_cache")
    args.schematic.write_text(text)
    print(f"{args.schematic.name}: instances={n_inst} nicknames={n_nick} "
          f"render_caches_removed={n_rc}")

    if not args.no_symlib:
        lib = extract_symlib(text, nickname)
        if lib:
            out = args.schematic.parent / f"{nickname}.kicad_sym"
            out.write_text(lib)
            print(f"wrote {out.name} ({len(lib)} bytes)")


if __name__ == "__main__":
    main()
