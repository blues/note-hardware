# Notecarrier-XI v1.4 — Altium ➜ KiCad 9 Porting Notes

Ported from the Altium Designer sources in [`../Altium/`](../../Altium/)
(project `Notecarrier-XI_V4`, design by Byte Lab / FAE for Blues) using
KiCad 9.0.9's Altium project importer plus the scripted cleanup/validation
in [`_Tools/kicad_validation/`](../../../../_Tools/kicad_validation/). See
the Mojo, Cygnet, Scoop and Notecarrier-CX Porting-Notes for shared
importer background — the CX notes cover most of the techniques reused
here (label promotion, castellation/join handling, plane-connected pad
ring treatment, text variables).

## Structure and import quirks

- Altium sheets `01_COVER` / `02_BLOCK-DIAGRAM` (no electrical content) are
  not ported; `03_IO-CONNECTION`, `04_NOTECARD-CONNECTION`, `05_POWER`,
  `06_STARNOTE-CONNECTION` become child sheets of a new root. The project
  references a FAE-internal library (`TRASFORMATORE - FAE_Library.SchLib`)
  by absolute path that is not part of the sources; all symbols are
  embedded in the SchDocs, so nothing is lost.
- **Label promotion**: 25 nets that Altium scopes globally were imported as
  sheet-local labels (on several sheets, or duplicated local+global) and
  were promoted to global labels after verifying each name is a single net
  in the Altium board.
- ANT1 pins 4 (`NC`) and 7 (`FEED_GNSS_BT`) are genuinely unconnected in
  the Altium board and carry explicit no-connect markers (anchored at the
  exact pin endpoints — ERC's rounded display coordinates are ~0.2 µm off).
- Four decorative FAE-logo symbols (`*:root_0_MyFAETechnology_*`, unnamed
  `*?` references) were removed: their imported geometry crashes KiCanvas
  with infinite recursion ("Maximum call stack size exceeded"), and
  KiCanvas compatibility is a hard requirement of this port. The Blues
  logos and all electrical content are unaffected.
- ASS1/ASS2 (assembly screws — BOM-only line items with no footprint) stay
  on the schematic; the importer's 4 zero-size no-layer junk pads were
  deleted; the four corner NPTH mounting holes got a proper footprint name
  (`MTG_NPTH_3.3mm`).
- **Inner layers**: Altium "GROUND"/"POWER" plane layers plot positive and
  imported as fully-filled zones (In1 = solid GND; In2 = split power
  planes: +VIO/+VBAT/+VUSB/+VMAIN/+VBUS/…). Fills are preserved from the
  import — **do not refill**.
- Unused annular-ring suppression is applied to PTH pads except the eleven
  plane-connected pads the shipped inner-layer gerbers actually connect
  (C14/C21/J1.3/J1.4/OBJ2.1/P1.4/P1.16/P2.1/P2.16 — determined by probing
  the shipped G1/G2 rasters at every hole, with the raster alignment
  calibrated against the NC-drill file). Vias keep all annuli (KiCad's
  layer pruning ignores zone fills and would break plane connectivity).
- Altium keepout areas import with all-object semantics; they are
  copper-pour keepouts in this design (antenna area) and were relaxed to
  `copperpour not_allowed` only.
- One null-length (1 nm) Edge.Cuts segment from the importer was removed;
  Edge.Cuts stroke widths match the Altium outline aperture (0.2 mm).

## Deliberately-unrouted antenna option pads (DRC exclusions)

The ANT1 matching network provides alternate stuffing options. In the
shipped fab data one row of option pads (`NetANT1_3`, `NetANT1_5`,
`NetANT1_6` — L6.1/C26.2/ANT1.3, R23.1/R22.1/ANT1.5, R23.2/R22.2/ANT1.6)
has **no connecting copper** — the nets exist in the schematic and in the
shipped ODB++ netlist, but the copper is deliberately left open (verified
against the shipped gerbers: the fitted row is trace-connected, the option
row is not). KiCad's ratsnest flags these six pad pairs; they are recorded
as DRC exclusions in `Notecarrier-XI.kicad_pro` rather than "fixed", to
keep the copper identical to the fab data.

## Known copper deviations vs the shipped gerbers (accepted, documented)

The connectivity is proven identical to the Altium board and the shipped
ODB++ netlist (85/85 partitions on both checks), but KiCad's Altium
importer does not bring every plotted-copper construct. The per-layer
raster diffs in `../validation/` show, and this port accepts:

- **Thermal-land regions under the power components** (L2 buck inductor,
  D2/D3/D4 power diodes, J8): Altium plots solid heat-spreading lands with
  matching mask/paste openings there; the importer does not import these
  region objects (arc-bounded regions), so they are absent from the KiCad
  copper, mask and paste. All the parts' pads themselves match, and the
  lands are extensions of already-connected nets (+VBUS/+VSOLAR/GND/…).
- **Antenna keepout borders**: Altium plots the antenna-area keepout
  outlines on every copper layer of the fab data; KiCad rule areas do not
  plot.
- **Signal-via inner annuli** (In1/In2): KiCad plots them, Altium
  suppresses unused rings — no electrical effect.
- **Plane pullback boundary slivers** (In1/In2) and **silkscreen TrueType
  metric offsets** — same accepted classes as the other ports.

## Design rules

Clearance 0.1499 mm (the board routes with 0.15 mm spacing), track
0.15 mm, via 0.6/0.3 mm, hole-to-hole 0.1 mm, edge clearance 0,
`min_resolved_spokes 1`, severity baseline from the Notecarrier-A port.

## Validation results (see `../validation/`)

| Gate | Result |
|---|---|
| ERC / DRC (error severity, incl. schematic parity) | **0 / 0** (6 documented DRC exclusions, see above) |
| Netlist vs Altium PcbDoc (fresh headless import) | **85/85 nets exact** (schematic *and* board side) |
| Netlist vs shipped ODB++ (`PCB + 3D + 2D/FAB/ODB`) | **85/85 partitions** |
| BOM vs `BOM-ActiveBOM.xlsx` | exact on refdes and part name. **MPNs are effectively unverified on this board**: the shipped ActiveBOM fills its `MPN` column for only 1 of 66 lines (`J9`), so there is nothing to compare the remaining parts against. The column mapping is correct — the source data simply does not carry them. |
| Gerber raster diff vs `PCB + 3D + 2D/FAB/Gerber` | pads/tracks/planes match; deviations limited to the documented classes above |
| KiCanvas / RAG extract | render + parse clean (after FAE-logo removal) |
