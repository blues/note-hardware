---
product: Notecarrier-CX
version: v1.7
doc_type: schematic
source_file: Notecarrier-CX/v1.7/Schematic/Production.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-CX — SCHEMATIC (v1.7)

_Source: `Notecarrier-CX/v1.7/Schematic/Production.PDF`_

## Page 1

# Notecarrier-CX — Cover

## Module

- Copyright: © 2023 Blues Inc.
- Module name: **Notecarrier-CX**

## Sheet Index

- **01** — Cover
- **02** — Block Diagram
- **03** — IO Connectors
- **04** — Notecard Connector
- **05** — Power
- **06** — MCU

## Components / References

- **PCB1** — PCB
  - Marking / part number: **2201-080**
- **DOC1** — HW-E
  - Marking / part number: **100544**
- **FD1** — no value/part shown
- **FD2** — no value/part shown
- **FD5** — no value/part shown
  - Nearby text: **TOP**

## Connectors

- No connectors shown on this page.

## Named Nets / Signals

- No named nets or signals shown on this page.

## Design Considerations Notes

- **SOFTWARE CONFIG NOTE:**
  - Contains important notes for software development.
  - Things like: pin configuration, timing requirements, IC configuration etc.
- **DESIGN NOTE:**
  - Hardware notes

## Revision Block

| Proto Rev | Prod Rev | Date | Description | # VAR | # BOM | # ECO |
|---:|---|---|---|---|---|---|
| 10 | - | 2025-4-23 | Initial documentation release | - | 3000-942-001 | |
| 11 | - | 2025-6-9 | Fixed USB, UART, added USER LED, swapped load SW. Used shorter capacitors to increase clearance | - | 3000-985-001 | |
| 12 | - | 2025-7-30 | Added AUX_UART pins, 0603 capacitors for clearance. Flipped header pinout, added user button, fixed CHG_LED blinking | - | 3001-001-001 | |
| 12 | - | 2025-8-19 | Added 1M pull-down to ENABLE_3V3, swapped user button logic | - | 3001-002-001 | |
| 13 | - | 2025-9-22 | Switch S1 swapped, J1 connector vertical, HOST connection default | - | 3001-018-001 | |
| 14 | - | 2025-10-07 | Switch S1 replaced, serigraphy adjusted | - | 3001-026-001 | |
| 15 | - | 2025-09-01 | Added pull up/down to SWD, added PA15 to the AUX_CHARGING, added VMAIN sense, swaped MOSI/MISO | - | - | |
| 16 | - | - | - | | | |
| 17 | - | 2026-02-12 | Moved P4 in layout to align with 2.54mm grid | | | |

## Available Variants

- No variants listed.

## Revision Format Explanation

| Proto Rev | Prod Rev | Date | Description | # BOM |
|---|---|---|---|---|
| - | - | 202y-mm-dd | Development phase, date only | - |
| 10 | - | 202y-mm-dd | Prototyping phase, revision numeric | 3000-xxx-xxx |
| - | A | 202y-mm-dd | Production phase, revision alphanumeric | 3000-xxx-xxx |

## Title Block

- **Title:** 01_COVER.SchDoc
- **Project:** 100544_notecarrier-cx.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** A.Duracic
- **Acceptor:** E. Stanisha
- **Sheet:** 1 of 6
- **Revision:** 17
- **Format:** A4

## Page 2

# Page: Power / Signals Block Diagram

## Component Reference Designators

- No component reference designators are visible on this page.
- Visible unreferenced functional blocks / parts:
  - BATT CONN
  - USB C
  - BATT CHG
  - BUCK/BOOST
  - LDO
  - PWR SWITCH
  - 0R0
  - 0R0
  - SIM Cage
  - Pin Headers
  - BOOT/RST Btns
  - Analog Switch
  - MCU
  - USER Button
  - PWR Switch
  - USB Switch
  - Toggle SW

## Connectors and Pin / Signal Labels

- BATT CONN
  - +VBAT

- USB C
  - +USB

- USB C
  - USB

- M.2 CONNECTOR KEY E
  - Notecard
  - AUX_CHARGING
  - ATTN
  - I2C
  - ALT_DFU_IDLE
  - ALT_DFU UART, BOOT, NRST
  - NC_USB

- SIM Cage
  - No pin labels shown

