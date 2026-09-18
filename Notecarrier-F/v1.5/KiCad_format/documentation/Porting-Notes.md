# Notecarrier-F v1.5 — Altium ➜ KiCad 9 Porting Notes

Ported from the Altium Designer sources for **Notecarrier-F v1.5**
(project `100275_NOTECARRIER-F`, schematic Rev 13, PCB `2201-139`, BOM
`3001-069-001`; design by Byte Lab Grupa d.o.o. for Blues; sources published in
[`../../Altium/`](../../Altium/)) using KiCad 9.0.9's **File → Import →
Non-KiCad Project → Altium Project** importer, followed by the scripted cleanup
and the validation battery in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo, Cygnet and Notecarrier-CX Porting-Notes for shared importer background.

The Altium board file is dated 27 Jan 2026 and was committed by the design house
as "Notecarrier F v1.5 - release", the same day as the Rev 13 schematic and the
`2201-139__2026-01-27` fabrication package, so — unlike the X-series ports —
this port is made from the exact snapshot that produced the published fab
outputs. The gerber diff below confirms it.

## Structure and import quirks

- Altium project: `01_COVER` / `02_BLOCK-DIAGRAM` / `03_NOTECARD-CONNECTION` /
  `04_FEATHER-CONNECTION` / `05_IO` / `06_POWER-INPUT` / `07_POWER-RAILS`
  SchDocs. Per house convention the cover and block-diagram sheets (no
  electrical content) are not ported; the five electrical sheets are child
  sheets of the root `Notecarrier-F.kicad_sch`, renamed
  `Notecarrier-F_<Sheet>.kicad_sch`. The importer left every sheet symbol
  unnamed (21 `duplicate_sheet_names` ERC errors); they were given the
  Altium sheet titles.
- **Layer mapping** (done in the importer's dialog): copper, paste, mask, silk
  and outline 1:1 (Byte Lab's outline lives on `Mechanical 15`, mapped to
  `Edge.Cuts`); Altium's unused plane layers (Power/Ground/Internal Plane
  3–16) left unmatched; the mechanical layers land on `User.N`, `F/B.Fab`,
  `Dwgs/Cmts.User` and keep their Altium names as KiCad layer user-names
  (`M1 Components Top`, `M11 Gerber Spec`, …). The two inner copper layers
  were renamed from the importer's `Mid Layer 3/4` to `Mid Layer 1/2` to match
  the `G1`/`G2` gerbers.
- **Project name.** The importer names the project after the Altium project
  (`100275_NOTECARRIER-F`); files and the `(project …)` instance blocks were
  renamed to `Notecarrier-F`, since KiCad ignores symbol instances whose
  project name does not match the `.kicad_pro`.
- **Designators.** `MOD1L`/`MOD1R` (the Feather sockets) end in a letter, which
  KiCad's annotation treats as "un-annotated" (netlist/BOM export warn, DRC
  parity cannot match them). They are `MODL1`/`MODR1` in this port, in both the
  schematic and the board; `boards.yaml` carries the `refdes_map` back to the
  shipped names. Their silkscreen references are hidden on the fabricated
  board, so the artwork is unaffected (gerber diff exact).
- **Cover-sheet symbols.** `FD1`–`FD8` (fiducials), `DOC1` and `PCB1` (document
  number pseudo-parts) live on the un-ported cover sheet. The eight fiducial
  footprints are marked *board only* (`attr board_only exclude_from_bom`) so
  schematic parity does not report them as extra; they stay in the
  pick-and-place data, where the shipped file also lists them.
  `ASS1` (the M2.5 screw) has no footprint and is *excluded from board*.
- **48 free NPTH holes.** Altium models the tented-via / anchor holes as free
  pads with no designator; the importer wrote them as 48 nameless footprints
  with one NPTH pad each. They are `H1`–`H48`, footprint `NPTH_free_hole`,
  *board only* and excluded from BOM and placement data.
- **Unconnected pins.** `MOD2` (the Feather-outline graphic, 28 pins) and the
  fiducial symbol had passive pins with nothing attached; their embedded
  symbols now use `no_connect`-type pins. `MOD2` is excluded from the BOM, as
  in the shipped BOM. `J11` (unfitted 1×2 header) is DNP in both schematic and
  board.
