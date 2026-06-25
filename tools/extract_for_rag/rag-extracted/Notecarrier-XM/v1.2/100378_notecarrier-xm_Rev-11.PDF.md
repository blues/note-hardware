---
product: Notecarrier-XM
version: v1.2
doc_type: schematic
source_file: Notecarrier-XM/v1.2/100378_notecarrier-xm_Rev-11.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-XM — SCHEMATIC (v1.2)

_Source: `Notecarrier-XM/v1.2/100378_notecarrier-xm_Rev-11.PDF`_

## Page 1

# Notecarrier-XM — Cover Sheet

## Module
- Module name: **Notecarrier-XM**
- Copyright: **© 2023 Blues Inc.**

## Sheet Index
- **01** — Cover
- **02** — Block Diagram
- **03** — IO Connectors
- **04** — Notecard Connector
- **05** — Power

## Components / Reference Designators
- **PCB1** — PCB, **2200-917**
- **DOC1** — HW-E, **100378**
- **FD1** — board support marker, value/part not shown
- **FD2** — board support marker, value/part not shown
- **FD3** — board support marker, value/part not shown
- **FD5** — board support marker, value/part not shown
- **FD6** — board support marker, value/part not shown
- **FD7** — board support marker, value/part not shown

## Board Support
- **TOP**
  - FD1
  - FD2
  - FD5
  - FD6
- **BOTTOM**
  - FD3
  - FD7

## Connectors
- No connectors shown on this page.

## Named Nets / Signals
- No named nets or signals shown on this page.

## Revision Block
| Proto. Rev. | Prod. Rev. | Date | Description | # VAR | # BOM | # ECO |
|---|---|---|---|---|---|---|
| 10 | - | 2024-03-22 | Initial prototype release |  | 3000-742-001 |  |
| 11 | - | 2024-06-04 | Fixed M.2 screw location |  | 3000-793-001 |  |

## List of Available Variants
- No variants listed.

## Revision Format Explanation
| Proto. Rev. | Prod. Rev. | Date | Description | # BOM |
|---|---|---|---|---|
| - | - | 202y-mm-dd | Development phase, date only | - |
| 10 | - | 202y-mm-dd | Prototyping phase, revision numeric | 3000-xxx-xxx |
| - | A | 202y-mm-dd | Production phase, revision alphanumeric | 3000-xxx-xxx |

## Design Considerations
- **Software Config Note**
  - Contains important notes for software development.
  - Things like: pin configuration, timing requirements, IC configuration etc.
- **Design Note**
  - Hardware notes

## Title Block
- **Title:** 01_COVER.SchDoc
- **Project:** 100378_notecarrier-xm.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Marsic
- **Acceptor:** J. Wiedey
- **Sheet:** 1 of 5
- **Rev:** 11
- **Format:** A4

## Page 2

# Schematic Page Transcription

## Page / Document
- Title: `02_BLOCK-DIAGRAM.SchDoc`
- Project: `100378_notecarrier-xm.PrjPCB`
- Sheet: `2 of 5`
- Revision: `11`
- Format: `A4`
- Copyright: `Copyright © 2023 Blues Inc.`

## Title Block Notes
- Company:
  - `Byte Lab Grupa d.o.o.`
  - `Medarska 69/1, 10000 Zagreb, Croatia`
  - `www.byte-lab.com`
- Author: `M. Marsic`
- Acceptor: `J. Wiedey`

## Components / Functional Blocks
- USB C
  - Part/value shown: `USB C`
- ORing
  - Part/value shown: `ORing`
- Buck/Boost 3V3
  - Part/value shown: `Buck/Boost 3V3`
- PIN HEADER
  - Part/value shown: `PIN HEADER`
- M.2 CONNECTOR KEY E
  - Part/value shown: `M.2 CONNECTOR KEY E`

## Reference Designators
- No component reference designators are visible on this page.

## Connectors and Pin / Signal Labels

### USB C
- `+VUSB`

### PIN HEADER
- `+VBAT`
- `+VUSB`
- `+VMAIN`
- `+VIO`
- `+VACT_GPS_IN`
- `+VACT_GPS_OUT`
- `I2C`
- `UART`
- `AUX_UART`
- `AUX_GPIO`
- `DFU`
- `NRST`
- `ATTN`

### M.2 CONNECTOR KEY E
- `+VMODEM`
- `+VIO`
- `+VACT_GPS_IN`
- `+VACT_GPS_OUT`
- `I2C`
- `UART`
- `AUX_UART`
- `AUX_GPIO`
- `DFU`
- `NRST`
- `ATTN`

