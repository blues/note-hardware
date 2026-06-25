---
product: Notecarrier-XS
version: v1.2
doc_type: schematic
source_file: Notecarrier-XS/v1.2/100426_notecarrier-xs_Rev-11.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-XS — SCHEMATIC (v1.2)

_Source: `Notecarrier-XS/v1.2/100426_notecarrier-xs_Rev-11.PDF`_

## Page 1

# Notecarrier-XS — Cover Page

## Module

- Module name: **Notecarrier-XS**
- Copyright: **© 2023 Blues Inc.**

## Components / References

- **FD1** — board support fiducial / marker
- **FD2** — board support fiducial / marker
- **FD3** — board support fiducial / marker
- **FD4** — board support fiducial / marker
- **FD5** — board support fiducial / marker
- **FD6** — board support fiducial / marker
- **PCB1** — PCB, **2200-914**
- **DOC1** — HW-E, **100426**

## Connectors

- No connectors shown on this page.

## Named Nets / Signals

- No named nets or signals shown on this page.

## Sheet Index

- **01** — Cover
- **02** — Block Diagram
- **03** — IO Connectors
- **04** — Notecard Connector
- **05** — Power
- **05** — Starnote Connector

## Revision Block

| Proto. Rev | Prod. Rev | Date | Description | # VAR | # BOM | # ECO |
|---|---|---|---|---:|---|---|
| 10 |  | 2024-04-19 | Initial prototype release | 1 | 3000-771-001 |  |
| 11 |  | 2024-05-23 | Fixed standoff location, LED to OR0 | 1 | 3000-789-001 |  |

## List of Available Variants

- No variants listed.

## Revision Format Explanation

| Proto. Rev | Prod. Rev | Date | Description | # BOM |
|---|---|---|---|---|
| - | - | 202y-mm-dd | Development phase, date only | - |
| 10 | - | 202y-mm-dd | Prototyping phase, revision numeric | 3000-xxx-xxx |
| - | A | 202y-mm-dd | Production phase, revision alphanumeric | 3000-xxx-xxx |

## Design Considerations

- **Software config note:**
  - Contains important notes for software development.
  - Things like: pin configuration, timing requirements, IC configuration etc.
- **Design note:**
  - Hardware notes

## Board Support Notes

- **Top:** FD1, FD2, FD3, FD4
- **Bottom:** FD5, FD6
- **PCB1:** PCB, 2200-914
- **DOC1:** HW-E, 100426

## Title Block

- **Title:** 01_COVER.SchDoc
- **Project:** 100426_notecarrier-xs.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Marsic
- **Acceptor:** J. Wiedey
- **Sheet:** 1 of 5
- **Revision:** 11
- **Format:** A4

## Page 2

# Schematic Page Transcription

## Components / Blocks

- No component reference designators are visible on this page.

- USB C
  - Part/value shown: USB C

- BAT JST
  - Part/value shown: BAT JST

- LiPo Charger
  - Part/value shown: LiPo Charger

- PIN HEADER
  - Part/value shown: PIN HEADER

- Buck 3V3
  - Part/value shown: Buck 3V3

- M.2 CONNECTORKEY E
  - Associated module/block: Notecard

- M.2 CONNECTORKEY E
  - Associated module/block: Starnote

## Connectors and Pin / Signal Labels

- USB C
  - `+VUSB`

- BAT JST
  - `+VBAT`

- PIN HEADER
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

- M.2 CONNECTORKEY E — Notecard
  - `+VMODEM`
  - `STATUS`
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

- M.2 CONNECTORKEY E — Starnote
  - `+VMODEM`
  - `UART`
  - `+VIO`

## Named Nets / Signals

- `+VUSB`
- `+VBAT`
- `+VMAIN`
- `+VMODEM`
- `+VIO`
- `+VACT_GPS_IN`
- `+VACT_GPS_OUT`
- `I2C`
- `STATUS`
- `UART`
- `AUX_UART`
- `AUX_GPIO`
- `DFU`
- `NRST`
- `ATTN`

## Title Block / Notes

