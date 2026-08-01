# ⚠️ Notecarrier-F — this port represents **v1.2**, not v1.3

**These KiCad files are a faithful port of Notecarrier-F v1.2, filed in the
v1.3 directory.** The port itself is sound; the problem is that it is labelled
as a revision it does not describe. Do not use it as the reference for the
shipped v1.3 board until the v1.2 → v1.3 delta below has been applied.

## Evidence

Compared against the two released assemblies, refdes by refdes, using each
revision's own pick-and-place file:

| Compared against | Result |
|---|---|
| **v1.2** released build (`3000-613-002`, byte `release/1.2`) | **86 of 86 placed parts present**, 0 missing, 0 board-side mismatches, 4 rotation differences of the footprint-origin kind. `B360A-13-F` in `DO-214AC_SMA` for all six diodes — exactly as in this port. `R11`/`R12` present — as in this port. |
| **v1.3** released build (`3000-653-002`, published in the parent folder) | 4 parts missing, 9 rotation differences, and the wrong part number *and* package for all six diodes. |

So every discrepancy against v1.3 is simply a v1.2 → v1.3 design change. An
earlier version of this file attributed them to porting mistakes; that was
wrong, and this correction supersedes it.

## The v1.2 → v1.3 delta that still needs applying

Agreed approach: delta-port these files in place so they describe v1.3, which is
the revision this repository publishes.

The copper change is small and localised — 2.5 % of the top layer, 7.4 % of the
bottom and 0.5 % of each inner layer (600 dpi raster comparison of
`2200-783__2023-05-31` against `2200-814__2023-07-10`).

### 1. Add the `F_VIO` regulator (sheet: Power-Rails)

| Ref | Part | Package | Side | Pick-and-place |
|---|---|---|---|---|
| `U9` | AP2139AK-3.3TRG1 (3.3 V LDO) | SOT-23-5 | Bottom | 16.097, 15.800 |
| `C33` | 1 µF | 0603 | Bottom | 18.750, 16.200 |
| `C34` | 1 µF | 0603 | Bottom | 16.125, 12.675 |

From sheet 7 of `../100275_NOTECARRIER-F_Rev-11.PDF`:

* `U9` pin 1 `VIN` **and** pin 3 `CE` → the `DS5` anode node (`Net-(DS5-A)` in
  this port — the charger output shared with `C22`–`C25`, `R13`, and `U3`
  pins 4/5)
* `U9` pin 2 `GND` → `GND`; pin 5 `VOUT` → `F_VIO`; pin 4 `NC` → unconnected
* `C33` 1 µF from the `VIN` node to `GND`; `C34` 1 µF from `F_VIO` to `GND`

### 2. Add `DS7` (sheet: Power-Input)

`DS7` = STPS3H100U, SMB, bottom, pick-and-place 11.625, 90.225. From sheet 6:
**pin 2 (anode) on `VUSB`, pin 1 (cathode) on `VMAIN`** — the Notecard USB
input diode.

### 3. Re-part the six diodes

| Refs | v1.3 part | v1.3 package | Symbol to use |
|---|---|---|---|
| `DS1`, `DS2`, `DS4`, `DS5` | FSV1045V (45 V, 10 A) | `blues-kicad-lib:TO277-3` | `blues-kicad-lib:FSV1045V` — 3 pins: 1 = A1, 2 = A2 (both anode), 3 = C |
| `DS3`, `DS6`, `DS7` | STPS3H100U (100 V, 3 A) | `blues-kicad-lib:SMB_Fv1.2` | the existing 2-pin `blues-kicad-lib:D_Schottky_Filled_Swapped` is correct |

`DS3`/`DS6` need only Value, MPN and Footprint changes. `DS1`/`DS2`/`DS4`/`DS5`
move from a 2-pin symbol to the 3-pin `FSV1045V`, so the anode net must reach
**both** pins 1 and 2 and the cathode net pin 3 — the same arrangement the
Notecarrier-Pi v2.0 port uses for its `TO277-3` diodes.

**The symbol swap is purely additive — no net changes.** `blues-kicad-lib:FSV1045V`
(*not* the mirrored `Notecarrier-Pi-local` variant) puts cathode pin 3 at local
(−3.81, 0) and anodes 1/2 at (+3.81, ±1.27). The existing
`D_Schottky_Filled_Swapped` puts its cathode pin 2 at local (−3.81, 0) and anode
pin 1 at (+3.81, 0). The cathode therefore lands on exactly the coordinate it
already occupies, so **every existing wire survives untouched**; each diode needs
only two short anode stubs plus a junction where the old anode wire meets them:

