---
product: Notecarrier-F
version: v1.3
doc_type: schematic
source_file: Notecarrier-F/v1.3/KiCad_format/documentation/Notecarrier-F_SCH_RevA.pdf
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-F — SCHEMATIC (v1.3)

_Source: `Notecarrier-F/v1.3/KiCad_format/documentation/Notecarrier-F_SCH_RevA.pdf`_

## Page 1

# Schematic Page

## Title Block

- Company: Blues Inc
- Title: Notecarrier-F
- Drawn By: Heath Raftery
- File: Notecarrier-F.kicad_sch
- Copyright: Copyright (c) 2023 Blues Inc
- Rev: A
- Date: 2023-05-03
- Sheet: 1/5
- Logo / mark: EmpiricalEE
- Contact: contact@empirical.ee

## Hierarchical Sheets / Interfaces

### Power

- Sheet name: Power
- File: Notecarrier-F_Power.kicad_sch
- Pins:
  - V+
  - N_EN
  - D_P
  - D_N
  - N_AUX5
  - N_VIO
  - F_VUSB
  - F_BAT
  - EN_F_BAT

### Notecard

- Sheet name: Notecard
- File: Notecarrier-F_Notecard.kicad_sch
- Pins:
  - D_P
  - D_N
  - N_AUX5
  - N_NRST
  - N_RX
  - N_TX
  - N_SCL
  - N_SDA
  - N_ATTN
  - N_AUX_EN
  - N_AUX_RX
  - N_AUX_TX
  - N_AUX1
  - N_AUX2
  - N_AUX3
  - N_AUX4

### Feather

- Sheet name: Feather
- File: Notecarrier-F_Feather.kicad_sch
- Pins:
  - N_VIO
  - F_VUSB
  - F_BAT
  - EN_F_BAT
  - N_SCL
  - N_SDA
  - N_ATTN
  - N_AUX_RX
  - N_AUX_TX
  - N_AUX3
  - N_AUX4
  - F_3V3
  - F_NRST_SW
  - F_EN
  - F_SDA
  - F_SCL
  - F_D5
  - F_D6
  - F_D9
  - F_D10
  - F_D11
  - F_D12
  - F_D13
  - F_BO_SW
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

### IO

- Sheet name: IO
- File: Notecarrier-F_IO.kicad_sch
- Pins:
  - V+
  - N_EN
  - N_NRST
  - N_RX
  - N_TX
  - N_SCL
  - N_SDA
  - N_ATTN
  - N_AUX_EN
  - N_AUX_RX
  - N_AUX_TX
  - N_AUX1
  - N_AUX2
  - N_AUX3
  - N_AUX4
  - F_3V3
  - F_NRST_SW
  - F_EN
  - F_SDA
  - F_SCL
  - F_D5
  - F_D6
  - F_D9
  - F_D10
  - F_D11
  - F_D12
  - F_D13
  - F_BO_SW
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

## Named Nets / Signals

- V+
- N_EN
- D_P
- D_N
- N_AUX5
- N_VIO
- F_VUSB
- F_BAT
- EN_F_BAT
- N_NRST
- N_RX
- N_TX
- N_SCL
- N_SDA
- N_ATTN
- N_AUX_EN
- N_AUX_RX
- N_AUX_TX
- N_AUX1
- N_AUX2
- N_AUX3
- N_AUX4
- F_3V3
- F_NRST_SW
- F_EN
- F_SDA
- F_SCL
- F_D5
- F_D6
- F_D9
- F_D10
- F_D11
- F_D12
- F_D13
- F_BO_SW
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

## Visible Net Connections

