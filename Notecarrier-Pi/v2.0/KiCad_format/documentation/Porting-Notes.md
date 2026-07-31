# Notecarrier-Pi v2.0 — Delta-Port Notes (OrCAD/Allegro ➜ KiCad 9)

The Notecarrier-Pi is authored in OrCAD Capture / Allegro, for which no KiCad
importer exists, so this port could not be made the way the Altium-authored
boards were. Instead it is a **delta port**: the hand-made, fully validated
**Notecarrier-Pi v1.1 KiCad port** (by EmpiricalEE, in `../../v1.1/`) was
upgraded to KiCad 9 and every v1.1 → v2.0 design change was extracted from
the published fabrication data, applied, and re-verified. The result is
validated against the published v2.0 package with the same gate battery used
for the Altium ports.

## Version provenance (why there is no disclaimer)

* **Schematic**: the published `Notecarrier-Pi Schematic v2..pdf` is
  byte-identical to the internal **V5** schematic release of project
  `2017-3047 (NOTECARRIER-M2-PI)`; the schematic delta was captured from it
  and cross-checked against the internal V5 BOM.
* **Board**: the published `Notecarrier-Pi Gerbers v2.zip` **is** the
  internal **V6** board release (`20173047_notecarrier-m2-pi_v6`); the film
  set used during porting was md5-verified byte-identical to the zip contents.
* The board silkscreen legend reads **"NOTECARRIER-PI 2.1"** and the copper
  doc number reads `20173047_V6`; both are the shipped v2.0 product's actual
  markings and are transcribed verbatim.

## The delta, v1.1 ➜ v2.0

Schematic (single sheet, captured from the V5 PDF):

* New 3.3 V buck converter: U3 (AP62250WU-7), L4 (LQH32PN 4.7 µH), C13–C17,
  R19/R20 (0R `3V3_RAW`→`3V3` links), R22/R26 (feedback divider), R23/R25
  (enable), plus supply diode-OR DS3/DS4 (FSV1045V): `VIO#` (HAT 3.3 V, was
  `VIO` in v1.1) and `3V3` OR into `VIO`.
* Grove connector J5 replaced by two Qwiic connectors J5/J6
  (BM04B-SRSS-TB), powered from `VIO_P`.
* New test points TP5–TP7 and `AUX5`/`BOOT` taps to the M.2 socket.
* The fuse F1 sits between `VIO` (diode-OR output) and `VIO_P` as in v1.1.

Board (4-layer; every change extracted from the published films):

* 34 component placements moved/added (all verified pad-by-pad against the
  film flashes; the three DIP switches moved from the bottom to the top side).
* Outer-layer copper: ~360 track/via changes applied at full film-coordinate
  precision.
* **In2 (POWER)**: all three routes re-drawn — the `V+` feed re-routed
  around new GND stitch vias, a new `VIO` run (diode-OR output DS4 ➜ fuse
  F1), and the `VIO_P` run re-targeted to the new Qwiic position. The In2
  GND island was reshaped to the film outline.
* **In1 (GND plane)**: the plane pulls back from the buck area and the
  extended slot in v6; reproduced with explicit pour-keepout areas taken
  from the film polygons (incl. the small relief moats the plane has always
  had — the v1.1 port relied on preserved fills for these; this port's
  fills are regenerated, so the moats are now modeled explicitly).
* Bottom pours: `VUSB` widened, `V+`/`VMODEM`/shield pours reshaped, new
  `/3V3_RAW`, `/3V3_SW` and GND patches under the buck (solid-connect zones
  named `SolidGND`, which the inherited `GndZone2GndPad` rule exempts), and
  the main GND pour's south-west boundary re-drawn from the film winding.
* SIM eject slot extended 2 mm (routed slot now ends at y = 2 mm).
* Silkscreen re-laid: title block ("NOTECARRIER-PI 2.1"), ON/OFF +
  ATTN / SERIAL TXRX / GPS ACTIVE switch labels moved to the top side, a
  QWIIC pinout block (GND/3V3/SDA/SCL + pin-1 ticks + brackets), the layer
  marker "4" and the L4 frame on the bottom, and the copper version text
  updated to `20173047_V6`.

## Verification battery

Gates run by `_Tools/kicad_validation/run_all.py notecarrier-pi`
(artifacts in [`../validation/`](../validation/)):

