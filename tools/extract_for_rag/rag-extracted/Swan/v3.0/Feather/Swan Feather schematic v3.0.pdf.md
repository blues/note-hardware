---
product: Swan
version: v3.0
doc_type: schematic
source_file: Swan/v3.0/Feather/Swan Feather schematic v3.0.pdf
generated_by: tools/extract_for_rag/extract.py
---

# Swan — SCHEMATIC (v3.0)

_Source: `Swan/v3.0/Feather/Swan Feather schematic v3.0.pdf`_

## Page 1

# Page Summary

- **Page name:** 00 - REVISION
- **Project:** SWAN
- **Board:** SWAN-F
- **Sheet:** 1 / 5
- This page contains revision history, title block information, and a few visible board/PCB reference items. No schematic circuit connections are shown.

# Components / Reference Designators

## Visible on Page

- **CS1** — `CS V7 6L 35um`
- **FID1** — value/part not shown
- **FID2** — value/part not shown

## Mentioned in Revision Notes Only

- **R25** — changed to not mounted
- **J2** — MPN changed to `4UCON 00820`; pin2 swapped with pin3
- **J3** — MPN changed to `4UCON 00815`
- **J4** — changed to 4UCON supplier
- **J5** — changed to 7x2 header to support STLINK V3 standard
- **J6** — supply changed to `+VIO`
- **U6** — MCU MPN changed to `STM32L4R5ZIY6`

# Connectors and Pin Labels

- **J2** — mentioned only in revision notes
  - Pin references mentioned: `pin2`, `pin3`
  - No pin labels shown
- **J3** — mentioned only in revision notes
  - No pin labels shown
- **J4** — mentioned only in revision notes
  - No pin labels shown
- **J5** — mentioned only in revision notes as `7x2 header`
  - No pin labels shown
- **J6** — mentioned only in revision notes
  - No pin labels shown
- **QWIIC connector** — mentioned in revision notes
  - Reference designator not shown on this page
  - No pin labels shown

# Named Nets / Signals

- `I2C1`
- `CS`
- `BOOT`
- `+VIO`
- `NC`
- `PAD51`
- `PAD65`
- `PAD66`
- `PAD67`
- `PAD68`
- `PAD69`

# Revision History

- **Revision 1**
  - **Date:** 11/02/2021
  - **Author:** M.Gregis
  - **Description:** First Draft

- **Revision 2**
  - **Date:** 18/06/2021
  - **Author:** G.Boschini
  - **Description:**
    - Uploaded symbol from library
    - Changed R25 to not mounted
    - Changed J2, J3, J4 to 4UCON supplier

- **Revision 3**
  - **Date:** 26/07/2021
  - **Author:** M. Cossali
  - **Description:**
    - Uploaded symbol from library
    - Changed J2 MPN to 4UCON 00820 and J3 MPN to 4UCON 00815
    - Changed the MCU U6 MPN to STM32L4R5ZIY6

- **Revision 4**
  - **Date:** 13/09/2021
  - **Author:** G.Boschini
  - **Description:**
    - Swapped J2 pin2 with pin3

- **Revision 5**
  - **Date:** 15/09/2021
  - **Author:** G.Boschini
  - **Description:**
    - Added pullup resistor on I2C1 nets

- **Revision 6**
  - **Date:** 04/02/2022
  - **Author:** M.Gregis
  - **Description:**
    - Added QWIIC connector
    - Changed J5 to 7x2 header to support STLINK V3 standard.

- **Revision 7**
  - **Date:** 17/02/2022
  - **Author:** M.Gregis
  - **Description:**
    - Updated PCB
    - Added new Castellated PAD for CS signal `(PAD65)`
    - BOOT signal made available on Castellated PAD `(PAD51)`
    - added PAD66/67/68/69 `(NC)`
    - Changed J6 supply to +VIO

# Title Block Notes

- **Company:** FAE TECHNOLOGY
- **Address:** via C. Battisti 136, 24025, Gazzaniga (Bg), Italy
- **Mail:** info@fae.technology
- **Tel:** +39 035738130
- **Project:** SWAN
- **Board:** SWAN-F
- **Designer:** M. Gregis
- **Approved:** G.Boschini
- **Project Code:** 2021-0248
- **Customer:** Blues
- **Internal Code:** -
- **Code:** -
- **Date:** Tuesday, April 26, 2022
- **Rev.:** 7
- **Rev. changes:** See Revision Page
- **Sheet:** 1 / 5
- **Legal note:** Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.

