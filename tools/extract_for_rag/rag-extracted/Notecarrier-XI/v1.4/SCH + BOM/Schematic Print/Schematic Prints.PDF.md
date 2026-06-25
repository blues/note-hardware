---
product: Notecarrier-XI
version: v1.4
doc_type: schematic
source_file: Notecarrier-XI/v1.4/SCH + BOM/Schematic Print/Schematic Prints.PDF
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-XI — SCHEMATIC (v1.4)

_Source: `Notecarrier-XI/v1.4/SCH + BOM/Schematic Print/Schematic Prints.PDF`_

## Page 1

# Notecarrier-XI — Cover Page

## Sheet Index

- **01** — Cover
- **02** — Block Diagram
- **03** — IO Connection
- **04** — Notecard Connection
- **05** — Power
- **06** — Starnote Connection

## Components / Reference Designators

### Board Support

- **FD1** — board support marker / fiducial; value not shown
- **FD2** — board support marker / fiducial; value not shown
- **FD3** — board support marker / fiducial; value not shown
- **FD4** — board support marker / fiducial; value not shown
- **FD5** — board support marker / fiducial; value not shown
- **FD6** — board support marker / fiducial; value not shown
- **PCB1** — PCB
- **DOC1** — HW-E

### Reference Designators Mentioned Only in Revision Notes

- **P3** — ESLOV Connector; removed in revision 2
- **J7** — Starnote-I SIM cage; removed in revision 2
- **D4** — added for USB Starnote power; value not shown
- **J9** — added for Starnote firmware update via WiFi; value not shown
- **R24** — added for Starnote firmware update via WiFi; value not shown
- **R25** — added for Starnote firmware update via WiFi; value not shown
- **R26** — added for Starnote firmware update via WiFi; value not shown
- **R27** — added for Starnote firmware update via WiFi; value not shown
- **R28** — added for Starnote firmware update via WiFi; value not shown
- **SW2** — added for Starnote boot; value not shown
- **C31** — added for Starnote boot; value not shown
- **D5** — added for Starnote boot; value not shown

## Connectors

- No connector pin labels are shown on this page.

## Named Nets / Signals

- No named nets or signals are shown on this page.

## Revision History

| Revision | Date | Description |
|---:|---|---|
| 1 | 2025-03-03 | Initial prototype release |
| 2 | 2025-07-03 | Removed ESLOV Connector (P3). Removed the Starnote-I SIM cage (J7 and supporting passive components). Added Ignion NN03-310 Notecard LTE antenna, matching network and uFl antenna connector. Added supercaps and supercap charger IC. Added solar panel input connection and changed LiPo linear charger. |
| 3 | 2025-08-22 | Added D4 for USB Starnote power. Added J9, R24, R25, R26, R27, R28 for Starnote fw update via wifi. |
| 4 | 2025-10-08 | Added SW2, C31, D5 for Starnote boot. |

## Design Considerations Notes

- **Software Config Note:**
  - Contains important notes for software development.
  - Things like: pin configuration, timing requirements, IC configuration etc.
- **Design Note:**
  - Hardware notes

## Title Block

- **Company:** FAE Technology
- **Project:** Notecarrier-XI
- **Board:** Notecarrier-XI
- **Designer:** S. Vaghi / L. Brighenti
- **Project Code:** 2025-0019
- **Internal Code:** -
- **Page name:** 01_COVER.SchDoc
- **Approved:** -
- **Customer:** BLUES Inc
- **Code:** -
- **Data:** 08/10/2025
- **Rev.:** 4
- **Rev. changes:** not filled
- **Sheet:** 01 / 06

## Legal Note

- “Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.”

## Page 2

## Page

- Page name: `02_BLOCK-DIAGRAM.SchDoc`
- Sheet: `02 / 06`
- Project: `Notecarrier-XI`
- Board: `Notecarrier-XI`

## Component Reference Designators

- No component reference designators are visible on this page.
- Functional blocks / parts shown:
  - `USB C`
  - `SOLAR JST`
  - `BAT JST`
  - `LiPo Charger`
  - `BuckBoost Supercap Charger`
  - `Buck 3V3`
  - `PIN HEADER`
  - `M.2 CONNECTOR KEY E` — `Notecard`
  - `M.2 CONNECTOR KEY E` — `Starnote`
  - Unlabeled capacitor symbol to ground on `+VMODEM`