- V+: Power to IO
- N_EN: Power to IO
- D_P: Power to Notecard
- D_N: Power to Notecard
- N_AUX5: Power to Notecard
- N_VIO: Power to Feather
- F_VUSB: Power to Feather
- F_BAT: Power to Feather
- EN_F_BAT: Power to Feather
- N_NRST: Notecard to IO
- N_RX: Notecard to IO
- N_TX: Notecard to IO
- N_SCL: Notecard to IO and Feather
- N_SDA: Notecard to IO and Feather
- N_ATTN: Notecard to IO and Feather
- N_AUX_EN: Notecard to IO
- N_AUX_RX: Notecard to IO and Feather
- N_AUX_TX: Notecard to IO and Feather
- N_AUX1: Notecard to IO
- N_AUX2: Notecard to IO
- N_AUX3: Notecard to IO and Feather
- N_AUX4: Notecard to IO and Feather
- F_3V3: Feather to IO
- F_NRST_SW: Feather to IO
- F_EN: Feather to IO
- F_SDA: Feather to IO
- F_SCL: Feather to IO
- F_D5: Feather to IO
- F_D6: Feather to IO
- F_D9: Feather to IO
- F_D10: Feather to IO
- F_D11: Feather to IO
- F_D12: Feather to IO
- F_D13: Feather to IO
- F_BO_SW: Feather to IO
- F_TX_SW: Feather to IO
- F_RX_SW: Feather to IO
- F_MISO: Feather to IO
- F_MOSI: Feather to IO
- F_SCK: Feather to IO
- F_A5: Feather to IO
- F_A4: Feather to IO
- F_A3: Feather to IO
- F_A2: Feather to IO
- F_A1: Feather to IO
- F_A0: Feather to IO
- F_AREF: Feather to IO

## Components / Mechanical / Graphical

- FID1: fiducial, value/part not shown
- FID2: fiducial, value/part not shown
- FID3: fiducial, value/part not shown
- FID4: fiducial, value/part not shown
- FID5: fiducial, value/part not shown
- FID6: fiducial, value/part not shown
- H1: mounting hole / mechanical, value/part not shown
- H2: mounting hole / mechanical, value/part not shown
- H3: mounting hole / mechanical, value/part not shown
- H4: mounting hole / mechanical, value/part not shown
- H5_1: mounting hole / mechanical, value/part not shown
- H5_2: mounting hole / mechanical, value/part not shown
- H5_3: mounting hole / mechanical, value/part not shown
- H5_4: mounting hole / mechanical, value/part not shown
- Logo: graphical logo, value/part not shown

## Notes

- Section label: Graphical and Mechanical
- No discrete connector reference designators are visible on this page; visible interface pins are hierarchical sheet pins.

## Page 2

# Schematic Page Transcription

## Sheet Sections

- Primary Battery
- Solar
- Notecard USB
- Main Power Bus
- 1V8 Power Supply
- Notecard VIO Power Supply
- Feather VBAT Power Supply

## Components

### Capacitors

- C1: 10 µF
- C2: 1 µF
- C3: 0.1 µF
- C4: 10000 pF
- C10: 0.1 µF
- C11: 10 µF
- C12: 47 µF
- C13: 4.7 µF
- C14: 10 µF
- C15: 10 µF
- C16: 10 µF
- C17: 10 µF
- C18: 0.1 µF
- C19: 0.1 µF
- C20: 10 µF
- C21: 0.1
- C22: 22 µF
- C23: 22 µF
- C24: 22 µF
- C25: 0.1 µF

### Diodes / TVS

- DS1: FSV1045V
- DS2: FSV1045V
- DS3: STPS3H100U
- DS4: FSV1045V
- DS5: FSV1045V
- DS6: STPS3H100U
- DS7: STPS3H100U
- TVS1: SM6T6V8A, 6871072

### Inductors

- L1: XFL4020-222MEC
- L2: 1.5 µH
- L3: 1285AS-H-2R2M=P2

### Resistors

- R1: 10k, shown crossed out
- R2: 10k
- R3: 470R
- R4: 10k
- R5: 1M
- R13: 1.1M
- R14: 180k
- R16: 10 MOhms
- R17: 82 kOhms

### ICs

- U1: TPS62748YFPT
  - Pin labels shown: VIN, GND, VOS, LOAD, SW, EN, VSEL, CTRL
- U2: BQ24210DQCT
  - Additional text: 296-28738-1-ND, BAT-CHG
  - Pin labels shown: VBUS, ISET, VSS, VTSB, TS, EXP, BAT, VDPM, CHG, EN, PG
