---
product: Notecarrier-F
version: v1.3
doc_type: schematic
source_file: Notecarrier-F/v1.3/100275_NOTECARRIER-F_Rev-11.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-F — SCHEMATIC (v1.3)

_Source: `Notecarrier-F/v1.3/100275_NOTECARRIER-F_Rev-11.PDF`_

## Page 1

# Notecarrier F — Cover Page

## Module
- Module name: **Notecarrier F**

## Document Notice
- This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.

## Sheet Index
- **01** — Cover
- **02** — Block diagram
- **03** — Notecard connection
- **04** — Feather connection
- **05** — I/O
- **06** — Power - Input
- **07** — Power - Rails

## Components / Board Support References
- **FD1** — Fiducial, TOP
- **FD2** — Fiducial, TOP
- **FD3** — Fiducial, TOP
- **FD4** — Fiducial, TOP
- **FD5** — Fiducial, BOTTOM
- **FD6** — Fiducial, BOTTOM
- **FD7** — Fiducial, BOTTOM
- **FD8** — Fiducial, BOTTOM
- **DOC1** — HW-E, 100275
- **PCB1** — PCB, 2200-814

## Connectors
- No connectors shown on this page.

## Named Nets / Signals
- No named nets or signals shown on this page.

## Design Considerations

### Software Config Note
- Contains important notes for software development.
- Things like: pin configuration, timing requirements, IC configuration etc.

### Design Note
- Hardware notes

## Revision Block
- **Rev. Proto.:** 10
  - **Rev. Prod.:** -
  - **Date:** 2023-05-31
  - **Description:** Initial board release
  - **# BOM:** 3000-613-002
- **Rev. Proto.:** 11
  - **Rev. Prod.:** -
  - **Date:** 2023-07-10
  - **Description:** Changed R3, DS1-7, J1-3 & added U9
  - **# BOM:** 3000-653-001

## List of Available Variants
- No variants listed.

## Revision Format Explanation
- **Proto.:** -
  - **Prod.:** -
  - **Date:** 202y-mm-dd
  - **Description:** Development phase, date only
  - **# BOM:** -
- **Proto.:** 10
  - **Prod.:** -
  - **Date:** 202y-mm-dd
  - **Description:** Prototyping phase, revision numeric
  - **# BOM:** 3000-xxx-xxx
- **Proto.:** -
  - **Prod.:** A
  - **Date:** 202y-mm-dd
  - **Description:** Production phase, revision alphanumeric
  - **# BOM:** 3000-xxx-xxx

## Title Block
- **Title:** 01_COVER.SchDoc
- **Project:** 100275_NOTECARRIER-F.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Hamin
- **Acceptor:** T. Zvonc
- **Sheet:** 1 of 7
- **Rev:** 11
- **Format:** A4

## Page 2

## Document Note

- This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.

## Title Block

- **Title:** `02_BLOCK-DIAGRAM.SchDoc`
- **Project:** `100275_NOTECARRIER-F.PrjPCB`
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Hamin
- **Acceptor:** T. Zvonc
- **Sheet:** 2 of 7
- **Rev:** 11
- **Format:** A4

## Component Reference Designators

- **SW3** — BUTTON

## Functional Blocks / Parts Shown

- **LIPO** — JST-PH
- **uUSB**
- **PV 0.5W** — JST-PH
- **BAT (Primary)** — JST-PH
- **Feather uUSB**
- **BATTERY CHARGER**
- **OR NETWORK**
- **BUCK BOOST** — `+3V3@2A`
- **SW LOW PWR**
- **BUCK BOOST** — `+3V6@2A`
- **I2C QWIC** — two blocks shown
- **I2C SHIFTER** — two blocks shown
- **FEATHER CONNECTOR**
- **SW DFU TOGGLE**
- **ANALOG SWITCH**
- **M.2 CONNECTOR KEYE**
- **NANO SIM CONNECTOR**
- **SW GPS ACT/PASS**
- **SW BUTTON**

## Connectors and Visible Pin / Signal Labels

- **LIPO JST-PH**
  - `VBAT`

- **uUSB**
  - `VUSB`

- **PV 0.5W JST-PH**
  - `VSOLAR`

- **BAT (Primary) JST-PH**
  - `V+`

- **Feather uUSB**
  - `F_3V3`

- **I2C QWIC** connector/block
  - `SW_I2C`

- **I2C QWIC** connector/block
  - `SW_I2C`

- **FEATHER CONNECTOR**
  - `F_BAT`
  - `DFU NETS`
  - `F_I2C`
  - `USER_F`

- **M.2 CONNECTOR KEYE**
  - `N_VIO`
  - `N_ATTN`
  - `DFU NETS`
  - `N_I2C`
  - `VMODEM`
  - `NANO SIM SIGNALS`
  - `VACT_GPS_OUT`
  - `Notecard Reset`

- **NANO SIM CONNECTOR**
  - `NANO SIM SIGNALS`

- **SW GPS ACT/PASS**
  - `VACT_GPS_OUT`

- **SW BUTTON**
  - `Notecard Reset`

## Named Nets / Signals

- `VBAT`
- `VUSB`
- `VSOLAR`
- `V+`
- `F_3V3`
- `VMAIN`
- `+3V3@2A`
- `+3V6@2A`
- `N_VIO`
- `N_ATTN`
- `EN_F_BAT`
- `F_BAT`
- `SW_I2C`
- `F_I2C`
- `USER_F`
- `DFU NETS`
- `N_I2C`
- `NANO SIM SIGNALS`
- `VACT_GPS_OUT`
- `Notecard Reset`
- `VMODEM`