## Connectors and Pin Labels

### USB C Connector, left

- Labels / connected signals:
  - `+VUSB`
  - `USB`

### SOLAR JST

- Labels / connected signals:
  - `+VSOLAR`

### BAT JST

- Labels / connected signals:
  - `+VBAT`

### PIN HEADER

- Labels / connected signals:
  - `+VBAT`
  - `+VUSB`
  - `+VMAIN`
  - `+VIO`
  - `+VACT_GPS_IN`
  - `+VACT_GPS_OUT`
  - `I2C, UART, AUX_UART, AUX_GPIO, DFU, NRST, ATTN`

### M.2 CONNECTOR KEY E — Notecard

- Labels / connected signals:
  - `USB`
  - `I2C`
  - `STATUS`
  - `+VMODEM`
  - `+VIO`
  - `+VACT_GPS_IN`
  - `+VACT_GPS_OUT`
  - `I2C, UART, AUX_UART, AUX_GPIO, DFU, NRST, ATTN`

### USB C Connector, right / top

- Labels / connected signals:
  - `+VUSB_S`
  - `USB`

### M.2 CONNECTOR KEY E — Starnote

- Labels / connected signals:
  - `USB`
  - `+VMODEM`
  - `UART`
  - `ODFU`
  - `+VIO`

## Named Nets / Signals

- `+VUSB_S`
- `+VUSB`
- `+VSOLAR`
- `+VBAT`
- `+VMAIN`
- `+VMODEM`
- `+VIO`
- `+VACT_GPS_IN`
- `+VACT_GPS_OUT`
- `USB`
- `I2C`
- `STATUS`
- `UART`
- `ODFU`
- `AUX_UART`
- `AUX_GPIO`
- `DFU`
- `NRST`
- `ATTN`
- `GND` / ground symbol shown at capacitor on `+VMODEM`

## Functional Connections Shown

- `+VUSB` from left `USB C` to `LiPo Charger`.
- `+VSOLAR` from `SOLAR JST` to `LiPo Charger`.
- `+VBAT` between `BAT JST`, `LiPo Charger`, and `PIN HEADER`.
- `+VUSB` routed to `PIN HEADER`.
- `LiPo Charger` outputs `+VMAIN`.
- `+VMAIN` feeds:
  - `BuckBoost Supercap Charger`
  - `Buck 3V3`
  - `PIN HEADER`
- `BuckBoost Supercap Charger` outputs `+VMODEM` to Notecard `M.2 CONNECTOR KEY E`.
- `+VMODEM` also routes from Notecard `M.2 CONNECTOR KEY E` to Starnote `M.2 CONNECTOR KEY E`.
- `Buck 3V3` outputs `+VIO` to Notecard `M.2 CONNECTOR KEY E`.
- `+VIO` also routes to:
  - `PIN HEADER`
  - Starnote `M.2 CONNECTOR KEY E`
- `USB` bus connects:
  - left `USB C`
  - Notecard `M.2 CONNECTOR KEY E`
  - right/top `USB C`
  - Starnote `M.2 CONNECTOR KEY E`
- `I2C` bus connects `LiPo Charger` and Notecard `M.2 CONNECTOR KEY E`.
- `STATUS` signal connects `LiPo Charger` to Notecard `M.2 CONNECTOR KEY E`.
- `UART` connects Notecard `M.2 CONNECTOR KEY E` to Starnote `M.2 CONNECTOR KEY E`.
- `ODFU` connects Notecard `M.2 CONNECTOR KEY E` to Starnote `M.2 CONNECTOR KEY E`.
- `+VACT_GPS_IN` and `+VACT_GPS_OUT` connect between `PIN HEADER` and Notecard `M.2 CONNECTOR KEY E`.

## Title Block Notes

- Company / logo: `FAE TECHNOLOGY`
- Project: `Notecarrier-XI`
- Board: `Notecarrier-XI`
- Designer: `S. Vaghi / L. Brighenti`
- Project Code: `2025-0019`
- Internal Code: `-`
- Page name: `02_BLOCK-DIAGRAM.SchDoc`
- Approved: `-`
- Customer: `BLUES Inc`
- Code: `-`
- Date: `08/10/2025`
- Rev.: `4`
- Sheet: `02 / 06`
- Copyright note: `Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.`