## Named Nets / Signals
- `+VUSB`
- `+VBAT`
- `+VMAIN`
- `+VMODEM`
- `+VIO`
- `+VACT_GPS_IN`
- `+VACT_GPS_OUT`
- `I2C`
- `UART`
- `AUX_UART`
- `AUX_GPIO`
- `DFU`
- `NRST`
- `ATTN`

## Block Connectivity Shown
- `USB C` provides `+VUSB` to `ORing`.
- `+VBAT` feeds `ORing`.
- `ORing` outputs `+VMAIN`.
- `+VMAIN` feeds:
  - `+VMODEM` path to `M.2 CONNECTOR KEY E`
  - `Buck/Boost 3V3`
  - `PIN HEADER`
- `Buck/Boost 3V3` outputs `+VIO` to:
  - `M.2 CONNECTOR KEY E`
  - `PIN HEADER`
- `PIN HEADER` connects to `M.2 CONNECTOR KEY E` via:
  - `+VACT_GPS_IN`
  - `+VACT_GPS_OUT`
  - `I2C, UART, AUX_UART, AUX_GPIO, DFU, NRST, ATTN`

## Page 3

# Components

- **P1**: Header Castellated 2.54mm 1X16
- **P2**: Header Castellated 2.54mm 1X16
- **P3**: 12402012E212A, USB C Connector
- **R11**: 5k1
- **R12**: 5k1
- **R3**: 1M
- **C2**: 10n/1000V

# Connectors

## P1 — Header Castellated 2.54mm 1X16

- Pin 1: `+VBAT`
- Pin 2: `+VUSB`
- Pin 3: `+VMAIN`
- Pin 4: `+VIO`
- Pin 5: `BOOT`
- Pin 6: `NRST`
- Pin 7: `AUX_NCHARGING`
- Pin 8: `VIO_EN`
- Pin 9: `+VACT_GPS_OUT`
- Pin 10: `+VACT_GPS_IN`
- Pin 11: `ALT_DFU_IDLE`
- Pin 12: `ALT_DFU_NRESET`
- Pin 13: `ALT_DFU_BOOT`
- Pin 14: `ALT_DFU_TX`
- Pin 15: `ALT_DFU_RX`
- Pin 16: `GND`

## P2 — Header Castellated 2.54mm 1X16

- Pin 1: `GND`
- Pin 2: `AUX_TX`
- Pin 3: `AUX_RX`
- Pin 4: `AUX_EN`
- Pin 5: `AUX4`
- Pin 6: `AUX3`
- Pin 7: `AUX2`
- Pin 8: `AUX1`
- Pin 9: `ATTN`
- Pin 10: `CTX`
- Pin 11: `RTX`
- Pin 12: `TX`
- Pin 13: `RX`
- Pin 14: `SCL`
- Pin 15: `SDA`
- Pin 16: `GND`

## P3 — USB C Connector, 12402012E212A

- Pin A4: `VBUS` → `+VUSB`
- Pin A9: `VBUS` → `+VUSB`
- Pin B4: `VBUS` → `+VUSB`
- Pin B9: `VBUS` → `+VUSB`
- Pin A5: `CC1` → R11 5k1 to `GND`
- Pin B5: `CC2` → R12 5k1 to `GND`
- Pin A6: `D+` → `USB_D_P`
- Pin B6: `D+` → `USB_D_P`
- Pin A7: `D-` → `USB_D_N`
- Pin B7: `D-` → `USB_D_N`
- Pin A8: `SBU1` → no connect shown
- Pin B8: `SBU2` → no connect shown
- Pin A1: `GND` → `GND`
- Pin A12: `GND` → `GND`
- Pin B1: `GND` → `GND`
- Pin B12: `GND` → `GND`
- Pin M: `M` → `USB_SHIELD`

# USB Shield Network

- `USB_SHIELD` connects to P3 pin `M`.
- `C2` 10n/1000V between `USB_SHIELD` and `GND`.
- `R3` 1M between `USB_SHIELD` and `GND`.

# Named Nets / Signals

- `+VBAT`
- `+VUSB`
- `+VMAIN`
- `+VIO`
- `+VACT_GPS_OUT`
- `+VACT_GPS_IN`
- `GND`
- `BOOT`
- `NRST`
- `AUX_NCHARGING`
- `VIO_EN`
- `ALT_DFU_IDLE`
- `ALT_DFU_NRESET`
- `ALT_DFU_BOOT`
- `ALT_DFU_TX`
- `ALT_DFU_RX`
- `AUX_TX`
- `AUX_RX`
- `AUX_EN`
- `AUX4`
- `AUX3`
- `AUX2`
- `AUX1`
- `ATTN`
- `CTX`
- `RTX`
- `TX`
- `RX`
- `SCL`
- `SDA`
- `USB_D_P`
- `USB_D_N`
- `USB_SHIELD`

