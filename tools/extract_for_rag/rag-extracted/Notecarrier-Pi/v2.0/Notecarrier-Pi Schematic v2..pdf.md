---
product: Notecarrier-Pi
version: v2.0
doc_type: schematic
source_file: Notecarrier-Pi/v2.0/Notecarrier-Pi Schematic v2..pdf
generated_by: tools/extract_for_rag/extract.py
---

# Notecarrier-Pi — SCHEMATIC (v2.0)

_Source: `Notecarrier-Pi/v2.0/Notecarrier-Pi Schematic v2..pdf`_

## Page 1

# Components

- **OBJ1**: 9774025151R
  - Connected to **GND**
- **CS1**: CS V5 4L 18um
- **FID1**: fiducial, value/part not shown
- **FID2**: fiducial, value/part not shown
- **FID3**: fiducial, value/part not shown
- **FID4**: fiducial, value/part not shown
- **ASS1**: KNOB M2.5x4 - INOX

# Connectors

- No connector pin labels are visible on this page.

# Named Nets / Signals

- **GND**
- Signals mentioned in revision notes:
  - **M2_ATTN_P**
  - **3.3V**
  - **VIO**
  - **3V3**
  - **AUX5**
  - **BOOT**
  - **I2C**

# Revision History

- **Revision 1**
  - Date: 12/05/2020
  - Author: Martin Cossali
  - Description: First draft

- **Revision 2**
  - Date: 09/07/2020
  - Author: Martin Cossali
  - Description:
    - Updated symbol from library.
    - Added J5 Grove connector.

- **Revision 3**
  - Date: 26/08/2020
  - Author: Martin Cossali
  - Description:
    - Updated symbol from library.
    - Added DSW3 switch to connect M2_ATTN_P with Raspberry Pi.
    - Changed connector J1 MPN to Adafruit 2223 connector, with square pin profile.

- **Revision 4**
  - Date: 22/09/2020
  - Author: Martin Cossali
  - Description:
    - Updated symbol from library.
    - Connected J5 to the same 3.3V I2C bus as Notecard and Raspberry Pi.
    - Removed C14, C15, Q2, R14, R15, R17, R23, R24 and U4.

- **Revision 5**
  - Date: 07/12/2022
  - Author: Matteo Gregis
  - Description:
    - Updated J5 to QWIIC connector
    - Added on-board 3V3 regulator.
    - Added diode-or between VIO and 3V3.
    - Renamed J3.38 to AUX5 and J3.65 to BOOT. added test point to those pins.

# Title Block Notes

- Project: **NOTEBOX**
- Board: **NOTECARRIER-M2-PI**
- Project Code: **2017-3047**
- Internal Code: **-**
- Page name: **00 - REVISION**
- Code: **-**
- Date: **Monday, December 12, 2022**
- Rev.: **4**
- Rev. changes: **See Revision Page**
- Sheet: **1 / 3**
- Company: **Blues Inc**
- Designed by: **FAE Technology**
  - via C. Battisti, 136
  - 24025 Gazzaniga (Bg), Italy
  - Mail: info@fae.technology
  - Phone: +39035738130
- Copyright: **Copyright (c) 2020 Blues Inc**

## Page 2

# Schematic Page Transcription

## Component Reference Designators

- No component reference designators are visible on this page.

## Functional Blocks / Parts

- Raspberry Pi HAT Connector
- M.2 Connector Key E
- DIP-SW
- Grove Connector
- Protection Net
- Nano SIM Connector
- uUSB

## Connectors and Pin / Signal Labels

### Raspberry Pi HAT Connector

- ATTN
- I2C/USART
- V+
- VIO_P

### M.2 Connector Key E

- ATTN
- I2C/USART
- Nano SIM Signals
- VIO_P
- VMODEM_P

### Grove Connector

- I2C
- VIO_P

### Nano SIM Connector

- Nano SIM Signals

### uUSB

- VUSB

## Named Nets / Signals

- ATTN
- I2C
- I2C/USART
- Nano SIM Signals
- V+
- VUSB
- VIO_P
- VMODEM_P