## Page 3

# Schematic Page Transcription

## Page Sections

- I/O Pin Headers & Castellations
- Mech Support / Solar Connector
- Solar Connector
- USB C Connector
- QWIIC Connector
- Battery Connector

## Components

- **P1** — Header 2.54mm 1x16
- **P2** — Header 2.54mm 1x16
- **J1** — Header 2.54mm 1x4
- **J8** — B2B-PH-SM4-TBT(LF)(SN)
- **P4** — 12402012E212A
- **J2** — SM04B-SRSS-TB(LF)(SN)
- **J3** — S2B-PH-SM4-K-TB
- **R1** — 5k1
- **R2** — 5k1
- **R3** — 1M
- **C1** — 10n/1000V

## Connectors and Pin Labels

### P1 — Header 2.54mm 1x16

- Pin 1 — +VBAT
- Pin 2 — +VUSB
- Pin 3 — +VMAIN
- Pin 4 — +VIO
- Pin 5 — BOOT
- Pin 6 — NRST
- Pin 7 — AUX_NCHARGING
- Pin 8 — VIO_EN
- Pin 9 — +VACT_GPS_OUT
- Pin 10 — +VACT_GPS_IN
- Pin 11 — ALT_DFU_IDLE
- Pin 12 — ALT_DFU_NRESET
- Pin 13 — ALT_DFU_BOOT
- Pin 14 — ALT_DFU_TX
- Pin 15 — ALT_DFU_RX
- Pin 16 — GND

### P2 — Header 2.54mm 1x16

- Pin 1 — GND
- Pin 2 — AUX_TX
- Pin 3 — AUX_RX
- Pin 4 — AUX_EN
- Pin 5 — AUX4
- Pin 6 — AUX3
- Pin 7 — AUX2
- Pin 8 — AUX1
- Pin 9 — ATTN
- Pin 10 — CTX
- Pin 11 — RTX
- Pin 12 — NC_TX / TX
- Pin 13 — NC_RX / RX
- Pin 14 — SCL
- Pin 15 — SDA
- Pin 16 — GND

### J1 — Header 2.54mm 1x4

- Pin 1 — +VSOLAR
- Pin 2 — +VSOLAR
- Pin 3 — GND
- Pin 4 — GND

### J8 — B2B-PH-SM4-TBT(LF)(SN)

- Pin 1 — +VSOLAR
- Pin 2 — GND
- M — no-connect marker shown

### P4 — USB C Connector, 12402012E212A

- A4 — VBUS, +VUSB
- A9 — VBUS, +VUSB
- A5 — CC1, via R1 5k1 to GND
- A6 — D+, USB_D_P
- A7 — D-, USB_D_N
- A8 — SBU1, no-connect marker shown
- A1 — GND
- A12 — GND
- B4 — VBUS, +VUSB
- B9 — VBUS, +VUSB
- B5 — CC2, via R2 5k1 to GND
- B6 — D+, USB_D_P
- B7 — D-, USB_D_N
- B8 — SBU2, no-connect marker shown
- B1 — GND
- B12 — GND
- M — USB_SHIELD
  - USB_SHIELD connected to GND through **C1 10n/1000V**
  - USB_SHIELD connected to GND through **R3 1M**

### J2 — QWIIC Connector, SM04B-SRSS-TB(LF)(SN)

- Pin 1 — GND
- Pin 2 — +VIO
- Pin 3 — SDA
- Pin 4 — SCL

### J3 — Battery Connector, S2B-PH-SM4-K-TB

- Pin 1 — +VBAT
- Pin 2 — GND
- M — no-connect marker shown

## Named Nets / Signals

- +VBAT
- +VUSB
- +VMAIN
- +VIO
- +VACT_GPS_OUT
- +VACT_GPS_IN
- +VSOLAR
- GND
- BOOT
- NRST
- AUX_NCHARGING
- VIO_EN
- ALT_DFU_IDLE
- ALT_DFU_NRESET
- ALT_DFU_BOOT
- ALT_DFU_TX
- ALT_DFU_RX
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
- NC_TX
- NC_RX
- SCL
- SDA
- USB_D_P
- USB_D_N
- USB_SHIELD

## Design Notes

