---
product: Notecarrier-XP
version: v3.1
doc_type: schematic
source_file: Notecarrier-XP/v3.1/100380_notecarrier-xp_Rev-13.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-XP — SCHEMATIC (v3.1)

_Source: `Notecarrier-XP/v3.1/100380_notecarrier-xp_Rev-13.PDF`_

## Page 1

# Notecarrier-XP — Cover Sheet

## Module

- Module name: **Notecarrier-XP**
- Copyright: **© 2023 Blues Inc.**

## Sheet Index

- **01** — Cover
- **02** — Block Diagram
- **03** — IO Connectors
- **04** — Notecard Connector
- **05** — Power

## Components / Board Items

- **PCB1** — PCB, **2200-925**
- **DOC1** — HW-E, **100380**
- **FD1** — board support / fiducial, TOP
- **FD2** — board support / fiducial, TOP
- **FD3** — board support / fiducial, TOP
- **FD4** — board support / fiducial, TOP
- **FD5** — board support / fiducial, BOTTOM
- **FD6** — board support / fiducial, BOTTOM

## Connectors

- No connectors shown on this sheet.

## Named Nets / Signals

- No named nets or signals shown on this sheet.

## Design Considerations

- **Software config note:**
  - Contains important notes for software development.
  - Things like: pin configuration, timing requirements, IC configuration etc.
- **Design note:**
  - Hardware notes

## Revision Block

| Proto Rev | Prod Rev | Date | Description | # VAR | # BOM | # ECO |
|---:|---|---|---|---:|---|---|
| 10 | - | 2024-04-18 | Initial prototype release | 1 | 3000-765-001 | |
| 11 | - | 2024-06-06 | Fixed M.2 screw position, silkscreen | 1 | 3000-795-001 | |
| 12 | - | 2024-06-14 | Connected U3.A1 to EN_VMODEM, silkscreen | 1 | 3000-807-001 | |
| 13 | - | 2024-06-17 | EN_XP implemented, silkscreen | 1 | 3000-808-001 | |

## List of Available Variants

- Table present with columns:
  - # VAR
  - Variant name
  - Description
- No variant entries filled in on this sheet.

## Revision Format Explanation

| Proto Rev | Prod Rev | Date Format | Description | BOM Format |
|---|---|---|---|---|
| - | - | 202y-mm-dd | Development phase, date only | - |
| 10 | - | 202y-mm-dd | Prototyping phase, revision numeric | 3000-xxx-xxx |
| - | A | 202y-mm-dd | Production phase, revision alphanumeric | 3000-xxx-xxx |

## Title Block Notes

- **Title:** 01_COVER.SchDoc
- **Project:** 100380_notecarrier-xp.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** M. Marsic
- **Acceptor:** J. Wiedey
- **Sheet:** 1 of 5
- **Revision:** 13
- **Format:** A4

## Page 2

# Schematic Page Transcription

## Title Block / Notes

