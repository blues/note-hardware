Blues Notecarrier-A Series Solar JST Input
==========================================

The JST input powers the on-board
[Texas Instruments bq24210 Li-Ion Battery Solar Charger IC](https://www.ti.com/lit/ds/symlink/bq24210.pdf)
through an
[ON Semiconductor FSV1045V Schottky rectifier](https://www.onsemi.com/pdf/datasheet/fsv1045v-d.pdf).

Section 7 of the charger datasheet states that the Absolute Maximum Ratings of
the `VBUS` input are -0.3V and 20V. However, these are merely the limits of the
device beyond which damage will occur and do not inform the Blues customer
recommendations below.

Section 7.3 of the charger datasheet gives a `VBUS` Voltage Range of 3.5V - 18V,
and a `VBUS` Operating Voltage Range of 3.5 to 7V. Accounting for the forward
voltage drop across the rectifier, these ranges will be used to recommend the
absolute maximums and operating range of the Notecarrier `SOLAR` input.

The **ELECTRICAL CHARACTERISTICS** table of the rectifier reports the Forward
Voltage Drop under various conditions. Conservatively ignoring the conditions
and just picking the minimum and maximum values gives a range of 0.18V - 0.44V.

Combining this information in the most conservative way gives the follow values
for our `SOLAR` input:

* `VSOLAR` Absolute Maximum Ratings
  * Minimum: 0V
  * Maximum: 18V + 0.18V = 18.18V
  * This is the allowable voltage range, although the battery is unlikely to
  charge outside of the Operating Range calculated below.
* `VSOLAR` Charging Range
  * Minimum: 3.5V + 0.44V = 3.94V
  * Maximum: 7V + 0.18V = 7.18V
  * This is the voltage range which will keep the charger in the domain where it
  is capable of charging a battery.

But Will It Charge?
-------------------

Section 10 of the charger datasheet (Power Supply Recommendations) reads in its
entirety:

> In order for the IC to charge a battery, the power source at VBUS must be
larger than the undervoltage lockout threshold of 3.3 V typical and the battery
voltage, V(BAT) plus 200 mV typical to prevent SLEEP mode but less than the OVP
threshold of 7.5 V typical. The input power source can be a low impedance USB
port or wall adapter or a high impedance solar panel if the VBUS_DPM feature if
appropriately configured.

Our recommended Operating Range avoids under-voltage lockout since we specify at
least 3.5V and the maximum UVLO level is 3.45V per Table 7.5 (Electrical
Characteristics).

Our recommended Operating Range avoids the the over-voltage protection threshold
since we specify no more that 7V and the minimum OVP threshold is 7.3V per Table
7.5 (Electrical Characteristics).

Table 7.5 (Electrical Characteristics) states that the Input Power Good
threshold is 250mV +/- 50mV above the present battery level. Accounting for the
typical drop across the rectifier at 25&deg;C, the charger is expected to enter
Charge Mode whenever the solar panel generates a voltage that is typically 0.25V
\+ 0.28V = 0.53V above VBAT. Again accounting for the rectifier, if the `SOLAR`
input voltage rises above 7.3V + 0.28V = 7.58V (typical), the charger will go
into over-voltage protection mode until the `SOLAR` input falls about 200mV
below the level at which it entered OVP - typically around 7.38V.

What About Airnote?
-------------------

For reference, our
[Airnote solar panel](https://waf-e.dubudisk.com/anysolar.dubuplus.com/techsupport@anysolar.biz/O18Adzu/DubuDisk/www/Gen2/SM301K09L%20DATA%20SHEET%20202007.pdf)
has a maximum open-circuit voltage of 6.22V. Thus, it will never put the charger
into over-voltage protection and will always charge its LiPo battery whenever it
exceeds `VBAT` by 0.53V (typical).