## Page 2

# Page: 01 - BLOCK DIAGRAM

## Component Reference Designators

- No component reference designators are visible on this page.

## Functional Blocks / Parts

- JST CONNECTOR
- BAT CHARGER
- MICROUSB
- LDO
- DIODE-OR
- BUCK
- BOOST
- 3V3 OUT BUCKBOOST
- STM32L4R5ZIY6
- BOOT BTN
- RST BTN
- USR LED

## Connectors and Pin / Signal Labels

- JST CONNECTOR
  - +VBAT

- MICROUSB
  - +VUSB
  - 1x DEVICE USB

- FEATHER CONNECTOR
  - 2V5 .. 3V3
  - @ 500mA
  - 1x DEVICE USB
  - 16x GPIO
  - 2x DAC
  - 6x ADC
  - 3x I2C
  - 3x UART + FLOW CTRL
  - 1x UART
  - 1x SPI + 1x QSPI
  - RST#
  - 3V3_ENABLE

- QWIIC CONNECTOR
  - +3V3_USB
  - 3V3

- JTAG
  - JTAG/SWD

## Named Nets / Signals

- +VBAT
- +VUSB
- +3V3_USB
- 2V5 .. 3V3
- 1V8
- 3V3
- 3V3_ENABLE
- DISCHARGE
- EN
- RST#
- JTAG/SWD
- GPIO
- 1x DEVICE USB
- 16x GPIO
- 2x DAC
- 6x ADC
- 3x I2C
- 3x UART + FLOW CTRL
- 1x UART
- 1x SPI + 1x QSPI
- @ 500mA

## Title Block Notes

- Company: FAE Technology
- Address: via C. Battisti 136, 24025, Gazzaniga (Bg), Italy
- Mail: info@fae.technology
- Tel: +39 035738130
- Project: SWAN
- Board: SWAN-F
- Designer: M. Gregis
- Project Code: 2021-0248
- Page name: 01 - BLOCK DIAGRAM
- Approved: G.Boschini
- Customer: Blues
- Internal Code: -
- Code: -
- Date: Tuesday, April 26, 2022
- Rev.: 7
- Rev. changes: See Revision Page
- Sheet: 2 / 5
- Copyright note: “Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.”

## Page 3

# Schematic Page: 02 - FEATHER CONNECTORS

## Components

- **J1**: 10118192-0002LF
- **J2**: 00820
- **J3**: 00815
- **C1**: 10n/1kV
- **R1**: 1M
- **C2**: 100n/16V
- **C3**: 100n/16V

## Connectors

### J1 — 10118192-0002LF

- **Pin 1**: Vcc, connected to **+VUSB**
- **Pin 2**: D-, connected to **USB_DM**
- **Pin 3**: D+, connected to **USB_DP**
- **Pin 4**: ID
- **Pin 5**: GND
- **Pin 6**: E1
- **Pin 7**: E2
- **Pin 8**: E3
- **Pin 9**: E4
- **Pin 10**: E5
- **Pin 11**: E6
- Shield connection labeled **USB_SHIELD**

### J2 — 00820

- **Pin 1**: RST#
- **Pin 2**: +3V3_OUT
- **Pin 3**: +VIN
- **Pin 4**: GND
- **Pin 5**: A0
- **Pin 6**: A1
- **Pin 7**: A2
- **Pin 8**: A3
- **Pin 9**: A4
- **Pin 10**: A5
- **Pin 11**: SCK
- **Pin 12**: MOSI
- **Pin 13**: MISO
- **Pin 14**: RX
- **Pin 15**: TX
- **Pin 16**: BOOT

### J3 — 00815

- **Pin 1**: +VBAT
- **Pin 2**: EN
- **Pin 3**: +VUSB
- **Pin 4**: D13
- **Pin 5**: D12
- **Pin 6**: D11
- **Pin 7**: D10
- **Pin 8**: D9
- **Pin 9**: D6
- **Pin 10**: D5
- **Pin 11**: SCL
- **Pin 12**: SDA

## Pads / Test Points

### USB Pads

- **PAD1**: USB_DP
- **PAD2**: USB_DM

### Left Feather-Connector Pads

