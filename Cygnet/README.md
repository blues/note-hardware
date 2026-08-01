# Cygnet

STM32L433CC in Adafruit Feather form factor

  - Schematics
  - Bills of material
  - PCB layouts and Gerber files
  - Dimensioned drawings
  - KiCad design files ([v1.2/KiCad_format](v1.2/KiCad_format), converted from the original sources and validated against the shipped fabrication outputs)

> **⚠️ One open discrepancy in the KiCad port.** Inner layer 1 (`In1_Cu`) carries
> roughly fifty annular rings that the shipped Gerbers do not, so its fabrication
> equivalence on that layer is **not proven** and the gerber gate fails. Every
> other layer matches, and the schematic, netlist and BOM are exact. See
> [the porting notes](v1.2/KiCad_format/documentation/Porting-Notes.md) before
> using these files to manufacture.
