# Notecarrier-F v1.3 — Altium ➜ KiCad 9 Porting Notes

Ported from the Altium Designer sources for **Notecarrier-F v1.3**
(project `100275_NOTECARRIER-F`, schematic Rev 11, PCB `2200-814`, BOM
`3000-653-002`; design by Byte Lab Grupa d.o.o. for Blues; sources published in
[`../../Altium/`](../../Altium/)) using KiCad 9.0.9's **File → Import →
Non-KiCad Project → Altium Project** importer, followed by the scripted cleanup
in [`scripts/`](scripts/) and the validation battery in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). The
procedure is the one used for the [v1.5 port](../../../v1.5/KiCad_format/documentation/Porting-Notes.md);
see the Mojo, Cygnet and Notecarrier-CX Porting-Notes for shared importer
background.

## Provenance of the sources

The v1.3 Altium project was not in any current design-file tree; it was
recovered from the history of the Blues design archive, where the design house
committed it on **10 July 2023** — the date of the `2200-814__2023-07-10`
fabrication package — together with the Rev 11 schematic PDF. That PDF is
byte-identical (md5) to the `100275_NOTECARRIER-F_Rev-11.PDF` published in the
parent folder, and the shipped gerber zip in the archive is byte-identical to
the one published here.

Three snapshots of the v1.3 project exist in the archive (10 July, 11 July and
31 August 2023). Their board files were compared headlessly through KiCad's
Altium reader: tracks, vias, pads, zones and text are identical in all three
(the 31 August file carries one duplicated pad record). The 31 August re-save
differs in the **Production variant only**: it flips `J9`/`J10` to fitted,
matching the released BOM report generated the same day. This port therefore
uses the 10 July (fab-day) board and schematics, with `J9`/`J10` fitted as the
released BOM `3000-653-002` states. The gerber diff below confirms the board
matches the shipped artwork.

## Structure and import quirks

- Altium project: `01_COVER` / `02_BLOCK-DIAGRAM` / `03_NOTECARD-CONNECTION` /
  `04_FEATHER-CONNECTION` / `05_IO` / `06_POWER-INPUT` / `07_POWER-RAILS`
  SchDocs. Per house convention the cover and block-diagram sheets (no
  electrical content) are not ported; the five electrical sheets are child
  sheets of the root `Notecarrier-F.kicad_sch`, renamed
  `Notecarrier-F_<Sheet>.kicad_sch` and given the Altium sheet titles.
- **Layer mapping** (importer dialog, auto-match): copper, paste, mask, silk
  and outline 1:1; Altium's unused plane layers left unmatched; the mechanical
  layers land on `User.N`, `F/B.Fab`, `Dwgs/Cmts.User` and keep their Altium
  names as KiCad layer user-names (`M1 Components Top`, `M11 Gerber Spec`, …).
  The two inner copper layers were renamed from the importer's `Mid Layer 3/4`
  to `Mid Layer 1/2` to match the `G1`/`G2` gerbers.
- **Project name.** Files and the `(project …)` instance blocks were renamed
  from `100275_NOTECARRIER-F` to `Notecarrier-F`.
- **Net label scope.** Byte Lab's flat Altium design uses globally scoped net
  labels; the importer writes every one as a sheet-local KiCad label. The 44
  label names that appear on more than one sheet or that share a name with a
  power net were promoted to **global labels**; the rest stay local. The
  result was checked pad-by-pad against the nets carried by the Altium board
  file itself (see the validation table): every board net maps to exactly one
  KiCad net, with no conflicts.
- **Designators.** `MOD1L`/`MOD1R` (the Feather sockets) end in a letter, which
  KiCad's annotation treats as un-annotated. They are `MODL1`/`MODR1` in this
  port, in both the schematic and the board; `boards.yaml` carries the
  `refdes_map` back to the shipped names. Their silkscreen references are hidden
  on the fabricated board, so the artwork is unaffected.
- **Power symbols.** The importer leaves all 172 power symbols as `#PWR?`; they
  were annotated `#PWR001`–`#PWR172`.
- **Production variant** (from the PrjPCB, cross-checked against the released
  BOM and pick-and-place file): `J11`, `R11`, `R12` are DNP in schematic and
  board; `MOD2` (the Feather-outline graphic, 28 pins) is excluded from the BOM
  and placement data and its embedded symbol uses `no_connect`-type pins;
  `ASS1` (the M2.5 screw, a BOM line with no footprint) is excluded from the
  board. `J9`/`J10` are fitted (see *Provenance*).
