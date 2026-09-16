# Notecarrier-F v1.5

This folder contains the KiCad 9 design files for the Blues Notecarrier-F **v1.5**
(Byte Lab project `100275_NOTECARRIER-F`, schematic Rev 13, PCB `2201-139`,
BOM `3001-069-001`). They were generated with KiCad 9.0.9's Altium project
importer from the Altium Designer sources published in [`../Altium/`](../Altium/),
then cleaned up and validated against the released fabrication package, BOM and
pick-and-place files in the parent folder. See
[documentation/Porting-Notes.md](documentation/Porting-Notes.md) for the
process, the accepted differences, and the validation results (ERC, DRC with
schematic parity, BOM, gerber diff, placement, KiCanvas and RAG gates all pass).

Symbols and footprints captured during the import live in the project-local
`Notecarrier-F-altium-import` libraries, so the project is self-contained.
`blues-kicad-lib` (set `BLUES_KICAD_LIB_DIR`) is referenced for consistency
with the other ports but nothing in this project depends on it.

## Contents

- This file
	- `README.md`
- KiCad source files
	- `Notecarrier-F.kicad_pro`
	- `Notecarrier-F.kicad_prl`
	- `Notecarrier-F.kicad_sch` (root)
	- `Notecarrier-F_Notecard-Connection.kicad_sch`
	- `Notecarrier-F_Feather-Connection.kicad_sch`
	- `Notecarrier-F_IO.kicad_sch`
	- `Notecarrier-F_Power-Input.kicad_sch`
	- `Notecarrier-F_Power-Rails.kicad_sch`
	- `Notecarrier-F.kicad_pcb`
	- `Notecarrier-F.kicad_wks`
- Project libraries (captured from the Altium import)
	- `Notecarrier-F-altium-import.kicad_sym`
	- `Notecarrier-F-altium-import.pretty/`
- Library tables
	- `sym-lib-table`
	- `fp-lib-table`
- Documentation
	- `documentation/Porting-Notes.md`
	- `documentation/Notecarrier-F_SCH.pdf` — schematic exported from these sheets
- Validation artefacts (`_Tools/kicad_validation/run_all.py notecarrier-f`)
	- `validation/*` — ERC/DRC reports, BOM and placement comparisons, per-layer
	  gerber diff images and the frozen baseline, KiCanvas renders, and the
	  cross-check against the independently hand-ported schematic

## Notes for users

- `MOD1L`/`MOD1R` (the Feather sockets) are `MODL1`/`MODR1` in this project
  because KiCad cannot annotate a designator that ends in a letter. Nothing
  else differs from the released designators.
- The outer 24-pin sockets `J9`/`J10` are fitted on the product and in this
  design, but are missing from the released BOM spreadsheet (see Porting-Notes).
- Zone fills are the imported Altium fills. Do not refill them unless you are
  prepared to re-verify the copper against the shipped gerbers.

## Revision History

| Revision |    Date    |   Author   | Description |
|:--------:| ---------- | ---------- | ----------- |
|     A    | 2026-09-16 | Blues      | Import of the released v1.5 Altium sources (Rev 13 / 2201-139 / 3001-069-001); all validation gates pass. Supersedes the schematic-only delta port that briefly occupied this folder. |

### Original Altium Design File Revision History (Byte Lab 100275)

| Revision |    Date    |   Author     | Description | BOM |
|:--------:| ---------- | ------------ | ----------- | --- |
|    10    | 2023-05-31 | M. Hamin     | Initial board release | 3000-613-002 |
|    11    | 2023-07-10 | M. Hamin     | Changed R3, DS1-7, J1-3 & added U9 (v1.3) | 3000-653-001 |
|    12    | 2025-11-26 | A. Duracic   | R11/R12 mounted, USB-C connector and WiFi cutout placed, AUX and U6 removed, current draw reduced (internal "v1.4") | 3001-020-002 |
|    13    | 2026-01-26 | A. Duracic   | TVS added to USB-C connector, VSOLAR rewired, F_VUSB generates VUSB, VMAIN TVS changed (v1.5) | 3001-069-001 |