- Pin Headers
  - +VUSB
  - +VBAT
  - +VMAIN
  - +VIO
  - +V_AREF
  - +3V3_OUT
  - I2C
  - SPI
  - A0..5
  - D5..12
  - AUX_UART
  - EN

## Named Nets / Signals

### Power Nets

- +VBAT
- +USB
- +VMAIN
- +VMODEM
- +VIO
- +3V3_OUT
- +3V3_VUSB
- +V_AREF

### Signal Nets

- AUX_CHARGING
- ATTN
- I2C
- SPI
- A0..5
- D5..12
- AUX_UART
- EN
- IO_BOOT
- IO_NRST
- IO_BOOT/NRST
- IO_UART
- ALT_DFU_IDLE
- ALT_DFU UART, BOOT, NRST
- HST_BOOT, HST_NRST
- HST_UART
- HST_USB
- NC_USB
- USB
- USB_SW
- +3V3_ENABLE

## Title Block / Notes

- Copyright © 2023 Blues Inc.
- Title: `02_BLOCK-DIAGRAM.SchDoc`
- Project: `100544_notecarrier-cx.PrjPCB`
- Company:
  - Byte Lab Grupa d.o.o.
  - Medarska 69/1, 10000 Zagreb, Croatia
  - www.byte-lab.com
- Author: A.Duracic
- Acceptor: E. Stanisha
- Sheet: 2 of 6
- Rev: 17
- Format: A4

## Page 3

# Components

- **P1**: Header Castellated 2.54mm 1X16
- **P2**: Header Castellated 2.54mm 1X16
- **P4**: Header 2.54mm 1x5
- **P3**: 12402012E212A
- **R1**: 5k1
- **R2**: 5k1
- **S1**: SSSS820101
- **R22**: 11k
- **U1**: NX3DV42GU
- **C32**: 100n
- **J1**: BM04B-SRSS-TB(LF)(SN)
- **P5**: S2B-PH-SM4-K-TB

# Connectors and Pin Labels

## P1 — Header Castellated 2.54mm 1X16

Pin labels shown top-to-bottom; pin numbers not shown:

- +VACT_GPS_IN
- +VACT_GPS_OUT
- ATTN
- +VMAIN
- +VBAT
- EN
- +VUSB
- D13
- D12
- D11
- D10
- D9
- D6
- D5
- SCL
- SDA

## P2 — Header Castellated 2.54mm 1X16

Pin labels shown top-to-bottom; pin numbers not shown:

- NRST
- +3V3_OUT
- +V_AREF
- GND
- A0
- A1
- A2
- A3
- A4
- A5
- SCK
- MOSI
- MISO
- IO_RX
- IO_TX
- BOOT0

## P4 — Header 2.54mm 1x5

Pin labels shown top-to-bottom; pin numbers not shown:

- GND
- +VIO
- AUX_EN
- AUX_RX
- AUX_TX

## P3 — USB C Connector, 12402012E212A

- **A4**: VBUS, net +VUSB
- **A9**: VBUS, net +VUSB
- **A5**: CC1, connected through R1 5k1 to GND
- **A6**: D+, net USB_D_P
- **A7**: D-, net USB_D_N
- **A8**: SBU1
- **A1**: GND
- **A12**: GND
- **M**: connected to GND
- **B4**: VBUS, net +VUSB
- **B9**: VBUS, net +VUSB
- **B5**: CC2, connected through R2 5k1 to GND
- **B6**: D+, net USB_D_P
- **B7**: D-, net USB_D_N
- **B8**: SBU2
- **B1**: GND
- **B12**: GND

## J1 — QWIIC Connector, BM04B-SRSS-TB(LF)(SN)

- **1**: GND
- **2**: +VIO
- **3**: HST_SDA
- **4**: HST_SCL

## P5 — Battery Connector, S2B-PH-SM4-K-TB

- **1**: +VBAT
- **2**: GND
- **M**: no net label shown

# IC / Switch Pin Signals

## U1 — NX3DV42GU

- **Pin 9, VCC**: +VUSB, with C32 100n to GND
- **Pin 3, GND**: GND
- **Pin 10, S**: USB_SW
- **Pin 8, OE**: GND
- **Pin 1, D+**: USB_D_P
- **Pin 2, D-**: USB_D_N
- **Pin 5, HSD1+**: USB_HST_D_P
- **Pin 4, HSD1-**: USB_HST_D_N
- **Pin 7, HSD2+**: USB_NC_D_P
- **Pin 6, HSD2-**: USB_NC_D_N