- Copyright © 2023 Blues Inc.
- Title: `02_BLOCK-DIAGRAM.SchDoc`
- Project: `100426_notecarrier-xs.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 2 of 5
- Rev: 11
- Format: A4

## Page 3

# Schematic Page Transcription

## Page / Title Block Notes

- Copyright © 2023 Blues Inc.
- Title: `03_IO-CONNECTION.SchDoc`
- Project: `100426_notecarrier-xs.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: `www.byte-lab.com`
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 3 of 5
- Rev: 11
- Format: A4

## Components / Reference Designators

- P1: Header 2.54mm 1x16
- P2: Header 2.54mm 1x16
- P3: SM05B-SRSS-TB
- J1: Header 2.54mm 1x4
- P4: 12402012E212A
- R1: 5k1
- R2: 5k1
- C1: 10n/1000V
- R3: 1M
- J2: SM04B-SRSS-TB(LF)(SN)
- J3: S2B-PH-SM4-K-TB

## Connectors and Pin Labels

### P1 — Header 2.54mm 1x16

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

### P2 — Header 2.54mm 1x16

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
- Pin 12: `TX` / `NC_TX`
- Pin 13: `RX` / `NC_RX`
- Pin 14: `SCL`
- Pin 15: `SDA`
- Pin 16: `GND`

### P3 — ESLOV Connector, SM05B-SRSS-TB

- Pin 1: `+VESLOV`
- Pin 2: `ATTN`
- Pin 3: `SCL`
- Pin 4: `SDA`
- Pin 5: `GND`
- MP1: no-connect mark shown
- MP2: no-connect mark shown

### J1 — Mech Support Connector, Header 2.54mm 1x4

- Pin 1: no-connect mark shown
- Pin 2: no-connect mark shown
- Pin 3: no-connect mark shown
- Pin 4: no-connect mark shown

### P4 — USB C Connector, 12402012E212A

- A4: `VBUS`, connected to `+VUSB`
- A9: `VBUS`, connected to `+VUSB`
- B4: `VBUS`, connected to `+VUSB`
- B9: `VBUS`, connected to `+VUSB`
- A5: `CC1`, connected through R1 5k1 to `GND`
- B5: `CC2`, connected through R2 5k1 to `GND`
- A6: `D+`, connected to `USB_D_P`
- B6: `D+`, connected to `USB_D_P`
- A7: `D-`, connected to `USB_D_N`
- B7: `D-`, connected to `USB_D_N`
- A8: `SBU1`, no-connect mark shown
- B8: `SBU2`, no-connect mark shown
- A1: `GND`
- A12: `GND`
- B1: `GND`
- B12: `GND`
- M: connected to `USB_SHIELD`

### J2 — QWIIC Connector, SM04B-SRSS-TB(LF)(SN)

- Pin 1: `GND`
- Pin 2: `+VIO`
- Pin 3: `SDA`
- Pin 4: `SCL`

### J3 — Battery Connector, S2B-PH-SM4-K-TB

- Pin 1: `+VBAT`
- Pin 2: `GND`
- M: no-connect mark shown

## Other Circuit Connections

- R1: 5k1 from USB-C `CC1` to `GND`
- R2: 5k1 from USB-C `CC2` to `GND`
- C1: 10n/1000V between `USB_SHIELD` and `GND`
- R3: 1M between `USB_SHIELD` and `GND`

## Named Nets / Signals

- `+VBAT`
- `+VUSB`
- `+VMAIN`
- `+VIO`
- `+VACT_GPS_OUT`
- `+VACT_GPS_IN`
- `+VESLOV`
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
- `NC_TX`
- `NC_RX`
- `SCL`
- `SDA`
- `USB_D_P`
- `USB_D_N`
- `USB_SHIELD`

## Design Notes

- QWIIC Connector note: “The I2C bus is pulled up by the Notecard”
- Battery Connector note: “Li-Po Battery 3.3V - 4.2V”

## Page 4

# Schematic Page Transcription

## Title Block / Notes