## Page 3

# Page: Notecard connection

## Sheet sections

- Notecard Fasteners
- SIM Card socket
- Notecard connection

## Components

- **ASS1**: KNOB M2.5x4-INOX
- **C5**: 100n
- **C6**: 33p
- **C7**: 33p
- **C8**: 33p
- **C9**: 100n
- **F1**: SF-0603F150-2, F1.5A
- **F2**: 046703.5NR
- **J5**: SF72S006VBDR2500, NanoSIM socket
- **J6**: MDT420E01001, Notecard connector
- **J11**: CES-102-01-S-S
- **OBJ1**: 9774025151R
- **R1A**: 100R
- **R1B**: 100R
- **R1C**: 100R
- **R1D**: 100R
- **R1E**: 100R
- **R1F**: 100R
- **R1G**: 100R
- **R1H**: 100R
- **R6**: 15k
- **R7**: 22R
- **R8**: 22R
- **R9**: 22R
- **R20A**: 100R
- **R20B**: 100R
- **R20C**: 100R
- **R20D**: 100R
- **R20E**: 100R
- **R20F**: 100R
- **R20G**: 100R
- **R20H**: 100R
- **SW1**: CJS-1200TA
- **SW2**: EVP-BB2A9B000
- **TVS2**: PESD5V0L5UV,125

## Connectors and pin labels

### OBJ1 — 9774025151R

- Pin 1: GND

### J5 — SF72S006VBDR2500 NanoSIM socket

- Pin 1: VCC
- Pin 2: RST
- Pin 3: CLK
- Pin 5: GND
- Pin 6: VPP
- Pin 7: IO
- Pin 8: GND
- Pin 9: GND
- Pin 10: CSW
- Pin 11: GND
- Pin 12: GND
- Pin 13: DSW
- Pin 14: GND
- Pin 15: GND
- Pin 16: GND
- Pin 17: GND
- Pin 18: GND
- Pin 19: GND

### J6 — MDT420E01001 Notecard connector

#### Bottom side

- Pin 2: VIO_P
- Pin 4: VIO_P
- Pin 6: GND
- Pin 8: SIM_VCC
- Pin 10: SIM_RST
- Pin 12: SIM_IO
- Pin 14: SIM_CLK
- Pin 16: SIM_PRESENT
- Pin 18: GND
- Pin 20: VACT_GPS_OUT
- Pin 22: VACT_GPS_IN
- Pin 32: ALT_DFU_BOOT
- Pin 34: ALT_DFU_RESET
- Pin 36: ALT_DFU_ACTIVE
- Pin 38: AUX_CHARGING
- Pin 40: SCL_P
- Pin 42: SDA_P
- Pin 44: NC44
- Pin 46: AUX1
- Pin 48: AUX2
- Pin 50: AUX3
- Pin 52: AUX4
- Pin 54: ATTN_P
- Pin 56: AUX_EN_P
- Pin 58: AUX_RX_P
- Pin 60: AUX_TX_P
- Pin 62: RX_P
- Pin 64: TX_P
- Pin 66: NC66
- Pin 68: NC68
- Pin 70: VMODEM_P
- Pin 72: VMODEM_P
- Pin 74: VMODEM_P

#### Top side

- Pin 1: NC1
- Pin 3: GND
- Pin 5: GND
- Pin 7: USB_DP
- Pin 9: USB_DN
- Pin 11: GND
- Pin 13: VUSB
- Pin 15: NC15
- Pin 17: NC17
- Pin 19: NC19
- Pin 21: NC21
- Pin 23: NC23
- Pin 33: GND
- Pin 35: NC35
- Pin 37: NC37
- Pin 39: GND
- Pin 41: ALT_DFU_RX
- Pin 43: ALT_DFU_TX
- Pin 45: GND
- Pin 47: RTX
- Pin 49: CTX
- Pin 51: GND
- Pin 53: NC53
- Pin 55: NC55
- Pin 57: GND
- Pin 59: NC59
- Pin 61: NC61
- Pin 63: NC63
- Pin 65: BOOT
- Pin 67: RST
- Pin 69: NC69
- Pin 71: GND
- Pin 73: GND
- Pin 75: NC75

### J11 — CES-102-01-S-S

- Pin 1: RTX
- Pin 2: CTX

## Switch pin labels

### SW1 — CJS-1200TA

- Pin 1: ACTIVE
- Pin 2: VACT_GPS path
- Pin 3: PASSIVE

### SW2 — EVP-BB2A9B000

- Signal label: N_NRST
- Connected to GND

## Named nets and signals

- ACTIVE
- ALT_DFU_ACTIVE
- ALT_DFU_BOOT
- ALT_DFU_RESET
- ALT_DFU_RX
- ALT_DFU_TX
- ATTN_P
- AUX1
- AUX2
- AUX3
- AUX4
- AUX_CHARGING
- AUX_EN_P
- AUX_RX_P
- AUX_TX_P
- BOOT
- CTX
- D_N
- D_P
- GND
- N_ATTN
- N_AUX1
- N_AUX2
- N_AUX3
- N_AUX4
- N_AUX_EN
- N_AUX_RX
- N_AUX_TX
- N_BOOT
- N_NRST
- N_RX
- N_SCL
- N_SDA
- N_TX
- N_VIO
- PASSIVE
- RST
- RTX
- RX_P
- SCL_P
- SDA_P
- SIM_CLK
- SIM_IO
- SIM_NPRESENT
- SIM_PRESENT
- SIM_RST
- SIM_VCC
- TX_P
- USB_DN
- USB_DP
- VACT_GPS_IN
- VACT_GPS_OUT
- VIO_P
- VMAIN
- VMODEM_P
- VUSB