## S1 — SSSS820101

- Connected nets shown:
  - GND
  - +VUSB
  - USB_SW through R22 11k
  - GND

# Named Nets / Signals

- +VACT_GPS_IN
- +VACT_GPS_OUT
- ATTN
- +VMAIN
- +VBAT
- EN
- +VUSB
- D13
- D12
- D11
- D10
- D9
- D6
- D5
- SCL
- SDA
- NRST
- +3V3_OUT
- +V_AREF
- GND
- A0
- A1
- A2
- A3
- A4
- A5
- SCK
- MOSI
- MISO
- IO_RX
- IO_TX
- BOOT0
- +VIO
- AUX_EN
- AUX_RX
- AUX_TX
- USB_D_P
- USB_D_N
- USB_SW
- USB_HST_D_P
- USB_HST_D_N
- USB_NC_D_P
- USB_NC_D_N
- HST_SDA
- HST_SCL

# Design Notes

- USB C Connector:
  - “The USB C upstream facing port is configured to use 1.5A@5V or 3A@5V. The total power is limited by the downward facing port the device is connected to, which may be as low as 0.5A@5V.”

- USB Switch:
  - “The USB connection is routed depending on the position of SW1
    NC (with marker): Host MCU
    NO (w/o marker): Notecard”

- QWIIC Connector:
  - “The I2C bus is pulled up by the Notecard”

- Battery Connector:
  - “Li-Po Battery
    3.3V - 4.2V”

# Title Block

- **Copyright**: Copyright © 2023 Blues Inc.
- **Title**: 03_IO-CONNECTION.SchDoc
- **Project**: 100544_notecarrier-cx.PrjPCB
- **Company**: Byte Lab Grupa d.o.o.
- **Address**: Medarska 69/1, 10000 Zagreb, Croatia
- **Website**: www.byte-lab.com
- **Author**: A.Duracic
- **Acceptor**: E. Stanisha
- **Sheet**: 3 of 6
- **Revision**: 17
- **Format**: A4

## Page 4

# 04_NOTECARD-CONNECTION.SchDoc

## Components

- **J3** — MDT580E01002
- **J4** — SF72S006VBDR2500, NanoSIM
- **R4** — 0R0
- **R5** — 22R
- **R6** — 22R
- **R7** — 15k
- **R8** — 22R
- **C2** — 100n
- **C3** — 33p
- **C4** — 33p
- **C5** — 33p
- **TVS1** — PESD5V0L5UV,125
- **ASS1** — KNOB M2.5x4-INOX
- **STANDOFF1** — 9774040151R, Standoff

## Connector J3 — Notecard Connector

Part: **MDT580E01002**

### Left / bottom-side pins

- **2** — VIO_P
- **4** — VIO_P
- **6** — GND
- **8** — SIM_VCC
- **10** — SIM_RST
- **12** — SIM_IO
- **14** — SIM_CLK
- **16** — SIM_PRESENT
- **18** — GND
- **20** — VACT_GPS_OUT
- **22** — VACT_GPS_IN
- **32** — ALT_DFU_BOOT
- **34** — ALT_DFU_RESET
- **36** — ALT_DFU_ACTIVE
- **38** — AUX_CHARGING
- **40** — SCL_P
- **42** — SDA_P
- **44** — NC44
- **46** — AUX1
- **48** — AUX2
- **50** — AUX3
- **52** — AUX4
- **54** — ATTN_P
- **56** — AUX_EN_P
- **58** — AUX_RX_P
- **60** — AUX_TX_P
- **62** — RX_P
- **64** — TX_P
- **66** — NC66
- **68** — NC68
- **70** — VMODEM_P
- **72** — VMODEM_P
- **74** — VMODEM_P

### Right / top-side pins

- **1** — XP_ENABLE
- **3** — GND
- **5** — GND
- **7** — USB_DP
- **9** — USB_DN
- **11** — GND
- **13** — VUSB
- **15** — NC15
- **17** — NC17
- **19** — NC19
- **21** — NC21
- **23** — NC23
- **33** — GND
- **35** — NC35
- **37** — NC37
- **39** — GND
- **41** — ALT_DFU_RX
- **43** — ALT_DFU_TX
- **45** — GND
- **47** — RTX
- **49** — CTX
- **51** — GND
- **53** — NC53
- **55** — NC55
- **57** — GND
- **59** — NC59
- **61** — NC61
- **63** — NC63
- **65** — BOOT
- **67** — RST
- **69** — NC69
- **71** — GND
- **73** — GND
- **75** — XP_MODEM_VSEL

