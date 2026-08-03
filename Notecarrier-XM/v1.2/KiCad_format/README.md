# Notecarrier-XM — KiCad format

This directory contains the design files for the Blues **Notecarrier-XM**
in **KiCad 9** format, ported from the internal Altium Designer sources
(project `100378_notecarrier-xm`, Byte Lab Grupa d.o.o. for Blues) and
validated against the shipped production BOM and the published v1.2
fabrication package — see
[`documentation/Porting-Notes.md`](documentation/Porting-Notes.md) and
[`validation/`](validation/).

> **⚠️ Disclaimer:** the exact Altium snapshot that produced the published
> v1.2 fabrication package was never captured in version control, so this
> port was made from the closest available source — the post-v1.2
> development state. It differs from the published v1.2 board in reviewed,
> documented ways, and **more so than the Notecarrier-X/-XS ports**: the
> silkscreen reads **V1.3**, and several signals (the central AUX/UART
> bundle, `AUX_NCHARGING`, and the optional GPS-power jumper area around the
> production-DNP R2) are **routed along different paths** than the published
> board. Connectivity matches the source design 37/37 and the remaining
> copper/mask/paste/drill match the published fab. Details in
> [`documentation/Porting-Notes.md`](documentation/Porting-Notes.md).
>
> Since publication the port has additionally been checked against the
> **released build's** pick-and-place file: all 13 placed parts match the
> shipped boards on side and rotation.

## Contents

| Path | Description |
|---|---|
| `Notecarrier-XM.kicad_pro` / `.kicad_prl` | KiCad project |
| `Notecarrier-XM.kicad_sch` | Root schematic sheet |
| `Notecarrier-XM_IO-Connection.kicad_sch` | IO connection sheet |
| `Notecarrier-XM_Notecard-Connection.kicad_sch` | Notecard connection sheet |
| `Notecarrier-XM_Power.kicad_sch` | Power sheet |
| `Notecarrier-XM.kicad_pcb` | 2-layer castellated board (zone fills preserved from the Altium import — do not refill) |
| `Notecarrier-XM.kicad_wks` | Drawing sheet (shared Blues template) |
| `Notecarrier-XM-altium-import.kicad_sym` / `.pretty/` | Project libraries captured during the import |
| `sym-lib-table` / `fp-lib-table` | Library tables |
| `documentation/` | Porting notes (incl. the source-fidelity disclaimer) and plotted PDFs |
| `manufacturing/Notecarrier-XM_RevA.zip` | KiCad-exported gerbers + drill |
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
published v1.2 fabrication package (`../2200-917__2024-06-12.zip`), BOM
(`../BOM-3000-793-001.xlsx`) and drawings in the parent folder remain the
manufacturing ground truth for the shipped product.