| Ref | Sheet | Placement | Anode stub (vertical) | Junction |
|---|---|---|---|---|
| `DS1` | Power-Input | (199.39, 58.42) rot 0 | x = 203.20, y 57.15 → 59.69 | (203.20, 58.42) |
| `DS2` | Power-Input | (182.88, 44.45) rot 180 | x = 179.07, y 43.18 → 45.72 | (179.07, 44.45) |
| `DS4` | Power-Input | (36.83, 55.88) rot 180 | x = 33.02, y 54.61 → 57.15 | (33.02, 55.88) |
| `DS5` | Power-Rails | (207.01, 49.53) rot 180 | x = 203.20, y 48.26 → 50.80 | (203.20, 49.53) |

Draw each stub as **two** wires meeting at the junction rather than one wire with
a junction at its midpoint — a mid-wire junction can stop a pin at the wire's
endpoint from binding (the failure diagnosed on Notecarrier-A v2.3).

Cathode orientation was confirmed against the port's own netlist rather than
assumed: `DS1` pin 2 = `VMAIN`, `DS2` pin 2 = `VMAIN`, `DS4` pin 2 = `VSOLAR`,
`DS5` pin 2 = `F_BAT` — all cathodes, and page 7 of the released schematic shows
`DS5` pin 3 → `F_BAT`, matching. `DS3` and `DS6` keep their 2-pin symbol, so
their pin-to-net mapping is untouched and needs no polarity analysis.

The library footprints are already the right geometry: `TO277-3` has copper pads
1.45 × 1.15 mm and a 4.15 × 4.65 mm tab against the shipped paste apertures of
1.4 × 1.1 and 4.1 × 4.6 (the usual ~0.05 mm paste shrink), and `SMB_Fv1.2` is
2.3 × 2.3 against 2.25 × 2.25 paste.

### 3a. The `F_VIO` rail migration — the real substance of this revision

**This is the part an earlier draft of this errata missed entirely, and it is the
reason v1.3 exists.** `U9` is not an isolated addition: v1.3 moves the
Feather-side reference rail of both level shifters off the raw battery and onto
the new regulated 3.3 V.

In v1.2 (these files today) *both* `TXS0102DCUR` level shifters take their
Feather-side supply from `F_BAT`, which is unregulated battery voltage. v1.3
introduces `F_VIO` from `U9` and moves exactly six nodes onto it. Read off
pages 4 and 7 of `../100275_NOTECARRIER-F_Rev-11.PDF`:

| Node | v1.2 net (this port) | v1.3 net |
|---|---|---|
| `U4` pin 7 `VCCB` | `F_BAT` | **`F_VIO`** |
| `C14` pin 1 (100 n, `U4` `VCCB` decoupling) | `F_BAT` | **`F_VIO`** |
| `U1` pin 3 `VCCA` | `F_BAT` | **`F_VIO`** |
| `C11` pin 1 (100 n, `U1` `VCCA` decoupling) | `F_BAT` | **`F_VIO`** |
| `R11` pin 2 (`F_SDA` pull-up) | `F_BAT` | **`F_VIO`** |
| `R12` pin 2 (`F_SCL` pull-up) | `F_BAT` | **`F_VIO`** |

Everything else on `F_BAT` stays: `DS5` pin 3 (cathode) and `MOD1R` pin 1 (the
Feather `BAT` pin). Unchanged and worth stating so they are not disturbed:
`U1` pin 7 `VCCB`, `U1` pin 6 `OE` and `R16` pin 1 remain on `F_3V3`; `U4`
pin 3 `VCCA` remains on `N_VIO`.

`F_VIO` is drawn in the released schematic with the same double-chevron
off-sheet-connector glyph as `F_BAT` and `N_VIO`. This port renders that glyph
as a **power symbol**, so `F_VIO` needs a `power_F_VIO` symbol —
`blues-kicad-lib` has `power_F_BAT`, `power_F_3V3` and `power_N_VIO` but **no
`power_F_VIO`**, so it must be added (modelled on `power_F_BAT`).

#### Where the cut has to be made

The Feather sheet's `F_BAT` connectivity was probed by renaming each naming
object in turn and re-exporting the netlist. It is **not** one node — it is four
separate wire nodes that the power symbols unify by name:

