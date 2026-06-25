---
product: Swan
version: v3.0
doc_type: schematic
source_file: Swan/v3.0/Carrier/Swan Carrier schematic v3.0.pdf
generated_by: tools/extract_for_rag/extract.py
---

# Swan — SCHEMATIC (v3.0)

_Source: `Swan/v3.0/Carrier/Swan Carrier schematic v3.0.pdf`_

## Page 1

## Components

- **CS1**: CS V5 2L 35um
- **FID1**: Fiducial
- **FID2**: Fiducial

## Connectors

- No connectors shown on this page.

## Named Nets / Signals

- **TX3** — referenced in revision notes
- **RX3** — referenced in revision notes
- **MOD 1 pin 53** — referenced in revision notes
- **MOD 1 pin 51** — referenced in revision notes
- **J1** — referenced in revision notes
- **J2** — referenced in revision notes

## Revision Table

- **Revision 1**
  - Date: 11/02/2020
  - Author: M. Gregis
  - Description: First Draft

- **Revision 3**
  - Date: 26/07/2021
  - Author: M. Cossali
  - Description:
    - Updated symbol from library
    - Changed J1 and J2 to NU
    - Changed net MOD 1 pin 53 and J2 pin 11 to TX3
    - Changed net MOD 1 pin 51 and J2 pin 13 to RX3

- **Revision 4**
  - Date: 13/09/2021
  - Author: G.Boschini
  - Description: Swap J1 pin 2 with pin4

- **Revision 5**
  - Date: 13/09/2021
  - Author: M. Gregis
  - Description:
    - Updated SWAN pinout

## Title Block

- Company: FAE Technology
- Address: via C. Battisti 136, 24025, Gazzaniga (Bg), Italy
- Mail: info@fae.technology
- Tel: +39 035738130
- Project: SWAN
- Board: SWAN-C
- Page name: 00 - REVISION
- Designer: M.Gregis
- Approved: G.Boschini
- Project Code: 2021-0248
- Customer: BLUES
- Internal Code: -
- Code: -
- Data: Thursday, April 21, 2022
- Rev.: 5
- Rev. changes: See Revision Page
- Sheet: 1 / 3
- Note: Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.

## Page 2

## Page

- Page name: **01 - BLOCK DIAGRAM**
- Project: **SWAN**
- Board: **SWAN-C**
- Sheet: **2 / 3**

## Components

- No component reference designators are visible on this page.

## Connectors / Headers

### SWAN CONNECTOR

- Central block labeled: **SWAN CONNECTOR**

### Left 16x2 Header

- Connector label: **16x2 HEADER**
- Pin / signal labels shown:
  - **3V3 OUT @ 2A**
  - **3V3 VIN**
  - **2x DAC OUT**
  - **6x ADC IN (max 3.3V)**
  - **7x GPIO**
  - **1x SPI**
  - **1x UART**
  - **1x UART + FLOW CTRL**
  - **1x I2C**
  - **RST SIGNAL**

### Right 16x2 Header

- Connector label: **16x2 HEADER**
- Pin / signal labels shown:
  - **4.2V BATTERY IN/OUT**
  - **(357mA CHARGE CURRENT)**
  - **5V VUSB**
  - **10x GPIO**
  - **2x UART + FLOW CTRL**
  - **2x I2C**
  - **1x QSPI**
  - **PWR ENABLE SIGNAL**

## Named Nets / Signals

- **3V3 OUT @ 2A**
- **3V3 VIN**
- **2x DAC OUT**
- **6x ADC IN (max 3.3V)**
- **7x GPIO**
- **1x SPI**
- **1x UART**
- **1x UART + FLOW CTRL**
- **1x I2C**
- **RST SIGNAL**
- **4.2V BATTERY IN/OUT**
- **357mA CHARGE CURRENT**
- **5V VUSB**
- **10x GPIO**
- **2x UART + FLOW CTRL**
- **2x I2C**
- **1x QSPI**
- **PWR ENABLE SIGNAL**

## Title Block

- Company: **FAE TECHNOLOGY**
- Address: **via C. Battisti 136, 24025, Gazzaniga (Bg), Italy**
- Mail: **info@fae.technology**
- Tel: **+39 035738130**
- Project: **SWAN**
- Board: **SWAN-C**
- Designer: **M.Gregis**
- Project Code: **2021-0248**
- Internal Code: **-**
- Page name: **01 - BLOCK DIAGRAM**
- Approved: **G.Boschini**
- Customer: **BLUES**
- Code: **-**
- Data: **Thursday, February 17, 2022**
- Rev.: **5**
- Rev. changes: **See Revision Page**
- Sheet: **2 / 3**
- Copyright note: **Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.**

## Page 3

# Components

