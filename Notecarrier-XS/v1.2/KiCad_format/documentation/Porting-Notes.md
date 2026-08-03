# Notecarrier-XS — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for **Notecarrier-XS**
(project `100426_notecarrier-xs`, design by Byte Lab Grupa d.o.o. for Blues)
using KiCad 9.0.9's Altium project importer plus the scripted
cleanup/validation in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo, Cygnet and Notecarrier-CX Porting-Notes for shared importer background.

## ⚠️ Source-fidelity disclaimer — read first

**This port was NOT generated from the exact design snapshot that produced
the published v1.2 fabrication package** (`2200-914__2024-06-06.zip` in the
parent folder). That exact snapshot was never captured in the design house's
version control; the closest available state — the post-v1.2 development
state, captured shortly after the v1.2 release and before the v1.3 changes
were finished — was used instead. A full per-layer gerber comparison against
the published v1.2 fab package (see [`../validation/`](../validation/)) shows
the following differences, all reviewed and accepted:

1. **Silkscreen**: the source silk reads **V1.3** where the published board
   reads **V1.2**, and most legend text (STARNOTE / NOTECARD / QWIIC / LIPO /
   ESLOV, the pin-name rows, component outlines) is slightly repositioned on
   both sides. Same content, different layout pass.
2. **R4 moved sides**: R4 — a 0R0 jumper between `+VACT_GPS_IN` and
   `+VACT_GPS_OUT` that is **not populated in production** (absent from the
   shipped BOM) — sits on the **top** side of the published board but on the
   **bottom** side in this source, with its pads/mask/paste apertures and a
   small amount of local routing on both copper layers differing accordingly.
   Production boards ship without R4 fitted, so the populated product is
   electrically identical; the difference only matters if you fit the
   optional jumper.
3. **Everything else matches**: outside the two clusters above, the copper,
   mask and paste layers are exact against the published fab package, the
   drill data matches, and the netlist was proven identical to the source
   board (57/57 net partitions) — see the validation summary below.

**What has since been confirmed against the released build.** The shipped
pick-and-place file for this assembly is generated from the released design, so
comparing against it tests the port independently of the source snapshot it was
made from. All 44 placed parts are present in the port, on the same board side,
at the same rotation as the boards that were actually built. (Position residuals are reported but not gated: the assembly file references
each part's body centre while KiCad measures from the footprint origin, so
asymmetric parts carry a fixed per-footprint offset — it even changes sign when
a part is rotated 180°. Copper geometry is proven exactly by the gerber diff.)

This does **not** resolve item 2 above: R4 is unpopulated in production, so it
does not appear in the pick-and-place file at all, and which side it sits on
remains established from the gerber comparison alone.

What is still missing to retire this disclaimer entirely is a **netlist from the
released snapshot** — a Protel `.NET`, or better an IPC-D-356A/ODB++ export of the
released PCB, which would also validate geometry and plugs into the netlist gate
already used for the Notecarrier-CX and -XI ports. A sweep of all 293
repositories in the Blues organisation found no such file for this board.

If the exact released v1.2 Altium snapshot ever becomes available, this port
should be regenerated from it and the disclaimer dropped.

## Structure and import quirks

- Altium project: `01_COVER` / `02_BLOCK-DIAGRAM` / `03_IO-CONNECTION` /
  `04_NOTECARD-CONNECTION` / `05_POWER` / `06_STARNOTE-CONNECTION` SchDocs.
  Per house convention the cover and block-diagram sheets (no electrical
  content) are not ported; the four electrical sheets become child sheets of
  a new root.
- **Label promotion**: 25 net names that Altium scopes globally were imported
  as sheet-local labels (present on multiple sheets, or duplicated as both
  local and global labels) — which silently splits them per sheet in KiCad.
  All were promoted to global labels; every name was first verified to be a
  single net in the Altium board's pad-to-net table.
- **DNP flags**: LD1, R11 and R4 are absent from the shipped production BOM
  (`BOM-3000-789-002.xlsx`; R4/R11 are also the project variant's unfitted
  set) and carry KiCad DNP flags. BOM comparison keys on the
  `BL PART NUMBER` field — the DbLib passives carry `N/A` manufacturer part
  numbers in the schematic source.
- **Footprint library**: 11 footprints crash KiCad's `FootprintSave` when
  exported through pcbnew (R-0402, C-0603, SOT-583, C-0805,
  QFN40P300X150X80-18N, IND_XFL4020, BGA8N40P2X4_180x100x50, SOT666, R-0603,
  J-NANOSIM-SF72S006VBA, L-0603); they were extracted textually from the
  board file instead (instance placement/net tokens stripped).
- The six 1 µm-copper NPTH pads (3.3 mm mounting holes, connector
  polarization/anchor drills on J4/J6/P4) are intentional Altium
  mechanical-hole modelling and are kept; the unnamed mount-hole footprints
  are named `MTG_NPTH_3.3mm`.
- Edge.Cuts uses the Altium outline width convention (0.199898 mm) with two
  null-length segments removed.
- **One DRC exclusion**: the two same-number SW1 pads (net `Net-(J6-~{RST})`)
  are not joined by copper on the published fab either — verified by
  flood-fill connectivity test on the shipped GTL raster — so the
  "missing connection" item is excluded as fab-accurate.
- `kicad-cli` F8-equivalent (Update PCB from Schematic) run with *re-link by
  reference* ON and *replace footprints* OFF; the only errors are the
  footprint-less assembly pseudo-symbols ASS1/ASS2 (documentation items, not
  board components).

## Validation summary

Gates run by `_Tools/kicad_validation/run_all.py notecarrier-xs`
(artifacts in [`../validation/`](../validation/)):

| Gate | Result |
|---|---|
| ERC (error severity) | PASS — 0 |
| DRC + schematic parity (error severity) | PASS — 0 violations, 1 documented exclusion |
| BOM vs `BOM-3000-789-002.xlsx` | PASS — exact on `BL PART NUMBER` per refdes |
| Netlist vs source PcbDoc (pad-to-net partitions) | PASS — 57/57 |
| Gerber raster diff vs published `2200-914__2024-06-06.zip` | PASS with the two documented deviation clusters above |
| Placement vs shipped pick-and-place file | PASS — 44/44 on board side and rotation (`../validation/pnp-compare.txt`) |
| kicanvas headless render (all sheets + board) | PASS |
| RAG extract parse | PASS |

The published fab package ships no ODB++/IPC-D-356 netlist, so the
independent-netlist gate is replaced by the pad-to-net partition comparison
against a fresh headless import of the source board.