- QWIIC Connector:
  - **DESIGN NOTE:** The I2C bus is pulled up by the Notecard
- Battery Connector:
  - **DESIGN NOTE:** Li-Po Battery 3.3V - 4.2V

## Title Block

- Company/logo: FAE Technology
- Project: Notecarrier-XI
- Board: Notecarrier-XI
- Designer: S. Vaghi / L. Brighenti
- Project Code: 2025-0019
- Internal Code: -
- Page name: 03_IO-CONNECTION.SchDoc
- Approved: -
- Customer: BLUES Inc
- Code: -
- Data: 08/10/2025
- Rev.: 4
- Sheet: 03 / 06
- Footer note: Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.

## Page 4

# Schematic Page Transcription

## Page Sections

- **Notecard Connector**
- **SIM Card**
- **Notecard Support**
- **Antenna uFL to IGNION NN03-310**

---

## Components

### Notecard Connector

- **J4**: MDT420E01001
- **R4**: 0R0

### SIM Card

- **J5**: SF72S006VBDR2500
- **R5**: 22R
- **R6**: 22R
- **R7**: 15k
- **R8**: 22R
- **C2**: 100n
- **C3**: 33p
- **C4**: 33p
- **C5**: 33p
- **TVS1**: PESD5V0L5UV,125

### Notecard Support

- **ASS1**: KNOB M2.5x4-INOX
- **OBJ1**: 9774025151R

### Antenna uFL to IGNION NN03-310

- **J7**: U.FL-R-SMT-1(10)
- **R20**: 0R0
- **R21**: 0R0
- **R22**: 0R0
- **R23**: 0R0
- **C24**: 2.2p
- **C25**: 1p
- **C26**: 0.5p
- **L3**: LQW15AN2N3G80D
- **L4**: LQW18AN10NG80D
- **L5**: LQW18AN8N4G80D
- **L6**: LQW18AN12NG80D
- **ANT1**: NN03-310, LTE-GNSS-BT

---

## Connectors and Pin Labels

### J4 — Notecard Connector — MDT420E01001

#### Left / Bottom-side pins

- **2**: VIO_P
- **4**: VIO_P
- **6**: GND
- **8**: SIM_VCC
- **10**: SIM_RST
- **12**: SIM_IO
- **14**: SIM_CLK
- **16**: SIM_PRESENT
- **18**: GND
- **20**: VACT_GPS_OUT
- **22**: VACT_GPS_IN
- **32**: ALT_DFU_BOOT
- **34**: ALT_DFU_RESET
- **36**: ALT_DFU_ACTIVE
- **38**: AUX_CHARGING
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

#### Right / Top-side pins

- **1**: XP_ENABLE
- **3**: GND
- **5**: GND
- **7**: USB_DP
- **9**: USB_DN
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
- **41**: ALT_DFU_RX
- **43**: ALT_DFU_TX
- **45**: GND
- **47**: RTX
- **49**: CTX
- **51**: GND
- **53**: NC53
- **55**: NC55
- **57**: GND
- **59**: NC59
- **61**: NC61
- **63**: NC63
- **65**: BOOT
- **67**: RST
- **69**: NC69
- **71**: GND
- **73**: GND
- **75**: XP_MODEM_VSEL

### J5 — SIM Card Connector — SF72S006VBDR2500

- **1**: VCC
- **2**: RST
- **3**: CLK
- **5**: GND
- **6**: VPP
- **7**: IO
- **8**: GND
- **9**: GND
- **10**: CSW
- **11**: GND
- **12**: GND
- **13**: DSW
- **14**: GND
- **15**: GND
- **16**: GND
- **17**: GND
- **18**: GND
- **19**: GND

### J7 — u.FL Connector — U.FL-R-SMT-1(10)

- Signal connection: **LTE_50**
- Ground / shield connection: **GND**

### ANT1 — Antenna — NN03-310

- **1**: FEED_LTE
- **2**: MN1-A
- **3**: MN1-B
- **4**: NC
- **5**: MN2-A
- **6**: MN2-B
- **7**: FEED_GNSS_BT

### OBJ1 — Support / Hardware Item

- Visible pin: **T**
- Connected to: **GND**

---

## Named Nets and Signals

### Power and Ground