## Connector J4 — SIM Card

Part: **SF72S006VBDR2500**

- **1** — VCC
- **2** — RST
- **3** — CLK
- **5** — GND
- **6** — VPP
- **7** — IO
- **8** — GND
- **9** — GND
- **10** — CSW
- **11** — GND
- **12** — GND
- **13** — DSW
- **14** — GND
- **15** — GND
- **16** — GND
- **17** — GND
- **18** — GND
- **19** — GND

## Named Nets / Signals

- **+VIO**
- **GND**
- **SIM_VCC**
- **SIM_RST**
- **SIM_RST_FILT**
- **SIM_IO**
- **SIM_IO_FILT**
- **SIM_CLK**
- **SIM_CLK_FILT**
- **SIM_NPRESENT**
- **SIM_PRESENT**
- **+VACT_GPS_OUT**
- **+VACT_GPS_IN**
- **VACT_GPS_OUT**
- **VACT_GPS_IN**
- **ALT_DFU_BOOT**
- **ALT_DFU_NRESET**
- **ALT_DFU_RESET**
- **ALT_DFU_IDLE**
- **ALT_DFU_ACTIVE**
- **ALT_DFU_RX**
- **ALT_DFU_TX**
- **AUX_NCHARGING**
- **AUX_CHARGING**
- **SCL**
- **SCL_P**
- **SDA**
- **SDA_P**
- **ATTN**
- **ATTN_P**
- **AUX_EN**
- **AUX_EN_P**
- **AUX_RX**
- **AUX_RX_P**
- **AUX_TX**
- **AUX_TX_P**
- **USB_NC_D_P**
- **USB_NC_D_N**
- **USB_DP**
- **USB_DN**
- **+VUSB**
- **VUSB**
- **+VMODEM**
- **VMODEM_P**
- **VIO_P**
- **XP_ENABLE**
- **XP_MODEM_VSEL**
- **AUX1**
- **AUX2**
- **AUX3**
- **AUX4**
- **RX_P**
- **TX_P**
- **RTX**
- **CTX**
- **BOOT**
- **RST**
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
- **VCC**
- **CLK**
- **VPP**
- **IO**
- **DSW**
- **CSW**

## Title Block / Notes

- **Copyright:** Copyright © 2023 Blues Inc.
- **Title:** 04_NOTECARD-CONNECTION.SchDoc
- **Project:** 100544_notecarrier-cx.PrjPCB
- **Company:** Byte Lab Grupa d.o.o.
- **Address:** Medarska 69/1, 10000 Zagreb, Croatia
- **Website:** www.byte-lab.com
- **Author:** A.Duracic
- **Acceptor:** E. Stanisha
- **Sheet:** 4 of 6
- **Rev:** 17
- **Format:** A4

## Page 5

# Page Notes

- Copyright © 2023 Blues Inc.

# Sections

- Battery Charger w/ Power Path
- 3V3 Buck/Boost Regulator
- 3V3_OUT Switch
- USB LDO
- VDETECT

# Components

## ICs

- U2: RT6160BWSC
  - Pins/balls shown:
    - B2: LX1
    - B3: LX1
    - A2: VIN
    - A3: VIN
    - C1: AGND
    - C2: PGND
    - C3: PGND
    - D2: LX2
    - D3: LX2
    - E2: VOUT
    - E3: VOUT
    - A1: EN
    - B1: VSEL
    - E1: SDA
    - D1: SCL
- U3: BQ25628ERYKR
  - Pins shown:
    - 18: VBUS
    - 12: SDA
    - 13: SCL
    - 11: INT
    - 14: CE
    - 3: PG
    - 10: STAT
    - 7: QON
    - 17: PMID
    - 2: REGN
    - 16: SW
    - 1: BTST
    - 9: SYS
    - 4: ILIM
    - 5: TS_BIAS
    - 6: TS
    - 8: BAT
    - 15: GND
- U4: TPS22917DBVR
  - Pins shown:
    - 1: VIN
    - 4: CT
    - 3: ON
    - 6: VOUT
    - 5: QOD
    - 2: GND