- **PAD69**: no readable signal label
- **PAD3**: no readable local label
- **PAD68**: no readable signal label
- **PAD4**: no readable local label
- **PAD67**: no readable signal label
- **PAD5**: no readable local label
- **PAD66**: no readable signal label
- **PAD6**: no readable local label
- **PAD65**: CS
- **PAD7**: no readable signal label
- **PAD9**: D0
- **PAD11**: no readable signal label
- **PAD12**: D1
- **PAD13**: no readable signal label
- **PAD18**: D2
- **PAD16**: no readable signal label
- **PAD21**: D3
- **PAD23**: no readable signal label
- **PAD25**: D4
- **PAD27**: no readable signal label
- **PAD29**: A6
- **PAD31**: no readable signal label
- **PAD33**: A7
- **PAD35**: no readable signal label
- **PAD37**: D14
- **PAD39**: no readable signal label
- **PAD41**: D15
- **PAD43**: no readable signal label
- **PAD45**: RTS
- **PAD47**: no readable signal label
- **PAD49**: CTS
- **PAD51**: no readable signal label
- **PAD53**: QEN

### Right Feather-Connector Pads

- **PAD8**: no readable signal label
- **PAD10**: RX2
- **PAD14**: no readable signal label
- **PAD15**: TX2
- **PAD17**: no readable signal label
- **PAD19**: RTS2
- **PAD20**: no readable signal label
- **PAD22**: CTS2
- **PAD24**: no readable signal label
- **PAD26**: RX3
- **PAD28**: no readable signal label
- **PAD30**: TX3
- **PAD32**: no readable signal label
- **PAD34**: RTS3
- **PAD36**: no readable signal label
- **PAD38**: CTS3
- **PAD40**: no readable signal label
- **PAD42**: D8
- **PAD44**: no readable signal label
- **PAD46**: D7
- **PAD48**: no readable signal label
- **PAD50**: SCL2
- **PAD52**: no readable signal label
- **PAD54**: SDA2

### Bottom Pads

- **PAD55**: T_VCP_TX; TX0 text nearby
- **PAD56**: T_VCP_RX; RX0 text nearby
- **PAD57**: SDA3
- **PAD58**: SCL3
- **PAD59**: QCS
- **PAD60**: QI4
- **PAD61**: QI3
- **PAD62**: QI2
- **PAD63**: QI1
- **PAD64**: QI0

## Named Nets / Signals

- **+3V3_OUT**
- **+VBAT**
- **+VIN**
- **+VUSB**
- **A0**
- **A1**
- **A2**
- **A3**
- **A4**
- **A5**
- **A6**
- **A7**
- **BOOT**
- **CS**
- **CTS**
- **CTS2**
- **CTS3**
- **D0**
- **D1**
- **D2**
- **D3**
- **D4**
- **D5**
- **D6**
- **D7**
- **D8**
- **D9**
- **D10**
- **D11**
- **D12**
- **D13**
- **D14**
- **D15**
- **EN**
- **GND**
- **MISO**
- **MOSI**
- **QCS**
- **QEN**
- **QI0**
- **QI1**
- **QI2**
- **QI3**
- **QI4**
- **RST#**
- **RTS**
- **RTS2**
- **RTS3**
- **RX**
- **RX0**
- **RX2**
- **RX3**
- **SCL**
- **SCL2**
- **SCL3**
- **SCK**
- **SDA**
- **SDA2**
- **SDA3**
- **T_VCP_RX**
- **T_VCP_TX**
- **TX**
- **TX0**
- **TX2**
- **TX3**
- **USB_DM**
- **USB_DP**
- **USB_SHIELD**

## Title Block Notes

- **Company**: FAE Technology
- **Address**: via C. Battisti 136, 24025, Gazzaniga (Bg), Italy
- **Mail**: info@fae.technology
- **Tel**: +39 035738130
- **Project**: SWAN
- **Board**: SWAN-F
- **Designer**: M. Gregis
- **Approved**: G.Boschini
- **Project Code**: 2021-0248
- **Customer**: Blues
- **Internal Code**: -
- **Code**: -
- **Page name**: 02 - FEATHER CONNECTORS
- **Data**: Tuesday, April 26, 2022
- **Rev.**: 7
- **Rev. changes**: See Revision Page
- **Sheet**: 3 / 5
- **Copyright note**: Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.

## Page 4

# 03 - POWER

## Sheet Sections

- MAIN SUPPLY
- 3V3 OUTPUT SUPPLY
- USB LDO

## Components