- **+VIO**
- **+VACT_GPS_OUT**
- **+VACT_GPS_IN**
- **+VMAIN**
- **+VUSB**
- **GND**

### USB

- **USB_D_P**
- **USB_D_N**
- **USB_DP**
- **USB_DN**
- **VUSB**

### SIM

- **SIM_VCC**
- **SIM_RST**
- **SIM_IO**
- **SIM_CLK**
- **SIM_NPRESENT**
- **SIM_PRESENT**

### Notecard / DFU / Control

- **ALT_DFU_BOOT**
- **ALT_DFU_NRESET**
- **ALT_DFU_RESET**
- **ALT_DFU_IDLE**
- **ALT_DFU_ACTIVE**
- **ALT_DFU_RX**
- **ALT_DFU_TX**
- **AUX_NCHARGING**
- **AUX_CHARGING**
- **BOOT**
- **NRST**
- **RST**
- **XP_ENABLE**
- **XP_MODEM_VSEL**

### I2C / AUX / UART

- **SCL**
- **SCL_P**
- **SDA**
- **SDA_P**
- **AUX1**
- **AUX2**
- **AUX3**
- **AUX4**
- **ATTN**
- **ATTN_P**
- **AUX_EN**
- **AUX_EN_P**
- **AUX_RX**
- **AUX_RX_P**
- **AUX_TX**
- **AUX_TX_P**
- **RX**
- **RX_P**
- **TX**
- **TX_P**
- **NC_RX**
- **NC_TX**
- **RTX**
- **CTX**

### Modem / GPS

- **VACT_GPS_OUT**
- **VACT_GPS_IN**
- **VMODEM_P**

### RF / Antenna

- **LTE_50**
- **LTE_50_A**
- **LTE_50_B**
- **LTE_50_C**
- **LTE_50_D**
- **FEED_LTE**
- **FEED_GNSS_BT**

### No-connect Labels Visible on J4

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

---

## Title Block Notes

- **Company / logo**: FAE TECHNOLOGY
- **Project**: Notecarrier-XI
- **Board**: Notecarrier-XI
- **Page name**: 04_NOTECARD-CONNECTION.SchDoc
- **Designer**: S. Vaghi / L. Brighenti
- **Approved**: -
- **Project Code**: 2025-0019
- **Customer**: BLUES Inc
- **Internal Code**: -
- **Code**: -
- **Date**: 08/10/2025
- **Rev.**: 4
- **Rev. changes**: blank
- **Sheet**: 04 / 06
- **Copyright note**: “Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.”

## Page 5

# Page: Power

## Functional Blocks

- VBUS ORing
- 3V3 Buck/Boost Regulator
- Battery Charger w/ Power Path
- BuckBoost Supercapacitor Charger/Balancer

## Components

### VBUS ORing

- C9: 10u
- D2: FSV1045V
- D3: DFLS1100-7
- D4: DFLS1100-7

### 3V3 Buck/Boost Regulator

- U1: ISL9122AIRNZ-T
- L1: MCKK1608T1R0MN
- C6: 22u
- C7: 100n
- C8: 22u
- R9: 10M

### Battery Charger w/ Power Path

- U3: BQ25628ERYKR
- L7: XFL4020-152MEC
- LD1: SML-P12WTT86R
- C10: 47n/50V
- C11: 100n
- C12: 10u
- C13: 10u
- C27: 4u7
- C28: 10u
- C29: 100n
- C30: 4u7
- R29: 3k
- R30: 3k
- R31: 11k
- R32: 15k

### BuckBoost Supercapacitor Charger/Balancer

- U2: LTC3128EUFD#PBF
- L2: SRP7050WA-3R3M
- C14: BCAP0010_P300_X12
- C15: 10u
- C16: 10u
- C18: 10u
- C19: 10u
- C20: 10u
- C21: BCAP0010_P300_X12
- C22: 10u
- C23: 220p
- R10: 0R0
- R11: 100k
- R12: 732k
- R14: 100k
- R18: 7k32
- R19: 135k

## Connectors

- No connector reference designators visible on this page.

## IC Pin Labels

### U1: ISL9122AIRNZ-T

- Pin 1: LX1
- Pin 2: GND
- Pin 3: LX2
- Pin 4: VOUT
- Pin 5: EN
- Pin 6: SDA
- Pin 7: SCL
- Pin 8: VIN
- Pin 9: EP

