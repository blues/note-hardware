# Notecarrier-F v1.3

This folder contains the KiCad 9 design files for the Blues Notecarrier-F **v1.3**
(Byte Lab project `100275_NOTECARRIER-F`, schematic Rev 11, PCB `2200-814`,
BOM `3000-653-002`). They were generated with KiCad 9.0.9's Altium project
importer from the Altium Designer sources published in [`../Altium/`](../Altium/),
then cleaned up with the scripts in [`documentation/scripts/`](documentation/scripts/)
and validated against the released fabrication package, BOM and pick-and-place
file in the parent folder. See
[documentation/Porting-Notes.md](documentation/Porting-Notes.md) for the
process, the accepted differences, and the validation results (ERC, DRC with
schematic parity, BOM, gerber diff, placement, KiCanvas and RAG gates).

The Altium sources are the design house's release-day snapshot (10 July 2023,
the date of the `2200-814__2023-07-10` fabrication package), recovered from the
Blues design archive; the Rev 11 schematic PDF committed beside them is
byte-identical to the one published here, and the gerber diff confirms the
board matches the shipped artwork.

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
	- `documentation/scripts/` — the post-import cleanup scripts, for reproducibility
- Validation artefacts (`_Tools/kicad_validation/run_all.py notecarrier-f-v13`)
	- `validation/*` — ERC/DRC reports, BOM and placement comparisons, per-layer
	  gerber diff images and the frozen baseline, KiCanvas renders, and the
	  pad-by-pad comparison of the KiCad netlist against the Altium board's nets

## Notes for users

- `MOD1L`/`MOD1R` (the Feather sockets) are `MODL1`/`MODR1` in this project
  because KiCad cannot annotate a designator that ends in a letter. Nothing
  else differs from the released designators.
- `J9`/`J10` (the outer 24-pin sockets) are fitted: the released BOM
  `3000-653-002` lists them, although the release-day Altium variant still
  marked them unfitted (the design house flipped the variant in its
  2023-08-31 re-save, the same day the BOM report was generated).
- `J11`, `R11`, `R12` are unfitted (DNP) on the production variant.
- Zone fills are the imported Altium fills. Do not refill them unless you are
  prepared to re-verify the copper against the shipped gerbers.

## Revision History

| Revision |    Date    |   Author   | Description |
|:--------:| ---------- | ---------- | ----------- |
|     A    | 2024-06    | Blues      | Hand port of the Notecarrier-F Altium design to KiCad 7 (notes kept as `documentation/History_Porting-Notes-hand-port.md`). Later shown to describe v1.2 (BOM 3000-613-002) rather than v1.3. |
|     B    | 2026-08-01 | Blues      | Upgraded to KiCad 9; schematic delta-ported to v1.3 while the board still described v1.2 (ERRATA). |
|     C    | 2026-09-18 | Blues      | Superseded by a direct import of the release-day v1.3 Altium sources (Rev 11 / 2200-814 / 3000-653-002); all validation gates pass. |

### Original Altium Design File Revision History (Byte Lab 100275)

| Revision |    Date    |   Author     | Description | BOM |
|:--------:| ---------- | ------------ | ----------- | --- |
|    10    | 2023-05-31 | M. Hamin     | Initial board release (v1.2) | 3000-613-002 |
|    11    | 2023-07-10 | M. Hamin     | Changed R3, DS1-7, J1-3 & added U9 (v1.3) | 3000-653-002 |
