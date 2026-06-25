---
product: Cygnet
version: v1.2
doc_type: schematic
source_file: Cygnet/v1.2/Schematic Prints.pdf
generated_by: tools/extract_for_rag/extract.py
---

# Cygnet — SCHEMATIC (v1.2)

_Source: `Cygnet/v1.2/Schematic Prints.pdf`_

## Page 1

# Cygnet Revision Note

## Components

- No schematic components shown on this page.
- Component references mentioned in revision notes:
  - U4.8 — do not populate/mount (DNM) note added
  - J1 — part numbers and footprints changed
  - L1 — part numbers and footprints changed

## Connectors

- No connectors shown on this page.
- Connector reference mentioned in revision notes:
  - J1 — part numbers and footprints changed

## Named Nets / Signals

- VIN
- PU
- PD
- SWDIO
- SWCLK
- +VIO

## Revision History

| Revision | Date | Author | Description |
|---|---|---|---|
| 1 | 11/01/2023 | S.KRAVITZ | First Draft |
| 2 | 11/14/2023 | S.KRAVITZ | Second Draft |
| 3 | 1/3/2024 | S.KRAVITZ | Third Draft - removed VIN, combined ideal diodes, all components on top. Copied original project, now on Cygnet Feather v2 |
| 4 | 1/12/2024 | S.KRAVITZ | PCB layout complete and ready for review |
| 5 | 2/15/2024 | S.KRAVITZ | Post design review, many changes |
| 6 | 2/27/2024 | S.KRAVITZ | PCB layout complete and ready for review |
| 7 | 3/18/2024 | S.KRAVITZ | Add "do not populate/ mount (DNM)" note to U4.8 |
| 8 | 4/4/2024 | S.KRAVITZ | Change PU to PD and vv SWDIO/ SWCLK. Change PNs and footprints for J1, L1 |
| 9 | 4/15/2024 | S.KRAVITZ | PU to +VIO change SWDIO |
| 10 | 6/2/2024 - 7/11/2024 | S.KRAVITZ | Various changes after manufacturing review |

## Title Block

- Logo: blues
- Title: CYGNET REVISION NOTE
- Size: A
- Date: 8/29/2024
- File: `C:\Users\..\CYGNET REVISION v1.2.SchDoc`
- Number: blank
- Revision: blank
- Sheet: blank
- Drawn By: blank

## Page 2

# CYGNET CPU Schematic Page Transcription

## Title Block

- Title: **CYGNET CPU**
- Size: **A**
- Date: **8/29/2024**
- File: `C:\Users\..\CYGNET CPU v1.2.SchDoc`
- Number: not filled
- Revision: not filled
- Sheet: not filled
- Drawn By: not filled

## Page Notes / Section Labels

- Decoupling capacitors for: **VDD1, VDD2, VBAT, VDDUSB, VDDA**
- **DEBUG CONNECTOR**
- **USER LED (active high)**
- **BUTTONS**
- **QWIIC CONNECTOR**

## Components

### ICs

- **U1** — STM32L433

### Capacitors

- **C1** — 4.7uF/10V
- **C2** — 0.1uF/16V-X5R
- **C3** — 0.1uF/16V-X5R
- **C4** — 0.1uF/16V-X5R
- **C5** — 0.1uF/16V-X5R
- **C6** — 1uF/16V-X5R
- **C7** — 10nF/16V-X5R
- **C8** — 100nF/16V-X5R
- **C9** — 100nF/16V-X5R
- **C10** — 1uF/16V-X5R
- **C11** — 100nF/16V-X5R
- **C12** — 4pF
- **C13** — 4pF
- **C14** — 0.1uF/16V-X5R
- **C15** — 0.1uF/16V-X5R
- **C16** — 0.1uF/16V-X5R

### Resistors

- **R1** — 10k
- **R2** — 10k
- **R3** — 10M
- **R4** — 4.3M
- **R5** — 10k
- **R6** — 10k
- **R7** — 1k
- **R8** — 10k
- **R9** — 10k
- **R10** — 10k
- **R28** — 0

### LEDs

- **LD1** — YSML-P12U2TT86R

### Crystal / Resonator

- **Y1** — value not shown

### TVS / ESD Protection

- **TVS1** — ESD5Z3.3T1G
- **TVS2** — ESD5Z3.3T1G
- **TVS3** — ESD5Z3.3T1G

### Switches / Buttons

- **BOOT** — PB-SKRPADE010
- **RST** — PB-SKRPABE0102
- **USER4** — PB-SKRPADE010

### Connectors

- **J4** — BM04B-SRSS-TBT(LF)(SN)
- **J5** — FTSH-107-01-L-DV-K

## Connector Pin Labels

### J4 — Qwiic Connector, BM04B-SRSS-TBT(LF)(SN)

- Pin 1 — GND
- Pin 2 — +3V3_OUT
- Pin 3 — SDA
- Pin 4 — SCL
- Pin 5 / MNT1 — GND
- Pin 6 / MNT2 — GND

### J5 — Debug Connector, FTSH-107-01-L-DV-K

