# Mojo v1.1 — KiCad format

This directory contains the design files for the Blues **Mojo** v1.1
(internal design name *Mojo-v4*) in **KiCad 9** format. They were generated
by porting the original Altium Designer design files found in
[`../Sources/`](../Sources/), and validated against the shipped BOM and
fabrication outputs — see
[`documentation/Porting-Notes.md`](documentation/Porting-Notes.md) for the
full porting log and [`validation/`](validation/) for the evidence
(ERC/DRC reports, per-layer gerber diffs against the production gerbers,
KiCanvas render checks).

## Contents

| Path | Description |
|---|---|
| `Mojo.kicad_pro` / `Mojo.kicad_prl` | KiCad project (design rules match the Altium DRC report) |
| `Mojo.kicad_sch` | Schematic (single flat sheet, symbols embedded) |
| `Mojo.kicad_pcb` | Board (footprints embedded; zone fills preserved from the Altium import — do not refill) |
| `Mojo.kicad_wks` | Drawing sheet (shared Blues template) |
| `Mojo-altium-import.kicad_sym` / `Mojo-altium-import.pretty/` | Project symbol/footprint libraries captured during the import |
| `sym-lib-table` / `fp-lib-table` | Library tables (project libraries + optional [blues-kicad-lib]) |
| `documentation/` | Porting notes and plotted schematic/board PDFs |
| `manufacturing/Mojo_RevA.zip` | Gerbers + Excellon drill files exported from KiCad (the authoritative production package remains [`../Fabrication/`](../Fabrication/)) |
| `validation/` | Port-QA artifacts: ERC/DRC reports, `<Layer>-{KiCad,Altium,diff}.png` gerber diffs, BOM comparison, KiCanvas screenshots |

The project is self-contained: all symbols and footprints are embedded or
provided in the project libraries. The external [blues-kicad-lib] is only
referenced for consistency with the other Blues KiCad ports and is not
required to open or edit this project. No 3D models are included.

Note: the production ("Normal") assembly variant is represented with KiCad
DNP flags on J2/J3/J7/J8; test point, mounting holes and logo items are
excluded from the BOM, matching the shipped
[`BOM-Mojo-v4-Normal.xls`](../Assembly%20Normal/BOM/).

## Revision History

| Revision | Date | Author | Notes |
|---|---|---|---|
| A | 2026-07-28 | Blues Inc | Initial port of Mojo v1.1 (Mojo-v4) from Altium Designer sources, KiCad 9.0.9 |

### Original (Altium) revision

| Revision | Notes |
|---|---|
| v4 (public v1.1) | Production release, 2024-06 |

[blues-kicad-lib]: https://github.com/blues/blues-kicad-lib