| Feather `power_F_BAT` instance | Nodes it feeds | v1.3 action |
|---|---|---|
| (137.16, 92.71) | `R11.2` | retarget to `F_VIO` |
| (144.78, 92.71) | `R12.2` | retarget to `F_VIO` |
| (151.13, 116.84) | `C11.1`, `U1.3` | retarget to `F_VIO` |
| (245.11, 102.87) | `C14.1`, `U4.7`, `MOD1R.1` (+ `DS5.2` through the hierarchy) | **mixed — needs wire surgery** |

So three of the four are a one-line retarget each. Only the fourth is real work:
`C14.1` and `U4.7` must be cut away from `MOD1R.1`/`DS5.2` and given their own
`F_VIO` connection. The `F_BAT` hierarchical labels on the Feather sheet sit at
(154.94, 160.02), (231.14, 105.41) and (30.48, 132.08), and on Power-Rails at
(248.92, 49.53).

### 4. Unfit, rename

* `R11` and `R12` (10 k) are **struck through with a red X** on page 4 of the
  released v1.3 schematic and appear in neither `BOM-3000-653-002.xlsx` nor
  `PNP-3000-653-002.pnp`. So v1.3 does **not** delete them — it leaves them on
  the drawing as unfitted. The faithful representation is therefore `(dnp yes)`
  plus exclude-from-BOM, exactly how this port already handles `J11` — *not*
  deletion, which an earlier draft of this errata wrongly called for. Their
  pull-up net still moves to `F_VIO` per the table above.
* `J11` (`CES-102-01-S-S`) is unfitted in both revisions; keep it DNP.
* **`MODL1`/`MODR1` cannot be renamed to the released `MOD1L`/`MOD1R`.** This was
  tried and reverted. KiCad derives a symbol's annotation number from the
  *trailing digits* of its reference, so `MOD1L` — which ends in a letter — is
  treated as unannotated: every netlist export then prints
  `Warning: schematic has annotation errors`, and `kicad-cli sch export bom`
  emits the designators literally as `MOD1L?` and `MOD1R?`. That is worse than a
  naming difference, so the KiCad files keep `MODL1`/`MODR1` and the mapping to
  the released BOM is recorded here:

  | This KiCad project | Released BOM `3000-653-002` | Part |
  |---|---|---|
  | `MODL1` | `MOD1L` | `CES-116-01-L-S`, 1×16 Feather header |
  | `MODR1` | `MOD1R` | `CES-112-01-L-S`, 1×12 Feather header |

### 5. Board work

Swap and place the footprints at the v1.3 pick-and-place positions, apply the
v1.2 → v1.3 copper delta on all four layers, and repair the zone fills in the
areas whose pads changed. Reconstructing the affected fill areas from the v1.3
films is preferred; refilling those zones is an accepted fallback, validated
against the shipped fab.

For this board the frames coincide conveniently:
`film_x = pnp_x`, `film_y = pnp_y`, and `board_kicad = (pnp_x + 50, 153 − pnp_y)`.

### 6. Parts that had to be built from scratch — DONE

Built and registered in project-local libraries (`Notecarrier-F-local.kicad_sym`,
`Notecarrier-F-local.pretty`, both added to `sym-lib-table`/`fp-lib-table`):

* **`SOT-23-5_Fv1.3` footprint** — five 0.6 × 1.5 mm rectangular SMD pads at
  (−0.95, −1.175), (0, −1.175), (+0.95, −1.175), (+0.95, +1.175),
  (−0.95, +1.175), taken from the shipped copper with the usual paste shrink
  (0.55 × 1.45 apertures).
* **`AP2139AK-3.3TRG1` symbol** — VIN 1, GND 2, CE 3, NC 4, VOUT 5.

`U9`'s pin numbering was **derived from the shipped fab, not assumed**: the pad at
local (−0.95, −1.175) routes via (15.15, 13.45) → (15.15, 14.62) to the left pad
of `C34` (the `F_VIO` cap), which fixes that pad as pin 5 / `VOUT`; pins 1 and 3
both route upward together, consistent with `VIN` and `CE` being tied; pin 2
routes to a `GND` via at (16.5, 18.3). This matches page 7 of the released
schematic exactly.

Still to build: **`power_F_VIO`** (see §3a) — a power symbol modelled on
`blues-kicad-lib:power_F_BAT`.

