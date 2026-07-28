# Mojo v1.1 — Altium ➜ KiCad 9 Porting Notes

This project was ported from the Altium Designer sources in
[`Mojo/v1.1/Sources/`](../../Sources/) (internal design name *Mojo-v4*) using
KiCad 9.0.9's **File → Import → Non-KiCad Project → Altium Project** importer,
followed by the scripted cleanup and validation battery in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/).
It follows the conventions of the earlier Notecarrier-B/-A/-Pi/-F ports.

## Source material

| Input | Role |
|---|---|
| `Sources/Mojo.PrjPcb`, `Mojo.SchDoc`, `Cover Sheet.SchDoc`, `Design Notes.SchDoc`, `Mojo.PcbDoc` | imported |
| `Assembly Normal/BOM/BOM-Mojo-v4-Normal.xls` | BOM ground truth (production variant) |
| `Fabrication/Gerber/Mojo v4.*` | gerber/drill ground truth for the layer diffs |
| `Fabrication/Reports/{DRC,ERC}/Mojo.html` | Altium rule values (7 mil clearance, 0 mil board edge, 10 mil hole-to-hole) |

## Import quirks and how they were fixed

- **Flat-project virtual root / empty `(instances)` blocks.** The importer
  wraps a flat Altium project in a virtual root sheet. Because the project
  name (*Mojo*) collides with the design sheet name, that root is never
  written; the saved sheets carry **empty `(instances)` blocks**, which
  silently exclude every symbol from KiCad 9's connectivity graph — pins stop
  binding to wires, wire-only nets (CFP, CFN, VREG) vanish from netlists, and
  ERC reports their wires as dangling. Fixed by promoting the design sheet to
  project root and populating the instance data
  (`_Tools/kicad_validation/altium_post_import.py`). The same script
  normalizes the imported lib nicknames (`TBL *`, `Altium Content Vault`,
  `*`, `samacsys`) to the project library `Mojo-altium-import` and
  regenerates `Mojo-altium-import.kicad_sym` from the embedded symbols.
- **Cover Sheet / Design Notes.** Altium's decorative sheets are not carried
  over as schematic sheets (Notecarrier-B/-F precedent). Their content
  survives in the original PDFs under `Engineering (Normal)/`.
- **Annotation.** 21 power symbols imported as `#PWR?` and were numbered
  `#PWR01`–`#PWR21`. `LOGO`/`LOGO-BACK` violate KiCad's trailing-digit rule
  and became `LOGO1`/`LOGO2`; both are schematic-only artwork and are marked
  *exclude from board* and *exclude from BOM*.
- **Assembly variant.** Altium variant **Normal** (the production build) DNPs
  J2, J3, J7, J8. KiCad has no variant support, so the base design carries
  all 15 components and those four headers are flagged **DNP**, matching the
  shipped `BOM-Mojo-v4-Normal.xls`. Z1 (test point), MH1–MH4 and the logos
  are excluded from the BOM, as in the Altium BomDoc.
- **PWR_FLAG.** GND and 3V3 are driven externally (battery / host), so two
  `power:PWR_FLAG` symbols were added at the existing power-symbol contacts,
  the KiCad idiom for ERC's `power_pin_not_driven`.
- **Altium special strings.** `${VARIANTNAME}`, `${CURRENTTIME}`,
  `${ORGANIZATION}`, `${ADDRESS1..4}`, `${DOCUMENTNUMBER}`,
  `${PROJECTREVISION}` are defined as project text variables in
  `Mojo.kicad_pro` (empty where Altium had no value). Fab-notes texts of the
  form `'.ProjectID'` on the User.4 drawing layer were left verbatim — they
  are non-manufactured annotations from the Altium fab drawing.
