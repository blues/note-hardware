# ⚠️ Notecarrier-F v1.3 KiCad port — errata

**The power section of this port does not match the shipped v1.3 board.** The
schematic and board are missing parts that the released design has, and six
diodes carry the wrong part number *and* the wrong package. Do not use this port
as the reference for the power input / power rails until the items below are
fixed.

The rest of the port (Notecard connection, Feather connection, IO, and the
remainder of the board) is unaffected by these findings.

## How this was established

The design-house Altium sources (`byte/ByteLab/Notecarrier-F/dev/`) are the
authority, and they agree with the published schematic PDF
(`../100275_NOTECARRIER-F_Rev-11.PDF`), the published BOM
(`../BOM-3000-653-002.xlsx`), the published pick-and-place
(`../PNP-3000-653-002.pnp`) and the published fabrication package
(`../2200-814__2023-07-10.zip`). Every item below was cross-checked against at
least three of those five.

## 1. A whole regulator circuit is missing

`U9`, `C33` and `C34` are absent from both the port's schematic and its board.
They are present in the Altium source (`07_POWER-RAILS.SchDoc` contains the
`AP2139`), in the released BOM, in the released pick-and-place, and their pads
are physically present in the shipped bottom copper, mask and paste — five pads
at the SOT-23-5 position and two each for the 0603s, at exactly the
pick-and-place coordinates.

| Ref | Part | Package | Side | Pick-and-place position |
|---|---|---|---|---|
| `U9` | AP2139AK-3.3TRG1 (3.3 V LDO) | SOT-23-5 | Bottom | 16.097, 15.800 |
| `C33` | 1 µF | 0603 | Bottom | 18.750, 16.200 |
| `C34` | 1 µF | 0603 | Bottom | 16.125, 12.675 |

Circuit, from sheet 7 of the released schematic:

* `U9` pin 1 `VIN` **and** pin 3 `CE` → the `DS5` anode node (`Net-(DS5-A)` in
  this port — the charger output shared with `C22`–`C25`, `R13` and `U3` pins
  4/5)
* `U9` pin 2 `GND` → `GND`
* `U9` pin 5 `VOUT` → `F_VIO`
* `U9` pin 4 `NC` → not connected
* `C33` 1 µF from the `VIN` node to `GND`
* `C34` 1 µF from `F_VIO` to `GND`

## 2. `DS7` is missing

`DS7` (STPS3H100U, SMB, bottom side, pick-and-place 11.625, 90.225) is absent
from the port. From sheet 6 of the released schematic it is the Notecard USB
input diode: **pin 2 (anode) on `VUSB`, pin 1 (cathode) on `VMAIN`**.

Note the consequence for the port as it stands: `VUSB` and `VMAIN` are wired
without this diode, so the port does not represent how the shipped board feeds
`VMAIN` from USB.

## 3. All six diodes have the wrong part and the wrong package

The port gives every diode `B360A-13-F` in a `DO-214AC SMA` footprint. The
string `B360A` does not appear anywhere in the Altium source. The released
design uses:

| Refs | Part | Package | Pads |
|---|---|---|---|
| `DS1`, `DS2`, `DS4`, `DS5` | FSV1045V (45 V, 10 A) | **TO277-3** | 3 (incl. a 4.1 × 4.6 mm tab) |
| `DS3`, `DS6`, `DS7` | STPS3H100U (100 V, 3 A) | **SMB** | 2 (2.25 × 2.25 mm) |

This is a physical mismatch, not just metadata: the port's SMA footprints have
two pads where the shipped board has three for `DS1`/`DS2`/`DS4`/`DS5`, and the
`DS3`/`DS6` pads are the wrong size. Confirmed by counting paste apertures in
the shipped `…GBP` at each diode's pick-and-place position.

The port's own Porting-Notes note that the `TO277-3` footprint "is not in the
project pcblib … which is not available", which is the likely origin of the
substitution.

## 4. Smaller discrepancies to resolve alongside

* The port has `R11`, `R12` (10 k, on `F_BAT`) and `J11` (`CES-102-01-S-S`,
  flagged DNP) which the released BOM does not list.
* Refdes naming differs: the port uses `MODL1`/`MODR1` where the released BOM
  and pick-and-place use `MOD1L`/`MOD1R`.
* Against the released pick-and-place, 9 parts differ in rotation
  (`C26`, `C29`, `C31`, `DS1`–`DS5`, `R15`). Some of that is footprint-origin
  convention rather than a real difference, but the `DS*` entries should be
  re-checked once the diode footprints are corrected.
* The port's BOM was validated at creation against **992-00063-B**, an older
  Blues BOM whose 1 µF row lists only `C1, C2`. That is why the missing
  `C33`/`C34` were not caught. Future comparisons should use the
  `BOM-3000-653-002.xlsx` published alongside this port.

## What a fix requires

Adding the parts to the schematic is straightforward with the wiring above.
The board work is the substantial part: build `TO277-3` and `SMB` footprints
from the shipped paste/copper geometry, swap the six diodes onto them, place
`U9`/`C33`/`C34`/`DS7` at the pick-and-place coordinates, and re-route the
affected copper so it matches the shipped films. That is a partial re-port of
the power section rather than an edit, and it should be validated with the same
gerber-diff and placement gates the harness runs
(`_Tools/kicad_validation/run_all.py`).

## Fixed already

The board's 54 net-less 0.6 mm copper patches (footprint
`weird-no-fill-via_Fv1.2`) were assigned the `GND` net they sit in. That cleared
109 `shorting_items` and 54 `hole_clearance` violations without changing any
copper geometry — DRC now reports 0 errors. See the commit that added this file.
