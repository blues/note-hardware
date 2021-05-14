# Blues Wireless Notecard Host System Design Guide

The Blues Wireless Notecard family of products may be embedded into a host product using a standard M.2 Key E connector. This guide describes host product requirements, design choices, and optional interfaces. Reference designs illustrating the concepts described below may be found at [https://github.com/blues/note-hardware](https://github.com/blues/note-hardware)

# Table of Contents

<!--ts-->
   * [Requirements](#requirements)
      * [M.2 Connector](#m2-connector)
      * [Power](#power)
         * [VMODEM](#vmodem)
         * [VIO](#vio)
         * [Ground](#ground)
         * [Protection](#protection)
      * [No Connection Pins](#no-connection-pins)
      * [Serial Notecard Request Interfaces](#serial-notecard-request-interfaces)
         * [UART Serial](#uart-serial)
         * [I2C Serial](#i2c-serial)
      * [Cellular Antenna(s)](#cellular-antennas)
   * [Optional Items](#optional-items)
      * [Enable Pin](#enable-pin)
      * [Attention Pin](#attention-pin)
      * [Auxiliary GPIOs](#auxiliary-gpios)
      * [Reset Pin](#reset-pin)
      * [GPS Antenna](#gps-antenna)
      * [USB Serial Notecard Request Interface](#usb-serial-notecard-request-interface)
      * [Auxiliary UART Serial Notecard Request Interface](#auxiliary-uart-serial-notecard-request-interface)
      * [External SIM](#external-sim)
<!--te-->

# Requirements

## M.2 Connector

The Notecard plugs into a standard M.2 Key E connector such as Amphenol MDT420E01001. Once inserted into this connector, it is secured along the opposite edge to a grounded standoff by a mounting screw. Blues reference designs use a Würth Elektronik 9774025151R paired with an M2.5x4 metric machine screw.

## Power

#### VMODEM

To power the Notecard radio, you must provide a voltage of 2.5VDC to 5.5VDC, capable of sustained 750mA draw and brief 2A bursts. This voltage must be applied to the VMODEM\_P pins of the M.2 connector (pins 70, 72, and 74).

The best way to test the robustness of your design is to use a GSM carrier (for maximum power draw) and put the Notecard into a mode in which it repeatedly connects to the cellular network.

#### VIO

To power the Notecard MCU and its peripherals, you must supply a voltage of 1.8V or 3.3V, capable of at least 150mA draw. This voltage must be applied to the VIO\_P pins of the M.2 connector (pins 2 and 4).

Blues reference designs provide for a 300mA draw from this supply so that there is a current allowance for peripherals.

#### Ground

The 12 M.2 connector pins labeled as GND must be connected to the ground of the host system (pins 3, 5, 6, 11, 18, 33, 39, 45, 51, 57, 71, and 73).

#### Protection

Consider whether your power scheme requires protection such as

- Fuses to protect the host and Notecard from over-current events
- Diodes to isolate power sources from each other, if your host system uses more than one

Note that Blues reference designs do not use protection diodes on some signals to avoid interference with customer low-power designs.

## No Connection Pins

The 27 M.2 connector pins whose names begin with NC must be left unconnected (pins 1, 15, 17, 19, 21, 23, 32, 34, 35, 36, 37, 38, 41, 43, 44, 47, 49, 53, 55, 59, 61, 63, 65, 66, 68, 69, and 75).

## Serial Notecard Request Interfaces

To transmit serial JSON commands to Notecard and receive the responses, you may choose either the UART serial interface or the I2C interface, but not both concurrently. Both interfaces are active even in the Notecard&#39;s lowest-power mode, and both have on-Notecard pull-ups. These pins may be left disconnected, however in no circumstance should these pins be allowed to be inadvertently pulled to ground by, for example, a powered-off host MCU.

Open-source libraries for communicating serially over either of these interfaces via Python, C, Arduino, or Go are available at [https://github.com/blues](https://github.com/blues) and described at [https://dev.blues.io/](https://dev.blues.io/)

#### UART Serial

The UART Serial interface communicates at 9600 baud 8-N-1. Host system transmissions are received by Notecard on RX\_P (pin 62). The host system receives responses transmitted by Notecard on TX\_P (pin 64).

You should provide appropriate termination resistance on these transmission lines. The Notecarrier reference designs use two 100Ω resistors for this purpose.

#### I2C Serial

The I2C Serial interface uses a Blues-designed serial-over-I2C protocol to implement the same JSON command/response API as the UART Serial interface. Open-source libraries implementing this protocol are available at the links above.

The I2C Serial interface uses the SCL\_P (pin 40) and SDA\_P (pin 42) signals.

You should provide appropriate termination resistance on these transmission lines. The Notecarrier reference designs use two 100Ω resistors for this purpose.

## Cellular Antenna(s)

Blues reference Notecarriers incorporate a PCB-mounted cellular antenna to be connected to the Notecard U.FL connector labeled MAIN. The host system must provide a similar antenna, either PCB-mounted or external.

Host systems using LTE Cat-1 Notecards (NOTE-WBNA in North America or NOTE-WBEX in EMEA) may optionally supply a second antenna for receive diversity, connected to the Notecard U.FL connector labeled DIV.

Both the MAIN and DIV antennas should be designed to work for the full range of LTE Cat-M1, Cat-NBIoT, GSM, and LTE Cat-1 frequencies. Although all frequencies are important, in the US it is particularly important to provide the best coverage on Bands 2, 4, and 12.

# Optional Items

## Enable Pin

Blues Notecarrier reference designs allow a host to pull the EN pin low to disable the regulator which powers Notecard. The large pullup resistor on this signal results in very little current draw when EN is pulled low. This type of indirect power control scheme avoids controlling the line voltage directly. Your design may vary.

## Attention Pin

The ATTN\_P signal (pin 54) is a Notecard output which can be configured to:

- Inform the host MCU of certain asynchronous events (such as incoming data availability, or Notecard motion) in an interrupt-driven manner rather than just polling.
- Place the host MCU into a power-off sleep state and wake it back up again.

See the developer documentation for more details.

If unused, this pin should be left unconnected.

## Auxiliary GPIOs

The AUX1-4 signals (pins 46, 48, 50, and 52) are Notecard input/outputs which operate at VIO\_P. They can be configured in software to operate in several optional modes such as GPS Tracking Mode, GPIO Mode, and Internet Button Mode. See the developer documentation for more details.

If unused, these pins should be left unconnected.

## Reset Pin

The NRST signal (pin 67) is an optional active-low Notecard input/output. This pin should never be pulled-up or pulled-down by the carrier. The host system can reset Notecard by momentarily pulling this signal to GND for at least 350ns. Whenever the Notecard might perform its own software-based reset, this line will also be affected. As such, it is important when designing a system that this signal is not &#39;ganged&#39; in parallel with other devices&#39; reset pins or circuits. If a reset signal is to be sent to multiple devices, this signal should be isolated with a transistor so that the Notecard doesn&#39;t inadvertently reset other equipment.

For developer convenience, our Notecarriers invert this active-low NRST signal into an active-high RESET signal, but this will neither be appropriate nor necessary for most designs.

If unused, this pin should be left unconnected.

## GPS Antenna

For applications using GPS, the host system must provide a GPS antenna connected to the Notecard coaxial U.FL connector labeled GPS.

We recommend the use of an active GPS antenna, which provides much better performance than a passive antenna by using a Low Noise Amplifier (LNA). Many active GPS antennas are designed to power their LNA via a DC bias voltage applied to their coaxial RF cable. In order to use such an active antenna with Notecard, connect VACT\_GPS\_OUT (pin 20) to VACT\_GPS\_IN (pin 22). This will provide a voltage between 3.3VDC and 4.0VDC to power your antenna&#39;s LNA, which will vary based upon Notecard SKU and power load. In this active mode, do not connect a passive GPS antenna to Notecard, which will present a DC short, damaging the antenna and possibly your host system.

## USB Serial Notecard Request Interface

The USB Serial connection is an optional interface which implements the same JSON serial command/response protocol as the other Notecard serial interfaces. It uses the USB\_DP (pin 7), USB\_DM (pin 9), and VUSB (pin 13) signals to implement a USB 2.0 Full Speed CDC device.

This interface is convenient for system development work as it is natively supported by Windows, Mac, and Linux systems. Verbose debugging modes useful to developers are available on this interface. Notecard will not be able to utilize its lowest-power modes while a host is connected to this interface.

If unused, these pins should be left unconnected.

## Auxiliary UART Serial Notecard Request Interface

The Auxiliary UART Serial connection is an optional interface which implements the same JSON serial command/response protocol as the other Notecard serial interfaces. Host system transmissions are received by Notecard on AUX\_RX\_P (pin 58). The host system receives responses transmitted by Notecard on AUX\_TX\_P (pin 60). This interface is only enabled when AUX\_EN\_P (pin 56) is pulled up to VIO. This interface communicates at 115200 baud 8-N-1.

Verbose debugging modes useful to developers are available on this interface. Notecard will not be able to utilize its lowest-power modes while this interface is enabled using AUX\_EN\_P.

You should provide appropriate termination resistance on these transmission lines. The Notecarrier reference designs use two 100Ω resistors for this purpose.

If unused, these pins should be left unconnected.

## External SIM

Cellular Notecards have an onboard SIM which provides data connectivity out-of-the-box. An external SIM will not be generally necessary for connection to the cellular network in the countries listed on the Notecard datasheet. However, for applications where coverage outside these countries is required, the Notecard can be used with an external developer-provided SIM:

- SIM\_VCC (pin 8), a Notecard output provided by the Notecard&#39;s modem
- SIM\_RST (pin 10), a Notecard output
- SIM\_IO (pin 12), a Notecard I/O
- SIM\_CLK (pin 14), a Notecard output
- SIM\_NPRESENT (pin 16), an active-low Notecard input which tells the Notecard firmware that an external SIM is present and should be used instead of the internal SIM. Some of the Notecarrier reference designs use a JAE Electronics SF72S006VBAR2500 Nano-SIM connector which contains a mechanical switch that pulls this signal to ground when a Nano-SIM card is inserted.

If unused, these pins should be left unconnected.
