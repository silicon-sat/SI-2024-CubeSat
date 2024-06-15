# About

This is documentation page for the Ai Thinker RA-01/02 LoRa RF module. 

# Resources 
 - [Ai Thinker LoRa Doc Page](https://docs.ai-thinker.com/en/lora/man)

# Overview

Anxinke LoRa series modules (Ra-01/Ra-02) are designed and developed by Anxinke Technology. The radio frequency chip of this series of modules SX1278 mainly uses LoRa™ remote modem for ultra-long-distance spread spectrum communication. It has strong anti-interference and can Minimize current consumption. With the help of SEMTECH's LoRa™ patented modulation technology, SX1278 has a high sensitivity of over -148dBm, a power output of +20dBm, a long transmission distance and high reliability. At the same time, compared with traditional modulation technology, LoRa™ modulation technology also has obvious advantages in anti-blocking and selection, which solves the problem of distance, anti-interference and power consumption that traditional design solutions cannot simultaneously take into account.

## Ra-01/Ra-02 module characteristics

- LoRa™ modem
- Support FSK, GFSK, MSK, GMSK, **LoRa™** and OOK modulation methods
- Support frequency band **410MHz~525MHz**
- The working voltage is **3.3V** (Range: 2.7-3.6V), the maximum output is +20dBm, and the maximum working current is 105mA
- It has low power consumption characteristics in the receiving state, the receiving current is 12.15mA, the standby current is 1.6mA
- High sensitivity: as low as **-140dBm**
- Small size double row stamp hole patch package
- The module adopts **SPI interface**, half-duplex communication, with CRC, up to **256-byte packet engine**.
- Data rates up to **300 kBps**.

## Pin Function Definition

![RA 02 Pin Diagram](images/RA-02-pin.png)

| **RA-01** | **RA-02** | **PIN NAME** | **DESCRIPTION** |
| 1 | - | ANT | Antenna    |
| 2 | 1,2 | GND | Ground    |
| 3 | 3 | 3.3V | 3.3V power supply  |
| 4 | 4 | RESET | Reset    |
| 5 | 5 | DIO0 | Dig-IO0 software config |
| 6 | 6 | DIO1 | Dig-IO1 software config |
| 7 | 7 | DIO2 | Dig-IO2 software config |
| 8 | 8 | DIO3 | Dig-IO3 software config |
| 9 | 9 | GND | Ground    |
| 10 | 10 | DIO4 | Dig-IO4 config |
| 11 | 11 | DIO5 | Dig-IO5 software config |
| 12 | 12 | SCK | SPI clock input  |
| 13 | 13 | MISO | SPI data output  |
| 14 | 14 | MOSI | SPI data input  |
| 15 | 15 | NSS | SPI chip select input |
| 16 | 16 | GND | Ground    |
|--------|--------|--------|--------|
