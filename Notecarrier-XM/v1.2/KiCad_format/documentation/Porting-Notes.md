# Notecarrier-XM — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for **Notecarrier-XM**
(project `100378_notecarrier-xm`, design by Byte Lab Grupa d.o.o. for Blues)
using KiCad 9.0.9's Altium project importer plus the scripted
cleanup/validation in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo, Cygnet and Notecarrier-CX Porting-Notes for shared importer background.

## Source and provenance

The board is generated from the design house's **Rev-11 release snapshot**
of project `100378_notecarrier-xm` — the Altium sources behind the published
v1.2 fabrication package (`2200-917__2024-06-12.zip`), schematic
(`100378_notecarrier-xm_Rev-11.PDF`) and BOM (`BOM-3000-793-001.xlsx`) in the
parent folder. The snapshot's own project parameters carry exactly those
document numbers (`PCB_Num 2200-917`, `PCBA_BOM_Num 3000-793-001`,
`HW_E_Doc_Rev 11`) and its silkscreen reads **V1.2**.

That it is the released design was checked against the published fab
package, not assumed:

- **Copper, solder mask and paste are exact.** After rasterising both sides
  at 1200 dpi and removing sub-0.1 mm slivers, no difference cluster of
  0.045 mm² or larger remains on any of the six layers (normalised
  difference 0.000–0.007; see [`../validation/`](../validation/)). That
  includes the central AUX/UART bundle, `AUX_NCHARGING` and the GPS-power
  area around R2, which were the deviations the earlier disclaimer listed.
- **Silkscreen content matches**, including `V1.2`. What the silk diff still
  shows is the usual font class: Altium and KiCad render TrueType text with
  different metrics.
- **Connectivity matches the released board pad for pad.** Every pad's net in
  the Rev-11 PCB agrees with this port's schematic (0 conflicts,
  [`../validation/altium-netlist-compare.txt`](../validation/altium-netlist-compare.txt)),
  and the two netlists group pins into the same 37 nets.

### History: the earlier source-fidelity disclaimer

This port was first published in July 2026 from the closest source then
available, a post-v1.2 development state. Besides V1.3 silk, that state had
the R2 jumper fix that came later ("Fixed ACT_GPS jumper position") and the
rerouting that went with it, so the port carried a stronger disclaimer than
Notecarrier-X/-XS. When the Rev-11 snapshot arrived (October 2026), it was
compared with that development state record by record:

- **The schematics are identical in substance.** All three electrical sheets
  have the same components, values, part numbers, labels, ports and wiring.
  The only differences are from re-applying the sheet template. The KiCad
  schematic sheets therefore did not need to change.
- **The board differences are the disclaimed ones:**
  - R2 at its released position (146.64, 118.00, 90°), not the later one;
  - 67→29 track segments and 18→14 vias rerouted;
  - re-poured GND fills, without the four thin edge keepouts the later state
    added;
  - silk `V1.2`, `RST`, and no `VGPS` label.

  Every other footprint is byte-identical between the two imports.

The board was regenerated from Rev-11, and the disclaimer was retired.

### How the board was regenerated

Because the schematic and every other footprint were unchanged, the published
port's file was kept: setup, rules, title block, text variables, net table,
footprints with their schematic links and BOM fields, embedded 3D models, and
the castellation reconstruction described below. Only the geometry was
replaced, with Rev-11's as imported headlessly by KiCad 9.0.9:

- All tracks, vias and zones were replaced. Zones keep their Altium fills and
  are never refilled.
- All board graphics were replaced. The Edge.Cuts width was re-set to the
  port's 0.199898 mm convention, and pour clearance to 0.1499 as before.
- The moved R2 footprint was produced by a three-way merge: the port's
  metadata applied to Rev-11's geometry.
- Rev-11's 3D-model settings were applied to P1/P2.

The P1/P2 castellated headers sit at the same positions in both sources, so
their 64 reconstructed join rectangles carry over unchanged. Nets are carried
across by name, through pad correspondence, and any unmapped name stops the
script. The scripts are in the Notecarrier-X port's
[`documentation/scripts/`](../../../../Notecarrier-X/v1.2/KiCad_format/documentation/scripts/).
The importer assigns fresh UUIDs and object order on every run, so a re-run
reproduces the board structurally, not byte for byte.

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
- **Two documented DRC exclusions** (`items_not_allowed`, one per copper
  layer). The released GND pour's edge at x = 169.47 mm runs about 0.08 mm²
  into the clearance circle of fiducial FD2 (top) / FD7 (bottom). The shipped
  `2200-917` copper confirms the edge is fab-accurate (it has no notch there).
  KiCad's importer turns the fiducial's clearance into a no-pour rule area,
  which is why DRC reports it. Both exclusions are stored with that
  explanation in `Notecarrier-XM.kicad_pro`. The keys use KiCad's marker
  position: the point where the pour meets the rule-area outline, not the
  zone anchor the report prints.
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
| DRC + schematic parity (error severity) | PASS — 0 violations, 2 documented exclusions (fiducial clearance, above) |
| BOM vs `BOM-3000-793-001.xlsx` | PASS — exact on `BL PART NUMBER` per refdes |
| Netlist vs released Rev-11 PcbDoc (pad by pad) | PASS — 0 conflicts; 37/37 net partitions (`../validation/altium-netlist-compare.txt`) |
| Gerber raster diff vs published `2200-917__2024-06-12.zip` | PASS — copper/mask/paste 0.000–0.007, no difference cluster ≥ 0.045 mm²; silk = font-metric class only |
| Placement vs shipped pick-and-place file | PASS — 13/13 on board side and rotation (`../validation/pnp-compare.txt`) |
| kicanvas headless render (all sheets + board) | PASS |
| RAG extract parse | PASS |

The published fab package ships no ODB++/IPC-D-356 netlist, so the
independent-netlist gate is replaced by the pad-by-pad comparison against the
nets carried by the released Rev-11 board file.
