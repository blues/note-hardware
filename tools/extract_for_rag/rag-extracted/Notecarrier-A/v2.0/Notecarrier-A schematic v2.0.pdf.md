---
product: Notecarrier-A
version: v2.0
doc_type: schematic
source_file: Notecarrier-A/v2.0/Notecarrier-A schematic v2.0.pdf
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-A — SCHEMATIC (v2.0)

_Source: `Notecarrier-A/v2.0/Notecarrier-A schematic v2.0.pdf`_

## Page 1

## Components

- **CS1**: CS V16 4L 35um
- **FID1**: Fiducial
- **FID2**: Fiducial
- **FID3**: Fiducial
- **FID4**: Fiducial
- **OBJ1**: 9774025151R
- **ASS1**: KNOB M2.5x4-INOX

## Connectors

- No connectors visible on this page.

## Named Nets / Signals

- **GND**

## Revision Notes

- **Revision 16**
  - Date: 01/10/2021
  - Author: G.Boschini
  - Description: Added QWIIC connectors

## Title Block

- Company: Blues Inc
- Project: NOTEBOX
- Board: NOTECARRIER AL
- Project Code: 2021-0324
- Page name: 00 - REVISION
- Internal Code: -
- Code: -
- Date: Friday, October 01, 2021
- Rev.: 16
- Rev. changes: See Revision Page
- Sheet: 1 / 4
- Copyright: Copyright (c) 2020 Blues Inc

## Designer

- Designed by: FAE Technology
- Address: via C. Battisti, 136, 24025 Gazzaniga (Bg), Italy
- Mail: info@fae.technology
- Phone: +39035738130

## Page 2

# Components / Blocks

- No component reference designators are visible on this page.
- BATTERY CHARGER
- uUSB
- BUCK
- BOOST
- SWITCH
- LNA
- PROTECTION NET
- PADs
- I2C GROVE
- M.2 CONNECTOR KEY E
- NANO SIM CONNECTOR
- MAIN uFL
- GPS uFL
- Solar panel: 0.5W
- Li-po battery: 3.3V - 4.2V
- LTE antenna
- GPS antenna

# Connectors and Pin/Signal Labels

- I2C GROVE
  - I2C

- PADs
  - I2C
  - V+
  - PROTECTION NET

- M.2 CONNECTOR KEY E
  - V+
  - VACT_GPS_OUT
  - NANO SIM SIGNALS
  - VIO
  - PROTECTION NET

- NANO SIM CONNECTOR
  - NANO SIM SIGNALS

- MAIN uFL
  - LTE

- GPS uFL
  - GPS

- uUSB
  - VUSB

# Named Nets / Signals

- VBAT_BC
- VUSB
- VMAIN
- +1V8
- +3V3
- VIO
- VACT_GPS_OUT
- NANO SIM SIGNALS
- I2C
- V+
- PROTECTION NET
- LTE
- GPS

# Title Block

- Company: Blues Inc
- Project: NOTEBOX
- Board: NOTECARRIER AL
- Project Code: 2021-0324
- Page name: 01 - BLOCK DIAGRAM
- Internal Code: -
- Code: -
- Date: Friday, October 01, 2021
- Rev.: 16
- Rev. changes: See Revision Page
- Sheet: 2 / 4
- Copyright: Copyright (c) 2020 Blues Inc
- Designed by: FAE Technology
  - via C. Battisti, 136
  - 24025 Gazzaniga (Bg), Italy
  - Mail: info@fae.technology
  - Phone: +39035738130
- Address / Mail / Phone fields are present but blank.

## Page 3

# Page: 02 - POWER

## Components

### ICs
- U1 — TPS62748YFPT
- U2 — MAX17225ELT
- U3 — BQ24210DQCT

### Diodes / TVS
- DS2 — FSV1045V
- DS3 — FSV1045V
- DS4 — STPS3H100U
- DS5 — STPS3H100U
- DS6 — FSV1045V
- TVS1 — SM6T6V8A

### Inductors
- L1 — XFL4020-222MEC
- L2 — 1285AS-H-2R2M=P2

