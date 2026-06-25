---
product: Notecarrier-X
version: v1.2
doc_type: schematic
source_file: Notecarrier-X/v1.2/100379_notecarrier-x_Rev-11.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-X — SCHEMATIC (v1.2)

_Source: `Notecarrier-X/v1.2/100379_notecarrier-x_Rev-11.PDF`_

## Page 1

# Notecarrier-X — Cover

## Module
- Module name: **Notecarrier-X**
- Copyright: **© 2023 Blues Inc.**

## Sheet Index
- **01** — Cover
- **02** — Block Diagram
- **03** — IO Connectors
- **04** — Notecard Connector
- **05** — Power

## Components / References
- **FD1** — Fiducial / board support marker
- **FD2** — Fiducial / board support marker
- **FD3** — Fiducial / board support marker
- **FD4** — Fiducial / board support marker
- **FD5** — Fiducial / board support marker
- **FD6** — Fiducial / board support marker
- **PCB1** — PCB, part/value: **2200-918**
- **DOC1** — HW-E, part/value: **100379**

## Board Support
- **TOP**
  - FD1
  - FD2
  - FD3
  - FD4
  - FD5
- **BOTTOM**
  - FD6

## Connectors
- No connectors shown on this page.

## Named Nets / Signals
- No named nets or signals shown on this page.

## Design Considerations
- **SOFTWARE CONFIG NOTE:**
  - Contains important notes for software development.
  - Things like: pin configuration, timing requirements, IC configuration etc.
- **DESIGN NOTE:**
  - Hardware notes

## Revision Block
- **Rev. 10**
  - Proto.: 10
  - Prod.: -
  - Date: 2024-04-19
  - Description: Initial prototype release
  - # VAR: -
  - # BOM: 3000-763-001
- **Rev. 11**
  - Proto.: 11
  - Prod.: -
  - Date: 2024-04-06
  - Description: Fixed M.2 screw location
  - # VAR: -
  - # BOM: 3000-794-001

## List of Available Variants
- Table present with columns:
  - # VAR
  - Variant name
  - Description
- No variant entries shown.

## Revision Format Explanation
- Development phase, date only
  - Proto.: -
  - Prod.: -
  - Date format: 202y-mm-dd
  - # BOM: -
- Prototyping phase, revision numeric
  - Proto.: 10
  - Prod.: -
  - Date format: 202y-mm-dd
  - # BOM: 3000-xxx-xxx
- Production phase, revision alphanumeric
  - Proto.: -
  - Prod.: A
  - Date format: 202y-mm-dd
  - # BOM: 3000-xxx-xxx

## Title Block
- **Title:** 01_COVER.SchDoc
- **Project:** 100379_notecarrier-x.PrjPCB
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

## Components / Functional Blocks

- No component reference designators are visible on this page.
- Functional blocks shown:
  - USB C
  - BAT JST
  - LiPo Charger
  - Buck/Boost 3V3
  - PIN HEADER
  - M.2 CONNECTOR KEY E

## Connectors and Pin / Signal Labels

### USB C

- `+VUSB`

### BAT JST

- `+VBAT`

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
- Project: `100379_notecarrier-x.PrjPCB`
- Company:
  - Byte Lab Grupa d.o.o.
  - Medarska 69/1, 10000 Zagreb, Croatia
  - www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 2 of 5
- Rev: 11
- Format: A4

## Page 3

# Schematic Page Transcription

## Sections

- I/O Pin Headers
- ESLOV Connector
- USB C Connector
- QWIIC Connector
- Battery Connector

## Components

- P1: Header 2.54mm 1x16
- P2: Header 2.54mm 1x16
- P3: SM05B-SRSS-TB
- P4: 12402012E212A
- J1: SM04B-SRSS-TB(LF)(SN)
- J2: S2B-PH-SM4-K-TB
- R1: 5k1
- R2: 5k1
- R3: 1M
- C1: 10n/1000V

## Connectors and Pins

### P1 — Header 2.54mm 1x16

- Pin 1: +VBAT
- Pin 2: +VUSB
- Pin 3: +VMAIN
- Pin 4: +VIO
- Pin 5: BOOT
- Pin 6: NRST
- Pin 7: AUX_NCHARGING
- Pin 8: VIO_EN
- Pin 9: +VACT_GPS_OUT
- Pin 10: +VACT_GPS_IN
- Pin 11: ALT_DFU_IDLE
- Pin 12: ALT_DFU_NRESET
- Pin 13: ALT_DFU_BOOT
- Pin 14: ALT_DFU_TX
- Pin 15: ALT_DFU_RX
- Pin 16: GND