### U2: LTC3128EUFD#PBF

- Pin 1: SW1_1
- Pin 2: RSENP
- Pin 3: RSENS
- Pin 4: RUN
- Pin 5: PROG
- Pin 6: NC_1
- Pin 7: VIN
- Pin 8: PFO
- Pin 9: PFI
- Pin 10: MAXV
- Pin 11: FB
- Pin 12: PGOOD
- Pin 13: MID
- Pin 14: VOUTS
- Pin 15: VOUTP_1
- Pin 16: VOUTP_2
- Pin 17: SW2_1
- Pin 18: SW2_2
- Pin 19: SW1_2
- Pin 20: NC_2
- Pin 21: GND

### U3: BQ25628ERYKR

- Pin 1: BTST
- Pin 2: REGN
- Pin 3: PG
- Pin 4: ILIM
- Pin 5: TS_BIAS
- Pin 6: TS
- Pin 7: QON
- Pin 8: BAT
- Pin 9: SYS
- Pin 10: STAT
- Pin 11: INT
- Pin 12: SDA
- Pin 13: SCL
- Pin 14: CE
- Pin 15: GND
- Pin 16: SW
- Pin 17: PMID
- Pin 18: VBUS

## Named Nets / Signals

- +VBUS
- +VSOLAR
- +VUSB
- +VUSB_S
- +VMAIN
- +VIO
- +VBAT
- +VMODEM
- GND
- VIO_EN
- SDA
- SCL
- AUX_NCHARGING
- SW
- CHG_SW1
- CHG_SW2
- CHG_RSENS
- CHG_RPROG
- CHG_MAXV
- CHG_MID
- CHG_FB
- CHG_PGOOD

## Design Notes

### 3V3 Buck/Boost Regulator

- Input Voltage: 1.8V - 5.5V
- Output Voltage: 3.3V
- Peak Output Current: 500mA
- Average Current: 100mA

### Battery Charger

- Default charging voltage: 4.2V
- Default charging current: 320mA
- Default termination current: 20mA
- Default pre-charge current: 20mA
- No battery thermal protection

### Power Path / Buck Regulator

- Power Path:
  - Input current limit: 3.5A
  - 26mOhm reverse blocking transistor
  - 15mOhm battery transistor
- Buck Regulator:
  - 1.5MHz frequency
  - Input Voltage: 5V
  - Output Voltage: 3.3-4.2V
  - Peak current: 2.5A

### Supercapacitor Charger/Balancer Notes

- PLACE THERMAL VIA
- VREF=0.58V
- VOUT=4.826V
- ILIMIT=1.5A
- VMAXV=2.7V

## Title Block

- Company: FAE Technology
- Project: Notecarrier-XI
- Board: Notecarrier-XI
- Page name: 05_POWER.SchDoc
- Designer: S. Vaghi / L. Brighenti
- Approved: -
- Project Code: 2025-0019
- Customer: BLUES Inc
- Internal Code: -
- Code: -
- Date: 08/10/2025
- Rev.: 4
- Sheet: 05 / 06
- Copyright note: “Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.”

## Page 6

## Page Sections

- Starnote Connector
- USB C Connector
- Starnote Support
- Starnote user button
- Starnote ODFU

## Components

- **J6** — `MDT420E01001`, Starnote connector
- **P5** — `12402012E212A`, USB-C connector
- **R15** — `5k1`
- **R16** — `5k1`
- **C17** — `10n/1000V`
- **R17** — `1M`
- **ASS2** — `KNOB M2.5x4-INOX`
- **OBJ2** — `9774025151R`
- **D1** — `PESD5V0X1UB,135`
- **SW1** — `EVP-BB2A9B000`
- **D5** — `PESD5V0X1UB,135`
- **SW2** — `EVP-BB2A9B000`
- **C31** — `100n`
- **S9** — `GRIP 5Px2 - MDT`
- **R24** — `0R0`
- **R25** — `0R0`
- **R26** — `0R0`
- **R27** — `0R0`
- **R28** — `0R0`

## Connector J6 — Starnote Connector

- Part: `MDT420E01001`

### J6 Bottom Pins

