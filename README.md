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
comparison, and per-layer gerber raster diffs — see the `validation/` folder
and `documentation/Porting-Notes.md` inside each port).

|Product|KiCad version|Location|
|---|---|---|
|Notecarrier-A v2.0|KiCad 7|[Notecarrier-A/v2.0/KiCad_format](Notecarrier-A/v2.0/KiCad_format)|
|Notecarrier-B v2.1|KiCad 7|[_Legacy Hardware/Notecarrier-B/v2.1/KiCad_format](_Legacy%20Hardware/Notecarrier-B/v2.1/KiCad_format)|
|Notecarrier-CX v1.7|KiCad 9|[Notecarrier-CX/v1.7/KiCad_format](Notecarrier-CX/v1.7/KiCad_format)|
|Notecarrier-F v1.3|KiCad 7|[Notecarrier-F/v1.3/KiCad_format](Notecarrier-F/v1.3/KiCad_format)|
|Notecarrier-Pi v1.1|KiCad 7|[Notecarrier-Pi/v1.1/KiCad_format](Notecarrier-Pi/v1.1/KiCad_format)|
|Notecarrier-XI v1.4|KiCad 9|[Notecarrier-XI/v1.4/KiCad_format](Notecarrier-XI/v1.4/KiCad_format)|
|Cygnet v1.2|KiCad 9|[Cygnet/v1.2/KiCad_format](Cygnet/v1.2/KiCad_format)|
|Mojo v1.1|KiCad 9|[Mojo/v1.1/KiCad_format](Mojo/v1.1/KiCad_format)|
|Scoop v1.0|KiCad 9|[Scoop/v1.0/KiCad_format](Scoop/v1.0/KiCad_format)|

Some products do not have a KiCad port, deliberately:

* **Notecarrier-X / -XS / -XM / -XP** — the exact Altium sources matching the
  published fabrication packages are not available, and a conversion from a
  near-miss source state could not be proven accurate against the shipped
  gerbers, so no port is published (accuracy over coverage).
* **Swan v3.0 and Notecarrier-Pi v2.0** — authored in OrCAD/Allegro, for which
  no KiCad importer exists. (The Notecarrier-Pi v1.1 KiCad port remains the
  canonical KiCad reference for the Pi form factor.)
* **Notecarrier-A v2.3** — a PCB-only Allegro revision; the v2.0 KiCad port
  remains the canonical KiCad reference for the A form factor.

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