- Copyright © 2023 Blues Inc.
- Title: `04_NOTECARD-CONNECTION.SchDoc`
- Project: `100426_notecarrier-xs.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: `www.byte-lab.com`
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 4 of 5
- Rev: 11
- Format: A4

## Components

- J4 — `MQT420E01001`
- J5 — `SF72S006VBDR2500`
- R4 — `0R0`
- R5 — `22R`
- R6 — `22R`
- R7 — `15k`
- R8 — `22R`
- C2 — `100n`
- C3 — `33p`
- C4 — `33p`
- C5 — `33p`
- TVS1 — `PESD5V0L5UV,125`
- ASS1 — `KNOB M2.5x4-INOX`
- OBJ1 — `9774025151R`

## J4 Notecard Connector

Part: `MQT420E01001`

### Bottom / Left-Side Pins

- Pin 2: `VIO_P` — `+VIO`
- Pin 4: `VIO_P` — `+VIO`
- Pin 6: `GND`
- Pin 8: `SIM_VCC`
- Pin 10: `SIM_RST`
- Pin 12: `SIM_IO`
- Pin 14: `SIM_CLK`
- Pin 16: `SIM_NPRESENT`
- Pin 18: `GND`
- Pin 20: `VACT_GPS_OUT` — `+VACT_GPS_OUT`
- Pin 22: `VACT_GPS_IN` — `+VACT_GPS_IN`
- Pin 32: `ALT_DFU_BOOT`
- Pin 34: `ALT_DFU_RESET` — net label `ALT_DFU_NRESET`
- Pin 36: `ALT_DFU_ACTIVE` — net label `ALT_DFU_IDLE`
- Pin 38: `AUX_CHARGING` — net label `AUX_NCHARGING`
- Pin 40: `SCL_P` — `SCL`
- Pin 42: `SDA_P` — `SDA`
- Pin 44: `NC44` — no connect shown
- Pin 46: `AUX1`
- Pin 48: `AUX2`
- Pin 50: `AUX3`
- Pin 52: `AUX4`
- Pin 54: `ATTN_P` — `ATTN`
- Pin 56: `AUX_EN_P` — `AUX_EN`
- Pin 58: `AUX_RX_P` — `AUX_RX`
- Pin 60: `AUX_TX_P` — `AUX_TX`
- Pin 62: `RX_P` — net label `NC_RX`, port label `RX`
- Pin 64: `TX_P` — net label `NC_TX`, port label `TX`
- Pin 66: `NC66` — no connect shown
- Pin 68: `NC68` — no connect shown
- Pin 70: `VMODEM_P` — `+VMODEM`
- Pin 72: `VMODEM_P` — `+VMODEM`
- Pin 74: `VMODEM_P` — `+VMODEM`

### Top / Right-Side Pins

- Pin 1: `XP_ENABLE` — no connect shown
- Pin 3: `GND`
- Pin 5: `GND`
- Pin 7: `USB_DP` — net label `USB_D_P`
- Pin 9: `USB_DN` — net label `USB_D_N`
- Pin 11: `GND`
- Pin 13: `VUSB` — `+VUSB`
- Pin 15: `NC15` — no connect shown
- Pin 17: `NC17` — no connect shown
- Pin 19: `NC19` — no connect shown
- Pin 21: `NC21` — no connect shown
- Pin 23: `NC23` — no connect shown
- Pin 33: `GND`
- Pin 35: `NC35` — no connect shown
- Pin 37: `NC37` — no connect shown
- Pin 39: `GND`
- Pin 41: `ALT_DFU_RX`
- Pin 43: `ALT_DFU_TX`
- Pin 45: `GND`
- Pin 47: `RTX`
- Pin 49: `CTX`
- Pin 51: `GND`
- Pin 53: `NC53` — no connect shown
- Pin 55: `NC55` — no connect shown
- Pin 57: `GND`
- Pin 59: `NC59` — no connect shown
- Pin 61: `NC61` — no connect shown
- Pin 63: `NC63` — no connect shown
- Pin 65: `BOOT`
- Pin 67: `RST` — net label `NRST`
- Pin 69: `NC69` — no connect shown
- Pin 71: `GND`
- Pin 73: `GND`
- Pin 75: `XP_MODEM_VSEL` — no connect shown

## J5 SIM Card Connector

Part: `SF72S006VBDR2500`

- Pin 1: `VCC` — `SIM_VCC`
- Pin 2: `RST` — through R5 to `SIM_RST`
- Pin 3: `CLK` — through R6 to `SIM_CLK`
- Pin 5: `GND`
- Pin 6: `VPP`
- Pin 7: `IO` — through R8 to `SIM_IO`
- Pin 8: `GND`
- Pin 9: `GND`
- Pin 10: `CSW`
- Pin 11: `GND`
- Pin 12: `GND`
- Pin 13: `DSW` — `SIM_NPRESENT`
- Pin 14: `GND`
- Pin 15: `GND`
- Pin 16: `GND`
- Pin 17: `GND`
- Pin 18: `GND`
- Pin 19: `GND`

## Notecard Support

- ASS1 — `KNOB M2.5x4-INOX`
- OBJ1 — `9774025151R`
  - Pin 1 connected to `GND`

## Named Nets / Signals

- `+VIO`
- `GND`
- `SIM_VCC`
- `SIM_RST`
- `SIM_IO`
- `SIM_CLK`
- `SIM_NPRESENT`
- `+VACT_GPS_OUT`
- `+VACT_GPS_IN`
- `ALT_DFU_BOOT`
- `ALT_DFU_NRESET`
- `ALT_DFU_IDLE`
- `AUX_NCHARGING`
- `SCL`
- `SDA`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `ATTN`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `RX`
- `TX`
- `NC_RX`
- `NC_TX`
- `+VMODEM`
- `USB_D_P`
- `USB_D_N`
- `+VUSB`
- `ALT_DFU_RX`
- `ALT_DFU_TX`
- `RTX`
- `CTX`
- `BOOT`
- `NRST`

## Page 5

# 05_POWER.SchDoc

## Page / Title Block Notes

- Copyright © 2023 Blues Inc.
- Title: `05_POWER.SchDoc`
- Project: `100426_notecarrier-xs.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: `www.byte-lab.com`
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 5 of 5
- Rev: 11
- Format: A4