- **Cover-sheet symbols.** `FD1`–`FD8` (fiducials), `DOC1` and `PCB1` (document
  number pseudo-parts) live on the un-ported cover sheet. The eight fiducial
  footprints are marked *board only / not in BOM* so schematic parity does not
  report them; they stay in the placement data, where the shipped file lists
  them too.
- **48 free NPTH holes.** Altium models the anchor / tenting holes as free pads
  with no designator; the importer wrote them as 48 nameless footprints with
  one zero-copper NPTH pad each. They are `H1`–`H48` (numbered top-left first),
  footprints `NPTH_free_hole` (0.8 mm, 40×), `NPTH_free_hole_2.54mm` (4×) and
  `NPTH_free_hole_3.3mm` (4×), *board only* and excluded from BOM and
  placement data.
- **Footprint values.** The importer leaves the board footprints' `Value`
  fields empty; they were filled from the schematic so parity does not flag
  them.
- **`OBJ1` mounting hole.** Altium's pad stack is 6 mm on the outer layers and
  1.524 mm on the inner layers around a 3.7 mm hole — i.e. no inner copper
  survives drilling. KiCad flags a negative annulus, so the inner-layer size
  was set to 3.8 mm (the smallest legal ring) and the unused inner layers
  are dropped. The change is made on the live pad *before* the footprint is
  copied into the project library, so the board and the `.pretty` copy of
  `DIST-WASMSIM0250` agree and *Update Footprints from Library* cannot bring
  the invalid stack back. This is the one deliberate copper deviation; it is
  visible in the inner-layer gerber diff and has no effect on the drilled
  board.
- **Symbol libraries.** The original Altium lib nicknames (`BL_Analog`,
  `BL_Mechanical`, `BL_Passive`, `n21-p2`, `100275_NOTECARRIER-F-altium-import`)
  are kept on the symbols and aliased in `sym-lib-table` to the single merged
  project library `Notecarrier-F-altium-import.kicad_sym` (124 symbols,
  regenerated from the sheets' embedded `lib_symbols`; no name collisions).
  Footprints were saved out of the board with the KiCad Python API into
  `Notecarrier-F-altium-import.pretty` (38 footprints; bottom-side parts
  flipped back to the front before saving) and every footprint/symbol
  footprint field re-pointed at that library.
- **Nets.** The importer keeps Altium's auto-names on the board (`NetR13_1`,
  `NetJ6_20`, …). After the schematic edits, 53 board nets were renamed to the
  KiCad netlist's names by matching every pad (`scripts/f13_nets.py`; 0 pads
  whose board net spanned more than one schematic net, 0 connected pads left
  netless). **Zone fills are the ones saved at import — do not refill.**
- **Text variables.** Altium special strings resolved as project text variables
  (`AUTHOR`/`PCB_AUTHOR` M. Hamin, `ACCEPTOR`/`PCB_ACCEPTOR` T. Zvonc,
  `ADDRESS1`, `WEB`, `MODULE_NAME` Notecarier F, `HW_E_DOC_NUM` 100275,
  `PCB_NUM` 2200-814, `PCBA_BOM_NUM` 3000-653-002). Title blocks: rev
  `11 (v1.3)`, 2023-07-10.

## Design rules

Rules follow the board's own Altium rule set (read from the `.PcbDoc`:
clearance **0.1 mm**, polygon clearance 0.2 mm, track width min 0.1 mm,
hole-to-hole 0.2 mm) rather than the v1.5 values, since this revision was
routed to the older 0.1 mm rule — eight via/track and connector-pad gaps on
the fabricated board are between 0.10 and 0.145 mm. KiCad settings: clearance
**0.0999 mm** (a hair under 0.1 to absorb importer float rounding; also on the
`Default`/`All Nets` net classes), track 0.0999 mm, via 0.6/0.3 mm, annular
0.05 mm, hole clearance 0.0999 mm, hole-to-hole 0.1999 mm, edge clearance 0,
`min_resolved_spokes 1`, and the four imported GND pours' clearance set to
0.1999 mm (their imported parameter was 0.5 mm). The fabrication sheet in the
shipped package (`M11 Gerber Spec` layer: 4-layer FR-4 Tg140, 1.6 mm, min
track/spacing 0.15 mm, min hole 0.3 mm, ENIG) is the same as v1.5's. DRC/ERC
severities are the Notecarrier-A/CX/F v1.5 baseline (cosmetic classes as
warnings).