| Gate | Result |
|---|---|
| ERC (error severity) | PASS — 0 |
| DRC + schematic parity (error severity) | PASS — 0 violations, 0 unconnected, 33 documented exclusions |
| BOM vs internal V5 BOM | PASS — 54/54 exact on MPN per refdes (`bom-compare.txt`; the shipped BOM spreadsheet is internal and not committed) |
| Netlist | PASS — geometric net-partition comparison against the published films: 270 pads / 139 copper islands, 0 conflicts (`fabnet-compare.txt`; the fab package ships no ODB++/IPC-D-356 netlist) |
| Gerber raster diff vs published films | PASS — all ten layers (incl. In1/In2) at the film-outline-stroke baseline, deviations reviewed (below) |
| kicanvas headless render (sch + board) | PASS |
| RAG extract parse | PASS |

Because the published films are Allegro artwork films with an A3 drawing
frame, the gerber-diff gate uses the explicit render windows configured in
`boards.yaml` (`window:`), and the films' own outline strokes
(`original_has_outline: true`).

### Netlist-level proof of the tricky parts

A dedicated connectivity trace of the published films (copper islands from
tracks/flashes/regions + plated drill holes, each island's pads compared to
the KiCad netlist) both drove and proves the port: it caught eleven
two-terminal parts whose fab orientation flips between the revisions
(F1, R19, R20, R23, R26, C1, C7, C13, TVS3, C8, R5 — invisible to pad-position
checks on symmetric footprints) and, after correction, reports **zero
conflicting islands**. See `validation/fabnet-compare.txt`.

## Reviewed deviations from the published films

1. **Board outline stroke**: every fab film draws the board outline; KiCad
   layer exports do not. This is the constant "fab-only" baseline in the
   diff PNGs (same convention as the v1.1 port).
2. **Stroke font**: silk legends and the copper version text use KiCad's
   stroke font at matching height/thickness; glyph shapes differ slightly
   from the Allegro font (same convention as the v1.1 port).
3. **Pour boundaries**: fills are regenerated by KiCad 9 from outlines,
   rules and keepouts that encode the film shapes; thin clearance-driven
   slivers along pour edges differ (~arc-chording/clearance detail, no
   connectivity impact). Fab pours keep unconnected islands, so island
   removal is disabled on the zones (the three `isolated_copper` warnings
   are fab-accurate).
4. **Degenerate film dots**: the films contain zero-length draws that
   render as small dots; 14 that exist in the v6 films are kept as
   zero-length tracks (v1.1 convention), 2 that only existed in v4 were
   removed with the superseding pour.
5. **Board-outline-on-silk**: like the v1.1 port, the outline strokes the
   films draw on the silk layers are not reproduced.

## DRC exclusions and rule notes (33 exclusions)

* Most exclusions are inherited from the v1.1 port and re-anchored: KiCad's
  zone filler pulls fills back to exactly the `GndZone2GndPad`
  physical-clearance rule distance and integer-nanometre rounding then
  reports them 1 nm short (`0.126999 < 0.127`); the same class exists in the
  v1.1 project.
* The published board routes the `V+` inner-layer feed through mounting hole
  H1's keepout circle (2.84 mm from hole centre, keepout radius 3 mm). The
  v1.1 port excluded the equivalent violations; this port additionally uses
  a footprint variant (`FORO-0270-U_tracks-allowed`) documenting that tracks
  are allowed there, and keeps the exclusions for the remaining items.
* `min_copper_edge_clearance` is 0.95 mm (v1.1 used 1.0 mm): the published
  board routes `/SIM_NPRESENT` 0.955 mm from the extended SIM slot edge.
* J2's two keepout areas were made solid rectangles (the v1.1 originals were
  hollow rings whose interiors were cleared by fill-island removal, which
  this port disables — see deviation 3).

## Footprints

New parts use exact-film pad geometry in `Notecarrier-Pi-local.pretty`
(SOT23-6-DBV, LS-LQH32PN, TPS-0100, TPS-0150, CS-C-1206, J-4-0100-MDS-SH);
`FORO-0270-U_*` and `J-NANOSIM-SF72S006VBA_NO-FILL` are local variants of
shared-library parts with the keepout semantics this port needs. All other
footprints are unchanged from the v1.1 port.

## Sources

Conversion inputs (internal, not committed): the Allegro board releases V4
(= published v1.1) and V6 (= published v2.0) with their artwork films and
placement data, the V5 schematic PDF, and the V5 BOM. Public ground truth
(committed in the parent folder): `Notecarrier-Pi Gerbers v2.zip`,
`Notecarrier-Pi PCB v2.brd`, `Notecarrier-Pi PCB v2.pdf`,
`Notecarrier-Pi Schematic v2..pdf`.