### Resistors
- R1 — 10M/5%
- R4 — 82k
- R5 — 1M
- R6 — NU
- R8 — 10k
- R9 — 470R
- R10 — 10k

### Capacitors
- C1 — 10u/10V-X5R *(reference partly unclear)*
- C2 — 47u/6.3V-X5R
- C3 — 47u/6.3V-X5R
- C4 — 100n/10V-X5R
- C5 — 100n/16V
- C6 — 100n/16V
- C7 — 10u/6.3V-X5R
- C8 — 10u/6.3V-X5R
- C9 — 100n/16V
- C10 — 100n/16V
- C11 — 10n/1kV
- C12 — 10u/25V-X5R
- C13 — 1u/16V-X5R

### Connectors / Holders / Pads
- J2 — NU
- J3 — B2B-PH-SM4-TBT(LF)(SN)
- J4 — B2B-PH-SM4-TBT(LF)(SN)
- J9 — 12734
- J10 — 00711
- J11 — 10118192-0002LF
- J12 — B2B-PH-SM4-TBT(LF)(SN)
- BAT1 — NU, 3xAA battery holder
- PAD1 — pad to GND
- PAD2 — pad to GND

### Switch
- SW1 — CJS-1200TA

## Connectors and Pin Labels

### J9 — 12734
- Pin 1 — VUSB
- Pin 2 — VBAT
- Pin 3 — VMAIN
- Pin 4 — VIO
- Pin 5 — VSOLAR
- Pin 6 — V+
- Pin 7 — GND
- Pin 8 — EN
- Pin 9 — RST
- Pin 10 — BOOT
- Pin 11 — SCL
- Pin 12 — SDA
- Pin 13 — ATTN
- Pin 14 — AUX_EN
- Pin 15 — AUX_RX
- Pin 16 — AUX_TX
- Pin 17 — AUX1
- Pin 18 — AUX2
- Pin 19 — AUX3
- Pin 20 — AUX4
- Pin 21 — RX
- Pin 22 — TX

### J3 — Solar panel connector, B2B-PH-SM4-TBT(LF)(SN)
- Pin 1 — VSOLAR
- Pin 2 — GND

### J4 — Li-po battery connector, B2B-PH-SM4-TBT(LF)(SN)
- Pin 1 — VBAT
- Pin 2 — GND

### J12 — B2B-PH-SM4-TBT(LF)(SN)
- Pin 1 — V+
- Pin 2 — GND

### J2 — USB connector, NU
- Pin 1 — VCC / VUSB
- Pin 2 — D- / USB_DM
- Pin 3 — D+ / USB_DP
- Pin 4 — ID
- Pin 5 — GND
- Pin 6 — E1 / shield
- Pin 7 — E2 / shield
- Pin 8 — E3 / shield

### J11 — USB connector, 10118192-0002LF
- Pin 1 — VCC / VUSB
- Pin 2 — D- / USB_DM
- Pin 3 — D+ / USB_DP
- Pin 4 — ID
- Pin 5 — GND
- Pin 6 — E1 / USB_SHIELD
- Pin 7 — E2 / USB_SHIELD
- Pin 8 — E3 / USB_SHIELD
- Pin 9 — E4 / USB_SHIELD
- Pin 10 — E5 / USB_SHIELD
- Pin 11 — E6 / USB_SHIELD

### J10 — 00711
- Pin 1 — no readable label
- Pin 2 — GND
- Pin 3 — GND

### BAT1 — NU, 3xAA
- Pin 1 — + / VBAT
- Pin 2 — - / GND

### SW1 — CJS-1200TA
- Pin 1 — +1V8
- Pin 2 — VIO
- Pin 3 — +3V3

## Named Nets / Signals

- +1V8
- +3V3
- ATTN
- AUX1
- AUX2
- AUX3
- AUX4
- AUX5
- AUX_EN
- AUX_RX
- AUX_TX
- BAT-CHG
- BOOT
- EN
- GND
- RST
- RX
- SCL
- SDA
- TX
- USB_DM
- USB_DP
- USB_SHIELD
- V+
- VBAT
- VIO
- VMAIN
- VSOLAR
- VUSB

## Schematic Notes