## Design notes

- **N_VIO** rated for 150mA
- GPS ANT SW
- **VMODEM** rated for 2A pulsed
- RESET SW

## Title block and document notes

- Notice: “This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.”
- Title: **03_NOTECARD-CONNECTION.SchDoc**
- Project: **100275_NOTECARRIER-F.PrjPCB**
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Hamin
- Acceptor: T. Zvonc
- Sheet: 3 of 7
- Rev: 11
- Format: A4

## Page 4

## Page / Sections

- **DFU Enable**
- **Logic level shifter**
- **Feather module connection** — shown crossed out with large red X
- **QWIIC Connection**

## Components

- **U1**: TSX0102DCUR
- **U4**: TSX0102DCUR
- **U5**: DGQ2788AEN-T1-GE4
- **U6**: DGQ2788AEN-T1-GE4
- **SW3**: CJS-1200TA
- **SW4**: CJS-1200TA
- **R10**: 10k
- **R11**: 10k — shown crossed out
- **R12**: 10k — shown crossed out
- **R15**: 10k
- **R16**: 10k
- **R18**: 100k
- **C10**: 100n
- **C11**: 100n
- **C12**: 100n
- **C13**: 100n
- **C14**: 100n
- **C15**: 100n
- **J7**: SM04B-SRSS-TB(LF)(SN)
- **J8**: SM04B-SRSS-TB(LF)(SN)
- **MOD2**: Feather Module
- **MOD1L**: Feather/module left connector/header
- **MOD1R**: Feather/module right connector/header

## IC Signal Connections

### U6 — DGQ2788AEN-T1-GE4

- Pin 10, **V+**: `EN_F_BAT`
- Pin 2, **GND**: `GND`
- Pin 12, **COM1**: `F_NRST`
- Pin 16, **COM2**: `F_B0`
- Pin 14, **IN1-2**: `DFU_SW`
- Pin 4, **COM3**: `F_TX`
- Pin 8, **COM4**: `F_RX`
- Pin 6, **IN3-4**: `DFU_SW`
- Pin 11, **NO1**: `N_AUX4`
- Pin 15, **NO2**: `N_AUX3`
- Pin 3, **NO3**: `N_AUX_RX`
- Pin 7, **NO4**: `N_AUX_TX`
- Pins 13 / 1 / 5 / 9, **NC1 / NC2 / NC3 / NC4**: routed to shared bus shown near `ALT_DFU_ACTIVE`

### U5 — DGQ2788AEN-T1-GE4

- Pin 10, **V+**: `EN_F_BAT`
- Pin 2, **GND**: `GND`
- Pin 12, **COM1**: shared bus / `ALT_DFU_ACTIVE`
- Pin 16, **COM2**: shared bus / `ALT_DFU_ACTIVE`
- Pin 14, **IN1-2**: shared bus / `ALT_DFU_ACTIVE`
- Pin 4, **COM3**: shared bus / `ALT_DFU_ACTIVE`
- Pin 8, **COM4**: shared bus / `ALT_DFU_ACTIVE`
- Pin 6, **IN3-4**: shared bus / `ALT_DFU_ACTIVE`
- Pin 13, **NC1**: `ALT_DFU_RESET`
- Pin 11, **NO1**: `F_NRST_SW`
- Pin 1, **NC2**: `ALT_DFU_BOOT`
- Pin 15, **NO2**: `F_B0_SW`
- Pin 5, **NC3**: `ALT_DFU_RX`
- Pin 3, **NO3**: `F_TX_SW`
- Pin 9, **NC4**: `ALT_DFU_TX`
- Pin 7, **NO4**: `F_RX_SW`

### U4 — TSX0102DCUR

- Pin 5, **A1**: `N_SDA`
- Pin 4, **A2**: `N_SCL`
- Pin 6, **OE**: `EN_F_BAT`
- Pin 3, **VCCA**: `N_VIO`
- Pin 7, **VCCB**: `F_VIO`
- Pin 8, **B1**: `F_SDA`
- Pin 1, **B2**: `F_SCL`
- Pin 2, **GND**: `GND`

### U1 — TSX0102DCUR

- Pin 5, **A1**: `F_SDA`
- Pin 4, **A2**: `F_SCL`
- Pin 6, **OE**: `F_VIO`
- Pin 3, **VCCA**: `F_VIO`
- Pin 7, **VCCB**: `F_3V3`
- Pin 8, **B1**: `SW_SDA`
- Pin 1, **B2**: `SW_SCL`
- Pin 2, **GND**: `GND`

## Switches

### SW4 — CJS-1200TA

- Pin 3: `EN_F_BAT`, annotation `[DFU]`
- Pin 1: `GND`, annotation `[NORMAL]`
- Pin 2: `DFU_SW`
- Design note: `AUX SW`

### SW3 — CJS-1200TA

- Pin 3: `N_VIO`, annotation `[ON]`
- Pin 1: `N_ATTN`, annotation `[N_ATTN]`
- Pin 2: `EN_F_BAT`
- Design note: `FEATHER_EN SW`

## Connectors

### J8 — SM04B-SRSS-TB(LF)(SN)