## Functional Blocks

- Battery Charger w/ Power Path
- 3V3 Buck/Boost Regulator
- VBUS ORing

## Design Notes

### Battery Charger w/ Power Path

- Charger:
  - Default charging voltage: 4.2V
  - Default charging current: 320mA
  - Default termination current: 20mA
  - Default pre-charge current: 20mA
  - No battery thermal protection
- Power Path:
  - Input current limit: 3.5A
  - 26mOhm reverse blocking transistor
  - 15mOhm battery transistor
- Buck Regulator:
  - 1.5MHz frequency
  - Input Voltage: 5V
  - Output Voltage: 3.3-4.2V
  - Peak current: 2.5A

### 3V3 Buck/Boost Regulator

- Input Voltage: 1.8V - 5.5V
- Output Voltage: 3.3V
- Peak Output Current: 500mA
- Average Current: 100mA

## Components

### Battery Charger w/ Power Path

- `U2` — `BQ25628ERYKR`
  - Pin labels visible:
    - `18` VBUS
    - `12` SDA
    - `13` SCL
    - `11` INT
    - `14` CE
    - `3` PG
    - `10` STAT
    - `7` QON
    - `17` PMID
    - `2` REGN
    - `16` SW
    - `1` BTST
    - `9` SYS
    - `4` ILIM
    - `5` TS_BIAS
    - `6` TS
    - `8` BAT
    - `15` GND
- `LD1` — `SML-P12WTT86R`
- `L2` — `XFL4020-152MEC`
- `R10` — `0R0`
- `R11` — `3k`
- `R12` — `3k`
- `R13` — `11k`
- `R14` — `15k`
- `C9` — `47n/50V`
- `C10` — `100n`
- `C11` — `10u`
- `C12` — `10u`
- `C13` — `4u7`
- `C14` — `10u`
- `C15` — `100n`
- `C16` — `4u7`

### 3V3 Buck/Boost Regulator

- `U1` — `ISL9122AIINZ-T`
  - Pin / ball labels visible:
    - `B1` LX1
    - `A2` LX2
    - `C1` VIN
    - `B2` VOUT
    - `C2` EN
    - `A1` GND
    - `D2` SDA
    - `D1` SCL
- `L1` — `MCKK1608T1R0MN`
- `R9` — `10M`
- `C6` — `22u`
- `C7` — `100n`
- `C8` — `22u`

### VBUS ORing

- `U3` — `LM66200DRLR`
  - Pin labels visible:
    - `3` VIN1
    - `6` VIN2
    - `4` ON
    - `1` GND
    - `5` GND
    - `2` VOUT
    - `7` VOUT
    - `8` STAT