The three re-used footprints were verified against the shipped geometry rather
than trusted: `TO277-3` pads 1/2 at (±0.985, 2.75) 1.45 × 1.15 plus the
4.15 × 4.65 tab at (0, −1); `SMB_Fv1.2` pads at (±2.25, 0) 2.3 × 2.3 — and
`DS7`'s shipped copper is exactly (±2.250, 0) at 2.3 × 2.3; `C-0603_Fv1.2` pads
at (±0.725, 0) 0.8 × 0.75 rotated 270°.

### 7. Validation

Add a `notecarrier-f` entry to `_Tools/kicad_validation/boards.yaml` — gerber
diff against `../2200-814__2023-07-10.zip`, BOM against
`../BOM-3000-653-002.xlsx` (**not** the older `992-00063-B` used when this port
was made, which is why the v1.3 additions were never noticed), and the
placement gate against `../PNP-3000-653-002.pnp`. Then run the full battery.

## Progress: the schematic delta is DONE and verified; the board delta is not

Everything in §1–§4 and §6 above has been applied to the schematic sheets and
verified by re-exporting the netlist and BOM after every step. Verified state:

| Check | Result |
|---|---|
| `U9` | pin 1 `VIN` **and** pin 3 `CE` on `Net-(DS5-A1)`, pin 2 `GND` on `GND`, pin 5 `VOUT` on `F_VIO`, pin 4 `NC` open with a no-connect marker |
| `C33` / `C34` | `Net-(DS5-A1)` → `GND` / `F_VIO` → `GND` |
| `DS7` | pin 1 (cathode) `VMAIN`, pin 2 (anode) `VUSB` |
| `DS1`, `DS2`, `DS4`, `DS5` | 3-pin `FSV1045V`; both anode pins on the original anode net, pin 3 on the original cathode net, all four confirmed individually |
| `DS3`, `DS6` | `STPS3H100U` / `SMB_Fv1.2`, pin-to-net mapping untouched |
| `F_VIO` | `C11.1 C14.1 C34.1 R11.2 R12.2 U1.3 U4.7 U9.5` — exactly the intended set |
| `F_BAT` | `DS5.2 MOD1R.1` only |
| BOM refdes | 92 fitted symbols against 96 released designators; the only differences are `MODL1`/`MODR1` vs `MOD1L`/`MOD1R` (see §4), the non-electrical `DOC1`/`PCB1` rows, and `J9`/`J10` (below) |
| ERC | no new violation *class* versus the v1.2 baseline; the count rises only by the same pre-existing "configuration does not include the symbol library 'Device'/'power'" artifact that every other symbol already produces in a CLI environment |
| Annotation | clean — netlist export emits no warning |

**The board has not been touched yet, so these files are still not a usable
v1.3 deliverable.** The schematic now describes v1.3 while `Notecarrier-F.kicad_pcb`
still describes v1.2, which means the two are deliberately out of step until §5
is done. Do not run "Update PCB from Schematic" as a shortcut — it would place
the new parts at arbitrary positions and rip up the preserved zone fills.

### Two pre-existing discrepancies found along the way (not part of this delta)

Both predate the delta and are recorded here rather than silently changed:

* **`J9` and `J10` are DNP in this port but appear in the released BOM.** They are
  through-hole headers and absent from the pick-and-place, so the placement gate
  cannot arbitrate. Needs a decision from whoever owns the build.
* **56 MPN differences** between the port and `BOM-3000-653-002.xlsx`, spread
  across the whole board rather than concentrated in the delta — e.g. `C10`
  carries `CC0402KRX7R7BB104` where the released BOM buys
  `GCM155R71C104KA55D`. These are design-MPN-versus-purchasing-MPN divergences
  inherited from the Altium sources; the released BOM is authoritative for what
  was actually built. Reconciling them is a separate task from this revision
  delta and should not be folded into it.

## Already fixed

The board's 54 net-less 0.6 mm copper patches (footprint
`weird-no-fill-via_Fv1.2`) sit inside `GND` copper and have been assigned the
`GND` net they belong to. DRC went from 171 errors to 0 with no change to any
copper geometry.

## While this errata stands

The port's KiCad pages are excluded from the RAG extract
(`_Tools/extract_for_rag/extract.py`, `EXCLUDE_PATH`) so that v1.2 component
data is not served as v1.3. Its BOM and schematic-PDF pages come from the
published documents and are still indexed. Remove that exclusion once the delta
is applied.