- Pin 4: `GND`
- Pin 3: `F_3V3`
- Pin 2: `SW_SDA`
- Pin 1: `SW_SCL`

### J7 — SM04B-SRSS-TB(LF)(SN)

- Pin 4: `GND`
- Pin 3: `F_3V3`
- Pin 2: `SW_SDA`
- Pin 1: `SW_SCL`

### MOD1L / MOD2 Left Side — Feather Module

- Pin 1: `F_NRST` / `RESET#`
- Pin 2: `F_3V3` / `3V`
- Pin 3: `F_AREF` / `ARef`
- Pin 4: `GND`
- Pin 5: `F_A0` / `A0`
- Pin 6: `F_A1` / `A1`
- Pin 7: `F_A2` / `A2`
- Pin 8: `F_A3` / `A3`
- Pin 9: `F_A4` / `A4`
- Pin 10: `F_A5` / `A5`
- Pin 11: `F_SCK` / `SCK`
- Pin 12: `F_MOSI` / `MOSI`
- Pin 13: `F_MISO` / `MISO`
- Pin 14: `F_RX` / `D0(RX)`
- Pin 15: `F_TX` / `D1(TX)`
- Pin 16: `F_B0` / `B0`

### MOD1R / MOD2 Right Side — Feather Module

- Pin 1: `F_BAT` / `VBAT`
- Pin 2: `F_EN` / `EN`
- Pin 3: `F_VUSB` / `VUSB`
- Pin 4: `F_D13` / `D13`
- Pin 5: `F_D12` / `D12`
- Pin 6: `F_D11` / `D11`
- Pin 7: `F_D10` / `D10`
- Pin 8: `F_D9` / `D9`
- Pin 9: `F_D6` / `D6`
- Pin 10: `F_D5` / `D5`
- Pin 11: `F_SCL` / `SCL`
- Pin 12: `F_SDA` / `SDA`

### MOD2 Feather Module Pin Labels

- Left side:
  - 1 `RESET#`
  - 2 `3V`
  - 3 `ARef`
  - 4 `GND`
  - 5 `A0`
  - 6 `A1`
  - 7 `A2`
  - 8 `A3`
  - 9 `A4`
  - 10 `A5`
  - 11 `SCK`
  - 12 `MOSI`
  - 13 `MISO`
  - 14 `D0(RX)`
  - 15 `D1(TX)`
  - 16 `B0`
- Right side:
  - 28 `VBAT`
  - 27 `EN`
  - 26 `VUSB`
  - 25 `D13`
  - 24 `D12`
  - 23 `D11`
  - 22 `D10`
  - 21 `D9`
  - 20 `D6`
  - 19 `D5`
  - 18 `SCL`
  - 17 `SDA`

## Named Nets / Signals