- **Layer mapping.** Auto-match plus: unused internal-plane layers
  (P1/P2/Internal Plane 3–16) skipped; Altium mechanical layers land on
  `User.*` (Route Tool Path → User.10, V Cut → User.9, Board Notes → User.8,
  Scratch Data → User.7, fab/stackup tables → User.4/Dwgs.User). Copper,
  paste, mask, silk and Edge.Cuts map 1:1; the Altium display names are kept
  as KiCad layer user-names (`Top Layer`, `Top Overlay`, …).
- **Fonts.** The silkscreen uses TrueType **Arial**; some fab-note texts use
  **Arial Narrow**. Neither font is redistributed with this project (same
  policy as the Notecarrier-F port's Barlow). Stale `render_cache` blocks
  written on the (Linux) import machine were stripped so text renders with
  the real fonts where installed.
- **Schematic⇄board link.** After import the footprints carry no symbol
  links. *Update PCB from Schematic* (re-link by reference designator, no
  footprint replacement) restored the links and renamed the copper nets to
  the schematic names (`NetC3_2` → `Net-(IC1-CFN)` etc.). DRC now reports
  **0 schematic-parity issues**.
- **Footprint library.** All 11 footprints were exported from the board into
  `Mojo-altium-import.pretty` and the symbols' Footprint fields point at
  them, so the project opens without library warnings.

## Design-rule alignment (from the Altium DRC report)

| Rule | Altium | KiCad setting |
|---|---|---|
| Copper clearance | 7 mil (0.1778 mm) | `min_clearance`/netclasses/zones = **0.1777 mm** — a hair under 7 mil because the imported zone fills measure 0.177796 mm at their tightest (importer float rounding); the fills themselves are byte-preserved Altium geometry |
| Board edge clearance | 0 mil | 0 mm |
| Hole-to-hole | 10 mil | 0.254 mm |
| Thermal spokes | not enforced | `min_resolved_spokes = 1` — three pads (J1.2, J4.2, C2.1) have single-spoke reliefs in the as-manufactured fills |
| Keepouts (mounting holes) | holes allowed | keepout zones set to `pads allowed` (the NPTH pads of MH1–MH4 live inside them by design) |
| DRC/ERC severities | — | warning-severity baseline copied from the Notecarrier-A port |

Zone fills are the ones saved at import; they were **not** refilled
(re-filling changes the copper, cf. the Notecarrier-A port README).

## Validation results (see `../validation/`)

| Gate | Result |
|---|---|
| ERC (errors) | **0** — full-severity report archived as `erc.rpt` |
| DRC (errors, incl. schematic parity) | **0** — full report `drc.rpt`; remaining warnings are silk-over-pad/edge cosmetics also present in the source design |
| BOM vs `BOM-Mojo-v4-Normal.xls` | exact match (11 populated refdes; DNP + BOM-excluded parts handled as above) |
| Gerber raster diff vs `Fabrication/Gerber/` | copper/paste/mask: no differences beyond anti-aliasing; silk: same content, sub-mm glyph metric/anchor offsets from TrueType rendering engine differences (Altium vs KiCad), matching the accepted class in the Notecarrier-F port |
| Drill | 36 holes in the KiCad Excellon files, matching the design drill table (12+11+9+4) |
| KiCanvas | every `.kicad_sch`/`.kicad_pcb` renders headless with zero console errors (screenshots in `validation/kicanvas/`) |
| RAG extract | `_Tools/extract_for_rag/extract.py` parses the schematic (component + net tables) |

## Known acceptable differences

- Silkscreen text glyph geometry differs at the sub-millimetre level from the
  shipped gerbers (font rendering engines); positions, sizes and content are
  identical. See `validation/F_Silkscreen-diff.png` /
  `B_Silkscreen-diff.png`.
- The imported fab/assembly note tables (drill table, stackup table, notes)
  live on non-manufactured `User.*`/`Dwgs.User` layers and keep Altium's
  unresolved `'.ProjectID'`-style placeholders.
- `manufacturing/Mojo_RevA.zip` is the KiCad-exported fab package; the
  authoritative production package remains
  [`Fabrication/`](../../Fabrication/).