- “Solar panel connector”
- “Li-po battery 3.3V - 4.2V”
- “Riset = Kiset / Iiset where Kiset is 395 typically. With 470R --> 800mA”
- “LiPo must be equal to or greater than 800mAh”
- Current annotations:
  - 180mA
  - 150mA

## Title Block

- Company: Blues Inc
- Project: NOTEBOX
- Board: NOTECARRIER AL
- Project Code: 2021-0324
- Page name: 02 - POWER
- Internal Code: -
- Code: -
- Date: Friday, October 01, 2021
- Rev.: 16
- Rev. changes: See Revision Page
- Sheet: 3 / 4
- Designed by: FAE Technology
  - via C. Battisti, 136
  - 24025 Gazzaniga (Bg), Italy
  - Mail: info@fae.technology
  - Phone: +39035738130
- Copyright (c) 2020 Blues Inc

## Page 4

# Components

## Connectors and electromechanical

- **J5**: NanoSIM - SF72S006VBAR2500
- **J6**: MDT420E01001
  - Markings: `BOTTOM`, `TOP`
- **J7**: uFL-R-SMT-1-10
  - Note near connector: **ASS2 uFL 50mm**
- **J8**: uFL-R-SMT-1-10
  - Note near connector: **ASS3 uFL 50mm**
- **J13**: BM04B-SRSS-TBT
  - Note: **Qwiic connector**
- **J14**: BM04B-SRSS-TBT
  - Note: **Qwiic connector**
- **ANT1**: NN03-310
  - Marking inside antenna block: `LTE-GNSS-BT`
- **ANT2**: NN03-320
  - Marking inside antenna block: `GPS/BT`

## ICs / semiconductors

- **Q1**: AO3420
- **TVS2**: ESDLC5V0M5-TP
- **U5**: BGA725L6E6327FTSA1
  - Note: `Consumo 3V3: 3.6mA`
  - Marking: `LNA`

## Fuses

- **F1**: SF-0603F150-2, F1.5A
- **F2**: 3.5A/32V

## Resistors / resistor arrays

- **R12**: 22R
- **R14**: 22R
- **R15**: 22R
- **R16**: 15k
- **R18**: 200k
- **R21**: 1k
- **R22**: 100k
- **R25**: 0R
- **R26**: NU
- **R27**: 0R
- **R28**: 0R
- **R29**: 0R
- **R30**: NU
- **R31**: NU
- **RR1**: 100R/5%
- **RR2**: 100R/5%

## Capacitors

- **C16**: 100n/16V
- **C17**: 33p/50V-COG
- **C18**: 33p/50V-COG
- **C19**: 33p/50V-COG
- **C21**: 1n/50V
- **C22**: 1u/6.3V-X5R
- **C23**: 100n/16V
- **C25**: 0.5p/50V-COG
- **C26**: 1p/50V-COG
- **C27**: 2.2p/50V-COG
- **C28**: 4.6p/50V-COG
- **C29**: 1.1p/50V-COG

## Inductors

- **L5**: LQW15AN7N5H00D
- **L6**: LQW18AN12NG80
- **L7**: LQW18AN10NG80D
- **L8**: LQW18AN8N4G80D
- **L9**: LQW15AN2N3G80D

# Connectors and pin labels

## J5 — NanoSIM - SF72S006VBAR2500

- **1**: VCC
- **2**: RST
- **3**: CLK
- **5**: GND
- **6**: VPP
- **7**: IO
- **10**: CSW
- **13**: DSW
- **8, 9, 11, 12, 14, 15, 16, 17, 18, 19**: GND

## J6 — MDT420E01001

### Left side / even pins

- **2**: VIO_P
- **4**: VIO_P
- **6**: GND
- **8**: SIM_VCC
- **10**: SIM_RST
- **12**: SIM_IO
- **14**: SIM_CLK
- **16**: SIM_NPRESENT
- **18**: GND
- **20**: VACT_GPS_OUT
- **22**: VACT_GPS_IN
- **32**: NC32
- **34**: NC34
- **36**: NC36
- **38**: NC38
- **40**: SCL_P
- **42**: SDA_P
- **44**: NC44
- **46**: AUX1
- **48**: AUX2
- **50**: AUX3
- **52**: AUX4
- **54**: ATTN_P
- **56**: AUX_EN_P
- **58**: AUX_RX_P
- **60**: AUX_TX_P
- **62**: RX_P
- **64**: TX_P
- **66**: NC66
- **68**: NC68
- **70**: VMODEM_P
- **72**: VMODEM_P
- **74**: VMODEM_P