- U3: TPS63020DSJR
  - Additional text: 296-36491-1-ND
  - Pin labels shown: VINA, GND, FB, VOUT, L2-1, L2-2, EXP, PG, PS/SYNC, EN, VIN, L1-1, L1-2
- U5: MAX17225ELT+
  - Pin labels shown: OUT, LX, GND, EN, IN, SEL

## Connectors

### J1 — Primary Battery

- Part: S2BPHSM4TBLFSN
- Pin 2: V+
- Pin 1: GND
- Notes near connector:
  - Primary Battery
  - 2.5V – 4.2V

### J2 — Solar Panel Connector

- Part: S2BP HSM4TBLFSN / S2BPHSM4TBLFSN
- Pin 2: VSOLAR
- Pin 1: GND
- Note near connector:
  - Solar panel connector

### J3 — Li-po Battery

- Part: S2BPHSM4TBLFSN
- Pin 2: VBAT
- Pin 1: GND
- Notes near connector:
  - Li-po battery
  - 3.3V – 4.2V

### J4 — Notecard USB

- Part: 10118193-0001LF
- Pin 1: VBUS
- Pin 2: D-
- Pin 3: D+
- Pin 4: ID, no-connect mark shown
- Pin 5: GND
- Pin 6: Shield

## Named Nets / Signals

- 1V8
- D_N
- D_P
- EN_F_BAT
- F_BAT
- F_VUSB
- GND
- N_AUX5
- N_EN
- N_VIO
- VBAT
- VMAIN
- VSOLAR
- VUSB
- V+

## Visible Schematic Notes

- Primary Battery:
  - Primary Battery
  - 2.5V – 4.2V
- Solar:
  - Solar panel connector
  - Riset = Kiset / Iiset
  - where Kiset is 395 typically.
  - With 470R --> 800mA
  - Li-po battery 3.3V – 4.2V
  - Li-po must be equal to or greater than 800mAh
- Feather VBAT Power Supply:
  - BUCK-BOOST
  - Isdmax=1uA

## Title Block

- Company: Blues Inc
- Title: Notecarrier-F
- Drawn By: Heath Raftery
- Contact: contact@empirical.ee
- File: Notecarrier-F_Power.kicad_sch
- Copyright: Copyright (c) 2023 Blues Inc
- Rev: A
- Date: 2023-05-03
- Sheet: 2/5

## Page 3

# Schematic Page Transcription

## Sheet Sections

- **Notecard Connector**
- **SIM Card**
- **Label Promotion**

## Components

- **OBJ1**
  - Part/value: `9774025151R`
  - Distributor/order code: `732-7078-1-ND`

- **F1**
  - Part/value: `SF-0603F150-2`
  - Rating: `F1.5A`

- **F2**
  - Rating/value: `3.5A/32V`

- **J5**
  - Part/value: `NanoSIM - SF72S006VBAR2500`
  - Distributor/order code: `670-2967-1-ND`

- **J6**
  - Part/value: `MDT420F01001`

- **RR1**
  - Part/value: `741X163101JP`

- **RR2**
  - Part/value: `741X163101JP`

- **R6**
  - Value: `15k`

- **R7**
  - Value: `22R`

- **R8**
  - Value: `22R`

- **R9**
  - Value: `22R`

- **R10**
  - Value: `10 kOhms`
  - Shown crossed/not fitted

- **C5**
  - Value: `0.1uF`

- **C6**
  - Value: `33pF`

- **C7**
  - Value: `33pF`

- **C8**
  - Value: `33pF`

- **C9**
  - Value: `0.1uF`

- **SW1**
  - Part/value: `CJS-1200TA`
  - Positions labeled: `PASSIVE`, `ACTIVE`

- **SW2**
  - Function label: `RESET`
  - Part/value: `PTS810SJK250SMTRLFS`

- **TVS2**
  - Part/value: `PESD5V0L5UV,125`

## Connectors

### J5 — NanoSIM - SF72S006VBAR2500