### Integrated Circuits / Active Devices

- U1: TPS62748YFPT, BUCK
- U2: TPS63020DSJR, BUCK-BOOST
- U3: MCP73831-2ACI/MC
- U4: MAX17225ELT, BOOST
- U5: AP2139AK-3.3TRG1
- U7: MAX40203ANS+T, IDEAL-DIODE
  - Note: Consumo 3V6: 650nA
- U8: MAX40203ANS+T, IDEAL-DIODE
  - Note: Consumo 3V6: 650nA
- U9: MAX40203ANS+T, IDEAL-DIODE
  - Note: Consumo 3V6: 650nA
- U10: MAX40203ANS+T, IDEAL-DIODE
  - Note: Consumo 3V6: 650nA
- U12: MAX40203ANS+T, IDEAL-DIODE
  - Note: Consumo 3V6: 650nA
- U13: MAX40203ANS+T, IDEAL-DIODE
  - Note: Consumo 3V6: 650nA

### Diodes / LED / Protection

- LD1: SML-P12WTT86R
- TVS1: SM6T6V8A

### Inductors

- L1: 1285AS-H-2R2M=P2
- L2: XFL4020-222MEC
- L3: XFL4020-152MEC

### Resistors

- R2: 10M
- R3: NU
- R4: 0R
- R5: 1k
- R6: 1M
- R7: 2.8k
- R8: 1k
- R9: 82k
- R10: 180k
- R12: 10k
- R13: 8.2M

### Capacitors

- C4: 47u/16V-X5R
- C5: 4.7u/6.3V-X5R
- C6: 10u/10V-X5R
- C7: 10u/10V-X5R
- C8: 100n/16V-X5R
- C9: 4.7u/10V-X5R
- C10: 4.7u/10V-X5R
- C11: 100n/16V-X5R
- C12: 10u/6.3V-X5R
- C13: 10u/6.3V-X5R
- C14: 100n/16V-X5R
- C15: 100u/6.3V-X5R
- C16: 100u/6.3V-X5R
- C17: 100n/16V-X5R
- C18: 10u/10V-X5R
- C19: 10u/10V-X5R
- C20: 100n/16V-X5R
- C21: 1u/6V-X5R
- C22: 100n/16V-X5R
- C23: 1u/6V-X5R

## Connectors

### J4

- Part/value: 20404
- Pin 1: +VBAT / Li-po battery positive
- Pin 2: GND / Li-po battery negative
- Note near connector: Li-po battery 3.3V - 4.2V

## IC Pin Labels

### U1 TPS62748YFPT

- A2: VIN
- B2: GND
- C2: VOS
- D2: LOAD
- A1: SW
- B1: EN
- C1: VSEL
- D1: CTRL

### U2 TPS63020DSJR

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

### U3 MCP73831-2ACI/MC

- 1: VDD
- 2: VDD
- 3: VBAT
- 4: VBAT
- 5: STAT
- 6: VSS
- 7: NC
- 8: PROG
- 9: EXP

### U4 MAX17225ELT

- 1: OUT
- 2: LX
- 3: GND
- 4: SEL
- 5: IN
- 6: EN

### U5 AP2139AK-3.3TRG1

- 1: VIN
- 2: GND
- 3: CE
- 4: NC
- 5: VOUT

### U7 / U8 / U9 / U10 / U12 / U13 MAX40203ANS+T

- A1: VDD
- B1: EN
- A2: OUT
- B2: GND

## Named Nets / Signals

- +VIN
- +VBAT
- +VUSB
- +VMAIN
- +1V8
- +3V3
- +3V3_OUT
- +3V3_USB
- +VIO
- DISCHRG
- EN
- GND
- nEN_3V3_OUT

## Schematic Notes

- MAIN SUPPLY:
  - max 1.5A at +VMAIN
- 3V3 OUTPUT SUPPLY:
  - 150mA
  - +3V3/0.5A
  - Isdmax=1uA
- USB LDO:
  - Iqmax=1.5uA
  - Isdmax=1uA
  - VEN-IH=1.2V
  - VEN-IL=0.3V
  - IPD-EN=0.2uA

## Title Block