- Pin 1 — +VIO
- Pin 2 — unlabeled / no net shown
- Pin 3 — unlabeled / no net shown
- Pin 4 — SWDIO
- Pin 5 — GND
- Pin 6 — SWCLK
- Pin 7 — GND
- Pin 8 — unlabeled / no net shown
- Pin 9 — unlabeled / no net shown
- Pin 10 — unlabeled / no net shown
- Pin 11 — GND
- Pin 12 — NRST
- Pin 13 — LPUART1_RX
- Pin 14 — LPUART1_TX

## U1 Pin / Signal Labels

- Pin 1 — VBAT — +VIO
- Pin 2 — PC13 — USER_BTN
- Pin 3 — PC14-OSC32 IN — crystal/cap network
- Pin 4 — PC15-OSC32 OUT — crystal/cap network
- Pin 5 — PH0-OSC IN — ENABLE_3V3
- Pin 6 — PH1-OSC OUT — DISCHARGE_3V3
- Pin 7 — RST — NRST
- Pin 8 — VSSA/VREF- — GND
- Pin 9 — VDDA/VREF+ — AREF
- Pin 10 — PA0 — A0
- Pin 11 — PA1 — A1
- Pin 12 — PA2 — A2
- Pin 13 — PA3 — A3
- Pin 14 — PA4 — STAT
- Pin 15 — PA5 — SCK
- Pin 16 — PA6 — MISO
- Pin 17 — PA7 — A5
- Pin 18 — PB0 — D11
- Pin 19 — PB1 — A4
- Pin 20 — PB2 — no net shown
- Pin 21 — PB10 — LPUART1_RX
- Pin 22 — PB11 — LPUART1_TX
- Pin 23 — VSS — GND
- Pin 24 — VDD — +VIO
- Pin 25 — PB12 — no net shown
- Pin 26 — PB13 — D10
- Pin 27 — PB14 — D9
- Pin 28 — PB15 — D12
- Pin 29 — PA8 — LED_BUILTIN
- Pin 30 — PA9 — TX
- Pin 31 — PA10 — RX
- Pin 32 — PA11 — USB_DM
- Pin 33 — PA12 — USB_DP
- Pin 34 — PA13 — SWDIO
- Pin 35 — VSS — GND
- Pin 36 — VDDUSB — +3V3_USB
- Pin 37 — PA14 — SWCLK
- Pin 38 — PA15 — NCHG_DETECT
- Pin 39 — PB3 — +3V3_USB
- Pin 40 — PB4 — D13
- Pin 41 — PB5 — MOSI
- Pin 42 — PB6 — SCL
- Pin 43 — PB7 — SDA
- Pin 44 — PH3-BOOT0 — BOOT0
- Pin 45 — PB8 — D5
- Pin 46 — PB9 — D6
- Pin 47 — VSS — GND
- Pin 48 — VDD — +VIO

## Named Nets / Signals

- +3V3_OUT
- +3V3_USB
- +VIO
- +VMAIN
- A0
- A1
- A2
- A3
- A4
- A5
- AREF
- BOOT0
- D5
- D6
- D9
- D10
- D11
- D12
- D13
- DISCHARGE_3V3
- ENABLE_3V3
- GND
- LED_BUILTIN
- LPUART1_RX
- LPUART1_TX
- MISO
- MOSI
- NCHG_DETECT
- NRST
- RX
- SCK
- SCL
- SDA
- STAT
- SWCLK
- SWDIO
- TX
- USB_DM
- USB_DP
- USER_BTN

## Page 3

# Schematic Page: CYGNET POWER

## Sheet Sections

- MAIN SUPPLY
- 3V3_OUT SUPPLY
- BATTERY CHARGER
- USB LDO

## Named Nets / Signals

- `+VUSB`
- `+VBAT+VUSB`
- `+VMAIN`
- `+VIO`
- `+3V3_OUT`
- `+3V3_USB`
- `DISCHARGE_3V3`
- `ENABLE_3V3`
- `NCHG_DETECT`
- `EN`
- `GND`

## Components

### MAIN SUPPLY

- `C24` — `1uF/16V-X5R`
- `C25` — `1uF/16V-X5R`
- `R14` — `0R`
- `U4` — `LM66200DRLR`
  - Pins shown:
    - `8` ST
    - `6` VIN2
    - `3` VIN1
    - `4` ON
    - `2` VOUT
    - `7` VOUT
    - `1` GND
    - `5` GND
- `TVS4` — `SM6T6V8A`
- `C22` — `10uF/10V-X5R`
- `L1` — `1uH`
- `U3` — `ISL9122AIINZ-T`
  - Function label: `BUCK-BST`
  - Pins shown:
    - `A2` LX2
    - `A1` GND
    - `C1` VIN
    - `D1` SCL
    - `B1` LX1
    - `B2` VOUT
    - `C2` EN
    - `D2` SDA
- `C23` — `22u/10V-X5R`
- `R3` — `100k`

### 3V3_OUT SUPPLY

- `U2` — `TPS63020DSJT`
  - Note: `Isdmax=1uA`
  - Pins shown:
    - `1` VINA
    - `2` GND
    - `3` FB
    - `4` VOUT_1
    - `5` VOUT_2
    - `6` L2_1
    - `7` L2_2
    - `8` L1_1
    - `9` L1_2
    - `10` VIN_1
    - `11` VIN_2
    - `12` EN
    - `13` PS/SYNC
    - `14` PG
    - `15` EP
