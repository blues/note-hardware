# Notecarrier-XM — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for **Notecarrier-XM**
(project `100378_notecarrier-xm`, design by Byte Lab Grupa d.o.o. for Blues)
using KiCad 9.0.9's Altium project importer plus the scripted
cleanup/validation in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo, Cygnet and Notecarrier-CX Porting-Notes for shared importer background.

## ⚠️ Source-fidelity disclaimer — read first

**This port was NOT generated from the exact design snapshot that produced
the published v1.2 fabrication package** (`2200-917__2024-06-12.zip` in the
parent folder). That exact snapshot was never captured in the design house's
version control; the closest available state — the post-v1.2 development
state — was used instead. **The Notecarrier-XM deviations are larger than on
the Notecarrier-X/-XS ports**: beyond the silkscreen, several signals are
routed differently. A full per-layer gerber comparison against the published
v1.2 fab (see [`../validation/`](../validation/)) shows, all reviewed:

1. **Silkscreen**: the source silk reads **V1.3** where the published board
   reads **V1.2**, with legend text repositioned on both sides.
2. **Rerouted signals** (both copper layers): the published board routes the
   central AUX/UART bundle (`AUX1`–`AUX4`, `AUX_EN`, `AUX_RX`, `AUX_TX`,
   `RX`, `TX`), `AUX_NCHARGING`, and the optional GPS-power area
   (`+VACT_GPS_IN` / `+VACT_GPS_OUT`, around the production-DNP jumper R2)
   along different paths than this source, with the corresponding via
   placements differing. The connectivity is the same — the same pads connect
   to the same nets — but the copper geometry in those areas does not match
   the published board.
3. **Minor pour-boundary differences**: thin slivers along the GND pour
   perimeter and castellation clearances.
4. **Everything else matches**: the remaining copper, mask, paste and drill
   data match the published fab package, and the netlist was proven identical
   to the source board (37/37 net partitions).

**What has since been confirmed against the released build.** The shipped
pick-and-place file for this assembly is generated from the released design, so
comparing against it tests the port independently of the source snapshot it was
made from. All 13 placed parts are present in the port, on the same board side,
at the same rotation as the boards that were actually built. (Position residuals are reported but not gated: the assembly file references
each part's body centre while KiCad measures from the footprint origin, so
asymmetric parts carry a fixed per-footprint offset — it even changes sign when
a part is rotated 180°. Copper geometry is proven exactly by the gerber diff.)

What is still missing to retire this disclaimer entirely is a **netlist from the
released snapshot** — a Protel `.NET`, or better an IPC-D-356A/ODB++ export of the
released PCB, which would also validate geometry and plugs into the netlist gate
already used for the Notecarrier-CX and -XI ports. A sweep of all 293
repositories in the Blues organisation found no such file for this board.

If the exact released v1.2 Altium snapshot ever becomes available, this port
should be regenerated from it and the disclaimer dropped.

The dev project's parameters carry the v1.3-era document numbers
(`PCBA_BOM_Num 3000-825-001`, `PCB_Num 2200-932`); the KiCad project's
title-block text variables were set to the published v1.2 numbers
(`3000-793-001` / `2200-917`) so the drawings match the published product
documentation.

## Structure and import quirks

- Altium project: `01_COVER` / `02_BLOCK-DIAGRAM` / `03_IO-CONNECTION` /
  `04_NOTECARD-CONNECTION` / `05_POWER` SchDocs. Per house convention the
  cover and block-diagram sheets (no electrical content) are not ported; the
  three electrical sheets become child sheets of a new root.
- **Label promotion**: 25 net names that Altium scopes globally were imported
  as sheet-local labels; all were promoted to global labels after verifying
  each against the Altium board's pad-to-net table.
- **Castellated edge headers (P1/P2)**: as on Notecarrier-CX, Altium models
  each castellated position as *two* same-numbered PTH pads (the half-cut
  edge pad plus an inner hole) joined by solid copper that KiCad's importer
  drops — leaving 32 phantom "missing connection" items and 64 degenerate
  zero-size pads. The junk pads were removed and the 32 joins reconstructed
  as net-assigned filled copper rectangles on both outer layers (1.5 mm wide,
  matching the published fab's capsule shapes, pulled back from the board
  outline to satisfy the edge-clearance check). The 32 half-cut edge pads
  carry KiCad's castellated-pad property, which exempts them from the
  board-edge clearance check; `min_copper_edge_clearance` is 0 as on the
  other castellated ports.
- **DNP flag**: R2 — the optional GPS-power 0R jumper — is absent from the
  shipped production BOM (`BOM-3000-793-001.xlsx`), absent from the
  pick-and-place file, and is the project variant's unfitted part; it carries
  a KiCad DNP flag.
- The 1 µm-copper NPTH pads (3.3 mm mounting holes, connector anchors) are
  intentional Altium mechanical-hole modelling and are kept; the unnamed
  mount-hole footprints are named `MTG_NPTH_3.3mm`.
- Edge.Cuts uses the Altium outline width convention (0.199898 mm).
- `kicad-cli` F8-equivalent (Update PCB from Schematic) run with *re-link by
  reference* ON and *replace footprints* OFF; the only error is the
  footprint-less assembly pseudo-symbol ASS1 (a documentation item, not a
  board component).

## Validation summary

Gates run by `_Tools/kicad_validation/run_all.py notecarrier-xm`
(artifacts in [`../validation/`](../validation/)):

| Gate | Result |
|---|---|
| ERC (error severity) | PASS — 0 |
| DRC + schematic parity (error severity) | PASS — 0 violations, 0 exclusions |
| BOM vs `BOM-3000-793-001.xlsx` | PASS — exact on `BL PART NUMBER` per refdes |
| Netlist vs source PcbDoc (pad-to-net partitions) | PASS — 37/37 |
| Gerber raster diff vs published `2200-917__2024-06-12.zip` | PASS with the documented deviations above |
| Placement vs shipped pick-and-place file | PASS — 13/13 on board side and rotation (`../validation/pnp-compare.txt`) |
| kicanvas headless render (all sheets + board) | PASS |
| RAG extract parse | PASS |

The published fab package ships no ODB++/IPC-D-356 netlist, so the
independent-netlist gate is replaced by the pad-to-net partition comparison
against a fresh headless import of the source board.