- Company: FAE Technology
- Address: via C. Battisti 136, 24025, Gazzaniga (Bg), Italy
- Mail: info@fae.technology
- Tel: +39 035738130
- Project: SWAN
- Board: SWAN-F
- Page name: 03 - POWER
- Designer: M. Gregis
- Approved: G.Boschini
- Project Code: 2021-0248
- Customer: Blues
- Internal Code: -
- Code: -
- Data: Tuesday, April 26, 2022
- Rev.: 7
- Rev. changes: See Revision Page
- Sheet: 4 / 5
- Legal note: Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.

## Page 5

# 04 - CPU

## Title block

- Project: **SWAN**
- Board: **SWAN-F**
- Page name: **04 - CPU**
- Designer: **M. Gregis**
- Approved: **G. Boschini**
- Project Code: **2021-0248**
- Customer: **Blues**
- Internal Code: **-**
- Code: **-**
- Date: **Tuesday, April 26, 2022**
- Rev.: **7**
- Rev. changes: **See Revision Page**
- Sheet: **5 / 5**
- Company: **FAE Technology**
- Address: **via C. Battisti 136, 24025, Gazzaniga (Bg), Italy**
- Mail: **info@fae.technology**
- Tel: **+39 035738130**
- Copyright note: Italian legal notice stating the project is protected by copyright law and reproduction/use, even partial, is forbidden without FAE Technology S.p.A. consent.

## Functional blocks

- **MCU**
- **USER LED**
- **QWIIC CONNECTOR**

## Components

### ICs / semiconductors

- **U6**: STM32L4R5ZIY6
  - Note: **Consumo 3V3: 17mA**
  - Notes near symbol:
    - **VDD = +1V7 - +3V6**
    - **VDDUSB = +3V - +3V6**
    - **DO NOT CONNECT PB2 TO VDD**
    - **USB DETECT 5V TOLERANT PIN**
    - **SET DISCHRG PIN AS OPEN-DRAIN WITHOUT PU/PD**
    - **VERSION BITS PG[0..3]**
- **Q1**: DMN62DOUW-7
- **LD2**: SML-P12U2TT86R
- **TVS1**: ESD523.3T1G
- **TVS2**: ESD523.3T1G

### Crystal / oscillator

- **Y1**: ABS06-107-32.768KHZ-*

### Resistors

- **R20**: 1k
- **R24**: 10M
- **R25**: N.U.
- **R28**: 10k
- **R29**: 10k
- **R30**: 10k
- **R31**: 10k
- **R37**: 10k
- **R38**: 0R
- **R40**: 10k
- **R41**: 10k
- **R42**: 10k
- **R43**: 10k

### Capacitors

- **C24**: value partly unclear, appears **10u/16V-X5R**
- **C25**: 100n/16V-X5R
- **C26**: 100n/16V-X5R
- **C27**: 4.7u/6.3V-X5R
- **C28**: 100n/16V-X5R
- **C29**: 100n/16V-X5R
- **C30**: 100n/16V-X5R
- **C31**: 1u/16V-X5R
- **C32**: 4p/50V-C0G
- **C33**: 4p/50V-C0G
- **C34**: 100n/16V-X5R
- **C35**: 100n/16V-X5R
- **C36**: 100n/16V-X5R
- **C37**: 100n/16V-X5R
- **C38**: 100n/16V-X5R
- **C39**: 100n/16V-X5R
- **C40**: 100n/16V-X5R
- **C41**: 100n/16V-X5R
- **C42**: 100n/16V-X5R
- **C43**: 100n/16V-X5R
- **C44**: 100n/16V-X5R
- **C45**: 100n/16V-X5R
- **C46**: 10n/16V-X5R

### Switches / buttons

- **PB1**: PB-SKRPAD*E010 / PB-SKRPADDE010, part text partly unclear
- **PB3**: PB-SKRPABE010

### Connectors

- **J5**: 21691
- **J6**: BM04B-SRSS-TBT

## Connectors and pin labels

### J5 — 21691

Readable pin/signal labels:

- **Pin 1**: +VIO
- **Pin 2**: T_SWD
- **Pin 4**: T_SWC
- **Pin 6**: T_JTDO
- **Pin 8**: T_JTDI
- **Pin 13**: T_VCP_RX
- **Pin 14**: T_VCP_TX
- Several pins are connected to GND / debug wiring, but not all pin labels are clearly readable in the image.

### J6 — Qwiic connector, BM04B-SRSS-TBT

- **Pin 1**: +VIO
- **Pin 2**: GND
- **Pin 3**: SDA
- **Pin 4**: SCL

## MCU U6 visible pin labels