- `ALT_DFU_ACTIVE` — shown with leading backslash/overbar mark
- `ALT_DFU_BOOT`
- `ALT_DFU_RESET`
- `ALT_DFU_RX`
- `ALT_DFU_TX`
- `DFU_SW`
- `EN_F_BAT`
- `F_3V3`
- `F_A0`
- `F_A1`
- `F_A2`
- `F_A3`
- `F_A4`
- `F_A5`
- `F_AREF`
- `F_B0`
- `F_B0_SW`
- `F_BAT`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_EN`
- `F_MISO`
- `F_MOSI`
- `F_NRST`
- `F_NRST_SW`
- `F_RX`
- `F_RX_SW`
- `F_SCK`
- `F_SCL`
- `F_SDA`
- `F_TX`
- `F_TX_SW`
- `F_VIO`
- `F_VUSB`
- `GND`
- `N_ATTN`
- `N_AUX3`
- `N_AUX4`
- `N_AUX_RX`
- `N_AUX_TX`
- `N_SCL`
- `N_SDA`
- `N_VIO`
- `SW_SCL`
- `SW_SDA`

## Notes

### Software Config Notes

- `Flick switch towards "ON" to enable outboard DFU`
- Truth table:
  - `IN1-2, IN3-4`
  - `Logic 0 = NC is True/High, DFU = N`
  - `Logic 1 = NO is True/High, DFU = Y`

### Design Notes

- `AUX SW`
- `FEATHER_EN SW`
- `OE is referenced to VCCA`

## Title Block / Document Notes

- Property note: `This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.`
- Title: `04_FEATHER-CONNECTION.SchDoc`
- Project: `100275_NOTECARRIER-F.PrjPCB`
- Company: `Byte Lab Grupa d.o.o.`
- Address: `Medarska 69/1, 10000 Zagreb, Croatia`
- Website: `www.byte-lab.com`
- Author: `M. Hamin`
- Acceptor: `T. Zvonc`
- Sheet: `4 of 7`
- Rev: `11`
- Format: `A4`

## Page 5

## Components

- **J9** — `CES-124-01-S-S`
  - 24-pin connector/header
  - Marked with a large red X annotation
- **J10** — `CES-124-01-S-S`
  - 24-pin connector/header
  - Marked with a large red X annotation

## Connector J9 Pins

| Pin | Pin label | Connected net / signal label |
|---:|---|---|
| 1 | F_NRST | F_NRST_SW |
| 2 | F_EN | F_EN |
| 3 | SDA | SW_SDA |
| 4 | SCL | SW_SCL |
| 5 | F_D5 | F_D5 |
| 6 | F_D6 | F_D6 |
| 7 | F_D9 | F_D9 |
| 8 | F_D10 | F_D10 |
| 9 | F_D11 | F_D11 |
| 10 | F_D12 | F_D12 |
| 11 | F_D13 | F_D13 |
| 12 | F_B0_SW | F_B0_SW |
| 13 | F_TX_SW | F_TX_SW |
| 14 | F_RX_SW | F_RX_SW |
| 15 | F_MISO | F_MISO |
| 16 | F_MOSI | F_MOSI |
| 17 | F_SCK | F_SCK |
| 18 | F_A5 | F_A5 |
| 19 | F_A4 | F_A4 |
| 20 | F_A3 | F_A3 |
| 21 | F_A2 | F_A2 |
| 22 | F_A1 | F_A1 |
| 23 | F_A0 | F_A0 |
| 24 | F_AREF | F_AREF |

## Connector J10 Pins

| Pin | Pin label | Connected net / signal label |
|---:|---|---|
| 1 | F_3V3 | F_3V3 |
| 2 | VUSB | VUSB |
| 3 | VBAT | VBAT |
| 4 | VMAIN | VMAIN |
| 5 | N_VIO | N_VIO |
| 6 | VSOLAR | VSOLAR |
| 7 | V+ | V+ |
| 8 | GND | GND |
| 9 | N_EN | N_EN |
| 10 | N_NRST | N_NRST |
| 11 | N_BOOT | N_BOOT |
| 12 | GND | GND |
| 13 | N_SCL | N_SCL |
| 14 | N_SDA | N_SDA |
| 15 | N_ATTN | N_ATTN |
| 16 | N_AUXEN | N_AUX_EN |
| 17 | N_AUXRX | N_AUX_RX |
| 18 | N_AUXTX | N_AUX_TX |
| 19 | N_AUX1 | N_AUX1 |
| 20 | N_AUX2 | N_AUX2 |
| 21 | N_AUX3 | N_AUX3 |
| 22 | N_AUX4 | N_AUX4 |
| 23 | N_RX | N_RX |
| 24 | N_TX | N_TX |

## Named Nets / Signals

- F_NRST
- F_NRST_SW
- F_EN
- SDA
- SCL
- SW_SDA
- SW_SCL
- F_D5
- F_D6
- F_D9
- F_D10
- F_D11
- F_D12
- F_D13
- F_B0_SW
- F_TX_SW
- F_RX_SW
- F_MISO
- F_MOSI
- F_SCK
- F_A5
- F_A4
- F_A3
- F_A2
- F_A1
- F_A0
- F_AREF
- F_3V3
- VUSB
- VBAT
- VMAIN
- N_VIO
- VSOLAR
- V+
- GND
- N_EN
- N_NRST
- N_BOOT
- N_SCL
- N_SDA
- N_ATTN
- N_AUXEN
- N_AUX_EN
- N_AUXRX
- N_AUX_RX
- N_AUXTX
- N_AUX_TX
- N_AUX1
- N_AUX2
- N_AUX3
- N_AUX4
- N_RX
- N_TX

## Title Block / Notes

- **Title:** `05_IO.SchDoc`
- **Project:** `100275_NOTECARRIER-F.PrjPCB`
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Hamin
- **Acceptor:** T. Zvonc
- **Sheet:** 5 of 7
- **Rev:** 11
- **Format:** A4
- **Document note:** “This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.”

## Page 6

# 06_POWER-INPUT.SchDoc

## Page Sections

- Battery charger
- Non-Rechargeable battery
- Notecard power input (USB)
- Feather power input (USB)

## Components

### Battery charger

- **J2**: Solar input connector, labeled `[SOLAR] [3.5 - 7V]`
- **DS4**: FSV1045V
- **C1**: 1u
- **DS3**: STPS3H100U
- **U2**: BQ24210DQCT
  - Pin labels shown: VBUS, ISET, VSS, VTSB, TS, EXP, BAT, VDPM, CHG, EN, PG
  - Internal label: BAT-CHG
- **R3**: 470R
- **R4**: 10k
- **R2**: 10k
- **C2**: 1u
- **DS2**: FSV1045V
- **J3**: Battery connector, labeled `[VBAT] [3.3 - 4.2V]`

### Non-Rechargeable battery

- **DS1**: FSV1045V
- **J1**: Primary battery connector, labeled `[V+] [2.5 - 5.5V]`

### Notecard power input (USB)

- **J4**: 10118193-0001LF
- **C4**: 10n/1000V
- **R5**: 1M
- **TVS3**: PESD5V0L5UV,125
- **C3**: 100n
- **DS7**: STPS3H100U
- **TVS1**: SM6T6V8A

### Feather power input (USB)

- **DS6**: STPS3H100U

## Connectors and Pin Labels

### J1 — Primary battery connector

- Label: `[V+]`
- Voltage note: `[2.5 - 5.5V]`
- Pin 2: V+
- Pin 1: GND

### J2 — Solar input connector

- Label: `[SOLAR]`
- Voltage note: `[3.5 - 7V]`
- Pin 2: Solar input
- Pin 1: GND

### J3 — Secondary battery connector

- Label: `[VBAT]`
- Voltage note: `[3.3 - 4.2V]`
- Pin 2: VBAT
- Pin 1: GND

### J4 — USB connector

- Part: 10118193-0001LF
- Pin 1: VCC
- Pin 2: D-
- Pin 3: D+
- Pin 4: ID
- Pin 5: GND
- Pin S: Shield

## Named Nets / Signals

- **AUX_CHARGING**
- **D_N**
- **D_P**
- **F_VUSB**
- **GND**
- **VBAT**
- **VMAIN**
- **VSOLAR**
- **VUSB**
- **V+**

## Design Notes

### Battery charger — Solar input

- DESIGN NOTE:
  - Solar (PV) input connector

### Battery charger — Charge current setting

- DESIGN NOTE:
  - R[iset] = K[iset] / I[out]
  - K[iset] = 395 AQ typically
  - R[iset] = 470R --> I[out] = 800mA

### Battery charger — Secondary battery

- DESIGN NOTE:
  - Secondary battery (Rechargeable) connector
  - Li-po (3.3-4.2V) C>800mAh

### Non-Rechargeable battery

- DESIGN NOTE:
  - Primary battery (Non-Rechargable) connector

## Title Block / Document Notes

- Proprietary note:
  - This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.
- Title: **06_POWER-INPUT.SchDoc**
- Project: **100275_NOTECARRIER-F.PrjPCB**
- Company: **Byte Lab Grupa d.o.o.**
- Address: **Medarska 69/1, 10000 Zagreb, Croatia**
- Website: **www.byte-lab.com**
- Author: **M. Hamin**
- Acceptor: **T. Zvonc**
- Sheet: **6 of 7**
- Rev: **11**
- Format: **A4**

## Page 7

# 07_POWER-RAILS.SchDoc

## Page / Sheet Sections

- **Buck - Boost, 3.6V@2A**
- **Buck, 1.8V@300mA**
- **Boost, 3.3V@150mA**

## Components

### Buck - Boost, 3.6V@2A

- **U3** — TPS63020DSJR
  - Pin labels:
    - 1: VINA
    - 2: GND
    - 3: FB
    - 4: VOUT
    - 5: VOUT
    - 6: L2-1
    - 7: L2-2
    - 8: L1-2
    - 9: L1-1
    - 10: VIN
    - 11: VIN
    - 12: EN
    - 13: PS/SYNC
    - 14: PG
    - 15: EXP
- **U9** — AP2139AK-3.3TRG1
  - Pin labels:
    - 1: VIN
    - 2: GND
    - 3: CE
    - 4: NC
    - 5: VOUT
- **DS5** — FSV1045V
  - Pins shown: 1, 2, 3
- **L2** — 1.5uH
- **R13** — 1M1
- **R14** — 180k
- **C16** — 22u
- **C17** — 22u
- **C18** — 100n
- **C22** — 22u
- **C23** — 22u
- **C24** — 22u
- **C25** — 100n
- **C30** — 100n
- **C33** — 1u
- **C34** — 1u

### Buck, 1.8V@300mA

- **U8** — TPS62748YFPT
  - Pin labels:
    - A1: SW
    - B1: EN
    - C1: VSEL
    - D1: CTRL
    - A2: VIN
    - B2: GND
    - C2: VOS
    - D2: LOAD
- **L3** — 2u2
- **R19** — 10M
- **C20** — 22u
- **C26** — 100n
- **C27** — 22u
- **C31** — 100n
- **C32** — 100n

### Boost, 3.3V@150mA

- **U7** — MAX17225ELT+
  - Pin labels:
    - 1: OUT
    - 2: LX
    - 3: GND
    - 4: SEL
    - 5: IN
    - 6: EN
- **L1** — 2u2
- **R17** — 82k
- **C2** — 22u
- **C19** — 100n
- **C28** — 100n
- **C29** — 22u

## Connectors

- No connector reference designators are visible on this sheet page.

## Named Nets / Signals

- **VMAIN**
- **GND**
- **EN_F_BAT**
- **F_BAT**
- **F_VIO**
- **1V8**
- **N_EN**
- **N_VIO**

## Design Notes

### Buck - Boost, 3.6V@2A

- DESIGN NOTE:
  - C[0805] @ 5V ≈ 7uF
  - Cin rec. = 10uF
  - Cout rec. = 3x22uF

- DESIGN NOTE:
  - V[FB] = 500mV
  - Rx = Ry * ((V[OUT] / V[FB]) - 1)
  - Rx = 1.1MΩ for 3.6V

### Buck, 1.8V@300mA

- DESIGN NOTE:
  - C[0805] @ 5V ≈ 7uF
  - Cin rec. = 4u7
  - Cout rec. = 10uF

### Boost, 3.3V@150mA

- DESIGN NOTE:
  - C[0805] @ 5V ≈ 7uF
  - Cin rec. = 10uF
  - Cout rec. = 10uF

## Title Block / Document Notes

- Proprietary note:
  - “This document is the exclusive property of Byte Lab d.o.o. Company and it should not be distributed or reproduced into any other format without prior permission from Byte Lab d.o.o.”
- **Title:** 07_POWER-RAILS.SchDoc
- **Project:** 100275_NOTECARRIER-F.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Hamin
- **Acceptor:** T. Zvonc
- **Sheet:** 7 of 7
- **Rev:** 11
- **Format:** A4

## Page 8

# Title / Board Text

- **NOTECARRIER-F**
- **V1.3**
- **blues** logo/text
- **NOTECARD USB**
- **QWIIC**
- **QWIIC**

# Component Reference Designators

- No component reference designators are readable in the provided image.

# Connectors and Pin Labels

## Top Power Connectors

- **V+** connector
  - Pin labels: `-`, `+`
- **VBAT** connector
  - Pin labels: `-`, `+`
- **SOLAR** connector
  - Pin labels: `-`, `+`

## Left Vertical Header

Top to bottom:

- `F_3V3`
- `VUSB`
- `VBAT`
- `VMAIN`
- `N_VIO`
- `VSOLAR`
- `V+`
- `GND`
- `N_EN`
- `N_NRST`
- `N_BOOT`
- `N_SCL`
- `N_SDA`
- `N_ATTN`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `N_RX`
- `N_TX`
- `GND`

## Right Vertical Header

Top to bottom:

- `F_NRST`
- `F_EN`
- `SDA`
- `SCL`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_B0`
- `F_TX`
- `F_RX`
- `F_MISO`
- `F_MOSI`
- `F_SCK`
- `F_A5`
- `F_A4`
- `F_A3`
- `F_A2`
- `F_A1`
- `F_A0`
- `F_AREF`

