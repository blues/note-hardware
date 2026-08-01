# note-hardware

This repository contains open hardware designs for Notecarriers and other Notecard-related hardware available through our [online store](https://shop.blues.com).

## Designs

|Item|Description|Contents|
|---|---|---|
|[Notecard](Notecard)|Device to cloud data pump|Mechanical design files|
|Notecarrier|Notecard daughter boards | Full electrical and mechanical design|
|[Starnote](Starnote)|Satellite Notecard companion|Mechanical design files|
|[Cygnet](Cygnet)| STM32 in Adafruit Feather form| Full electrical and mechanical design|
|[Swan](Swan)| STM32 in Adafruit Feather form| Full electrical and mechanical design|
|[Airnote](Airnote)|Air quality monitor powered by Notecard|Mechanical design files|
|[_Legacy Hardware](_Legacy%20Hardware)|Components and designs no longer sold| Assorted design files

## KiCad Design Files

The original electrical designs in this repository were authored in Altium
Designer or OrCAD/Allegro. For a number of products a complete
[KiCad](https://www.kicad.org/) equivalent of the latest published version is
also provided in a `KiCad_format/` folder alongside the original design files.
Each KiCad port was converted from the original sources and validated against
the shipped fabrication outputs (ERC/DRC, BOM comparison, netlist/connectivity
comparison, per-layer gerber raster diffs, and — where the product ships a
pick-and-place file — a placement comparison against the released build; see the
`validation/` folder and `documentation/Porting-Notes.md` — named
`PortingNotes.md` in the four pre-2026 ports — inside each port).

|Product|KiCad version|Location|
|---|---|---|
|Notecarrier-A v2.0|KiCad 9|[Notecarrier-A/v2.0/KiCad_format](Notecarrier-A/v2.0/KiCad_format)|
|Notecarrier-B v2.1|KiCad 9|[_Legacy Hardware/Notecarrier-B/v2.1/KiCad_format](_Legacy%20Hardware/Notecarrier-B/v2.1/KiCad_format)|
|Notecarrier-CX v1.7|KiCad 9|[Notecarrier-CX/v1.7/KiCad_format](Notecarrier-CX/v1.7/KiCad_format)|
|Notecarrier-F v1.3 ‡|KiCad 9|[Notecarrier-F/v1.3/KiCad_format](Notecarrier-F/v1.3/KiCad_format)|
|Notecarrier-Pi v1.1|KiCad 9|[Notecarrier-Pi/v1.1/KiCad_format](Notecarrier-Pi/v1.1/KiCad_format)|
|Notecarrier-Pi v2.0|KiCad 9|[Notecarrier-Pi/v2.0/KiCad_format](Notecarrier-Pi/v2.0/KiCad_format)|
|Notecarrier-XI v1.4|KiCad 9|[Notecarrier-XI/v1.4/KiCad_format](Notecarrier-XI/v1.4/KiCad_format)|
|Notecarrier-X v1.2 †|KiCad 9|[Notecarrier-X/v1.2/KiCad_format](Notecarrier-X/v1.2/KiCad_format)|
|Notecarrier-XS v1.2 †|KiCad 9|[Notecarrier-XS/v1.2/KiCad_format](Notecarrier-XS/v1.2/KiCad_format)|
|Notecarrier-XM v1.2 †|KiCad 9|[Notecarrier-XM/v1.2/KiCad_format](Notecarrier-XM/v1.2/KiCad_format)|
|Cygnet v1.2 §|KiCad 9|[Cygnet/v1.2/KiCad_format](Cygnet/v1.2/KiCad_format)|
|Mojo v1.1|KiCad 9|[Mojo/v1.1/KiCad_format](Mojo/v1.1/KiCad_format)|
|Scoop v1.0|KiCad 9|[Scoop/v1.0/KiCad_format](Scoop/v1.0/KiCad_format)|

One further port is **unfinished and not usable** — it is present only so the
work is not lost:

|Product|State|Location|
|---|---|---|
|Notecarrier-A v2.3|⚠️ **work in progress — do not use**|[Notecarrier-A/v2.3/KiCad_format](Notecarrier-A/v2.3/KiCad_format)|

Its schematic is complete and ERC-clean, but the board's copper pours and
silkscreen are unfinished and DRC is not clean, so it is **not** a KiCad
equivalent of the v2.3 board. Use the complete
[Notecarrier-A v2.0](Notecarrier-A/v2.0/KiCad_format) port as the KiCad
reference for the A form factor. See
[`STATUS-INCOMPLETE.md`](Notecarrier-A/v2.3/KiCad_format/STATUS-INCOMPLETE.md)
for exactly what is verified, what remains, and what would unlock it.

‡ The Notecarrier-F KiCad port has **errata**: it is part-way through a
v1.2 → v1.3 delta port, so it currently holds a **v1.3 schematic and a v1.2
PCB**. The schematic now carries the v1.3 changes — the 3.3 V regulator circuit
(`U9`, `C33`, `C34`), the USB input diode `DS7`, the six re-parted diodes, and
the `F_VIO` rail that moves both level shifters off raw battery voltage — and
each was verified against the released schematic and BOM. The board has not been
updated yet, so the two are deliberately out of step.
The original diagnosis came from comparing the port against both revisions'
pick-and-place files: 86/86 parts matched v1.2, while 4 were missing against
v1.3. What has been applied so far, what remains, and why the board must not be
updated from the schematic automatically are all set out in
[`Notecarrier-F/v1.3/KiCad_format/ERRATA.md`](Notecarrier-F/v1.3/KiCad_format/ERRATA.md).

§ The Cygnet KiCad port has **one unproven layer**. Inner layer 1 (`In1_Cu`)
carries roughly fifty annular rings that the shipped Gerbers do not — 10.5 % of
the drawn area — so its fabrication equivalence on that layer is not proven and
its gerber gate fails. Every other layer matches, and the schematic, netlist and
BOM are exact, so the port is usable as an electrical reference; treat the inner
copper as unverified until
[the porting notes](Cygnet/v1.2/KiCad_format/documentation/Porting-Notes.md)
say otherwise.

† The Notecarrier-X, -XS and -XM ports carry a **source-fidelity
disclaimer**: they were made from the closest available design-house sources
rather than the exact released v1.2 snapshots, with the differences reviewed
and documented in each port's `documentation/Porting-Notes.md` (silk version
text on all three; the production-DNP GPS jumper on the opposite side on
X/XS; several rerouted signals on XM). All three have since been checked
against the **released build's** pick-and-place file — every placed part is on
the same board side at the same rotation as the boards that were actually
built — which narrows the disclaimer to silkscreen, the unpopulated jumper's
side, and routing geometry. Fully retiring it needs a netlist from the released
snapshot, which does not exist anywhere in the Blues organisation's
repositories.

Some products do not have a KiCad port, deliberately:

* **Notecarrier-XP** — the exact Altium sources matching the published
  fabrication package are not available, and the nearest source state
  differs electrically from the shipped board (an entire DNP subcircuit and
  a grounded presence-detect strap), so no port is published (accuracy over
  coverage).
* **Swan v3.0** — authored in OrCAD/Allegro, for which no KiCad importer
  exists. (The Notecarrier-Pi v2.0 port shows that an Allegro board *can* be
  delta-ported when a validated KiCad base and the full fab package exist;
  Swan has no prior KiCad port to delta from.)

(The unfinished Notecarrier-A v2.3 port listed above is a separate case: it is
in progress rather than deliberately skipped.)

## More Information

Various other resources that may be useful as you develop hardware around Notecard and Notecarriers.

### Hardware Application Notes

* [Notecarrier-A Series Solar JST Input](https://dev.blues.io/datasheets/application-notes/notecarrier-a-series-solar-jst-input/)
* [Notecard Host System Design Guide](https://dev.blues.io/datasheets/application-notes/notecard-host-system-design-guide/)
* [Low-Power Hardware Design](https://dev.blues.io/datasheets/application-notes/low-power-hardware-design/)
* [Designing for XP Variants of the Blues Notecard](https://dev.blues.io/datasheets/application-notes/designing-for-xp-variants-of-the-blues-notecard/)

### Learn more about Blues, Notecard, and Notehub

* [blues.com](https://blues.com)
* [notehub.io][Notehub]
* [dev.blues.com](https://dev.blues.com)

## Contributing

We love issues, fixes, and pull requests from everyone. By participating in this
project, you agree to abide by the Blues Inc.
[code of conduct](CODE_OF_CONDUCT.md).

For details on contributions we accept and the process for contributing, see our
[contribution guide](CONTRIBUTING.md).

## License

Copyright (c) 2026 Blues Inc. Released under the MIT license. See
[LICENSE](LICENSE) for details.

[blues]: https://blues.com
[notehub]: https://notehub.io
[archive]: https://github.com/blues/note-arduino/archive/master.zip
[code of conduct]: https://blues.github.io/opensource/code-of-conduct
[Notehub]: https://notehub.io