### P2 — Header 2.54mm 1x16

- Pin 1: GND
- Pin 2: AUX_TX
- Pin 3: AUX_RX
- Pin 4: AUX_EN
- Pin 5: AUX4
- Pin 6: AUX3
- Pin 7: AUX2
- Pin 8: AUX1
- Pin 9: ATTN
- Pin 10: CTX
- Pin 11: RTX
- Pin 12: TX
- Pin 13: RX
- Pin 14: SCL
- Pin 15: SDA
- Pin 16: GND

### P3 — ESLOV Connector, SM05B-SRSS-TB

- Pin 1: +VESLOV
- Pin 2: ATTN
- Pin 3: SCL
- Pin 4: SDA
- Pin 5: GND
- MP1: no connect shown
- MP2: no connect shown

### P4 — USB C Connector, 12402012E212A

- A4: VBUS, +VUSB
- A9: VBUS, +VUSB
- A5: CC1, via R1 5k1 to GND
- A6: D+, USB_D_P
- A7: D-, USB_D_N
- A8: SBU1, no connect shown
- A1: GND
- A12: GND
- M: USB_SHIELD
- B4: VBUS, +VUSB
- B9: VBUS, +VUSB
- B5: CC2, via R2 5k1 to GND
- B6: D+, USB_D_P
- B7: D-, USB_D_N
- B8: SBU2, no connect shown
- B1: GND
- B12: GND

### J1 — QWIIC Connector, SM04B-SRSS-TB(LF)(SN)

- Pin 1: GND
- Pin 2: +VIO
- Pin 3: SDA
- Pin 4: SCL

### J2 — Battery Connector, S2B-PH-SM4-K-TB

- M: no connect shown
- Pin 1: +VBAT
- Pin 2: GND

## Named Nets / Signals

- +VBAT
- +VUSB
- +VMAIN
- +VIO
- +VACT_GPS_OUT
- +VACT_GPS_IN
- +VESLOV
- ALT_DFU_IDLE
- ALT_DFU_NRESET
- ALT_DFU_BOOT
- ALT_DFU_TX
- ALT_DFU_RX
- ATTN
- AUX_NCHARGING
- AUX_TX
- AUX_RX
- AUX_EN
- AUX1
- AUX2
- AUX3
- AUX4
- BOOT
- CTX
- GND
- NRST
- RTX
- RX
- SCL
- SDA
- TX
- USB_D_P
- USB_D_N
- USB_SHIELD
- VIO_EN

## Design Notes

- QWIIC Connector:
  - DESIGN NOTE: The I2C bus is pulled up by the Notecard
- Battery Connector:
  - DESIGN NOTE: Li-Po Battery 3.3V - 4.2V

## Title Block Notes

- Copyright © 2023 Blues Inc.
- Title: 03_IO-CONNECTION.SchDoc
- Project: 100379_notecarrier-x.PrjPCB
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 3 of 5
- Rev: 11
- Format: A4

## Page 4

# Page Notes

- Copyright © 2023 Blues Inc.
- Section labels:
  - Notecard Connector
  - SIM Card
  - Notecard Support

# Components

- J3: MDT420E01001
- J4: SF72S006VBDR2500
- R4: 0R0
- R5: 22R
- R6: 22R
- R7: 15k
- R8: 22R
- C2: 100n
- C3: 33p
- C4: 33p
- C5: 33p
- TVS1: PESD5V0L5UV,125
- ASS1: KNOB M2.5x4-INOX
- OBJ1: 9774025151R

# Connectors

## J3 — MDT420E01001

### BOTTOM side pins

- Pin 2: VIO_P
- Pin 4: VIO_P
- Pin 6: GND
- Pin 8: SIM_VCC
- Pin 10: SIM_RST
- Pin 12: SIM_IO
- Pin 14: SIM_CLK
- Pin 16: SIM_NPRESENT
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

### TOP side pins

- Pin 1: XP_ENABLE
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
- Pin 75: XP_MODEM_VSEL

## J4 — SF72S006VBDR2500

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
- Internal marking: NanoSIM

# Named Nets / Signals