### Right side / odd pins

- **1**: NC1
- **3**: GND
- **5**: GND
- **7**: USB_DP
- **9**: USB_DM
- **11**: GND
- **13**: VUSB
- **15**: NC15
- **17**: NC17
- **19**: NC19
- **21**: NC21
- **23**: NC23
- **33**: GND
- **35**: NC35
- **37**: NC37
- **39**: GND
- **41**: NC41
- **43**: NC43
- **45**: GND
- **47**: NC47
- **49**: NC49
- **51**: GND
- **53**: NC53
- **55**: NC55
- **57**: GND
- **59**: NC59
- **61**: NC61
- **63**: NC63
- **65**: NC65
- **67**: NRST
- **69**: NC69
- **71**: GND
- **73**: GND
- **75**: NC75

## J7 — uFL-R-SMT-1-10

- **1**: LTE_50
- **2**: GND
- **3**: GND

## J8 — uFL-R-SMT-1-10

- **1**: GPS_50
- **2**: GND
- **3**: GND

## J13 — BM04B-SRSS-TBT, Qwiic connector

- **1**: GND
- **2**: VIO
- **3**: SDA_P
- **4**: SCL_P

## J14 — BM04B-SRSS-TBT, Qwiic connector

- **1**: GND
- **2**: VIO
- **3**: SDA_P
- **4**: SCL_P

## ANT1 — NN03-310

- **1**: FEED_LTE
- **2**: MN1-A
- **3**: MN1-B
- **4**: NC4
- **5**: MN2-A
- **6**: MN2-B
- **7**: FEED_GNSS_BT

## ANT2 — NN03-320

- **1**: M1
- **2**: M2
- **3**: FEED_BT
- **4**: FEED_GPS

# Named nets / signals

- **ATTN**
- **ATTN_P**
- **AUX1**
- **AUX2**
- **AUX3**
- **AUX4**
- **AUX5**
- **AUX_EN**
- **AUX_EN_P**
- **AUX_RX**
- **AUX_RX_P**
- **AUX_TX**
- **AUX_TX_P**
- **BOOT**
- **FEED_BT**
- **FEED_GNSS_BT**
- **FEED_GPS**
- **FEED_LTE**
- **GND**
- **GPS_50**
- **GPS_50_A**
- **GPS_50_B**
- **GPS_50_C**
- **GPS_50_D**
- **GPS_50_E**
- **LTE_50**
- **LTE_50_A**
- **LTE_50_B**
- **LTE_50_C**
- **LTE_50_D**
- **MN1-A**
- **MN1-B**
- **MN2-A**
- **MN2-B**
- **NRST**
- **RST**
- **RX**
- **RX_P**
- **SCL**
- **SCL_P**
- **SDA**
- **SDA_P**
- **SIM_CLK**
- **SIM_IO**
- **SIM_NPRESENT**
- **SIM_RST**
- **SIM_VCC**
- **TX**
- **TX_P**
- **USB_DM**
- **USB_DP**
- **VACT_GPS_IN**
- **VACT_GPS_OUT**
- **VIO**
- **VIO_P**
- **VMAIN**
- **VMODEM_P**
- **VUSB**

# Title block / notes

- **Company**: Blues Inc
- **Project**: NOTEBOX
- **Board**: NOTECARRIER AL
- **Project Code**: 2021-0324
- **Page name**: 03 - CONNECTOR
- **Internal Code**: -
- **Code**: -
- **Date**: Friday, October 01, 2021
- **Rev.**: 16
- **Rev. changes**: See Revision Page
- **Sheet**: 4 / 4
- **Designed by**: FAE Technology
  - via C. Battisti, 136
  - 24025 Gazzaniga (Bg), Italy
  - Mail: info@fae.technology
  - Phone: +39035738130
- **Copyright**: Copyright (c) 2020 Blues Inc