## Upper Horizontal Header

Left to right:

- `B0`
- `TX`
- `RX`
- `MISO`
- `MOSI`
- `SCK`
- `A5`
- `A4`
- `A3`
- `A2`
- `A1`
- `A0`
- `GND`
- `AREF`
- `3V3`
- `NRST`

## Lower Horizontal Header

Left to right:

- `F_SDA`
- `F_SCL`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `VUSB`
- `F_EN`
- `F_BAT`

## Small 2-Pin Header / Pads

- Pin labels:
  - `RTX`
  - `CTX`

## Bottom Connectors

- **NOTECARD USB**
  - Pin labels not readable
- **QWIIC**
  - Pin labels not readable
- **QWIIC**
  - Pin labels not readable

# Other Labeled Items

- Pushbutton / pad label: `N_NRST`

# Named Nets / Signals

- `3V3`
- `A0`
- `A1`
- `A2`
- `A3`
- `A4`
- `A5`
- `AREF`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `B0`
- `CTX`
- `F_3V3`
- `F_A0`
- `F_A1`
- `F_A2`
- `F_A3`
- `F_A4`
- `F_A5`
- `F_AREF`
- `F_B0`
- `F_BAT`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_EN`
- `F_MISO`
- `F_MOSI`
- `F_NRST`
- `F_RX`
- `F_SCK`
- `F_SCL`
- `F_SDA`
- `F_TX`
- `GND`
- `MISO`
- `MOSI`
- `N_ATTN`
- `N_BOOT`
- `N_EN`
- `N_NRST`
- `N_RX`
- `N_SCL`
- `N_SDA`
- `N_TX`
- `N_VIO`
- `NRST`
- `RTX`
- `SCK`
- `SCL`
- `SDA`
- `SOLAR`
- `TX`
- `RX`
- `VBAT`
- `VMAIN`
- `VSOLAR`
- `VUSB`
- `V+`

## Page 9

# Components / Reference Designators

- No component reference designators or values are readable in the image.
- Readable non-refdes labels:
  - `SIM` — SIM card connector area
  - `GPS ANT.` — selector area with labels `PASSIVE` and `ACTIVE`
  - `FEATHER_EN` — selector area with labels `ON` and `N_ATTN`
  - `AUX` — selector area with labels `NORMAL` and `DFU`
  - `RTX` / `CTX` — 2-pin pad/header area

# Connectors and Pin Labels

## Left Side Header

Top to bottom:

- `F_NRST`
- `F_EN`
- `SDA`
- `SCL`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_B0`
- `F_TX`
- `F_RX`
- `F_MISO`
- `F_MOSI`
- `F_SCK`
- `F_A5`
- `F_A4`
- `F_A3`
- `F_A2`
- `F_A1`
- `F_A0`
- `F_AREF`