- **C1**: `VCC`
- **C2**: `RST`
- **C3**: `CLK`
- **C5**: `GND`
- **C6**: `VPP/SWP`
- **C7**: `I/O`
- **DSW**: `DSW`
- **CSW**: `CSW`
- **SH**: `SH`

### J6 — MDT420F01001

- Symbol labels: `BOTTOM`, `TOP`

#### Left / even pins

- **2**: `VIO_P`
- **4**: `VIO_P`
- **6**: `GND`
- **8**: `SIM_VCC`
- **10**: `SIM_RST`
- **12**: `SIM_IO`
- **14**: `SIM_CLK`
- **16**: `SIM_NPRESENT`
- **18**: `GND`
- **20**: `VACT_GPS_OUT`
- **22**: `VACT_GPS_IN`
- **32**: `NC32`
- **34**: `NC34`
- **36**: `NC36`
- **38**: `NC38`
- **40**: `SCL_P`
- **42**: `SDA_P`
- **44**: `NC44`
- **46**: `AUX1`
- **48**: `AUX2`
- **50**: `AUX3`
- **52**: `AUX4`
- **54**: `ATTN_P`
- **56**: `AUX_EN_P`
- **58**: `AUX_RX_P`
- **60**: `AUX_TX_P`
- **62**: `RX_P`
- **64**: `TX_P`
- **66**: `NC66`
- **68**: `NC68`
- **70**: `VMODEM_P`
- **72**: `VMODEM_P`
- **74**: `VMODEM_P`

#### Right / odd pins

- **1**: `NC1`
- **3**: `GND`
- **5**: `GND`
- **7**: `USB_DP`
- **9**: `USB_DM`
- **11**: `GND`
- **13**: `VUSB`
- **15**: `NC15`
- **17**: `NC17`
- **19**: `NC19`
- **21**: `NC21`
- **23**: `NC23`
- **33**: `GND`
- **35**: `NC35`
- **37**: `NC37`
- **39**: `GND`
- **41**: `NC41`
- **43**: `NC43`
- **45**: `GND`
- **47**: `NC47`
- **49**: `NC49`
- **51**: `GND`
- **53**: `NC53`
- **55**: `NC55`
- **57**: `GND`
- **59**: `NC59`
- **61**: `NC61`
- **63**: `NC63`
- **65**: `NC65`
- **67**: `NRST`
- **69**: `NC69`
- **71**: `GND`
- **73**: `GND`
- **75**: `NC75`

## Named Nets / Signals

- `ACTIVE`
- `ATTN_P`
- `AUX1`
- `AUX2`
- `AUX3`
- `AUX4`
- `AUX_EN_P`
- `AUX_RX_P`
- `AUX_TX_P`
- `D_N`
- `D_P`
- `GND`
- `N_ATTND`
- `N_AUX1`
- `N_AUX2`
- `N_AUX3`
- `N_AUX4`
- `N_AUX5`
- `N_AUX_END`
- `N_AUX_RXD`
- `N_AUX_TXD`
- `N_NRST`
- `N_RXD`
- `N_SCL`
- `N_SCLD`
- `N_SDA`
- `N_SDAD`
- `N_TXD`
- `N_VIO`
- `PASSIVE`
- `RESET`
- `RX_P`
- `SCL_P`
- `SDA_P`
- `SIM_CLK`
- `SIM_IO`
- `SIM_NPRESENT`
- `SIM_RST`
- `SIM_VCC`
- `TX_P`
- `USB_DM`
- `USB_DP`
- `VACT_GPS_IN`
- `VACT_GPS_OUT`
- `VIO_P`
- `VMAIN`
- `VMODEM_P`
- `VUSB`

## Label Promotion Note

- **Label Promotion**
  - One of the net labels on this sheet needs to be common with other sheets.
  - In the original Altium source files, this was achieved for some labels by adding Off-Sheet Connectors to the nets. But any others, inadvertently perhaps, rely on promoting all net labels to global using the “Net Identifier Scope” setting.
  - This renders the original Off Sheet Connectors redundant.
  - To avoid losing that distinction, and to take advantage of the informative and scope-maintainance benefits of the top-level sheet introduced in the port, we opt to leave net labels as local, and promote the scope of those that require it here.
  - See `Porting-Notes.md` for more details.

