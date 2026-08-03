# note-hardware

This repository contains open hardware designs for Notecarriers and other Notecard-related hardware available through our [online store](https://shop.blues.com).

## Designs

|Item|Description|Contents|
|---|---|---|
|[Notecard](Notecard)|Device-to-cloud data pump|Dimensioned drawings and 3D models|
|[Notecarrier A](Notecarrier-A)|Carrier for battery- and solar-powered wireless applications|Full electrical and mechanical design, plus KiCad|
|[Notecarrier CX](Notecarrier-CX)|Carrier with an onboard STM32L433 MCU|Full electrical and mechanical design, plus KiCad|
|[Notecarrier F](Notecarrier-F)|Carrier for Adafruit Feather-compatible hosts|Full electrical and mechanical design, plus KiCad|
|[Notecarrier Pi](Notecarrier-Pi)|Carrier with a Raspberry Pi-compatible hardware interface|Full electrical and mechanical design, plus KiCad|
|[Notecarrier X](Notecarrier-X)|Small form-factor carrier with Qwiic and ESLOV ports|Full electrical and mechanical design, plus KiCad|
|[Notecarrier XI](Notecarrier-XI)|Companion carrier for Starnote for Iridium|Full electrical and mechanical design, plus KiCad|
|[Notecarrier XM](Notecarrier-XM)|Minimal small form-factor carrier, without an external SIM slot|Full electrical and mechanical design, plus KiCad|
|[Notecarrier XP](Notecarrier-XP)|Companion carrier for the Notecard XP|Full electrical and mechanical design|
|[Notecarrier XS](Notecarrier-XS)|Ultra-compact small form-factor carrier|Full electrical and mechanical design, plus KiCad|
|[Cygnet](Cygnet)|STM32L433 in Adafruit Feather form factor|Full electrical design, plus KiCad|
|[Swan](Swan)|STM32L4R5 in Adafruit Feather form factor|Full electrical and mechanical design|
|[Starnote](Starnote)|Satellite Notecard companion|3D models|
|[Scoop](Scoop)|Supercapacitor backup power for Notecard applications|Full electrical and mechanical design, plus KiCad|
|[Mojo](Mojo)|Energy-usage measurement for battery-powered systems|Full electrical and mechanical design, plus KiCad|
|[Airnote](Airnote)|Air quality monitor powered by Notecard|Enclosure 3D models and drawings|
|[Wireless for OPTA](Wireless%20for%20OPTA)|Cellular and Wi-Fi connectivity for Arduino Opta|3D model|
|[3D Models for Enclosures](3D%20Models%20for%20Enclosures)|Community-contributed enclosures, not supported by Blues|Printable STL and STEP models|
|[_Legacy Hardware](_Legacy%20Hardware)|Components and designs no longer sold|Assorted design files|

Each directory has its own README describing the available versions, the design
file formats, and any caveats that apply to that board.

## More Information

Various other resources that may be useful as you develop hardware around Notecard and Notecarriers.

### Application Notes

* [Antenna Guide](https://dev.blues.io/datasheets/application-notes/antenna-guide/)
* [Blues Security, Reliability, and Governance](https://dev.blues.io/datasheets/application-notes/blues-security-reliability-and-governance/)
* [Designing for XP Variants of the Blues Notecard](https://dev.blues.io/datasheets/application-notes/designing-for-xp-variants-of-the-blues-notecard/)
* [Low-Power Hardware Design](https://dev.blues.io/datasheets/application-notes/low-power-hardware-design/)
* [Notecard Carrier Board Design Guide](https://dev.blues.io/datasheets/application-notes/notecard-carrier-board-design-guide/)
* [Notecard Real-Time Clock](https://dev.blues.io/datasheets/application-notes/notecard-real-time-clock/)
* [Notecarrier A Series Solar JST Input](https://dev.blues.io/datasheets/application-notes/notecarrier-a-series-solar-jst-input/)
* [Starnote Carrier Board Design Guide](https://dev.blues.io/datasheets/application-notes/starnote-carrier-board-design-guide/)

### Tooling

The [_Tools](_Tools) directory holds the utilities used to maintain this
repository, including the KiCad validation harness that checks the KiCad ports
against the shipped fabrication packages.

### Learn more about Blues, Notecard, and Notehub

* [blues.com](https://blues.com)
* [notehub.io](https://notehub.io)
* [dev.blues.io](https://dev.blues.io)

## Contributing

We love issues, fixes, and pull requests from everyone. By participating in this
project, you agree to abide by the Blues Inc.
[code of conduct](CODE_OF_CONDUCT.md).

For details on contributions we accept and the process for contributing, see our
[contribution guide](CONTRIBUTING.md).

## License

Copyright (c) 2026 Blues Inc. Released under the MIT license. See
[LICENSE](LICENSE) for details.