## Right Side Header

Top to bottom:

- `F_3V3`
- `VUSB`
- `VBAT`
- `VMAIN`
- `N_VIO`
- `VSOLAR`
- `V+`
- `GND`
- `N_EN`
- `N_NRST`
- `N_BOOT`
- `N_SCL`
- `N_SDA`
- `N_ATTN`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `N_RX`
- `N_TX`
- `GND`

## SIM Connector

- Label: `SIM`
- Individual pin labels are not readable.

## RTX / CTX Pads or Header

- `RTX`
- `CTX`

# Named Nets / Signals

- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `CTX`
- `F_3V3`
- `F_A0`
- `F_A1`
- `F_A2`
- `F_A3`
- `F_A4`
- `F_A5`
- `F_AREF`
- `F_B0`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_EN`
- `F_MISO`
- `F_MOSI`
- `F_NRST`
- `F_RX`
- `F_SCK`
- `F_TX`
- `GND`
- `N_ATTN`
- `N_BOOT`
- `N_EN`
- `N_NRST`
- `N_RX`
- `N_SCL`
- `N_SDA`
- `N_TX`
- `N_VIO`
- `RTX`
- `SCL`
- `SDA`
- `VBAT`
- `VMAIN`
- `VSOLAR`
- `VUSB`
- `V+`

# Printed Notes / Labels

- `SOLAR 3.5V - 7V`
- `VBAT 3.3V - 4.2V`
- `V+ 2.5V - 5.5V`
- `GPS ANT.`
  - `PASSIVE`
  - `ACTIVE`
- `FEATHER_EN`
  - `ON`
  - `N_ATTN`
- `AUX`
  - `NORMAL`
  - `DFU`

# Title Block

- No title block text is visible.

## Page 10

## Source Type

- Image appears to be a 3D PCB render, not a schematic page.
- No readable component reference designators such as R/C/U/J numbers are visible.

## Board / Title Text

- `NOTECARRIER-F`
- `v1.3`
- `blues` logo on module
- `QWIIC` labels near two bottom connectors
- `SOLAR` label near top connector
- `VBAT` label near top connector

## Components / Parts Visible

- Notecard module with `blues` logo
- Board: `NOTECARRIER-F v1.3`
- Two connectors labeled `QWIIC`
- One connector labeled `VBAT`
- One connector labeled `SOLAR`
- One USB connector; nearby text appears to reference Notecarrier USB, but full label is not clearly readable
- Multiple pin-header connector rows
- Multiple JST-style connectors at top edge

## Connectors and Pin Labels

### Left Side Header

Readable labels, top to bottom:

- `F_3V3`
- `VUSB`
- `VBAT`
- `VMAIN`
- `N_VIO`
- `VSOLAR`
- `V+`
- `GND`
- `N_EN`
- `N_NRST`
- `N_BOOT`
- `N_SCL`
- `N_SDA`
- `N_ATTN`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `N_RX`
- `N_TX`
- `GND`

### Right Side Header

Readable labels, top to bottom:

- `F_NRST`
- `F_EN`
- `SDA`
- `SCL`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_B0`
- `F_TX`
- `F_RX`
- `F_MISO`
- `F_MOSI`
- `F_SCK`
- `F_A5`
- `F_A4`
- `F_A3`
- `F_A2`
- `F_A1`
- `F_A0`