## Title Block Notes

- Company: Blues Inc
- Project: NOTEBOX
- Board: NOTECARRIER-M2-PI
- Project Code: 2017-3047
- Page name: 01 - BLOCK DIAGRAM
- Internal Code: -
- Code: -
- Date: Wednesday, December 07, 2022
- Rev.: 4
- Rev. changes: See Revision Page
- Sheet: 2 / 3
- Designed by: FAE Technology
  - via C. Battisti, 136
  - 24025 Gazzaniga (Bg), Italy
  - Mail: info@fae.technology
  - Phone: +39035738130
- Copyright: Copyright (c) 2020 Blues Inc

## Page 3

# Schematic Page Transcription

## Page / Title Block

- Project: **NOTEBOX**
- Board: **NOTECARRIER-M2-PI**
- Project Code: **2017-3047**
- Page name: **02 - CONNECTOR**
- Sheet: **3 / 3**
- Date: **Friday, December 23, 2022**
- Rev.: **4**
- Rev. changes: **See Revision Page**
- Internal Code: **-**
- Code: **-**
- Company: **Blues Inc**
- Designed by: **FAE Technology**
  - via C. Battisti, 136
  - 24025 Gazzaniga (Bg), Italy
  - Mail: info@fae.technology
  - Phone: +39035738130
- Copyright: **Copyright (c) 2020 Blues Inc**

## Section Headings / Notes

- **RASPBERRY CONNECTOR**
- **3V3 BUCK**
  - Note: **1A max**
- **DIODE-ORs**
- **QWIIC CONNECTOR**
- **NOTECARD CONNECTOR + SIM**
- Switch notes:
  - **Remove protective film**
  - **Set to ON as default**

## Components

### Raspberry Connector

- **J1**: 20566
- **C1**: 22u/25V-X5R
- **C2**: 22u/25V-X5R
- **TVS2**: SM2T3V3A
- **TVS3**: SM6T6V8A

### 3V3 Buck

- **U3**: AP62250WU-7
- **L4**: LQH32PN4R7NN0L
- **C13**: 100n/50V
- **C14**: 22u/25V-X5R
- **C15**: 100n/50V
- **C16**: 10u/50V-X5R
- **C17**: 47u/6V3/X5R
- **R19**: 0R
- **R20**: 0R
- **R22**: 75k
- **R23**: 0R
- **R25**: 10k
- **R26**: 24k
- **TP5**: Test point

### Diode-ORs

- **DS1**: STPS3H100U
- **DS2**: STPS3H100U
- **DS3**: FSV1045V
- **DS4**: FSV1045V
- **TVS1**: SM6T6V8A

### Qwiic Connector

- **J5**: BM04B-SRSS-TBT(LF)(SN)
- **J6**: BM04B-SRSS-TBT(LF)(SN)

### Notecard Connector + SIM

- **J2**: NanoSIM - SF72S006VBAR2500
- **J3**: MDT420E01001
- **J4**: 10118192-0002LF
- **F1**: SF-0603F150-2, F1.5A
- **F2**: 3.5A/32V
- **DSW1**: DIP-SW-CHS-01TB
- **DSW2**: DIP-SW-CHS-01TB
- **DSW3**: DIP-SW-CHS-01TB
- **R1**: 22R
- **R2**: 22R
- **R3**: 22R
- **R4**: 15k
- **R5**: 1M
- **R6**: 100R
- **R7**: 100R
- **R8**: 100R
- **R9**: 100R
- **R10**: 100R
- **R11**: 100R
- **R12**: 100R
- **R13**: 100R
- **C3**: 100n/16V
- **C4**: 33p/50V-COG
- **C5**: 33p/50V-COG
- **C6**: 33p/50V-COG
- **C7**: 100n/10V
- **C8**: 10n/1kV
- **TVS4**: ESDLC5V0M5-TP
- **TP6**: Test point
- **TP7**: Test point

## Connectors and Pin Labels

### J1 — Raspberry Connector, 20566