- **Stacked labels.** On the Notecard sheet an empty label sat exactly on the
  `AUX_RX_P` label, mid-wire, leaving both dangling; the empty label was
  removed and the wire split at the label anchor (KiCad only connects a label
  to a wire *end*).
- **Symbol libraries.** The original Altium lib nicknames (`BL_Active`,
  `BL_Analog`, `BL_Digital`, `BL_Mechanical`, `BL_Passive`, `n21-p2`,
  `100275_NOTECARRIER-F-altium-import`) are kept on the symbols and aliased in
  `sym-lib-table` to the single merged project library
  `Notecarrier-F-altium-import.kicad_sym` (same approach as the CX and Cygnet
  ports). Footprints were saved out of the board with the KiCad Python API
  into `Notecarrier-F-altium-import.pretty` (36 footprints; bottom-side-only
  parts flipped back to the front before saving) and every footprint/symbol
  footprint field re-pointed at that library.
- **Nets.** The importer keeps Altium's auto-names on the board (`NetR13_1`,
  `NetJ6_42`, …) and sheet-local names for locally-scoped labels. After the
  schematic edits, the board's 47 affected nets were renamed to the schematic's
  names by matching every pad to the exported netlist (script: the
  `finish_board.py` step recorded in this folder's history; 0 pads whose board
  net spanned more than one schematic net, 0 connected pads without a board
  net). Zone fills are the ones saved at import — **do not refill**.
- **Text variables.** Altium special strings resolved as project text variables
  (`AUTHOR` A.Duracic, `ACCEPTOR` A.Vora, `ADDRESS1`, `WEB`, `MODULE_NAME`
  Notecarier F, `HW_E_DOC_NUM` 100275, `PCB_NUM` 2201-139, `PCBA_BOM_NUM`
  3001-069-001, `PCB_AUTHOR`/`PCB_ACCEPTOR`). Title blocks: rev `13 (v1.5)`,
  2026-01-26.

## Design rules

Rules follow the fabrication specification sheet in the shipped gerber package
(`2201-139__2026-01-27.PDF`: 4-layer FR-4, 1.6 mm, min track/spacing 0.15 mm,
min hole 0.3 mm, ENIG) and the board's measured minima: clearance **0.1499 mm**
(a hair under 0.15 to absorb importer float rounding; the same value is set on
the `Default`/`All Nets` net classes and on the five imported zones whose
clearance parameter was 0.5 mm), track 0.15 mm, via 0.6/0.3 mm, annular
0.05 mm (the 4UCON socket pads), hole clearance 0.15 mm (the USB-C shell NPTH
sits 0.165 mm from a VUSB track), hole-to-hole 0.25 mm, edge clearance 0 (the
JST shield tabs are 0.2 mm from the outline by design), `min_resolved_spokes 1`.
DRC/ERC severities are the Notecarrier-A/CX baseline (cosmetic classes —
silk overlap, TrueType text thickness, mask bridges, unused-ring padstacks,
off-grid endpoints, parity net-name warnings for unconnected pads — as
warnings).

## Validation results (see [`../validation/`](../validation/))

Gates run by `_Tools/kicad_validation/run_all.py notecarrier-f` on 2026-09-16
(KiCad 9.0.9, macOS):

| Gate | Result |
|---|---|
| ERC (error severity) | **PASS — 0** (`erc-errors.rpt`; warnings: 771 off-grid endpoints, 50 same local/global label, 18 undriven power pins, 16 wire endpoints — importer artefacts, see `erc.rpt`) |
| DRC + schematic parity (error severity) | **PASS — 0 violations, 0 unconnected, 0 parity errors** (`drc-errors.rpt`; 54 parity *warnings* are pads the schematic leaves unconnected) |
| BOM vs `BOM-3001-069-001.xlsx` | **PASS — exact, 90 populated designators** on `BL PART NUMBER` |
| Netlist vs shipped ODB++/IPC-356 | SKIPPED — none shipped; see the hand-port cross-check below |
| Gerber raster diff vs `2201-139__2026-01-27.zip` | **PASS** — F/B copper 0.002/0.003 and masks 0.004/0.009 (exact), paste 0.006/0.022, inner copper 0.059/0.061, silk 0.66/0.72; baseline frozen in `gerber-baseline.yaml` after review |
| Placement vs `3001-069-001_PnP-file_TOP.pnp` + `_BOT.pnp` | **PASS — 88/88** on side and rotation, 0 unexplained displacements (the gate now accepts a list of per-side files) |
| KiCanvas headless render (6 sheets + board) | **PASS** |
| RAG extract | **PASS** |