### Top Connectors

- Connector labeled `VBAT`
  - Polarity markings visible: `+`, `-`
- Connector labeled `SOLAR`
  - Polarity markings visible: `+`, `-`
- Left top connector:
  - Polarity markings visible: `+`, `-`
  - Other label not clearly readable

### Central / Feather-Style Header Area

Readable labels near the large horizontal header:

- `F_B0`
- `F_TX`
- `F_RX`
- `F_MISO`
- `F_MOSI`
- `F_SCK`
- `F_A5`
- `F_A4`
- `F_A3`
- `F_A2`
- `F_A1`
- `F_A0`
- `GND`
- `F_AREF`
- `F_3V3`
- `F_NRST`

### Bottom Connectors

- USB connector
  - Nearby text partially readable; appears to include `... USB`
- Two connectors labeled `QWIIC`
  - Pin labels are not clearly readable in the image

## Named Nets / Signals

- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `F_3V3`
- `F_A0`
- `F_A1`
- `F_A2`
- `F_A3`
- `F_A4`
- `F_A5`
- `F_AREF`
- `F_B0`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_EN`
- `F_MISO`
- `F_MOSI`
- `F_NRST`
- `F_RX`
- `F_SCK`
- `F_TX`
- `GND`
- `N_ATTN`
- `N_BOOT`
- `N_EN`
- `N_NRST`
- `N_RX`
- `N_SCL`
- `N_SDA`
- `N_TX`
- `N_VIO`
- `SCL`
- `SDA`
- `VBAT`
- `VMAIN`
- `VSOLAR`
- `VUSB`
- `V+`
- `SOLAR`

## Page 11

# Transcription

## Component Reference Designators

- No component reference designators are readable in the image.
- No component values/part numbers are readable, except board silkscreen functional labels noted below.

## Connectors and Pin Labels

### Left Edge Header

Top to bottom:

- F_NRST
- F_EN
- SDA
- SCL
- F_D5
- F_D6
- F_D9
- F_D10
- F_D11
- F_D12
- F_D13
- F_B0
- F_TX
- F_RX
- F_MISO
- F_MOSI
- F_SCK
- F_A5
- F_A4
- F_A3
- F_A2
- F_A1
- F_A0
- F_AREF

### Right Edge Header

Top to bottom:

- 3V3
- VUSB
- VBAT
- VMAIN
- N_VIO
- VSOLAR
- V
- GND
- N_EN
- N_NRST
- N_BOOT
- N_SCL
- N_SDA
- N_LATTN
- AUX_EN
- AUX_RX
- AUX_TX
- AUX1
- AUX2
- AUX3
- AUX4
- N_RX
- N_TX
- GND

### SIM Connector

- Label: SIM
- Individual pin labels not visible.

### Test Pads / Small Pad Connector

- RTX
- CTX

### GPS Antenna Area

- GPS ANT
- PASSIVE
- ACTIVE

### AUX Switch / Header Area

- NORMAL
- AUX
- DFU

### Feather Enable Area

- FEATHER_EN
- ON
- Other nearby label partially unreadable.

## Named Nets / Signals

- 3V3
- VUSB
- VBAT
- VMAIN
- N_VIO
- VSOLAR
- GND
- N_EN
- N_NRST
- N_BOOT
- N_SCL
- N_SDA
- N_LATTN
- N_RX
- N_TX
- AUX_EN
- AUX_RX
- AUX_TX
- AUX1
- AUX2
- AUX3
- AUX4
- F_NRST
- F_EN
- SDA
- SCL
- F_D5
- F_D6
- F_D9
- F_D10
- F_D11
- F_D12
- F_D13
- F_B0
- F_TX
- F_RX
- F_MISO
- F_MOSI
- F_SCK
- F_A5
- F_A4
- F_A3
- F_A2
- F_A1
- F_A0
- F_AREF
- RTX
- CTX

## Power / Input Labels

- SOLAR: `3.5V - 7V`
- VBAT: voltage text partially unreadable
- VUSB: voltage text partially unreadable

## Title Block / Notes

- No title block is visible.
- No schematic notes are visible.
