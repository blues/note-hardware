# Notecarrier-X — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for **Notecarrier-X**
(project `100379_notecarrier-x`, design by Byte Lab Grupa d.o.o. for Blues)
using KiCad 9.0.9's Altium project importer plus the scripted
cleanup/validation in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo, Cygnet and Notecarrier-CX Porting-Notes for shared importer background.

## Source and provenance

The board is generated from the design house's **Rev-11 release snapshot**
of project `100379_notecarrier-x` — the Altium sources behind the published
v1.2 fabrication package (`2200-918__2024-06-06.zip`), schematic
(`100379_notecarrier-x_Rev-11.PDF`) and BOM (`BOM-3000-794-001.xlsx`) in the
parent folder. The snapshot's own project parameters carry exactly those
document numbers (`PCB_Num 2200-918`, `PCBA_BOM_Num 3000-794-001`,
`HW_E_Doc_Rev 11`) and its silkscreen reads **V1.2**.

That it is the released design was checked against the published fab
package, not assumed:

- **Copper, solder mask and paste are exact.** After rasterising both sides
  at 1200 dpi and removing sub-0.1 mm slivers, no difference cluster of
  0.045 mm² or larger remains on any of the six layers (normalised
  difference 0.001–0.010; see [`../validation/`](../validation/)).
- **Silkscreen content matches**, including `V1.2`, `RST` on the back legend
  and the R4 outline on the top side. What the silk diff still shows is the
  usual font class: Altium and KiCad render TrueType text with different
  metrics.
- **Connectivity matches the released board pad for pad.** Every pad's net in
  the Rev-11 PCB agrees with this port's schematic (0 conflicts,
  [`../validation/altium-netlist-compare.txt`](../validation/altium-netlist-compare.txt)),
  and the two netlists group pins into the same 56 nets.

### History: the earlier source-fidelity disclaimer

This port was first published in July 2026 from the closest source then
available, a post-v1.2 development state. That source's silk read V1.3, and
it put the production-DNP GPS-power jumper R4 on the bottom side (the
released board has it on top), with a little local routing around it. The
port carried a disclaimer saying so. When the Rev-11 snapshot arrived
(October 2026), it was compared with that development state record by
record:

- **The schematics are identical in substance.** All three electrical sheets
  have the same components, values, part numbers, labels, ports and wiring.
  The only differences are from re-applying the sheet template (copyright
  year, template path, sheet-number spacing). The KiCad schematic sheets
  therefore did not need to change.
- **The board differs only in the disclaimed areas:** R4 placement plus 36→14
  track segments and 5→4 vias around it, a small `+VACT_GPS_IN` copper patch,
  the re-poured GND fills, and the silk text (`V1.3`→`V1.2`, `NRST`→`RST`).
  Every other footprint is byte-identical between the two imports.

The board was regenerated from Rev-11, and the disclaimer was retired.

### How the board was regenerated

Because the schematic and every other footprint were unchanged, the published
port's file was kept: setup, rules, title block, text variables, net table,
footprints with their schematic links and BOM fields, and embedded 3D models.
Only the geometry was replaced, with Rev-11's as imported headlessly by
KiCad 9.0.9:

- All tracks, vias and zones were replaced. Zones keep their Altium fills and
  are never refilled.
- All board graphics were replaced. The Edge.Cuts width was re-set to the
  port's 0.199898 mm convention, and pour clearance to 0.1499 as before.
- The moved R4 footprint was produced by a three-way merge: the port's
  metadata applied to Rev-11's geometry.
- Rev-11's 3D-model offsets were applied to the P1/P2 headers.

Nets are carried across by name, through pad correspondence, and any
unmapped name stops the script. The scripts are in [`scripts/`](scripts/).
Zone UUIDs are stable from run to run, which matters because DRC exclusions
refer to zones by UUID. Tracks, vias and graphics get fresh UUIDs and a
different order on every import. So a re-run reproduces the board structurally,
not byte for byte.