## Title Block

- Company: `Blues Inc`
- Title: `Notecarrier-F`
- Drawn By: `Heath Raftery`
- File: `Notecarrier-F_Notecard.kicad_sch`
- Copyright: `Copyright (c) 2023 Blues Inc`
- Revision: `A`
- Date: `2023-05-03`
- Sheet: `3/5`
- Logo/contact shown: `Empirical EE`, `contact@empirical.ee`

## Page 4

# Schematic Page Transcription

## Title Block

- **Title:** Notecarrier-F
- **Company:** Blues Inc
- **Drawn By:** Heath Raftery
- **File:** `Notecarrier-F_Feather.kicad_sch`
- **Copyright:** Copyright (c) 2023 Blues Inc
- **Rev:** A
- **Date:** 2023-05-03
- **Sheet:** 4/5
- **Logo / note:** Empirical EE, `contact@empirical.ee`

## Components

- **U4** — `TXS0102DCUR`
  - I2C level shifter
- **U6** — `DGQ2788AEN-T1-GE4`
  - Analog switch / mux for DFU enable routing
- **SW3** — `PTS810 SJM 250 SMTR LFS`
  - User switch
- **SW4** — `CJS-1200TA`
  - DFU enable switch
- **SW5** — `CJS-1200TA`
  - ATTN mode enable switch
- **J7** — `SM04B-SRSS-TB(LF)(SN)`
  - Qwiic connector
- **J8** — `SM04B-SRSS-TB(LF)(SN)`
  - Qwiic connector
- **R11** — `10k`
  - Pull-up from `F_SDA` to `F_3V3`
- **R12** — `10k`
  - Pull-up from `F_SCL` to `F_3V3`
- **TP1** — test point
  - On net `N_AUX3`
- **MODL1** — Feather Module connector, left-side header
- **MOD2** — Feather Module connector, left-side module pins
- **MODR1** — Feather Module connector, right-side header

## Connectors and Pin Labels

### J7 — Qwiic Connector, `SM04B-SRSS-TB(LF)(SN)`

- Pin 1: `F_SCL`
- Pin 2: `F_SDA`
- Pin 3: `F_3V3`
- Pin 4: `GND`

### J8 — Qwiic Connector, `SM04B-SRSS-TB(LF)(SN)`

- Pin 1: `F_SCL`
- Pin 2: `F_SDA`
- Pin 3: `F_3V3`
- Pin 4: `GND`

### Feather Module Connector — MODL1 / MOD2

- Pin 1: `RESET#` / `F_NRST`
- Pin 2: `3V` / `F_3V3`
- Pin 3: `(ARef)` / `F_AREF`
- Pin 4: `GND`
- Pin 5: `A0` / `F_A0`
- Pin 6: `A1` / `F_A1`
- Pin 7: `A2` / `F_A2`
- Pin 8: `A3` / `F_A3`
- Pin 9: `A4` / `F_A4`
- Pin 10: `A5` / `F_A5`
- Pin 11: `SCK` / `F_SCK`
- Pin 12: `MOSI` / `F_MOSI`
- Pin 13: `MISO` / `F_MISO`
- Pin 14: `D0(RX)` / `F_RX`
- Pin 15: `D1(TX)` / `F_TX`
- Pin 16: `B0` / `F_B0`

### Feather Module Connector — MODR1

- Pin 1: `VBAT` / `F_BAT`
- Pin 2: `EN` / `F_EN`
- Pin 3: `VUSB` / `F_VUSB`
- Pin 4: `D13` / `F_D13`
- Pin 5: `D12` / `F_D12`
- Pin 6: `D11` / `F_D11`
- Pin 7: `D10` / `F_D10`
- Pin 8: `D9` / `F_D9`
- Pin 9: `D6` / `F_D6`
- Pin 10: `D5` / `F_D5`
- Pin 11: `SCL` / `F_SCL`
- Pin 12: `SDA` / `F_SDA`

## IC Pin Connections