- U7: TLV77033PDBVR
  - Pins shown:
    - 1: VIN
    - 3: CE
    - 2: GND
    - 5: VOUT
    - 4: NC

## Diodes / LEDs

- D1: SML-P12WT86R
- D4: 1N4148WT-7

## Inductors

- L1: MCKK1608T1R0MN
- L2: 3u3

## Resistors

- R9: 0R0
- R10: 10M
- R11: 3k
- R12: 3k
- R13: 11k
- R14: 15k
- R17: 1M
- R20: 11k
- R21: 1M
- R23: 10M
- R24: 4M3

## Capacitors

- C1: 10u
- C6: 10u
- C7: 10u
- C8: 47n/50V
- C9: 100n
- C10: 100n
- C11: 10u
- C12: 10u
- C13: 4u7
- C14: 10u
- C15: 100n
- C16: 4u7
- C26: 4u7
- C27: 100n
- C28: 4u7
- C33: 10u
- C34: 10u
- C35: 10u
- C36: 10u
- C37: 10u
- C38: 10u

# Connectors

- No connector reference designators are visible on this page.

# Named Nets / Signals

- +VUSB
- +VMAIN
- +VMODEM
- +VBAT
- +VIO
- +3V3_OUT
- +3V3_USB
- GND
- AUX_NCHARGING
- HST_SDA
- HST_SCL
- SW
- EN
- ENABLE_3V3
- VSENSE

# Design Notes

## Battery Charger w/ Power Path

- DESIGN NOTE:
  - Charger:
    - Default charging voltage: 4.2V
    - Default charging current: 320mA
    - Default termination current: 20mA
    - Default pre-charge current: 20mA
    - No battery thermal protection
    - No battery behaviour: +VBAT is pulled to VUSB - 0.7V through D4 & R20

- DESIGN NOTE:
  - Power Path:
    - Input current limit: 3.5A
    - 26mOhm reverse blocking transistor
    - 15mOhm battery transistor
  - Buck Regulator:
    - 1.5MHz frequency
    - Input Voltage: 4.5-5.5V
    - Output Voltage: 3.3-4.2V
    - Peak current: 1.6A

- SOFTWARE CONFIG NOTE:
  - Charge current can be adjusted via I2C registers.
  - Make sure not to exceed 1.5A if programming the charger IC.

## 3V3 Buck/Boost Regulator

- DESIGN NOTE:
  - Input Voltage: 2.5V - 5.5V
  - Output Voltage: 3.3V
  - Max continuous output current over whole input voltage range: 1A

# Title Block

- Title: 05_POWER.SchDoc
- Project: 100544_notecarrier-cx.PrjPCB
- Company:
  - Medarska 69/1, 10000 Zagreb, Croatia
  - Byte Lab Grupa d.o.o.
  - www.byte-lab.com
- Author: A.Duracic
- Acceptor: E. Stanisha
- Sheet: 5 of 6
- Rev: 17
- Format: A4

## Page 6

# 06_MCU.SchDoc

## Title Block / Notes

- Copyright © 2023 Blues Inc.
- Title: `06_MCU.SchDoc`
- Project: `100544_notecarrier-cx.PrjPCB`
- Company: Byte Lab Grupa d.o.o.
- Address: Medarska 69/1, 10000 Zagreb, Croatia
- Website: `www.byte-lab.com`
- Author: A.Duracic
- Acceptor: E. Stanisha
- Sheet: 6 of 6
- Rev: 17
- Format: A4
- Software config note:
  - Use drive level `"medium high"` or `"high"` to ensure startup.
- Legend:
  - Internal pull-down upon reset
  - Internal pull-up upon reset
  - Not 5V tolerant
  - Weak outputs

## Components

### ICs

- U5A: STM32L433CCT6
- U5B: STM32L433CCT6
- U6: NX3L2467GU,115

### Connector

- J5: Header 1.27mm 2X7

### Resistors

- R3: 15k
- R15: 0R0
- R16: 100k
- R18: 15k
- R19: 3k
- R25: 10k
- R26: 10k
- R27: 10k
- R28: 10k

### Capacitors

- C17: 4u7
- C18: 100n
- C19: 100n
- C20: 100n
- C21: 100n
- C22: 4u7
- C23: 100n
- C24: 100n
- C25: 100n
- C29: 100n
- C30: 6p8
- C31: 6p8
- C39: 100n