Accepted gerber-diff classes (reviewed per layer, all cosmetic):

- **Signal-via / PTH inner annuli** (In1/In2): KiCad plots the unused
  inner-layer rings that Altium suppresses — isolated inside the plane
  clearances, no connectivity impact (same class as the Notecarrier-CX port).
- **Paste apertures** on the large exposed pads of U2/U3/U5/U7/U8: the aperture
  outline differs by a fraction of its line width.
- **Silkscreen**: TrueType glyph-metric offsets (Calibri substituted at import).

### Independent cross-check: the hand-ported schematic

Before the Altium sources were in hand, v1.5 had been delta-ported by hand from
the v1.3 KiCad project (USB-C, `U5` → NX3L2467, `DS8`, `VSOLAR`/`VBUS`, …),
verified pin-by-pin against the released Rev 13 PDF. Its netlist is kept as
`validation/handport-netlist.net`, and `validation/handport_compare.py`
compares the two schematics by connectivity partition
(`handport-netlist-compare.txt`). They agree on **109 of 110 nets**; the one
difference — `SW3` pin 3 on `N_VIO` (Altium, correct) vs `F_EN` (hand port) —
is a defect inherited from the **original hand-made v1.3 KiCad port** (since
superseded by a direct import of the v1.3 Altium sources, which does not have it).
The pin-level pass also caught a transposed `2Y0/2Y1` pin pair on the hand
port's `U5` symbol. Both findings are on the discarded hand port; this project
is the Altium truth.

## Known discrepancies in the released documents

- **`J9`/`J10` are fitted but missing from the released BOM.** The outer 24-pin
  sockets (4UCON `12736`) are on the Rev 13 schematic, on the board, and
  visibly populated on production units, but `BOM-3001-069-001.xlsx` (93
  lines) does not list them. The BOM gate skips them with a comment in
  `boards.yaml`; ask the design house to correct the spreadsheet.
- The Altium sheet notes still describe the removed v1.3 AUX slide switch
  ("Flick switch towards ON to enable outboard DFU") and its truth table with
  the old NC/NO wording; the wiring is correct (U5 is selected by
  `ALT_DFU_ACTIVE`).

## v1.3 → v1.5 design delta (for readers of the v1.3 port)

Byte Lab's Rev 13 revision block covers two steps: an unreleased Rev 12
("v1.4", 2025-11-26: R11/R12 mounted, USB-C connector and antenna-area copper
keepout, AUX switch and U6 removed, current draw reduced) and Rev 13 (v1.5,
2026-01-26: TVS on the USB-C connector, VSOLAR rewired, F_VUSB feeds VUSB,
VMAIN TVS changed). In component terms:

| Change | Detail |
|---|---|
| `J4` micro-USB → **USB-C** | Amphenol 12402012E212A; `R5` re-purposed as CC1 5k1, `R21` added as CC2 5k1; `D1` D5V0F4U6V-7 TVS array on D±/CC |
| `TVS3`, `C3`, `C4` removed | micro-USB protection / shield cap |
| `TVS1` | SM6T6V8A → ESDA7P120-1U1M (VMAIN) |
| `DS8` added | STPS3H100U, `F_VUSB` → `VUSB`: Feather USB now charges the LiPo and reaches `VMAIN` through `DS7` |
| `VSOLAR` | moved to the `J2` side of `DS4`; the charger input node is the new `VBUS` |
| `U6`, `SW4`, `C10` removed | no more AUX/DFU slide switch |
| `U5` | DGQ2788AEN → NX3L2467GU, selected by `ALT_DFU_ACTIVE` (100 k pull-up `R18`) |
| `R11`, `R12` | 10 k F_I2C pull-ups to `F_VIO`, now fitted |
| `MOD1L`/`MOD1R`, `J9`/`J10` | 4UCON 00542 / 00536 / 12736 |
| PCB `2201-139` | copper removed on all layers beneath the antenna end of the Notecard socket |

## Fonts

The silkscreen uses TrueType **Calibri** (substituted with Verdana Bold on the
import machine). The font is not redistributed with this project; silkscreen
text therefore renders with slightly different metrics than the fabricated
board, which is the silkscreen class accepted in the gerber diff above.
