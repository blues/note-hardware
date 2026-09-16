# Notecarrier F

  - Schematics
  - Bills of material
  - PCB layouts and Gerber files
  - Dimensioned drawings
  - 3D models
  - Altium Designer sources ([v1.5/Altium](v1.5/Altium))
  - KiCad design files
    - [v1.5/KiCad_format](v1.5/KiCad_format) — complete schematic + PCB, imported from the Altium sources in [v1.5/Altium](v1.5/Altium) and validated against the released fab package, BOM and pick-and-place files; see its [Porting-Notes](v1.5/KiCad_format/documentation/Porting-Notes.md)
    - [v1.3/KiCad_format](v1.3/KiCad_format) — ⚠️ mid-delta: the schematic describes v1.3 but the PCB still describes v1.2, so this is not yet a usable v1.3 deliverable; see its [ERRATA](v1.3/KiCad_format/ERRATA.md)

## Revisions

| Folder | Board silkscreen | Byte Lab schematic | BOM | Notes |
|---|---|---|---|---|
| [v1.5](v1.5) | NOTECARRIER-F V1.5 | 100275 Rev 13 (2026-01-26) | 3001-069-001 | USB-C connector; AUX/DFU switch removed (automatic Outboard DFU routing); Feather USB feeds VUSB; VSOLAR pin wired to the solar connector; copper keepout under the Notecard antenna area |
| [v1.3](v1.3) | NOTECARRIER-F V1.3 | 100275 Rev 11 (2023-07-10) | 3000-653-002 | Micro-USB; three DIP switches |
| [v1.0](v1.0) | — | n21-evt (2022) | — | Original release |
