# Notecarrier-CX v1.7 — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for **Notecarrier-CX v1.7**
(project `100544_notecarrier-cx`, design by Byte Lab Grupa d.o.o. for Blues)
using KiCad 9.0.9's Altium project importer plus the scripted
cleanup/validation in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo and Cygnet Porting-Notes for shared importer background.

## Structure and import quirks

- Altium project: `01_COVER` / `02_BLOCK-DIAGRAM` / `03_IO-CONNECTION` /
  `04_NOTECARD-CONNECTION` / `05_POWER` / `06_MCU` SchDocs. Per house
  convention the cover and block-diagram sheets (no electrical content) are
  not ported; the four electrical sheets become child sheets of a new root.
- **Label promotion**: 21 nets that Altium scopes globally
  (`HST_SDA`, `HST_SCL`, `VSENSE`, `AUX_NCHARGING`, `USB_NC_D_N/P`,
  `EN`, `ATTN`, the `ALT_DFU_*` group, …) were imported as sheet-local
  labels — on multiple sheets, or duplicated as both local and global labels
  — which silently splits them per sheet in KiCad. All were promoted to
  global labels; every name was first verified to be a single net in the
  Altium board.
- J1's hidden pin `M` (Qwiic connector shield/mount) is tied to GND in the
  Altium board; a GND power symbol was stacked on the hidden-pin position.
  J3 pin 63 (`NC63`) and U5 pins 20/25 (PB2/PB12) are genuinely unconnected
  in the Altium board and carry explicit no-connect markers.
- **Castellated headers** (P1/P2 16-pin edge rows, P4 5-pin AUX header —
  see `changes.txt` in the internal sources for the v1.6→v1.7 P4 grid
  alignment): Altium models each position as *two* same-numbered PTH pads
  (edge castellation + inner 0.1" hole) joined by small solid-region copper
  rectangles. The importer drops those joins and leaves 64 degenerate
  zero-size pads; the junk pads were removed and all 70 join rectangles were
  reconstructed from the shipped gerbers as net-assigned copper rectangles
  (pulled back 10 µm from the board edge to satisfy KiCad's edge-clearance
  check). Castellated pads carry the KiCad castellated property.
- **R23/R24 (VMAIN divider)** carry the corrected values (R23 = 10M upper,
  R24 = 4.3M lower — the v1.7 running change described in the internal
  `changes.txt`); the shipped production BOM in this repo matches.
- **R4 (0R)** is not populated in the production variant (absent from the
  shipped BOM, present in the ODB++ placement data) and is flagged DNP.
  P1/P2/P4 are bare-board castellations and are excluded from the BOM,
  matching the shipped BOM (which lists them only as documentation rows).
- STANDOFF1's 6 mm NPTH ring merges with the GND pour on the fabricated
  board and is assigned GND; P5's mounting tabs (`M`) are `$NONE$` in the
  shipped ODB++ netlist and stay netless.
- Unused annular-ring suppression is applied to PTH **pads** (Altium
  parity), except the plane-connected pads that the shipped inner-layer
  gerbers actually flash (P2.13, P3.M, P4.1) — KiCad does not count zone
  fills when pruning pad/via layers. For the same reason suppression is
  deliberately **not** applied to vias: it would break copper connectivity
  for the plane-connected GND stitching vias. Consequence (accepted,
  cosmetic): KiCad plots the unused inner-layer annuli of signal vias that
  Altium suppresses — visible as ~0.6 mm rings on the In1/In2 gerber diffs;
  no electrical effect (the rings are isolated in the plane clearances).
- Zone fills are preserved from the Altium import — **do not refill**.
- The original Altium lib nicknames (`BL_Active`, `BL_Analog`, `BL_Digital`,
  `BL_Mechanical`, `BL_Passive`, `n21-p2`, `100544_notecarrier-cx-altium-import`)
  are kept on the symbols and aliased in `sym-lib-table` to the single
  merged project library (avoids a kicad-cli crash seen when renaming
  nicknames in-place; same approach as the Cygnet port).
- Altium special strings resolved as project text variables
  (`AUTHOR`, `ACCEPTOR`, `ADDRESS1`, `WEB` on the schematic sheets;
  `PCB_AUTHOR`, `PCB_ACCEPTOR`, `PCBA_BOM_NUM` = 3001-018-001 on the board's
  mechanical sheet layers — values taken from the shipped PDFs/gerbers).

## Design rules

Rules follow the board's measured minima: clearance 0.1499 mm (the board
uses 0.15 mm spacing; a hair under to absorb importer float rounding),
track 0.15 mm, via 0.6/0.3 mm, hole-to-hole 0.1 mm (one shipped via pair
measures 0.103 mm), edge clearance 0 (castellated design),
`min_resolved_spokes 1`, severity baseline from the Notecarrier-A port.

## Validation results (see `../validation/`)

| Gate | Result |
|---|---|
| ERC / DRC (error severity, incl. schematic parity) | **0 / 0** |
| Netlist vs Altium PcbDoc (fresh headless import) | **89/89 nets exact** (schematic *and* board side) |
| Netlist vs shipped ODB++ (`FAB/ODB`) | **89/89 partitions** (ODB `$NONE$` = unconnected-pin bucket, ignored) |
| BOM vs `BOM-notecarrier-cx(Production).xlsx` | exact — 95 populated refdes; grouped alternate part numbers (e.g. 100n: 2000-908/2004-296) accepted per line |
| Gerber raster diff vs `FAB/Gerber` | copper exact on F/B (castellation joins and plane tongues reconstructed from the shipped gerbers); accepted classes documented below |
| KiCanvas / RAG extract | render + parse clean |

Accepted gerber-diff classes (reviewed per layer, all cosmetic):
- **Signal-via inner annuli** (In1/In2): KiCad plots them, Altium suppresses
  unused rings — isolated inside plane clearances, no connectivity impact.
- **Plane pullback boundary** (In1/In2): the preserved imported fill edge
  sits ~0.05 mm inside Altium's plotted plane edge along the outline.
- **Off-board copper**: Altium plots plane slivers slightly past the board
  outline at the castellation notches (removed by routing); KiCad copper is
  clamped at the outline.
- **Silkscreen**: TrueType metric offsets (fonts substituted at import).