- `R11` — `1k`
- `R12` — `1M`
- `R16` — `180k`
- `C19` — `100uF/6.3V`
- `C20` — `100uF/6.3V`
- `C21` — `10uF/16V-X5R`
- `L2` — `1.5uH`
- `C17` — `10uF/10V-X5R`
- `C18` — `10uF/10V-X5R`
- `R15` — `1M`

### BATTERY CHARGER

- `J6` — LIPO battery connector
  - Note: `LIPO BATTERY 3.3V - 4.2V`
- `C26` — `4.7uF/10V-X5R`
- `C27` — `4.7uF/10V-X5R`
- `LD2` — `SML-P12WTT86R`
- `U5` — `MCP73831-2ACI/MC`
  - Pins shown:
    - `1` VDD
    - `2` VDD
    - `3` VBAT
    - `4` VBAT
    - `5` EP
    - `6` STAT
    - `7` VSS
    - `8` PROG
    - `9` EP
- `R17` — `1k`
- `R18` — `2.8k`

### USB LDO

- `U6` — `AP2139AK-3.3TRG1`
  - Notes:
    - `Iqmax=1.5uA`
    - `Isdmax=1uA`
    - `VEN-IH=1.2V`
    - `VEN-IL=0.3V`
    - `IPD-EN=0.2uA`
  - Pins shown:
    - `1` VIN
    - `2` GND
    - `3` CE
    - `4` NC
    - `5` VOUT
- `R19` — `8.2M`
- `C30` — `10uF/16V-X5R`
- `C29` — `1uF/16V-X5R`
- `C28` — `10uF/16V-X5R`
- `C31` — `1uF/16V-X5R`

## Connectors

- `J6` — LIPO battery connector
  - `Pin 1` — `+VBAT+VUSB`
  - `Pin 2` — `GND`
  - `MP1` — mounting pad shown
  - `MP2` — mounting pad shown

## Title Block

- Title: `CYGNET POWER`
- Size: `A`
- Date: `8/29/2024`
- File: `C:\Users\..\CYGNET POWER v1.2.SchDoc`
- Number: blank
- Revision: blank
- Sheet: blank
- Drawn By: blank

## Page 4

# CYGNET FEATHER CONNECTOR

## Components

- **C32**: 0.01 uF
- **C33**: 0.1 uF
- **R20**: 5.1 k
- **R21**: 5.1 k
- **R22**: 1 M

## Connectors

### J1 — USB-C Connector

- Part/value shown: **12402012E212A**
- Pins / labels:
  - **A5**: CC1_A
  - **A6**: D+_A, net **USB_DP**
  - **A7**: D-_A, net **USB_DM**
  - **A8**: SBU1
  - **A4 / B9**: VBUS, net **+VUSB**
  - **B4 / A9**: VBUS, net **+VUSB**
  - **B5**: CC1_B, net **USB_CC2**
  - **B6**: D+_B, net **USB_DP**
  - **B7**: D-_B, net **USB_DM**
  - **B8**: SBU2
  - **A1 / B12**: GND
  - **B1 / A12**: GND
  - **SH1**: SHIELD, net **SHELL_GND**
  - **SH2**: SHIELD, net **SHELL_GND**
  - **SH3**: SHIELD, net **SHELL_GND**
  - **SH4**: SHIELD, net **SHELL_GND**

### CST16

- 16-pin connector
- Pins / labels:
  - **1**: NRST
  - **2**: +3V3_OUT
  - **3**: AREF
  - **4**: GND
  - **5**: A0
  - **6**: A1
  - **7**: A2
  - **8**: A3
  - **9**: A4
  - **10**: A5
  - **11**: SCK
  - **12**: MOSI
  - **13**: MISO
  - **14**: RX
  - **15**: TX
  - **16**: BOOT0

### CST12

- 12-pin connector
- Pins / labels:
  - **1**: +VBAT
  - **2**: EN
  - **3**: +VUSB
  - **4**: D13
  - **5**: D12
  - **6**: D11
  - **7**: D10
  - **8**: D9
  - **9**: D6
  - **10**: D5
  - **11**: SCL
  - **12**: SDA

## Named Nets / Signals

- **+3V3_OUT**
- **+VBAT**
- **+VUSB**
- **A0**
- **A1**
- **A2**
- **A3**
- **A4**
- **A5**
- **AREF**
- **BOOT0**
- **D5**
- **D6**
- **D9**
- **D10**
- **D11**
- **D12**
- **D13**
- **EN**
- **GND**
- **MISO**
- **MOSI**
- **NRST**
- **RX**
- **SCK**
- **SCL**
- **SDA**
- **SHELL_GND**
- **TX**
- **USB_CC2**
- **USB_DM**
- **USB_DP**

## Title Block

- **Title**: CYGNET FEATHER CONNECTOR
- **Size**: A
- **Date**: 8/29/2024
- **Number**: blank
- **Revision**: blank
