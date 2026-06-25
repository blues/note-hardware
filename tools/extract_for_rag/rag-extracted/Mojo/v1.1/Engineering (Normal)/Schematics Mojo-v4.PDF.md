---
product: Mojo
version: v1.1
doc_type: schematic
source_file: Mojo/v1.1/Engineering (Normal)/Schematics Mojo-v4.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Mojo — SCHEMATIC (v1.1)

_Source: `Mojo/v1.1/Engineering (Normal)/Schematics Mojo-v4.PDF`_

## Page 1

# Cover Sheet

## Project
- Blues Wireless
- Mojo 1.1
- v4

## Components
- No component reference designators visible on this page.

## Connectors
- No connectors visible on this page.

## Named Nets / Signals
- No named nets or signals visible on this page.

## Version History
- **v1 (2024-03-11)**
  - Initial Version
- **v2 (2024-03-21)**
  - Add 22K I2C SDA/SCL pullups
  - 3v3 labeled as "VIO" in serigraphy
- **v3 (2024-04-15)**
  - Changed sense resistor to 0R250.
  - Reposition Vbat/Vout. Updated layout as needed.
  - Moved GPIO test point to bottom and tented.
  - Serigraphy changes.
  - Updated battery connector to preferred supplier PN
- **v4 (2024-06-07)**
  - Made backside serigraphy bigger.

## Variants
- **Normal** — Normal product configuration

## Project ID Field
- Label: `+PROJECTID`
- Project ID: Mojo 1.1

## Copyright Field
- Label: `+COPYRIGHT`
- Copyright Notice: Copyright © 2024 Blues Wireless

## Title Block
- Title: blank
- Size: B
- Number: 1.
- Revision: blank
- Date: 6/7/2024
- Time: 3:59:23 PM
- Sheet: 1 of 3
- File: Cover Sheet.SchDoc
- Company: ToyBuilder Labs
- Address: 1100 S. Garfield Avenue, Alhambra, California 91801
- Phone: +1 (626) 808-4010

## Page 2

## Components

- **IC1**: LTC2959IDDB#TRMPBF
- **R1**: 250mΩ
- **R2**: RC0603FR-0722KL
- **R3**: RC0603FR-0722KL
- **C1**: 1uF, 0805, 10%
- **C2**: 1uF, 0805, 10%
- **C3**: 0.47 µF
- **Z1**: Test Point
- **MH1**: M2
- **MH2**: M2
- **MH3**: M2
- **MH4**: M2
- **LOGO**: Logo
- **LOGO-BACK**: Logo

## Connectors

- **J1**: 20404, labeled **BAT**
  - Pin 1: VBAT
  - Pin 2: GND

- **J2**: Header 2-Pin, 0.100 in; shown crossed out
  - Pins connected to: VBAT, GND

- **J3**: Header 2-Pin, 0.100 in; shown crossed out
  - Pins connected to: VLOAD, GND

- **J4**: 20404, labeled **LOAD**
  - Pin 1: VLOAD
  - Pin 2: GND

- **J5**: QWIIC SM04B-SRSS-TB(LF)(SN)
  - Pin 1: GND
  - Pin 2: 3V3
  - Pin 3: SDA
  - Pin 4: SCL

- **J6**: QWIIC SM04B-SRSS-TB(LF)(SN)
  - Pin 1: GND
  - Pin 2: 3V3
  - Pin 3: SDA
  - Pin 4: SCL

- **J7**: Header 2-Pin, 0.100 in; shown crossed out
  - Pins connected to: 3V3, GND

- **J8**: Header 3-Pin, 0.100 in; shown crossed out
  - Pins connected to: SCL, SDA, GND

## IC1 Pin Labels

- Pin 1: VDD
- Pin 2: SENSEP
- Pin 3: CFP
- Pin 4: CFN
- Pin 5: SENSEN
- Pin 6: SCL
- Pin 7: SDA
- Pin 8: GPIO
- Pin 9: VREG
- Pin 10: GND_1
- Pin 11: GND_2

## Named Nets / Signals

- 3V3
- GND
- VBAT
- VLOAD
- SDA
- SCL
- GPIO

## Notes

- I2C Address: `1100011b`
- Do not solder exposed pad
- Mounting Headers
- Mounting Screws

## Title Block