### Port A

- PA0
- PA1
- PA2
- PA3
- PA4
- PA5
- PA6
- PA7
- PA8
- PA9
- PA10
- PA11
- PA12
- PA13/JTMS/SWDIO
- PA14/JTCK/SWCLK
- PA15/JTDI

### Port B

- PB0
- PB1
- PB2/BOOT1
- PB3/JTDO
- PB4/NJTRST
- PB5
- PB6
- PB7
- PB8
- PB9
- PB10
- PB11
- PB12
- PB13
- PB14
- PB15

### Port C

- PC0
- PC1
- PC2
- PC3
- PC4
- PC5
- PC6
- PC7
- PC8
- PC9
- PC10
- PC11
- PC12
- PC13
- PC14-OSC32_IN
- PC15-OSC32_OUT

### Port D

- PD0
- PD1
- PD2
- PD3
- PD4
- PD5
- PD6
- PD7
- PD8
- PD9
- PD10
- PD11
- PD12
- PD13
- PD14
- PD15

### Port E

- PE0
- PE1
- PE2
- PE3
- PE4
- PE5
- PE6
- PE7
- PE8
- PE9
- PE10
- PE11
- PE12
- PE13
- PE14
- PE15

### Port F

- PF0
- PF1
- PF2
- PF3
- PF4
- PF5
- PF6
- PF7
- PF10
- PF11
- PF12
- PF13
- PF14
- PF15

### Port G

- PG0
- PG1
- PG2
- PG3
- PG4
- PG5
- PG6
- PG7
- PG8
- PG9
- PG10
- PG12
- PG13

### Oscillator / reset / boot / power labels on U6

- RST
- BOOT0
- PH0-OSC_IN
- PH1-OSC_OUT
- VDDIO2
- VDD
- VDDUSB
- VBAT
- VDDA
- VREF+
- VSS
- VSSA/VREF-

## Named nets / signals

### Power and ground

- +VIO
- +VMAIN
- +USB
- +3V3_USB
- GND

### Debug / programming / boot

- T_SWD
- T_SWC
- T_JTDO
- T_JTDI
- T_VCP_RX
- T_VCP_TX
- RST#
- BOOT
- BOOT0
- RST

### User LED

- LED

### USB

- USB_DM
- USB_DP
- OTG_FS_DM
- OTG_FS_DP
- USB DETECT

### UART / USART / LPUART

- USART1_TX
- USART1_RX
- USART1_RTS
- USART1_CTS
- USART2_TX
- USART2_RX
- USART2_RTS
- USART2_CTS
- USART3_TX
- USART3_RX
- USART3_RTS
- USART3_CTS
- LPUART1_RX
- LPUART1_TX
- TX
- RX
- TX2
- RX2
- TX3
- RX3
- RTS
- CTS
- RTS2
- CTS2
- RTS3
- CTS3

### I2C

- I2C1_SCL
- I2C1_SDA
- I2C2_SCL
- I2C2_SDA
- I2C3_SCL
- I2C3_SDA
- SCL
- SDA
- SCL2
- SDA2
- SCL3
- SDA3

### SPI

- SPI2_NSS
- SPI2_SCK
- SPI2_MISO
- SPI2_MOSI
- CS
- SCK
- MISO
- MOSI

### OSPI / QSPI-style signals

- OSPI1_P1_IO0
- OSPI1_P1_IO1
- OSPI1_P1_IO2
- OSPI1_P1_IO3
- OSPI1_P1_CLK
- OSPI1_P1_CS
- QIO0
- QIO1
- QIO2
- QIO3
- QCLK
- QCS

### ADC

- ADC1_IN2
- ADC1_IN3
- ADC1_IN4
- ADC1_IN5
- ADC1_IN6
- ADC1_IN8
- ADC1_IN13
- ADC1_IN14
- ADC1_IN16

### GPIO / board I/O labels

- GPIO
- A0
- A1
- A2
- A3
- A4
- A5
- A6
- A7
- D0
- D1
- D2
- D3
- D4
- D5
- D6
- D7
- D8
- D9
- D10
- D12
- D13
- D14
- D15
- QEN
- DISCHRG
- nEN_3V3_OUT

### Other MCU-related labels

- VERSION BITS PG[0..3]
- PC14-OSC32_IN
- PC15-OSC32_OUT
- PH0-OSC_IN
- PH1-OSC_OUT