- **2** — `VIO_P`
- **4** — `VIO_P`
- **6** — `GND`
- **8** — `SIM_VCC`
- **10** — `SIM_RST`
- **12** — `SIM_IO`
- **14** — `SIM_CLK`
- **16** — `SIM_PRESENT`
- **18** — `GND`
- **20** — `VACT_GPS_OUT`
- **22** — `VACT_GPS_IN`
- **32** — `ALT_DFU_BOOT`
- **34** — `ALT_DFU_RESET`
- **36** — `ALT_DFU_ACTIVE`
- **38** — `AUX_CHARGING`
- **40** — `SCL_P`
- **42** — `SDA_P`
- **44** — `NC44`
- **46** — `AUX1`
- **48** — `AUX2`
- **50** — `AUX3`
- **52** — `AUX4`
- **54** — `ATTN_P`
- **56** — `AUX_EN_P`
- **58** — `AUX_RX_P`
- **60** — `AUX_TX_P`
- **62** — `NC_TX`
- **64** — `NC_RX`
- **66** — `NC66`
- **68** — `NC68`
- **70** — `VMODEM_P`
- **72** — `VMODEM_P`
- **74** — `VMODEM_P`

### J6 Top Pins

- **1** — `XP_ENABLE`
- **3** — `GND`
- **5** — `GND`
- **7** — `USB_DP`
- **9** — `USB_DN`
- **11** — `GND`
- **13** — `VUSB`
- **15** — `NC15`
- **17** — `NC17`
- **19** — `NC19`
- **21** — `NC21`
- **23** — `NC23`
- **33** — `GND`
- **35** — `NC35`
- **37** — `NC37`
- **39** — `GND`
- **41** — `ALT_DFU_RX`
- **43** — `ALT_DFU_TX`
- **45** — `GND`
- **47** — `RTX`
- **49** — `CTX`
- **51** — `GND`
- **53** — `NC53`
- **55** — `NC55`
- **57** — `GND`
- **59** — `NC59`
- **61** — `NC61`
- **63** — `NC63`
- **65** — `BOOT`
- **67** — `RST`
- **69** — `NC69`
- **71** — `GND`
- **73** — `GND`
- **75** — `XP_MODEM_VSEL`

## Connector P5 — USB C Connector

- Part: `12402012E212A`

### P5 Left/A-Side Pins

- **A4** — `VBUS`
- **A9** — `VBUS`
- **A5** — `CC1`
- **A6** — `D+`
- **A7** — `D-`
- **A8** — `SBU1`
- **A1** — `GND`
- **A12** — `GND`
- **M** — shield / mount connection

### P5 Right/B-Side Pins

- **B4** — `VBUS`
- **B9** — `VBUS`
- **B5** — `CC2`
- **B6** — `D+`
- **B7** — `D-`
- **B8** — `SBU2`
- **B1** — `GND`
- **B12** — `GND`

## Connector S9 — Starnote ODFU

- Part: `GRIP 5Px2 - MDT`

### S9 Pins

- **1** — `S_AUX_RX`
- **2** — `AUX_TX`
- **3** — `S_AUX_TX`
- **4** — `AUX_RX`
- **5** — `S_AUX_EN`
- **6** — `AUX1`
- **7** — `S_BOOT`
- **8** — `AUX3`
- **9** — `S_NRST`
- **10** — `AUX4`

## Named Nets / Signals

- `+VIO`
- `+VMODEM`
- `+VUSB_S`
- `GND`
- `USB_S_D_P`
- `USB_S_D_N`
- `USB_SHIELD_2`
- `S_AUX_EN`
- `S_AUX_RX`
- `S_AUX_TX`
- `TX`
- `RX`
- `S_BOOT`
- `S_NRST`
- `AUX_TX`
- `AUX_RX`
- `AUX1`
- `AUX3`
- `AUX4`

## Title Block

- Company/logo: **FAE Technology**
- Project: **Notecarrier-XI**
- Board: **Notecarrier-XI**
- Designer: **S. Vaghi / L. Brighenti**
- Project Code: **2025-0019**
- Internal Code: **-**
- Page name: **06_STARNOTE-CONNECTION.SchDoc**
- Approved: **-**
- Customer: **BLUES Inc**
- Code: **-**
- Date: **08/10/2025**
- Rev.: **4**
- Rev. changes: blank
- Sheet: **06 / 06**
- Note: `Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.`