### U4 — `TXS0102DCUR`

- Pin 1, `B2`: `F_SCL`
- Pin 2, `GND`: `GND`
- Pin 3, `VCCA`: `N_VIO`
- Pin 4, `A2`: `N_SCLD`
- Pin 5, `A1`: `N_SDAD`
- Pin 6, `OE`: `EN_F_BAT`
- Pin 7, `VCCB`: `F_3V3`
- Pin 8, `B1`: `F_SDA`

### U6 — `DGQ2788AEN-T1-GE4`

- Pin 1, `NC2`: `F_B0_SW`
- Pin 2, `GND`: `GND`
- Pin 3, `NO3`: `N_AUX_RX`
- Pin 4, `COM3`: `F_TX`
- Pin 5, `NC3`: `F_TX_SW`
- Pin 6, `IN3-4`: `DFU_SW`
- Pin 7, `NO4`: `N_AUX_TX`
- Pin 8, `COM4`: `F_RX`
- Pin 9, `NC4`: `F_RX_SW`
- Pin 10, `V+`: `EN_F_BAT`
- Pin 11, `NO1`: `N_AUX4`
- Pin 12, `COM1`: `F_NRST`
- Pin 13, `NC1`: `F_NRST_SW`
- Pin 14, `IN1-2`: `DFU_SW`
- Pin 15, `NO2`: `N_AUX3`
- Pin 16, `COM2`: `F_B0`

## Switch Connections

### SW3 — User Switch, `PTS810 SJM 250 SMTR LFS`

- One side: `GND`
- Other side: `F_B0_SW`

### SW4 — DFU Enable Switch, `CJS-1200TA`

- Pin 1: `GND`
- Pin 2: `DFU_SW`
- Pin 3: `EN_F_BAT`

### SW5 — ATTN Mode Enable Switch, `CJS-1200TA`

- Pin 1: `N_ATTN`
- Pin 2: `EN_F_BAT`
- Pin 3: `N_VIO`

## Named Nets / Signals

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
- `F_VUSB`
- `GND`
- `N_ATTN`
- `N_AUX3`
- `N_AUX4`
- `N_AUX_RX`
- `N_AUX_TX`
- `N_SCLD`
- `N_SDAD`
- `N_VIO`
- `N_VIOD`

## Schematic Notes

### DFU Enable

- “FLICK SWITCH TOWARDS THE TEXT ‘ON’ TO ENABLE OUTBOARD DFU”
- Truth table:
  - `IN1-2`, `IN3-4`
  - Logic 0 = NC is TRUE/HIGH, DFU=N
  - Logic 1 = NO is TRUE/HIGH, DFU=Y
- Note near U6 outputs: “NOTECARD OR IO HEADER”

### Label Promotion

- “Several of the net labels on this sheet need to be common with other sheets. In the original Altium source files, this was achieved for some labels by adding Off-Sheet Connectors to the nets. But any others (inadvertently perhaps) rely on promoting all net labels to global using the ‘Net Identifier Scope’ setting. This renders the original Off Sheet Connectors redundant. To avoid losing that distinction, and to take advantage of the informative and scope-maintainance benefits of the top-level sheet introduced in the port, we opt to leave net labels as local, and promote the scope of those that require it here.”
- “See Porting-Notes.md for more details.”

### ATTN Mode Enable

- “Feather PWR flicked towards the text ON means ‘ATTN MODE’ IS OFF”
- Labels shown:
  - `ON`
  - `SWITCHED`

## Page 5

## Components

- **J9** — `SAM1085-24-ND`
- **J10** — `SAM1085-24-ND`

## Connectors

### J9 — SAM1085-24-ND

