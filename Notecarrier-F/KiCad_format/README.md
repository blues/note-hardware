# Notecarrier-F

This folder contains the design files for the Blues Wireless Notcarrier-F, in KiCad 7 format. They were generated by porting the original Altium design files. For a detailed description of the porting process, see [PortingNotes](documentation/PortingNotes.md).

Components in this design are sourced from the [blues-kicad-lib](https://github.com/blues/blues-kicad-lib) library. However, with the exception of 3D models, KiCad produces self-contained project files. Thus this project can still be used without access to the library.

## Contents

- This file
 	- `README.md`
- KiCad source files
	- `Notecarrier-F.kicad_pcb`
	- `Notecarrier-F.kicad_wks`
	- `sym-lib-table`
	- `fp-info-cache`
- Documentation
- Manufacturing artefacts
	- `manufacturing/*`
- Design references
	- `reference/*`
- Validation artefacts
	- `validation/*`


## Revision History

| Revision |    Date    |   Author   | Description |
|:--------:| ---------- | ---------- | ----------- |
|     A    | 2023-05-23 | H.Raftery  | Initial port from Altium design files, rev 2.0.<br /><br />Note this revision number is taken from the last entry in the "Revision History" table in the schematic (see below). It matches neither the folder name, the last commit message  or the PCB silkscreen (all are "v1.0"), and the date is inconsistent. No further guidance on resolving these inconsistencies is available in the version control history. |
|     B    | DRAFT      | H.Raftery  | Incoporate changes from rev 10 (PCB version 1.2, see table below) of subsequent design files. Additional porting notes have been added to the end of [PortingNotes](documentation/PortingNotes.md) |

### Original Altium Design File Revision History

| Revision |    Date    |   Author     | Description |
|:--------:| ---------- | ------------ | ----------- |
|    1.0   | 03-17-2022 | Ethan Pierce | Initial release Design |
|    2.0   | 02-10-2022 | Ethan Pierce | made changes from issues with proto1 build. located in confluence |

### Subsequent Altium Design File Revision History

| Revision |    Date    |   Author     | Description |
|:--------:| ---------- | ------------ | ----------- |
|    10    | 2023-05-31 | M. Hamin     | Initial board release |