- +VIO
- GND
- SIM_VCC
- SIM_RST
- SIM_IO
- SIM_CLK
- SIM_NPRESENT
- +VACT_GPS_OUT
- +VACT_GPS_IN
- ALT_DFU_BOOT
- ALT_DFU_NRESET
- ALT_DFU_IDLE
- AUX_NCHARGING
- SCL
- SDA
- AUX1
- AUX2
- AUX3
- AUX4
- ATTN
- AUX_EN
- AUX_RX
- AUX_TX
- RX
- TX
- +VMODEM
- USB_D_P
- USB_D_N
- +VUSB
- ALT_DFU_RX
- ALT_DFU_TX
- RTX
- CTX
- BOOT
- NRST

# Additional Connector Signal Names

- VIO_P
- VACT_GPS_OUT
- VACT_GPS_IN
- ALT_DFU_RESET
- ALT_DFU_ACTIVE
- AUX_CHARGING
- SCL_P
- SDA_P
- ATTN_P
- AUX_EN_P
- AUX_RX_P
- AUX_TX_P
- RX_P
- TX_P
- VMODEM_P
- XP_ENABLE
- USB_DP
- USB_DN
- VUSB
- RST
- XP_MODEM_VSEL
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

# Title Block

- Title: 04_NOTECARD-CONNECTION.SchDoc
- Project: 100379_notecarrier-x.PrjPCB
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 4 of 5
- Rev: 11
- Format: A4

## Page 5

# 05_POWER.SchDoc

## Page Sections

- Battery Charger w/ Power Path
- 3V3 Buck/Boost Regulator
- VBUS ORing

## Components

### ICs

- U1 — ISL9122AIINZ-T
  - Pin labels shown:
    - A1: GND
    - A2: LX2
    - B1: LX1
    - B2: VOUT
    - C1: VIN
    - C2: EN
    - D1: SCL
    - D2: SDA

- U2 — BQ25628ERYKR
  - Pin labels shown:
    - 1: BTST
    - 2: REGN
    - 3: PG
    - 4: ILIM
    - 5: TS_BIAS
    - 6: TS
    - 7: QON
    - 8: BAT
    - 9: SYS
    - 10: STAT
    - 11: INT
    - 12: SDA
    - 13: SCL
    - 14: CE
    - 15: GND
    - 16: SW
    - 17: PMID
    - 18: VBUS

- U3 — LM66200DRLR
  - Pin labels shown:
    - 1: GND
    - 2: VOUT
    - 3: VIN1
    - 4: ON
    - 5: GND
    - 6: VIN2
    - 7: VOUT
    - 8: STAT

### Inductors

- L1 — MCKK1608T1R0MN
- L2 — XFL4020-152MEC

### Resistors

- R9 — 10M
- R10 — 0R0
- R11 — 3k
- R12 — 3k
- R13 — 11k
- R14 — 15k

### Capacitors

- C6 — 22u
- C7 — 100n
- C8 — 22u
- C9 — 47n/50V
- C10 — 100n
- C11 — 10u
- C12 — 10u
- C13 — 4u7
- C14 — 10u
- C15 — 100n
- C16 — 4u7

### LED

- LD1 — SML-P12WTT86R

## Connectors

- No connector reference designators are visible on this page.

## Named Nets / Signals

- +VBAT
- +VBUS
- +VESLOV
- +VIO
- +VMAIN
- +VMODEM
- +VUSB
- AUX_NCHARGING
- GND
- SCL
- SDA
- SW
- VIO_EN

## Design Notes

### Battery Charger w/ Power Path — Charger

- Default charging voltage: 4.2V
- Default charging current: 320mA
- Default termination current: 20mA
- Default pre-charge current: 20mA
- No battery thermal protection

### Battery Charger w/ Power Path — Power Path

- Input current limit: 3.5A
- 26mOhm reverse blocking transistor
- 15mOhm battery transistor

### Battery Charger w/ Power Path — Buck Regulator

- 1.5MHz frequency
- Input Voltage: 5V
- Output Voltage: 3.3-4.2V
- Peak current: 2.5A

### 3V3 Buck/Boost Regulator

- Input Voltage: 1.8V - 5.5V
- Output Voltage: 3.3V
- Peak Output Current: 500mA
- Average Current: 100mA

## Title Block / Page Notes

- Copyright © 2023 Blues Inc.
- Title: 05_POWER.SchDoc
- Project: 100379_notecarrier-x.PrjPCB
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 5 of 5
- Rev: 11
- Format: A4
