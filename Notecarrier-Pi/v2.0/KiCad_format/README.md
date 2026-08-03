# Notecarrier-Pi v2.0 — KiCad format

This directory contains the design files for the Blues **Notecarrier-Pi v2.0**
in **KiCad 9** format. The original design is authored in OrCAD/Allegro (no
KiCad importer exists for it); this port was produced as a verified **delta
port**: the validated Notecarrier-Pi v1.1 KiCad port was upgraded to KiCad 9
and every v1.1 → v2.0 design change was applied and proven against the
published v2.0 fabrication package — see
[`documentation/Porting-Notes.md`](documentation/Porting-Notes.md) and
[`validation/`](validation/).

Version provenance is exact (no source-fidelity disclaimer needed): the
published v2.0 schematic PDF is byte-identical to the internal V5 schematic
release, and the published fab package is the internal V6 board release
(`20173047_notecarrier-m2-pi_v6`); this port was validated per-layer against
that exact package. Note the published board's silkscreen legend reads
"NOTECARRIER-PI 2.1" — that is the shipped v2.0 product's marking,
transcribed verbatim.

## Contents

| Path | Description |
|---|---|
| `Notecarrier-Pi.kicad_pro` / `.kicad_prl` | KiCad project (33 documented DRC exclusions — see Porting-Notes) |
| `Notecarrier-Pi.kicad_sch` | Schematic (single sheet) |
| `Notecarrier-Pi.kicad_pcb` | 4-layer board |
| `Notecarrier-Pi.kicad_dru` | Custom design rules (inherited from the v1.1 port) |
| `Notecarrier-Pi.kicad_wks` | Drawing sheet |
| `Notecarrier-Pi-local.pretty/` | Project-local footprints (new v2.0 parts + variants of shared-lib parts) |
| `sym-lib-table` / `fp-lib-table` | Library tables |
| `documentation/` | Porting notes and plotted schematic/PCB PDFs |
| `manufacturing/Notecarrier-Pi_RevA.zip` | KiCad-exported gerbers + drill |
| `validation/` | Validation-gate artifacts (ERC/DRC/BOM reports, per-layer gerber diffs vs the published fab films, netlist evidence, kicanvas renders) |

The schematic references the shared Blues symbol/footprint library via the
`BLUES_KICAD_LIB_DIR` path variable
([blues-kicad-lib](https://github.com/blues/blues-kicad-lib)), with
project-specific parts in `Notecarrier-Pi-local.pretty`, so the project opens
standalone.

## What changed from v1.1

The v2.0 revision adds an on-board 3.3 V buck converter (U3 AP62250 + diode-OR
supply for `VIO`), replaces the Grove connector with two Qwiic connectors
(J5/J6), moves the three DIP switches from the bottom to the top side,
re-routes the affected areas on all four copper layers, extends the SIM eject
slot, and re-lays the silkscreen. All deltas were extracted from and verified
against the published fab films.

## Provenance

Ported with the delta-port method and the validation harness in
[`_Tools/kicad_validation/`](../../../_Tools/kicad_validation/) (board name
`notecarrier-pi`). The original OrCAD/Allegro sources and the shipped BOM
spreadsheet are internal conversion inputs and are not part of this
repository; the published fab package (`../Notecarrier-Pi Gerbers v2.zip`),
board file, and drawings in the parent folder remain the manufacturing ground
truth for the shipped product.

## Revision History

| Revision |    Date    |   Author   | Description |
|:--------:| ---------- | ---------- | ----------- |
|     A    | 2026-07-31 | Blues      | Delta port of v2.0 (internal V5 schematic / V6 board) from the v1.1 KiCad port, KiCad 9. |
