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

The library footprints are already the right geometry: `TO277-3` has copper pads
1.45 × 1.15 mm and a 4.15 × 4.65 mm tab against the shipped paste apertures of
1.4 × 1.1 and 4.1 × 4.6 (the usual ~0.05 mm paste shrink), and `SMB_Fv1.2` is
2.3 × 2.3 against 2.25 × 2.25 paste.

### 4. Remove, rename

* Remove `R11` and `R12` (10 k on `F_BAT`) — v1.2 parts that v1.3 drops.
* `J11` (`CES-102-01-S-S`) is unfitted in both revisions; confirm and keep the
  DNP flag or drop it with `R11`/`R12`.
* Rename `MODL1` → `MOD1L` and `MODR1` → `MOD1R` to match the released BOM and
  pick-and-place.

### 5. Board work

Swap and place the footprints at the v1.3 pick-and-place positions, apply the
v1.2 → v1.3 copper delta on all four layers, and repair the zone fills in the
areas whose pads changed. Reconstructing the affected fill areas from the v1.3
films is preferred; refilling those zones is an accepted fallback, validated
against the shipped fab.

For this board the frames coincide conveniently:
`film_x = pnp_x`, `film_y = pnp_y`, and `board_kicad = (pnp_x + 50, 153 − pnp_y)`.

### 6. Only two things have to be built from scratch

An `AP2139AK-3.3TRG1` symbol (5 pins: VIN, GND, CE, NC, VOUT) and a SOT-23-5
footprint taken from the shipped geometry (five 0.6 × 1.5 mm copper pads,
0.55 × 1.45 paste). Everything else already exists in `blues-kicad-lib`.

### 7. Validation

Add a `notecarrier-f` entry to `_Tools/kicad_validation/boards.yaml` — gerber
diff against `../2200-814__2023-07-10.zip`, BOM against
`../BOM-3000-653-002.xlsx` (**not** the older `992-00063-B` used when this port
was made, which is why the v1.3 additions were never noticed), and the
placement gate against `../PNP-3000-653-002.pnp`. Then run the full battery.

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
