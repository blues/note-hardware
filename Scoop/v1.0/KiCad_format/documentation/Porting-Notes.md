# Scoop v1.0 — Altium ➜ KiCad 9 Porting Notes

Ported from the internal Altium Designer sources for *scoop-v4* (the design
revision shipped as public **Scoop v1.0** — the production gerbers in
[`../../992-00084-A_Gerbers.zip`](../../) are named `scoop v4.*`) using
KiCad 9.0.9's Altium project importer plus the scripted cleanup/validation in
[`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See the
Mojo and Cygnet Porting-Notes for shared importer background.

## Structure and import quirks

- Altium project: `Cover Sheet.SchDoc` (top) containing the `Scoop.SchDoc`
  design as a subsheet. Per house convention the cover sheet is not ported;
  the design sheet is promoted to project root (single flat sheet). Symbol
  instance data was re-anchored to the new root (project name/path rewrite),
  since stale instance paths otherwise leave the sheet "unannotated".
- **DbLib-driven parts**: the design references an Altium database library;
  two resistors carried unresolvable `${ALTIUM_VALUE}` placeholders. Their
  values/MPNs were restored from the shipped BOM and schematic PDF
  (R1 = 178k / RC0805FR-07178KL, R2 = 82k / RC0805FR-0782KL).
- **D1 (FSV1045V) is compile-masked in Altium** (greyed region on the shipped
  schematic PDF; absent from the PCB and BOM). It is kept on the schematic
  visually but flagged DNP + excluded from board and BOM — KiCad's closest
  semantics to Altium's compile mask.
- A `lib_name` cache reference (`..._1` symbol variant) had to keep its
  original un-prefixed name — KiCad resolves such overrides against the
  embedded library by exact string.
- J1/J2 carry the production connector part number (4UCON 20404, per the
  shipped BOM); the design-file JST part number (S2B-PH-SM4-TB) remains in
  the Description field.
- Production population: J3–J6 (debug/programming headers) are DNP; test
  points Z1–Z4 and fiducials/mounting holes are excluded from the BOM,
  matching `992-00084-A_BOM.xlsx` (12 populated PCBA references).
- The importer could not load a logo image referenced by absolute Windows
  path (`blues wireless logo snapshot.png`); the logo is present in the
  fabricated silkscreen (checked in the gerber diff) — only the schematic
  cover-sheet copy is affected, and that sheet is not ported.
- Altium's unused stackup remnants (Power Plane/Ground Plane/Internal Plane
  N) are unused on this 2-layer board and were left unmapped.
- Unused inner/outer annular-ring suppression enabled on PTH pads and vias
  (Altium parity), mounting-hole keepouts set to `pads allowed`, Altium
  special strings defined as project text variables.

## Design rules

Rules follow the fab notes (IPC Class 1, 2-layer) and measured board minima:
clearance 0.1015 mm (4 mil, rounding guard), track 0.17 mm, via 0.6/0.3 mm,
hole clearance 0.177 mm, edge clearance 0, `min_resolved_spokes 1`,
severity baseline from the Notecarrier-A port.

## Validation results (see `../validation/`)

| Gate | Result |
|---|---|
| ERC / DRC (error severity, incl. schematic parity) | **0 / 0** |
| Netlist vs Altium PcbDoc (fresh headless import) | **7/7 nets exact** (D1 compile-masked part excluded) |
| BOM vs `992-00084-A_BOM.xlsx` | exact — 12 populated refdes, MPN-compared (BOM "Name" column holds descriptions, not values) |
| Gerber raster diff vs `scoop v4.*` | PASS (copper/mask/paste; silk shows the usual TrueType metric offsets) |
| KiCanvas / RAG extract | render + parse clean |
