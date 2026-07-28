# Scoop v1.0 — KiCad format

This directory contains the design files for the Blues **Scoop** v1.0
(internal design *scoop-v4*) in **KiCad 9** format, ported from the original
Altium Designer sources and validated against the shipped BOM, production
gerbers, and the Altium board's own netlist — see
[`documentation/Porting-Notes.md`](documentation/Porting-Notes.md) and
[`validation/`](validation/).

## Contents

| Path | Description |
|---|---|
| `Scoop.kicad_pro` / `Scoop.kicad_prl` | KiCad project |
| `Scoop.kicad_sch` | Schematic (single flat sheet; the Altium cover sheet is not ported) |
| `Scoop.kicad_pcb` | 2-layer board (zone fills preserved from the Altium import — do not refill) |
| `Scoop.kicad_wks` | Drawing sheet (shared Blues template) |
| `Scoop-altium-import.kicad_sym` / `Scoop-altium-import.pretty/` | Project libraries captured during the import |
| `sym-lib-table` / `fp-lib-table` | Library tables |
| `documentation/` | Porting notes and plotted PDFs |
| `manufacturing/Scoop_RevA.zip` | Gerbers + drills exported from KiCad (authoritative package: [`../992-00084-A_Gerbers.zip`](../) ) |
| `validation/` | ERC/DRC reports, gerber diffs, BOM comparison, netlist cross-check, KiCanvas screenshots |

Note: D1 is compile-masked in the original design (not populated, not in the
BOM, not on the board) and is flagged DNP/excluded here; J3–J6 are DNP in the
production build.

## Revision History

| Revision | Date | Author | Notes |
|---|---|---|---|
| A | 2026-07-28 | Blues Inc | Initial port of Scoop v1.0 (scoop-v4) from Altium Designer sources, KiCad 9.0.9 |