## Connectors

- No connector reference designators visible on this page.

## Named Nets / Signals

- `+VBUS`
- `+VMAIN`
- `+VMODEM`
- `+VBAT`
- `+VIO`
- `+VUSB`
- `+VESLOV`
- `AUX_NCHARGING`
- `SDA`
- `SCL`
- `SW`
- `VIO_EN`
- `GND`

## No-Connect Markers Visible

- `U2` pin `11` INT
- `U2` pin `3` PG
- `U2` pin `7` QON
- `U3` pin `8` STAT

## Page 6

# 06_STARNOTE-CONNECTION.SchDoc

## Notes / Sections
- Copyright © 2023 Blues Inc.
- Section: Starnote Connector
- Section: Starnote Support

## Components
- J6 — MDT420E01001
- SW1 — EVP-BB2A9B000
- ASS2 — KNOB M2.5x4-INOX
- OBJ2 — 9774025151R

## Connector J6 — MDT420E01001

### Bottom side pins
- Pin 2 — VIO_P
- Pin 4 — VIO_P
- Pin 6 — GND
- Pin 8 — SIM_VCC
- Pin 10 — SIM_RST
- Pin 12 — SIM_IO
- Pin 14 — SIM_CLK
- Pin 16 — SIM_PRESENT
- Pin 18 — GND
- Pin 20 — VACT_GPS_OUT
- Pin 22 — VACT_GPS_IN
- Pin 32 — ALT_DFU_BOOT
- Pin 34 — ALT_DFU_RESET
- Pin 36 — ALT_DFU_ACTIVE
- Pin 38 — AUX_CHARGING
- Pin 40 — SCL_P
- Pin 42 — SDA_P
- Pin 44 — NC44
- Pin 46 — AUX1
- Pin 48 — AUX2
- Pin 50 — AUX3
- Pin 52 — AUX4
- Pin 54 — ATTN_P
- Pin 56 — AUX_EN_P
- Pin 58 — AUX_RX_P
- Pin 60 — AUX_TX_P
- Pin 62 — RX_P
- Pin 64 — TX_P
- Pin 66 — NC66
- Pin 68 — NC68
- Pin 70 — VMODEM_P
- Pin 72 — VMODEM_P
- Pin 74 — VMODEM_P

### Top side pins
- Pin 1 — NC1
- Pin 3 — GND
- Pin 5 — GND
- Pin 7 — USB_DP
- Pin 9 — USB_DN
- Pin 11 — GND
- Pin 13 — VUSB
- Pin 15 — NC15
- Pin 17 — NC17
- Pin 19 — NC19
- Pin 21 — NC21
- Pin 23 — NC23
- Pin 33 — GND
- Pin 35 — NC35
- Pin 37 — NC37
- Pin 39 — GND
- Pin 41 — ALT_DFU_RX
- Pin 43 — ALT_DFU_TX
- Pin 45 — GND
- Pin 47 — RTX
- Pin 49 — CTX
- Pin 51 — GND
- Pin 53 — NC53
- Pin 55 — NC55
- Pin 57 — GND
- Pin 59 — NC59
- Pin 61 — NC61
- Pin 63 — NC63
- Pin 65 — BOOT
- Pin 67 — RST
- Pin 69 — NC69
- Pin 71 — GND
- Pin 73 — GND
- Pin 75 — NC75

## Other Connections
- SW1 — EVP-BB2A9B000
  - Connected between J6 pin 67 / RST and GND.
- OBJ2 — 9774025151R
  - Pin 1 connected to GND.
- ASS2 — KNOB M2.5x4-INOX

## Named Nets / Signals
- +VIO
- +VMODEM
- GND
- NC_TX
- NC_RX
- TX
- RX
- VIO_P
- SIM_VCC
- SIM_RST
- SIM_IO
- SIM_CLK
- SIM_PRESENT
- VACT_GPS_OUT
- VACT_GPS_IN
- ALT_DFU_BOOT
- ALT_DFU_RESET
- ALT_DFU_ACTIVE
- AUX_CHARGING
- SCL_P
- SDA_P
- AUX1
- AUX2
- AUX3
- AUX4
- ATTN_P
- AUX_EN_P
- AUX_RX_P
- AUX_TX_P
- RX_P
- TX_P
- VMODEM_P
- USB_DP
- USB_DN
- VUSB
- ALT_DFU_RX
- ALT_DFU_TX
- RTX
- CTX
- BOOT
- RST
- NC1
- NC15
- NC17
- NC19
- NC21
- NC23
- NC35
- NC37
- NC44
- NC53
- NC55
- NC59
- NC61
- NC63
- NC66
- NC68
- NC69
- NC75

