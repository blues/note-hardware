# Notecarrier-X — KiCad format

This directory contains the design files for the Blues **Notecarrier-X**
in **KiCad 9** format, ported from the internal Altium Designer sources
(project `100379_notecarrier-x`, Byte Lab Grupa d.o.o. for Blues) and
validated against the shipped production BOM and the published v1.2
fabrication package — see
[`documentation/Porting-Notes.md`](documentation/Porting-Notes.md) and
[`validation/`](validation/).

Generated from the design house's **Rev-11 release snapshot** — the Altium
sources behind the published v1.2 fab package (`2200-918`). Copper, solder mask
and paste match that fab package to within raster resolution, and every pad's
net matches the released board. An earlier version of this port was built from a post-v1.2
development state and carried a source-fidelity disclaimer; it was
regenerated from Rev-11 in October 2026 and the disclaimer retired (see the
Porting-Notes history section).

## Contents

| Path | Description |
|---|---|
| `Notecarrier-X.kicad_pro` / `.kicad_prl` | KiCad project |
| `Notecarrier-X.kicad_sch` | Root schematic sheet |
| `Notecarrier-X_IO-Connection.kicad_sch` | IO connection sheet |
| `Notecarrier-X_Notecard-Connection.kicad_sch` | Notecard connection sheet |
| `Notecarrier-X_Power.kicad_sch` | Power sheet |
| `Notecarrier-X.kicad_pcb` | 2-layer board (zone fills preserved from the Altium import — do not refill) |
| `Notecarrier-X.kicad_wks` | Drawing sheet (shared Blues template) |
| `Notecarrier-X-altium-import.kicad_sym` / `.pretty/` | Project libraries captured during the import |
| `sym-lib-table` / `fp-lib-table` | Library tables |
| `documentation/` | Porting notes (provenance and verification), plotted PDFs, and the board-regeneration scripts (`scripts/`, also used for Notecarrier-XM) |
| `manufacturing/Notecarrier-X_RevA.zip` | KiCad-exported gerbers + drill |
| `validation/` | Validation-gate artifacts (ERC/DRC/BOM reports, per-layer gerber diffs, kicanvas renders) |

The schematic references the shared Blues symbol/footprint library via the
`BLUES_KICAD_LIB_DIR` path variable
([blues-kicad-lib](https://github.com/blues/blues-kicad-lib)), with all
symbols and footprints used by this design also embedded in the project
libraries above, so the project opens standalone.

## Provenance

Ported from Altium Designer sources with KiCad 9.0.9's importer and the
validation harness in
[`_Tools/kicad_validation/`](../../../_Tools/kicad_validation/). The original
Altium sources are internal and are not part of this repository; the
published v1.2 fabrication package (`../2200-918__2024-06-06.zip`), BOM
(`../BOM-3000-794-001.xlsx`) and drawings in the parent folder remain the
manufacturing ground truth for the shipped product.