Visible connected / labeled pins:

- Pin 1: VIO#
- Pin 2: V+
- Pin 3: SDA
- Pin 4: V+
- Pin 5: SCL
- Pin 6: GND
- Pin 8: AUX_RX
- Pin 9: GND
- Pin 10: AUX_TX
- Pin 14: GND
- Pin 20: GND
- Pin 25: GND
- Pin 30: GND
- Pin 31: ATTN
- Pin 34: GND
- Pin 39: GND
- Pin 40: shown with no-connect mark

### U3 — AP62250WU-7 Pin Labels

- Pin 1: GND
- Pin 2: SW
- Pin 3: VIN
- Pin 4: FB
- Pin 5: EN
- Pin 6: BST

### J5 — Qwiic Connector, BM04B-SRSS-TBT(LF)(SN)

- Pin 1: VIO_P
- Pin 2: GND
- Pin 3: SDA
- Pin 4: SCL

### J6 — Qwiic Connector, BM04B-SRSS-TBT(LF)(SN)

- Pin 1: VIO_P
- Pin 2: GND
- Pin 3: SDA
- Pin 4: SCL

### J3 — Notecard Connector, MDT420E01001

Visible connector markings:

- **TOP**
- **BOTTOM**

Left/even-side visible pin labels:

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
- Pin 32: NC32
- Pin 34: NC34
- Pin 36: NC36
- Pin 38: AUX5
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

Right/odd-side visible pin labels:

- Pin 1: NC1
- Pin 3: GND
- Pin 5: GND
- Pin 7: USB_DP
- Pin 9: USB_DM
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
- Pin 41: NC41
- Pin 43: NC43
- Pin 45: GND
- Pin 47: NC47
- Pin 49: NC49
- Pin 51: GND
- Pin 53: NC53
- Pin 55: NC55
- Pin 57: GND
- Pin 59: NC59
- Pin 61: NC61
- Pin 63: NC63
- Pin 65: BOOT
- Pin 67: NRST
- Pin 69: NC69
- Pin 71: GND
- Pin 73: GND
- Pin 75: NC75

### J4 — USB Connector, 10118192-0002LF

- Pin 1: VCC
- Pin 2: D-
- Pin 3: D+
- Pin 4: ID
- Pin 5: GND
- Shield / extra pins:
  - E1
  - E2
  - E3
  - E4
  - E5
  - E6

### J2 — NanoSIM Connector, SF72S006VBAR2500

Visible pin labels:

- Pin 1: VCC
- Pin 2: RST
- Pin 3: CLK
- Pin 5: GND
- Pin 6: VPP
- Pin 7: IO
- Pin 10: CSW
- Pin 13: DSW
- Additional visible bottom pins connected to ground/shield area:
  - Pin 8
  - Pin 9
  - Pin 11
  - Pin 12
  - Pin 14
  - Pin 15
  - Pin 17
  - Pin 18
  - Pin 19

## Named Nets / Signals

- 3V3
- ATTN
- ATTN_P
- AUX1
- AUX2
- AUX3
- AUX4
- AUX5
- AUX_EN
- AUX_EN_P
- AUX_RX
- AUX_RX_P
- AUX_TX
- AUX_TX_P
- BOOT
- GND
- NC1
- NC15
- NC17
- NC19
- NC21
- NC23
- NC32
- NC34
- NC35
- NC36
- NC37
- NC41
- NC43
- NC44
- NC47
- NC49
- NC53
- NC55
- NC59
- NC61
- NC63
- NC66
- NC68
- NC69
- NC75
- NRST
- RX_P
- SCL
- SCL_P
- SDA
- SDA_P
- SIM_CLK
- SIM_IO
- SIM_NPRESENT
- SIM_RST
- SIM_VCC
- TP5
- TP6
- TP7
- TX_P
- USB_DM
- USB_DP
- USB_SHIELD
- V+
- VACT_GPS_IN
- VACT_GPS_OUT
- VIO
- VIO#
- VIO_P
- VMODEM
- VMODEM_P
- VUSB