## Title Block
- Title: 06_STARNOTE-CONNECTION.SchDoc
- Project: 100426_notecarrier-xs.PrjPCB
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 6 of 6
- Rev: 11
- Format: A4

## Page 7

## Readable Component Reference Designators

- No component reference designators or component values/parts are readable on this page/image.

## Connectors and Pin Labels

- **STARNOTE connector**
  - Large edge/board connector labeled: `STARNOTE`
  - No individual pin labels readable.

- **NOTECARD connector**
  - Large edge/board connector labeled: `NOTECARD`
  - No individual pin labels readable.

- **Top 4-pin header**
  - 4 through-hole pads visible.
  - No pin labels readable.

- **Upper expansion header, 16 pins**
  - Pin labels, left to right:
    - `GND`
    - `SDA`
    - `SCL`
    - `RX`
    - `TX`
    - `RTX`
    - `CTX`
    - `ATTN`
    - `AUX1`
    - `AUX2`
    - `AUX3`
    - `AUX4`
    - `AUX_EN`
    - `AUX_RX`
    - `AUX_TX`
    - `GND`

- **Lower expansion header, 16 pins**
  - Pin labels, left to right:
    - `GND`
    - `RX`
    - `TX`
    - `BOOT`
    - `NRST`
    - `ALT DFU` / `IDLE` printed near same position
    - `VGPS_IN`
    - `VGPS_OUT`
    - `EN`
    - `NCHG`
    - `NRST`
    - `BOOT`
    - `VIO`
    - `VMAIN`
    - `VUSB`
    - `VBAT`

- **QWIIC connector**
  - Connector label: `QWIIC`
  - No individual pin labels readable.

- **LIPO connector**
  - Connector label: `LIPO`
  - Pin polarity labels:
    - `-`
    - `+`

- **ESLOV connector**
  - Connector label: `ESLOV`
  - No individual pin labels readable.

## Named Nets / Signals

- `GND`
- `SDA`
- `SCL`
- `RX`
- `TX`
- `RTX`
- `CTX`
- `ATTN`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `BOOT`
- `NRST`
- `ALT DFU`
- `IDLE`
- `VGPS_IN`
- `VGPS_OUT`
- `EN`
- `NCHG`
- `VIO`
- `VMAIN`
- `VUSB`
- `VBAT`
- `+`
- `-`

## Board Text / Notes

- `STARNOTE`
- `NOTECARD`
- `NOTECARRIER-XS`
- `V1.2`
- `blues`
- `QWIIC`
- `LIPO`
- `ESLOV`

## Page 8

# Visible Components

- No component reference designators are legible.
- No component values or part numbers are legible.
- One large right-side connector/port is visible, but its reference designator and pin labels are not readable.

# Connectors

## Upper 16-pin header

Reference designator not legible. Pin labels, left to right:

- GND
- AUX_TX
- AUX_RX
- AUX_EN
- AUX4
- AUX3
- AUX2
- AUX1
- ATTN
- CTX
- RTX
- TX
- RX
- SCL
- SDA
- GND

## Lower 16-pin header

Reference designator not legible. Pin labels, left to right:

- VBAT
- VUSB
- VMAIN
- UIO
- BOOT
- NRST
- NCHG
- EN
- VGPS_OUT
- VGPS_IN
- IDLE
- NRST
- BOOT
- TX
- RX
- GND

# Named Nets / Signals

- ATTN
- AUX1
- AUX2
- AUX3
- AUX4
- AUX_EN
- AUX_RX
- AUX_TX
- BOOT
- CTX
- EN
- GND
- IDLE
- NCHG
- NRST
- RX
- RTX
- SCL
- SDA
- TX
- UIO
- VBAT
- VGPS_IN
- VGPS_OUT
- VMAIN
- VUSB

# Visible Notes / Text

- `ALT DFU`
- No title block is visible.