**KiCad 9.0.9 importer defect worked around.** Altium stores each text's
TrueType font name in a fixed 64-byte UTF-16 field and does not clear the
bytes after the terminator. KiCad converts all 64 bytes. In this file the
leftover bytes contain an unpaired UTF-16 surrogate, so the conversion fails
and all nine TrueType texts (Barlow, Barlow SemiBold, Arial Black, Calibri)
silently fall back to the stroke font, at stroke-font size. The import was
therefore run on a copy of the PcbDoc with that padding zeroed
(`scripts/sanitize_fonts.py`). The copy has the same stream sizes and no other
change, and its import differs from the unpatched one only in those nine texts.

## Structure and import quirks

- Altium project: `01_COVER` / `02_BLOCK-DIAGRAM` / `03_IO-CONNECTION` /
  `04_NOTECARD-CONNECTION` / `05_POWER` SchDocs. Per house convention the
  cover and block-diagram sheets (no electrical content) are not ported; the
  three electrical sheets become child sheets of a new root.
- **Label promotion**: 25 net names that Altium scopes globally were imported
  as sheet-local labels (present on multiple sheets, or duplicated as both
  local and global labels) — which silently splits them per sheet in KiCad.
  All were promoted to global labels; every name was first verified to be a
  single net in the Altium board's pad-to-net table.
- **DNP flags**: LD1, R11 and R4 are absent from the shipped production BOM
  (`BOM-3000-794-001.xlsx`) and from the pick-and-place file, and carry KiCad
  DNP flags. BOM comparison keys on the
  `BL PART NUMBER` field — the DbLib passives carry `N/A` manufacturer part
  numbers in the schematic source.
- **Footprint library**: 11 footprints crash KiCad's `FootprintSave` when
  exported through pcbnew (R-0402, J-NANOSIM-SF72S006VBA, SOT-583, C-0603,
  QFN40P300X150X80-18N, C-0805, BGA8N40P2X4_180x100x50, IND_XFL4020, R-0603,
  L-0603, SOT666); they were extracted textually from the board file instead
  (instance placement/net tokens stripped).
- The 1 µm-copper NPTH pads (3.3 mm mounting holes, connector
  polarization/anchor drills) are intentional Altium mechanical-hole
  modelling and are kept; the unnamed mount-hole footprints are named
  `MTG_NPTH_3.3mm`.
- Edge.Cuts uses the Altium outline width convention (0.199898 mm).
- DRC is clean with **no exclusions** (0 violations, 0 unconnected items,
  0 parity issues).
- `kicad-cli` F8-equivalent (Update PCB from Schematic) run with *re-link by
  reference* ON and *replace footprints* OFF; the only errors are the
  footprint-less assembly pseudo-symbol ASS1 (a documentation item, not a
  board component).

## Validation summary

Gates run by `_Tools/kicad_validation/run_all.py notecarrier-x`
(artifacts in [`../validation/`](../validation/)):

| Gate | Result |
|---|---|
| ERC (error severity) | PASS — 0 |
| DRC + schematic parity (error severity) | PASS — 0 violations, 0 exclusions |
| BOM vs `BOM-3000-794-001.xlsx` | PASS — exact on `BL PART NUMBER` per refdes |
| Netlist vs released Rev-11 PcbDoc (pad by pad) | PASS — 0 conflicts; 56/56 net partitions (`../validation/altium-netlist-compare.txt`) |
| Gerber raster diff vs published `2200-918__2024-06-06.zip` | PASS — copper/mask/paste 0.001–0.010, no difference cluster ≥ 0.045 mm²; silk = font-metric class only |
| Placement vs shipped pick-and-place file | PASS — 41/41 on board side and rotation (`../validation/pnp-compare.txt`) |
| kicanvas headless render (all sheets + board) | PASS |
| RAG extract parse | PASS |

The published fab package ships no ODB++/IPC-D-356 netlist, so the
independent-netlist gate is replaced by the pad-by-pad comparison against the
nets carried by the released Rev-11 board file.