- **MOD1** — **NU**; labeled **SWAN BOARD**
- **J1** — **NU**
- **J2** — **NU**

# J1 Pin Labels

- **1**: RST#
- **2**: +3V3_OUT
- **3**: BOOT
- **4**: +VIN
- **5**: D0
- **6**: A0
- **7**: D1
- **8**: A1
- **9**: D2
- **10**: A2
- **11**: D3
- **12**: A3
- **13**: D4
- **14**: A4
- **15**: GND
- **16**: A5
- **17**: SCK
- **18**: A6
- **19**: MOSI
- **20**: A7
- **21**: MISO
- **22**: D14
- **23**: CS
- **24**: D15
- **25**: RTS
- **26**: RX
- **27**: CTS
- **28**: TX
- **29**: RX0
- **30**: SCL3
- **31**: TX0
- **32**: SDA3

# J2 Pin Labels

- **1**: +VUSB
- **2**: GND
- **3**: +VBAT
- **4**: EN
- **5**: RX2
- **6**: TX2
- **7**: RTS2
- **8**: D13
- **9**: CTS2
- **10**: D12
- **11**: TX3
- **12**: D11
- **13**: RX3
- **14**: D10
- **15**: RTS3
- **16**: D9
- **17**: CTS3
- **18**: D8
- **19**: D6
- **20**: D7
- **21**: D5
- **22**: SCL
- **23**: SCL2
- **24**: SDA
- **25**: SDA2
- **26**: QIO3
- **27**: QEN
- **28**: QIO2
- **29**: QCS
- **30**: QIO1
- **31**: QCLK
- **32**: QIO0

# MOD1 Pin Labels

- **1**: RST#
- **2**: VIN
- **3**: 3V3_OUT
- **4**: GND
- **5**: CS
- **6**: A0
- **7**: D0
- **8**: A1
- **9**: D1
- **10**: A2
- **11**: D2
- **12**: A3
- **13**: D3
- **14**: A4
- **15**: D4
- **16**: A5
- **17**: A6
- **18**: SCK
- **19**: A7
- **20**: MOSI
- **21**: D14
- **22**: MISO
- **23**: D15
- **24**: RX
- **25**: RTS
- **26**: TX
- **27**: CTS
- **28**: B
- **29**: QEN
- **30**: TX0
- **31**: RX0
- **32**: SDA3
- **33**: SCL3
- **34**: QCS
- **35**: QCLK
- **36**: QIO3
- **37**: QIO2
- **38**: QIO1
- **39**: QIO0
- **40**: SDA2
- **41**: SDA
- **42**: SCL2
- **43**: SCL
- **44**: D7
- **45**: D5
- **46**: D8
- **47**: D6
- **48**: CTS3
- **49**: D9
- **50**: RTS3
- **51**: D10
- **52**: TX3
- **53**: D11
- **54**: RX3
- **55**: D12
- **56**: CTS2
- **57**: D13
- **58**: RTS2
- **59**: VUSB
- **60**: TX2
- **61**: EN
- **62**: RX2
- **63**: VBAT
- **64**: USB_DM
- **65**: USB_DP

# Named Nets / Signals

- +3V3_OUT
- +VBAT
- +VIN
- +VUSB
- 3V3_OUT
- A0
- A1
- A2
- A3
- A4
- A5
- A6
- A7
- B
- BOOT
- CS
- CTS
- CTS2
- CTS3
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
- D11
- D12
- D13
- D14
- D15
- EN
- GND
- MISO
- MOSI
- QCLK
- QCS
- QEN
- QIO0
- QIO1
- QIO2
- QIO3
- RST#
- RTS
- RTS2
- RTS3
- RX
- RX0
- RX2
- RX3
- SCK
- SCL
- SCL2
- SCL3
- SDA
- SDA2
- SDA3
- TX
- TX0
- TX2
- TX3
- USB_DM
- USB_DP
- VBAT
- VIN
- VUSB

# Title Block Notes

- **Company**: FAE Technology
- **Address**: via C. Battisti 136, 24025, Gazzaniga (Bg), Italy
- **Mail**: info@fae.technology
- **Tel**: +39 035738130
- **Project**: SWAN
- **Board**: SWAN-C
- **Page name**: 02 - CONNECTORS
- **Designer**: M.Gregis
- **Approved**: G.Boschini
- **Project Code**: 2021-0248
- **Customer**: BLUES
- **Internal Code**: -
- **Code**: -
- **Data**: Wednesday, March 02, 2022
- **Rev.**: 5
- **Rev. changes**: See Revision Page
- **Sheet**: 3 / 3
- **Copyright note**: Il presente progetto è tutelato dalla legge sul diritto d'autore, che vieta a terzi la riproduzione e l'utilizzo anche parziale senza il consenso di FAE Technology S.p.A.