- Copyright: © 2023 Blues Inc.
- Title: `02_BLOCK-DIAGRAM.SchDoc`
- Project: `100380_notecarrier-xp.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: `www.byte-lab.com`
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 2 of 5
- Rev: 13
- Format: A4

## Component Reference Designators

- No component reference designators are visible on this page.

## Functional Blocks / Parts Shown

- USB C
- ORING
- Buck/Boost 3V8/3V3
- Buck/Boost 3V3
- PIN HEADER
- M.2 CONNECTOR KEY E

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
- `VIO_EN`
- `VMODEM_SEL`
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
- `VIO_EN`
- `VMODEM_SEL`
- `I2C`
- `UART`
- `AUX_UART`
- `AUX_GPIO`
- `DFU`
- `NRST`
- `ATTN`

## Page 3

# 03_IO-CONNECTION.SchDoc

## Sections

- I/O Pin Headers & Castellations
- USB C Connector

## Components

- **P1**: Header 2.54mm 1x16
- **P2**: Header 2.54mm 1x16
- **P3**: 12402012E212A, USB C connector
- **R1**: 5k1
- **R2**: 5k1
- **R3**: 1M
- **C1**: 10n/1000V

## Connectors

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

### P3 — USB C Connector, 12402012E212A

- A4: VBUS, net +VUSB
- A9: VBUS, net +VUSB
- A5: CC1, connected to R1 5k1 to GND
- A6: D+, net USB_D_P
- A7: D-, net USB_D_N
- A8: SBU1, no connection shown
- A1: GND
- A12: GND
- M: USB_SHIELD
- B4: VBUS, net +VUSB
- B9: VBUS, net +VUSB
- B5: CC2, connected to R2 5k1 to GND
- B6: D+, net USB_D_P
- B7: D-, net USB_D_N
- B8: SBU2, no connection shown
- B1: GND
- B12: GND

## Named Nets / Signals

- +VBAT
- +VUSB
- +VMAIN
- +VIO
- BOOT
- NRST
- AUX_NCHARGING
- VIO_EN
- +VACT_GPS_OUT
- +VACT_GPS_IN
- ALT_DFU_IDLE
- ALT_DFU_NRESET
- ALT_DFU_BOOT
- ALT_DFU_TX
- ALT_DFU_RX
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
- USB_D_P
- USB_D_N
- USB_SHIELD

## USB C Connector Related Connections

- **R1 5k1**: CC1 / A5 to GND
- **R2 5k1**: CC2 / B5 to GND
- **R3 1M**: USB_SHIELD to GND
- **C1 10n/1000V**: USB_SHIELD to GND
- **+VUSB**: connected to P3 VBUS pins A4, A9, B4, B9
- **USB_D_P**: connected to P3 D+ pins A6 and B6
- **USB_D_N**: connected to P3 D- pins A7 and B7

## Title Block / Notes

- Copyright © 2023 Blues Inc.
- Title: 03_IO-CONNECTION.SchDoc
- Project: 100380_notecarrier-xp.PrjPCB
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 3 of 5
- Rev: 13
- Format: A4

## Page 4

## Page / Sections

- Copyright © 2023 Blues Inc.
- Sections:
  - Notecard Connector
  - SIM Card
  - Notecard Support

## Components

- J1: MDT420E01001
- J2: SF72S006VBDR2500, NanoSIM
- R4: 0R0
- R6: 22R
- R7: 22R
- R8: 15k
- R9: 22R
- C3: 100n
- C4: 33p
- C5: 33p
- C6: 33p
- TVS1: PESD5V0L5UV,125
- TP1: PCB Testpoint
- ASS1: KNOB M2.5x4-INOX
- OBJ1: 9774025151R

## Connectors

### J1 — MDT420E01001

- Pin 1: XP_VREF
- Pin 2: VIO_P
- Pin 3: GND
- Pin 4: VIO_P
- Pin 5: GND
- Pin 6: GND
- Pin 7: USB_DP
- Pin 8: SIM_VCC
- Pin 9: USB_DN
- Pin 10: SIM_RST
- Pin 11: GND
- Pin 12: SIM_IO
- Pin 13: VUSB
- Pin 14: SIM_CLK
- Pin 15: NC15
- Pin 16: SIM_PRESENT
- Pin 17: NC17
- Pin 18: GND
- Pin 19: NC19
- Pin 20: VACT_GPS_OUT
- Pin 21: NC21
- Pin 22: VACT_GPS_IN
- Pin 23: EN_VMODEM
- Pin 32: ALT_DFU_BOOT
- Pin 33: GND
- Pin 34: ALT_DFU_RESET
- Pin 35: NC35
- Pin 36: ALT_DFU_ACTIVE
- Pin 37: NC37
- Pin 38: AUX_CHARGING
- Pin 39: GND
- Pin 40: SCL_P
- Pin 41: ALT_DFU_RX
- Pin 42: SDA_P
- Pin 43: ALT_DFU_TX
- Pin 44: NC44
- Pin 45: GND
- Pin 46: AUX1
- Pin 47: RTX
- Pin 48: AUX2
- Pin 49: CTX
- Pin 50: AUX3
- Pin 51: GND
- Pin 52: AUX4
- Pin 53: NC53
- Pin 54: ATTN_P
- Pin 55: NC55
- Pin 56: AUX_EN_P
- Pin 57: GND
- Pin 58: AUX_RX_P
- Pin 59: NC59
- Pin 60: AUX_TX_P
- Pin 61: NC61
- Pin 62: RX_P
- Pin 63: NC63
- Pin 64: TX_P
- Pin 65: BOOT
- Pin 66: NC66
- Pin 67: RST
- Pin 68: NC68
- Pin 69: NC69
- Pin 70: VMODEM_P
- Pin 71: GND
- Pin 72: VMODEM_P
- Pin 73: GND
- Pin 74: VMODEM_P
- Pin 75: XP_PRESENT

### J2 — SF72S006VBDR2500, NanoSIM

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

## Named Nets / Signals

- +VIO
- GND
- SIM_VCC
- SIM_RST
- SIM_IO
- SIM_CLK
- SIM_NPRESENT
- SIM_PRESENT
- +VACT_GPS_OUT
- +VACT_GPS_IN
- VACT_GPS_OUT
- VACT_GPS_IN
- ALT_DFU_BOOT
- ALT_DFU_NRESET
- ALT_DFU_RESET
- ALT_DFU_IDLE
- ALT_DFU_ACTIVE
- AUX_NCHARGING
- AUX_CHARGING
- SCL
- SCL_P
- SDA
- SDA_P
- AUX1
- AUX2
- AUX3
- AUX4
- ATTN
- ATTN_P
- AUX_EN
- AUX_EN_P
- AUX_RX
- AUX_RX_P
- AUX_TX
- AUX_TX_P
- RX
- RX_P
- TX
- TX_P
- +VMODEM
- VMODEM_P
- XP_VREF
- +VMAIN
- USB_DP
- USB_D_P
- USB_DN
- USB_D_N
- VUSB
- +VUSB
- EN_VMODEM
- ALT_DFU_RX
- ALT_DFU_TX
- RTX
- CTX
- BOOT
- NRST
- RST
- XP_PRESENT
- NC15
- NC17
- NC19
- NC21
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

## Title Block Notes

- Title: 04_NOTECARD-CONNECTION.SchDoc
- Project: 100380_notecarrier-xp.PrjPCB
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: www.byte-lab.com
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 4 of 5
- Rev: 13
- Format: A4

## Page 5

# 05_POWER.SchDoc

## Title Block

- Copyright © 2023 Blues Inc.
- Title: `05_POWER.SchDoc`
- Project: `100380_notecarrier-xp.PrjPCB`
- Company:
  - Byte Lab Grupa d.o.o.
  - Medarska 69/1, 10000 Zagreb, Croatia
  - `www.byte-lab.com`
- Author: M. Marsic
- Acceptor: J. Wiedey
- Sheet: 5 of 5
- Rev: 13
- Format: A4

## Connectors

- No connector reference designators visible on this page.

## Components

### Power ORing

- U1: `LM66200DRLR`

### 3V3 Buck/Boost Regulator

- U2: `ISL9122AIINZ-T`
- L1: `MCKK1608T1R0MN`
- C7: `22u`
- C8: `100n`
- C9: `22u`
- R10: `10M`

### 2G TX Capacitor Bank

- C10: `220u`
- C11: `220u`
- C12: `220u`
- C13: `220u`
- C14: `220u`
- C15: `220u`

### Modem Buck/Boost Regulator

- U3: `RT6160BWSC`
- L2: `XFL4020-152MEC`
- C16: `10u`
- C17: `10u`
- C2: `100n`
- R5: `10M`
- R11: `10M` marked with red X / not mounted indication

## IC Pin Labels and Connections

### U1 — LM66200DRLR

- Pin 3, `VIN1`: `+VBAT`
- Pin 6, `VIN2`: `+VUSB`
- Pin 4, `ON`: `GND`
- Pin 1, `GND`: `GND`
- Pin 5, `GND`: `GND`
- Pin 2, `VOUT`: `+VMAIN`
- Pin 7, `VOUT`: `+VMAIN`
- Pin 8, `STAT`: no-connect mark shown

### U2 — ISL9122AIINZ-T

- Pin B1, `LX1`: L1
- Pin A2, `LX2`: L1
- Pin C1, `VIN`: `+VMAIN`
- Pin B2, `VOUT`: `+VIO`
- Pin C2, `EN`: `VIO_EN` / R10 / C8 node
- Pin A1, `GND`: `GND`
- Pin D2, `SDA`: tied to lower right net shown to `GND`
- Pin D1, `SCL`: tied to lower right net shown to `GND`

### U3 — RT6160BWSC

- Pin B2, `LX1`: `IND1` / L2
- Pin B3, `LX1`: `IND1` / L2
- Pin D2, `LX2`: `IND2` / L2
- Pin D3, `LX2`: `IND2` / L2
- Pin A2, `VIN`: `+VMAIN`
- Pin A3, `VIN`: `+VMAIN`
- Pin E2, `VOUT`: `+VMODEM`
- Pin E3, `VOUT`: `+VMODEM`
- Pin A1, `EN`: `EN_VMODEM`
- Pin B1, `VSEL`: R5 / R11 / C2 node
- Pin E1, `SDA`: `GND`
- Pin D1, `SCL`: `GND`
- Pin C1, `AGND`: `GND`
- Pin C2, `PGND`: `GND`
- Pin C3, `PGND`: `GND`

## Named Nets / Signals

- `+VBAT`
- `+VUSB`
- `+VMAIN`
- `+VMODEM`
- `+VIO`
- `GND`
- `VIO_EN`
- `EN_VMODEM`
- `IND1`
- `IND2`

## Design Notes

### 3V3 Buck/Boost Regulator

- DESIGN NOTE:
  - Input Voltage: 1.8V - 5.5V
  - Output Voltage: 3.3V
  - Peak Output Current: 500mA
  - Average Current: 100mA

### Modem Buck/Boost Regulator

- DESIGN NOTE:
  - R11 and R5 shall not be mounted at the same time.

- DESIGN NOTE:
  - Input Voltage: 2.2V - 5.5V
  - Output Voltage:
    - 3.3V; VSEL = L
    - 3.85V; VSEL = H
  - Peak Output Current: 2A
  - Average Current: 250mA

## Page 6

# Board Markings

- **blues**
- **NOTECARRIER-XP**
- **V3.1**
- **XP_PRESENT**
- **ALT DFU**

# Components

- No readable component reference designators or values/parts are visible in the image.

# Connectors

## Top Header

Pin labels shown left-to-right:

- GND
- SDA
- SCL
- RX
- TX
- RTX
- CTX
- ATTN
- AUX1
- AUX2
- AUX3
- AUX4
- AUX_EN
- AUX_RX
- AUX_TX
- GND

## Bottom Header

Pin labels shown left-to-right:

- GND
- RX
- TX
- BOOT
- NRST
- IDLE
- VGPS_IN
- VGPS_OUT
- EN
- NCHG
- NRST
- BOOT
- VIO
- VMAIN
- VUSB
- VBAT

## Other Visible Connectors

- Large central card/module connector; no readable pin labels.
- USB-C connector; no readable pin labels.

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
- RTX
- RX
- SCL
- SDA
- TX
- VBAT
- VGPS_IN
- VGPS_OUT
- VIO
- VMAIN
- VUSB
- XP_PRESENT

# Title Block / Notes

- No schematic title block is visible.
- Readable board identification: **blues NOTECARRIER-XP V3.1**.

## Page 7

## Components

- No component reference designators or values are readable on this image.
- One large component has a visible top marking: `C` and `777` / `LLL`-like marking, but no reference designator is readable.

## Connectors

### Top header, left to right

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

### Bottom header, left to right

- Pin 1: `VBAT`
- Pin 2: `VUSB`
- Pin 3: `VMAIN`
- Pin 4: `VIO`
- Pin 5: `BOOT`
- Pin 6: `NRST`
- Pin 7: `NCHG`
- Pin 8: `EN`
- Pin 9: `VGPS_OUT`
- Pin 10: `VGPS_IN`
- Pin 11: `IDLE`
- Pin 12: `NRST`
- Pin 13: `BOOT`
- Pin 14: `TX`
- Pin 15: `RX`
- Pin 16: `GND`

### Right-side connector

- Large connector visible on right side.
- Pin labels are not readable.

## Named Nets / Signals

- `ALT DFU`
- `ATTN`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `AUX_EN`
- `AUX_RX`
- `AUX_TX`
- `BOOT`
- `CTX`
- `EN`
- `GND`
- `IDLE`
- `NCHG`
- `NRST`
- `RX`
- `RTX`
- `SCL`
- `SDA`
- `TX`
- `VBAT`
- `VGPS_IN`
- `VGPS_OUT`
- `VIO`
- `VMAIN`
- `VUSB`

## Title Block / Notes

- No title block is visible.
- Readable note/annotation near bottom header: `ALT DFU`