- Pin 1: `F_NRST_SW`
- Pin 2: `F_EN`
- Pin 3: `F_SDA`
- Pin 4: `F_SCL`
- Pin 5: `F_D5`
- Pin 6: `F_D6`
- Pin 7: `F_D9`
- Pin 8: `F_D10`
- Pin 9: `F_D11`
- Pin 10: `F_D12`
- Pin 11: `F_D13`
- Pin 12: `F_BO_SW`
- Pin 13: `F_TX_SW`
- Pin 14: `F_RX_SW`
- Pin 15: `F_MISO`
- Pin 16: `F_MOSI`
- Pin 17: `F_SCK`
- Pin 18: `F_A5`
- Pin 19: `F_A4`
- Pin 20: `F_A3`
- Pin 21: `F_A2`
- Pin 22: `F_A1`
- Pin 23: `F_A0`
- Pin 24: `F_AREF`

### J10 — SAM1085-24-ND

- Pin 1: `F_3V3`
- Pin 2: `VUSB`
- Pin 3: `VBAT`
- Pin 4: `VMAIN`
- Pin 5: `N_VIO`
- Pin 6: `VSOLAR`
- Pin 7: `V+`
- Pin 8: `GND`
- Pin 9: `N_EN`
- Pin 10: `N_NRST`
- Pin 11: `GND`
- Pin 12: `N_SCL`
- Pin 13: `N_SDA`
- Pin 14: `N_ATTN`
- Pin 15: `N_AUX_EN`
- Pin 16: `N_AUX_RX`
- Pin 17: `N_AUX_TX`
- Pin 18: `N_AUX1`
- Pin 19: `N_AUX2`
- Pin 20: `N_AUX3`
- Pin 21: `N_AUX4`
- Pin 22: `N_RX`
- Pin 23: `N_TX`
- Pin 24: `GND`

## Named Nets / Signals

- `F_NRST_SW`
- `F_EN`
- `F_SDA`
- `F_SCL`
- `F_D5`
- `F_D6`
- `F_D9`
- `F_D10`
- `F_D11`
- `F_D12`
- `F_D13`
- `F_BO_SW`
- `F_TX_SW`
- `F_RX_SW`
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
- `N_SCL`
- `N_SDA`
- `N_ATTN`
- `N_AUX_EN`
- `N_AUX_RX`
- `N_AUX_TX`
- `N_AUX1`
- `N_AUX2`
- `N_AUX3`
- `N_AUX4`
- `N_RX`
- `N_TX`

## Label Promotion

Promoted/local label pairs shown:

- `F_SDA` → `F_SDA`
- `F_SCL` → `F_SCL`
- `F_D5` → `F_D5`
- `F_D6` → `F_D6`
- `F_D9` → `F_D9`
- `F_D10` → `F_D10`
- `F_D11` → `F_D11`
- `F_D12` → `F_D12`
- `F_D13` → `F_D13`
- `F_BO_SW` → `F_BO_SW`
- `F_TX_SW` → `F_TX_SW`
- `F_RX_SW` → `F_RX_SW`
- `F_MISO` → `F_MISO`
- `F_MOSI` → `F_MOSI`
- `F_SCK` → `F_SCK`
- `F_A5` → `F_A5`
- `F_A4` → `F_A4`
- `F_A3` → `F_A3`
- `F_A2` → `F_A2`
- `F_A1` → `F_A1`
- `F_A0` → `F_A0`
- `F_AREF` → `F_AREF`
- `F_3V3`
- `V+`

## Notes

### Label Promotion note

> Several of the net labels on this sheet need to be common with other sheets.  
> In the original Altium source files, this was achieved for some labels by adding Off-Sheet Connectors to the nets. But any others (inadvertently perhaps) rely on promoting all net labels to global using "Net Identifier Scope" setting. This renders the original Off Sheet Connectors redundant. To avoid losing that distinction, and to take advantage of the informative and scope-maintainance benefits of the top-level sheet introduced in the port, we opt to leave net labels as local, and promote the scope of those that require it here.  
>
> See `Porting-Notes.md` for more details.

## Title Block

- Company: **Blues Inc**
- Title: **Notecarrier-F**
- Drawn By: **Heath Raftery**
- File: `Notecarrier-F_IO.kicad_sch`
- Copyright: **Copyright (c) 2023 Blues Inc**
- Rev: **A**
- Date: **2023-05-03**
- Sheet: **5/5**
- Logo/text: **EmpiricalEE**
- Contact: `contact@empirical.ee`