## Validation results (see [`../validation/`](../validation/))

Gates run by `_Tools/kicad_validation/run_all.py notecarrier-f-v13` on
2026-09-18 (KiCad 9.0.9, macOS):

| Gate | Result |
|---|---|
| ERC (error severity) | **PASS — 0** (`erc-errors.rpt`; warnings: 837 off-grid endpoints, 58 wire endpoints, 43 undriven power pins — importer artefacts, see `erc.rpt`; all six sheets present in the report) |
| DRC + schematic parity (error severity) | **PASS — 0 violations, 0 unconnected, 0 parity errors** (`drc-errors.rpt`; 53 parity *warnings* are pads the schematic leaves unconnected; 231 cosmetic warnings: silk overlap, TrueType text thickness, mask bridges, and 25 library-copy mismatches that are pad-rotation-only — 20 round free holes and 5 bottom-side parts (`DS6`, `DS7`, `TVS1`, `R20`, `SW4`) whose square/180°-symmetric pads the importer rotated per instance; geometrically identical to the library copies) |
| BOM vs `BOM-3000-653-002.xlsx` | **PASS — exact, 94 populated designators** on `BL PART NUMBER` |
| Netlist vs shipped ODB++/IPC-356 | SKIPPED — none shipped; see the Altium-board cross-check below |
| Gerber raster diff vs `2200-814__2023-07-10.zip` | **PASS** — F/B copper 0.001/0.001 and masks 0.004/0.009 (exact), paste 0.007/0.019, inner copper 0.054/0.053, silk 0.66/0.72; baseline frozen in `gerber-baseline.yaml` after review |
| Placement vs `PNP-3000-653-002.pnp` | **PASS — 89/89** on side and rotation, 0 unexplained displacements |
| KiCanvas headless render (6 sheets + board) | **PASS** |
| RAG extract | **PASS** |

Accepted gerber-diff classes (reviewed per layer, all cosmetic):

- **Signal-via / PTH inner annuli** (In1/In2): KiCad plots the unused
  inner-layer rings that Altium suppresses — isolated inside the plane
  clearances, no connectivity impact (same class as the CX and v1.5 ports).
  The routed inner tracks match exactly.
- **`OBJ1`**: Altium flashes a 1.524 mm disc inside the 3.7 mm hole on the
  inner layers, KiCad a 3.8 mm ring (see *Structure*); neither survives drilling.
- **Paste apertures** on the large exposed pads: the aperture outline differs
  by a fraction of its line width.
- **Silkscreen**: TrueType glyph-metric offsets (Calibri substituted at import).

### Cross-check: KiCad netlist vs the Altium board's nets

`validation/altium-netlist-compare.txt` compares the netlist exported from this
schematic with the nets carried by the Altium `.PcbDoc` itself (read headlessly
by KiCad 9.0.9, untouched apart from the `MOD1L/R` designators), pad by pad:
**489 pads, 116 board nets, 0 conflicts, 0 connected pads left netless, 0
schematic nets without a board pad.** Since the Altium board is the artwork
that was fabricated, this ties the ported schematic to the shipped copper
independently of the importer's schematic conversion.

## Relation to the earlier KiCad files in this folder

Until 2026-09-18 this folder held a hand-made KiCad 7 port (2024) whose board
was later shown to describe **v1.2** (BOM 3000-613-002): it lacked `U9`,
`C33`/`C34`, `DS7` and used a different diode part and package for `DS1`–`DS6`.
Its schematic had been delta-ported to v1.3 in August 2026 while the board was
still v1.2 (documented in an ERRATA file at the time). Both are superseded by
this import; the original notes are kept as
[`History_Porting-Notes-hand-port.md`](History_Porting-Notes-hand-port.md)
because the repository's gerber-diff recipe was first written there. The
`SW3` pin 3 / `F_EN` wiring defect that the v1.5 cross-check attributed to the
hand port is absent here (`SW3.3` is on `N_VIO`, as in Altium).

## Fonts

The silkscreen uses TrueType **Calibri** (substituted with DejaVu Sans Bold on
the import machine). The font is not redistributed with this project; silkscreen
text therefore renders with slightly different metrics than the fabricated
board, which is the silkscreen class accepted in the gerber diff above.