### Diodes / LEDs / ESD

- D1: PESD5V0X1UB,135
- D2: PESD5V0X1UB,135
- D3: PESD5V0X1UB,135
- LD2: SML-P12U2TT86R

### Switches

- S2: SKRPABE010
- S3: SKRPADE010
- S4: SKRPADE010

### Crystal

- Y1: ABS07-32.768KHZ-6-T

## Connectors

### J5 — Header 1.27mm 2X7

- Pin 1: no label visible
- Pin 2: no label visible
- Pin 3: +VIO
- Pin 4: SWDIO
- Pin 5: GND
- Pin 6: SWCLK
- Pin 7: GND
- Pin 8: no label visible
- Pin 9: no label visible
- Pin 10: no label visible
- Pin 11: GND
- Pin 12: HST_NRST
- Pin 13: LP_UART_RX
- Pin 14: LP_UART_TX

## Host MCU — U5A STM32L433CCT6

### Visible Pin / Signal Mapping

- Pin 10, PA0: HST_A0 / A0
- Pin 11, PA1: HST_A1 / A1
- Pin 12, PA2: HST_A2 / A2
- Pin 13, PA3: HST_A3 / A3
- Pin 14, PA4: VSENSE
- Pin 15, PA5: HST_SCK / SCK
- Pin 16, PA6: HST_MISO / MISO
- Pin 17, PA7: HST_A5 / A5
- Pin 29, PA8: HST_USER_LED
- Pin 30, PA9: HST_TX
- Pin 31, PA10: HST_RX
- Pin 32, PA11: USB_HST_D_N
- Pin 33, PA12: USB_HST_D_P
- Pin 34, JTMS-SWDIO/PA13: SWDIO
- Pin 37, JTCK-SWCLK/PA14: SWCLK
- Pin 38, JTDI/PA15: AUX_NCHARGING
- Pin 18, PB0: HST_D11 / D11
- Pin 19, PB1: HST_A4 / A4
- Pin 20, PB2: no net label visible
- Pin 39, JTDO-TRACESWO/PB3: +3V3_USB label visible on this line
- Pin 40, JTRST/PB4: HST_D13 / D13
- Pin 41, PB5: HST_MOSI / MOSI
- Pin 42, PB6: HST_SCL / SCL
- Pin 43, PB7: HST_SDA / SDA
- Pin 45, PB8: HST_D5 / D5
- Pin 46, PB9: HST_D6 / D6
- Pin 21, PB10: LP_UART_RX
- Pin 22, PB11: LP_UART_TX
- Pin 25, PB12: no net label visible
- Pin 26, PB13: HST_D10 / D10
- Pin 27, PB14: HST_D9 / D9
- Pin 28, PB15: HST_D12 / D12
- Pin 2, PC13: USER_BTN
- Pin 3, PC14/OSC32_IN: OSC32_IN
- Pin 4, PC15/OSC32_OUT: OSC32_OUT
- Pin 5, PH0/OSC_IN: ENABLE_3V3
- Pin 6, PH1/OSC_OUT: no net label visible
- Pin 44, PH3/BOOT0: HST_BOOT0
- Pin 7, RST: HST_NRST

### Associated Parts

- C24: 100n from HST_NRST to GND
- R19: 3k in series with LD2 from HST_USER_LED
- LD2: SML-P12U2TT86R to GND
- R26: 10k associated with SWCLK to GND
- R25: 10k associated with SWDIO and +VIO
- R27: 10k associated with HST_SDA and +VIO
- R28: 10k associated with HST_SCL and +VIO

## Host MCU Power — U5B STM32L433CCT6

### Visible Power Pins

- Pin 1, VBAT: tied to +VIO rail
- Pin 24, VDD: tied to +VIO rail
- Pin 48, VDD: tied to +VIO rail
- Pin 36, VDDUSB: tied to +3V3_USB rail
- Pin 9, VDDA/VREF+: tied to +V_AREF rail
- Pin 23, VSS: GND
- Pin 47, VSS: GND
- Pin 35, VSS: GND
- Pin 8, VSSA/VREF-: GND

### Decoupling / Power Parts

- C17: 4u7
- C18: 100n
- C19: 100n
- C20: 100n
- C21: 100n
- C22: 4u7
- C23: 100n
- R15: 0R0