- Size: B
- Number: 2.
- Revision: v4
- Date: 6/7/2024
- Time: 3:59:23 PM
- Sheet: 2 of 3
- Status: Normal
- File: Mojo.SchDoc
- Company: ToyBuilder Labs
- Address: 1100 S Garfield Avenue, Alhambra, CA 91801
- Phone: (626) 808-4010

## Page 3

## Components

- No component reference designators are visible on this page.
- Parts/components mentioned without visible reference designators:
  - LTC2959 sensor
  - 0.050 Ohm sensor, 2 pcs, datasheet reference value with 533 nAh LSB

## Connectors

- No connectors are visible on this page.
- No connector pin labels are visible on this page.

## Named Nets / Signals / Electrical Terms

- VDD
- POR
- GPIO
- ALERT
- Charge Complete
- ADC
- ACR
- VSENSE
- VSENSEP
- VSENSEN
- SENSEP
- SENSEN
- V(sensep)
- tPULSE
- RSENSE

## Design Notes

- Power supply voltages and currents
- Other design calculations
- Board bringup details
- Test points & Expected waveform / measurements

## Notes on LTC2959 Sensor

- Sensor has 50 mV Sense Range
- `V = IR :: I(range) = V(range) / R`
- Resistor / Current Sense Range: lower range = finer resolution current sensing

| Resistor | Current Sense Range |
|---|---:|
| 0.500 Ohm | 0.1 A |
| 0.250 Ohm | 0.2 A |
| 0.100 Ohm | 0.5 A |
| 0.050 Ohm | 1.0 A |
| 0.050 Ohm | 1.0 A |
| 0.025 Ohm | 2.0 A |
| 0.010 Ohm | 5.0 A |
| 0.005 Ohm | 10.0 A |
| 0.025 Ohm | 20.0 A |
| 0.001 Ohm | 50.0 A |
| blank | blank |

- 0.050 Ohm sensor, there are 2 pcs, is the datasheet's reference value with 533 nAh LSB.
- V(sensep) has 65 V max limit, but as a practical matter, you are limited by your battery's ability to supply voltage.

## Power-Up Sequence

- When VDD rises above a threshold of approximately 1.45 V, the LTC2959 generates an internal power-on reset (POR) signal that sets all registers to their default state.
- In the default state, the coulomb counter is active while the multi-purpose ADC operates in sleep mode.
- The accumulated charge register is set to mid-scale, `80000000h`, and all ADC channel outputs are set to `0000h`.
- All threshold registers and the min-max tracking registers are set to their default values.
- The min/max tracking registers of the ADC will update upon completion of the first ADC conversion.
- The GPIO pin is configured as an analog input.
- The ALERT and Charge Complete functionalities are not enabled at startup.

## Coulomb Counter Table

| Symbol | Parameter | Condition | Values | Units |
|---|---|---|---|---|
| VSENSE | Sense Voltage Differential Input Range | VSENSEP − VSENSEN | ±50 | mV |
| TCE | Total Charge Error, Note 4 | 10 mV ≤ \|VSENSE\| ≤ 50 mV Continuously | 0.1, ±1 | % |
| TCE | Total Charge Error, Note 4 | 1 mV ≤ \|VSENSE\| ≤ 10 mV Continuously | 0.2, ±2 | % |
| TCE | Total Charge Error, Note 4 | 10 mV ≤ \|VSENSE\| ≤ 50 mV Pulses with tPULSE > 1 ms | 1 | % |
| VOS | Offset Voltage | — | ±1, ±10 | µV |
| RIDR | Differential Input Resistance Across SENSEP and SENSEN | — | 800 | kΩ |
| QLSB | Charge LSB, Note 5 | RSENSE = 50 mΩ | 533 | nAh |
| EDB | Deadband Inaccuracy | Deadband = 20 µV | ±10 | % |

## Coulomb Counter Note

- Note 4: The coulomb counter measures static signals as well as dynamic inputs, current pulses. It may take several short pulses to increment/decrement the ACR.

## Title Block

- Title: blank
- Size: B
- Number: .
- Revision: blank
- Date: 6/7/2024
- Time: 3:59:24 PM
- Sheet: 3 of 3
- File: Design Notes.SchDoc
- Company: ToyBuilder Labs
- Address: 1100 S Garfield Avenue, Alhambra, CA 91801
- Phone: +1 (626) 808-4010
- Logo text: ToyBuilder LABS