# Sheet Notes / Title Block

- Copyright © 2023 Blues Inc.
- Title: `03_IO-CONNECTION.SchDoc`
- Project: `100378_notecarrier-xm.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 3 of 5
- Rev: 11
- Format: A4

## Page 4

# Schematic Page Transcription

## Page / Sections

- Copyright © 2023 Blues Inc.
- Section: **Notecard Connector**
- Section: **Notecard Support**

## Components

- **J5** — MDT420E01001
- **R2** — 0R0
- **ASS1** — KNOB M2.5x4-INOX
- **OBJ1** — 9774025151R
  - Connected to **GND**

## Connector J5 — MDT420E01001

### J5 Pin Labels and Connected Nets

- **Pin 1** — XP_ENABLE — no connection shown
- **Pin 2** — VIO_P — **+VIO**
- **Pin 3** — GND — **GND**
- **Pin 4** — VIO_P — **+VIO**
- **Pin 5** — GND — **GND**
- **Pin 6** — GND — **GND**
- **Pin 7** — USB_DP — **USB_D_P**
- **Pin 8** — SIM_VCC — **SIM_VCC**
- **Pin 9** — USB_DN — **USB_D_N**
- **Pin 10** — SIM_RST — **SIM_RST**
- **Pin 11** — GND — **GND**
- **Pin 12** — SIM_IO — **SIM_IO**
- **Pin 13** — VUSB — **+VUSB**
- **Pin 14** — SIM_CLK — **SIM_CLK**
- **Pin 15** — NC15 — no connection shown
- **Pin 16** — SIM_NPRESENT — **SIM_NPRESENT**
- **Pin 17** — NC17 — no connection shown
- **Pin 18** — GND — **GND**
- **Pin 19** — NC19 — no connection shown
- **Pin 20** — VACT_GPS_OUT — **+VACT_GPS_OUT**
- **Pin 21** — NC21 — no connection shown
- **Pin 22** — VACT_GPS_IN — **+VACT_GPS_IN**
- **Pin 23** — NC23 — no connection shown
- **Pin 32** — ALT_DFU_BOOT — **ALT_DFU_BOOT**
- **Pin 33** — GND — **GND**
- **Pin 34** — ALT_DFU_RESET — **ALT_DFU_NRESET**
- **Pin 35** — NC35 — no connection shown
- **Pin 36** — ALT_DFU_ACTIVE — **ALT_DFU_IDLE**
- **Pin 37** — NC37 — no connection shown
- **Pin 38** — AUX_CHARGING — **AUX_NCHARGING**
- **Pin 39** — GND — **GND**
- **Pin 40** — SCL_P — **SCL**
- **Pin 41** — ALT_DFU_RX — **ALT_DFU_RX**
- **Pin 42** — SDA_P — **SDA**
- **Pin 43** — ALT_DFU_TX — **ALT_DFU_TX**
- **Pin 44** — NC44 — no connection shown
- **Pin 45** — GND — **GND**
- **Pin 46** — AUX1 — **AUX1**
- **Pin 47** — RTX — **RTX**
- **Pin 48** — AUX2 — **AUX2**
- **Pin 49** — CTX — **CTX**
- **Pin 50** — AUX3 — **AUX3**
- **Pin 51** — GND — **GND**
- **Pin 52** — AUX4 — **AUX4**
- **Pin 53** — NC53 — no connection shown
- **Pin 54** — ATTN_P — **ATTN**
- **Pin 55** — NC55 — no connection shown
- **Pin 56** — AUX_EN_P — **AUX_EN**
- **Pin 57** — GND — **GND**
- **Pin 58** — AUX_RX_P — **AUX_RX**
- **Pin 59** — NC59 — no connection shown
- **Pin 60** — AUX_TX_P — **AUX_TX**
- **Pin 61** — NC61 — no connection shown
- **Pin 62** — RX_P — **RX**
- **Pin 63** — NC63 — no connection shown
- **Pin 64** — TX_P — **TX**
- **Pin 65** — BOOT — **BOOT**
- **Pin 66** — NC66 — no connection shown
- **Pin 67** — RST — **NRST**
- **Pin 68** — NC68 — no connection shown
- **Pin 69** — NC69 — no connection shown
- **Pin 70** — VMODEM_P — **+VMAIN**
- **Pin 71** — GND — **GND**
- **Pin 72** — VMODEM_P — **+VMAIN**
- **Pin 73** — GND — **GND**
- **Pin 74** — VMODEM_P — **+VMAIN**
- **Pin 75** — XP_MODEM_VSEL — no connection shown

## Named Nets / Signals

- **+VIO**
- **GND**
- **SIM_VCC**
- **SIM_RST**
- **SIM_IO**
- **SIM_CLK**
- **SIM_NPRESENT**
- **+VACT_GPS_OUT**
- **+VACT_GPS_IN**
- **ALT_DFU_BOOT**
- **ALT_DFU_NRESET**
- **ALT_DFU_IDLE**
- **AUX_NCHARGING**
- **SCL**
- **SDA**
- **AUX1**
- **AUX2**
- **AUX3**
- **AUX4**
- **ATTN**
- **AUX_EN**
- **AUX_RX**
- **AUX_TX**
- **RX**
- **TX**
- **+VMAIN**
- **USB_D_P**
- **USB_D_N**
- **+VUSB**
- **ALT_DFU_RX**
- **ALT_DFU_TX**
- **RTX**
- **CTX**
- **BOOT**
- **NRST**

## Other Signal / Pin Function Labels on J5

- **VIO_P**
- **XP_ENABLE**
- **USB_DP**
- **USB_DN**
- **VUSB**
- **VACT_GPS_OUT**
- **VACT_GPS_IN**
- **ALT_DFU_RESET**
- **ALT_DFU_ACTIVE**
- **AUX_CHARGING**
- **SCL_P**
- **SDA_P**
- **ATTN_P**
- **AUX_EN_P**
- **AUX_RX_P**
- **AUX_TX_P**
- **RX_P**
- **TX_P**
- **VMODEM_P**
- **RST**
- **XP_MODEM_VSEL**
- **NC15**
- **NC17**
- **NC19**
- **NC21**
- **NC23**
- **NC35**
- **NC37**
- **NC44**
- **NC53**
- **NC55**
- **NC59**
- **NC61**
- **NC63**
- **NC66**
- **NC68**
- **NC69**

## Connections / Notes

- **R2 0R0** connects between **+VACT_GPS_OUT** and **+VACT_GPS_IN**.
- **J5 pins 70, 72, and 74** are tied to **+VMAIN**.
- **J5 pins 2 and 4** are tied to **+VIO**.
- Multiple J5 pins connect to **GND**: 3, 5, 6, 11, 18, 33, 39, 45, 51, 57, 71, 73.

## Title Block

- **Title:** 04_NOTECARD-CONNECTION.SchDoc
- **Project:** 100378_notecarrier-xm.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Marsic
- **Acceptor:** J. Wiedey
- **Sheet:** 4 of 5
- **Rev:** 11
- **Format:** A4

## Page 5

# Schematic Page Transcription

## Blocks

- **VBUS ORing**
- **3V3 Buck/Boost Regulator**

## Components

- **U3**: LM66200DRLR
  - Pins shown:
    - 3: VIN1
    - 6: VIN2
    - 4: ON
    - 1: GND
    - 5: GND
    - 2: VOUT
    - 7: VOUT
    - 8: STAT, no-connect

- **U1**: ISL9122AIINZ-T
  - Pins shown:
    - B1: LX1
    - A2: LX2
    - C1: VIN
    - C2: EN
    - A1: GND
    - B2: VOUT
    - D2: SDA, no-connect
    - D1: SCL, no-connect

- **L5**: MCKK1608T1R0MN

- **R1**: 10M

- **C1**: 22u

- **C3**: 22u

## Connectors

- No connectors visible on this page.

## Named Nets / Signals

- **+VBAT**
- **+VUSB**
- **+VMAIN**
- **+VIO**
- **VIO_EN**
- **GND**
- **VIN1**
- **VIN2**
- **ON**
- **STAT**
- **VOUT**
- **VIN**
- **EN**
- **LX1**
- **LX2**
- **SDA**
- **SCL**

## Design Notes

- **3V3 Buck/Boost Regulator**
  - DESIGN NOTE:
    - Input Voltage: 1.8V - 5.5V
    - Output Voltage: 3.3V
    - Peak Output Current: 500mA
    - Average Current: 100mA

## Title Block / Page Notes

- Copyright © 2023 Blues Inc.
- Title: **05_POWER.SchDoc**
- Project: **100378_notecarrier-xm.PrjPCB**
- Company: **Byte Lab Grupa d.o.o.**
- Address: **Medarska 69/1, 10000 Zagreb, Croatia**
- Website: **www.byte-lab.com**
- Author: **M. Marsic**
- Acceptor: **J. Wiedey**
- Sheet: **5 of 5**
- Rev: **11**
- Format: **A4**
