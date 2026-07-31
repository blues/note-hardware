# ⚠️ INCOMPLETE PORT — DO NOT PUBLISH OR COMMIT AS-IS

Work in progress on the Notecarrier-A v2.3 KiCad port. The board is **not yet
fab-accurate** and has not passed the validation battery. Deliberately left
untracked in git.

## Provenance (proven)

* The published v2.3 board file (`../PCB/20210324_notecarrier-m2-al_v20.brd`)
  and gerber zip are byte-identical (md5) to the internal Allegro **v20**
  release; the matching schematic is internal **v19** (v19→v20 was a
  silk/PCB respin). `fae/notecarrier/notecarrier-al/changes.txt` lists the v20
  changes verbatim.
* **v2.3 is a re-layout, not a tweak**: 51 of 94 parts moved (the M.2 socket
  J6 by 29 mm, OBJ1 by 39 mm, F1 by 40 mm), ~75 % of vias moved and most
  traces changed. A "delta port" therefore degenerates into a full
  reconstruction from the published artwork films.

## Done and verified

* **Scaffold**: copied from the validated v2.0 port (= Allegro v16), upgraded
  to KiCad 9 (schematics via an eeschema round-trip, board via pcbnew).
* **Schematic delta COMPLETE — ERC 0 errors**: J2 and its two support symbols
  removed; J11 micro-USB → **USB-C** (Amphenol `12402012E212A`) with a new
  16-pin symbol, VBUS/D±/GND paralleled per the v19 sheet, SBU1/2 floating;
  **R32/R33** 5.1 k CC pull-downs added. BOM refdes set matches the internal
  v19 BOM exactly (87/87 electrical refs).
* **USB-C footprint** built from the v20 film pad flashes and drill data, and
  its **pad naming derived from the fab's own connectivity** — the tracer
  caught a genuine pad-order error (CC1/CC2 and the D pairs transposed) that
  no geometric check would have found. Now consistent: CC2→R32 at film
  y 12.01, D pairs at 13.01/13.51 and 14.01/14.51, CC1→R33 at 15.01,
  SBU1/SBU2 unrouted.
* **Board sync** (scripted equivalent of Update-PCB-from-Schematic, re-link by
  reference ON / replace footprints OFF).
* **Placements**: **86 of 92 footprints pad-exact** against the v20 films. The
  6 others (`ANT1`, `ANT2`, `J9`, `BAT1`, `TP4`, `TP5`) show the *same*
  deviation when the untouched v2.0 port is measured against the v16 films, so
  they are a pre-existing footprint characteristic (their pads are drawn as
  film regions, not flashes), not a placement error — J9's 44 THT pads sit
  exactly on the v20 drill holes.
* **Copper rebuilt wholesale from the v20 films** — 1 469 items (685 F.Cu,
  437 B.Cu, 10 In1, 36 In2 traces + 301 vias), at full film precision. The
  film frame was validated first by checking the v2.0 port's own copper
  against the v16 films (701/717 tracks match exactly):
  `film_x = kicad_x − 130`, `film_y = 140 − kicad_y` for **all four** layers.
  Board-outline strokes (the films draw the outline on every copper layer)
  were excluded.
* **Nets**: resolved to 2 net-less items (both tiny isolated F.Cu stubs);
  18 unconnected pads remain. The copper doc-number text is a PCB_TEXT
  updated to `2017-3047_V20`, with the film's duplicate stroke copper removed.
* **Rules** set to the fabricated board's constraints (0.127 mm tracks,
  0.0889 mm clearance).
* Per-layer copper match against the published films: **F.Cu 1.9 %,
  B.Cu 1.6 %, In1 2.4 %, In2 3.1 % mismatch** (1-pixel tolerance at 600 dpi).

## The one blocking technical problem

DRC still reports ~583 errors, and they nearly all trace to a single cause:
**Allegro's pour regions cannot be reproduced with KiCad's polygon API as
used here.** The films encode each pour as one very large contour (842
vertices on B.Cu, 650 on In1) that weaves around every pad and via so that
the enclosed-clearance areas are *even-odd* holes. KiCad's
`SHAPE_POLY_SET` fills such a contour with **non-zero winding**, so those
clearance areas come out solid copper. The consequences are the remaining
`hole_clearance` (199), `shorting_items` (199) and `clearance` (126)
violations — copper where the fab has none.

Things already tried and ruled out: honouring `%LPC` clear-polarity regions
(they exist — 8 on B.Cu, 17 on In1 — and are now subtracted, but they only
cover a few special cases); `SHAPE_POLY_SET::Unfracture()`; splitting the
contour at repeated vertices (there are none — the contour self-*touches*
rather than revisiting exact points); and preserving duplicate vertices
through the chain builder.

What would unlock it, in rough order of preference:

1. An **IPC-2581 / ODB++ / Fabmaster export** of the Allegro v20 board. This
   gives exact copper *with net names* and removes the entire reconstruction
   problem — by far the cheapest fix if the design house or a seat of Allegro
   can produce one.
2. An **even-odd capable polygon engine** in the conversion script (e.g.
   `shapely`/Clipper driven directly with the even-odd fill rule) to convert
   each pour contour into outlines-plus-holes before handing it to KiCad.
3. Re-poured KiCad zones with hand-recovered outlines — the approach used on
   the Notecarrier-Pi v2.0 port, but there the pours were largely unchanged;
   here all ~36 pour areas would have to be reconstructed by judgement, which
   is the least defensible option.

## Also still outstanding

* Silkscreen re-lay: `changes.txt` items 2–7 (serigraphy moved off the
  headers, arrows removed from VUSB/BAT/MAIN/VIO, `VSOLAR` on J9.5 and
  `BOOT` on J9.10 added, legend un-occlusion, version text → 2.3).
* 38 `copper_edge_clearance`, 9 `courtyards_overlap`, 9 `solder_mask_bridge`
  and 3 `tracks_crossing` items to triage after the pours are fixed.
* A `notecarrier-a-v2.3` entry in `_Tools/kicad_validation/boards.yaml` (the
  Allegro film window/`original_has_outline` support added for Notecarrier-Pi
  v2.0 is reusable), then the full battery, `README.md` and
  `documentation/Porting-Notes.md`, and the root README row.

Until the pour problem is solved and the battery passes, this port must not be
committed: the repository's rule is accuracy over coverage.