## UART DFU Switch — U6 NX3L2467GU,115

### Visible Pin / Signal Mapping

- Pin 14, VCC: +VIO
- Pin 6, GND: GND
- Pin 16, 1Z: HST_NRST
- Pin 4, 2Z: HST_BOOT0
- Pin 8, 3Z: HST_TX
- Pin 12, 4Z: HST_RX
- Pin 2, 1S: ALT_DFU_IDLE select net
- Pin 10, 2S: ALT_DFU_IDLE select net
- Pin 1, 1Y0: ALT_DFU_NRESET
- Pin 15, 1Y1: IO_NRST / NRST
- Pin 5, 2Y0: ALT_DFU_BOOT
- Pin 3, 2Y1: IO_BOOT0 / BOOT0
- Pin 9, 3Y0: ALT_DFU_RX
- Pin 7, 3Y1: IO_TX
- Pin 13, 4Y0: ALT_DFU_TX
- Pin 11, 4Y1: IO_RX

### Associated Parts

- R16: 100k from +VIO to ALT_DFU_IDLE net
- C25: 100n from +VIO/VCC to GND

## MCU Crystal

- Y1: ABS07-32.768KHZ-6-T
- C30: 6p8 from OSC32_IN to GND
- C31: 6p8 from OSC32_OUT to GND
- Nets:
  - OSC32_IN
  - OSC32_OUT
  - GND

## User Buttons

### USER_BTN Button Circuit

- S4: SKRPADE010
- R3: 15k to +VIO
- C39: 100n to GND
- D3: PESD5V0X1UB,135 to GND
- Nets:
  - USER_BTN
  - +VIO
  - GND

### IO_NRST Button Circuit

- S2: SKRPABE010
- D1: PESD5V0X1UB,135 to GND
- Nets:
  - IO_NRST
  - GND

### IO_BOOT0 Button Circuit

- S3: SKRPADE010
- R18: 15k to GND
- C29: 100n to GND
- D2: PESD5V0X1UB,135 to GND
- Nets:
  - IO_BOOT0
  - +VIO
  - GND

## Sheet Ports / External Signal Labels

### Host MCU Ports

- A0 → HST_A0
- A1 → HST_A1
- A2 → HST_A2
- A3 → HST_A3
- VSENSE → VSENSE
- SCK → HST_SCK
- MISO → HST_MISO
- A5 → HST_A5
- USB_HST_D_N
- USB_HST_D_P
- AUX_NCHARGING
- D11 → HST_D11
- A4 → HST_A4
- D13 → HST_D13
- MOSI → HST_MOSI
- SCL → HST_SCL
- SDA → HST_SDA
- D5 → HST_D5
- D6 → HST_D6
- D10 → HST_D10
- D9 → HST_D9
- D12 → HST_D12
- ENABLE_3V3

### UART DFU Switch Ports

- ALT_DFU_NRESET
- NRST
- ALT_DFU_BOOT
- BOOT0
- ALT_DFU_RX
- IO_TX
- ALT_DFU_TX
- IO_RX
- ALT_DFU_IDLE

## Named Nets / Signals

- +3V3_USB
- +V_AREF
- +VIO
- A0
- A1
- A2
- A3
- A4
- A5
- ALT_DFU_BOOT
- ALT_DFU_IDLE
- ALT_DFU_NRESET
- ALT_DFU_RX
- ALT_DFU_TX
- AUX_NCHARGING
- BOOT0
- D5
- D6
- D9
- D10
- D11
- D12
- D13
- ENABLE_3V3
- GND
- HST_A0
- HST_A1
- HST_A2
- HST_A3
- HST_A4
- HST_A5
- HST_BOOT0
- HST_D5
- HST_D6
- HST_D9
- HST_D10
- HST_D11
- HST_D12
- HST_D13
- HST_MISO
- HST_MOSI
- HST_NRST
- HST_RX
- HST_SCK
- HST_SCL
- HST_SDA
- HST_TX
- HST_USER_LED
- IO_BOOT0
- IO_NRST
- IO_RX
- IO_TX
- LP_UART_RX
- LP_UART_TX
- MISO
- MOSI
- NRST
- OSC32_IN
- OSC32_OUT
- SCK
- SCL
- SDA
- SWCLK
- SWDIO
- USER_BTN
- USB_HST_D_N
- USB_HST_D_P
- VSENSE
