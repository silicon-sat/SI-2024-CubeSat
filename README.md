🛰️ This is the portal for Summer Internship 2024 on Introduction to CubeSat and Satellite Communication. 📡


# Resources

- **LECTURE SLIDES**
  - [June 25: CubeSat101](docs/lectures/2024-0625-CubeSat101.pdf): Basic concepts and processes.
  - [June 26: CubeSat Communication I](docs/lectures/2024-0626-CubeSat-Communication.pdf): LoRa-based CubSat Commuication HW architecture.
  - [June 27: CubeSat Communication II](docs/lectures/2024-0627-CubeSat-Communication-2.pdf): Digital Communication, EM Spectrum, EM Field, LoRa Radio Architecture.
  - [July 01: CMOS VLSI Design](docs/lectures/2024-0701-Intro-VLSI-Design.pdf): An introduction.
  - [July 02: LoRa Basics](docs/lectures/2024-0702-LoRa-Basics.pdf): Spread-Spectrum Modem, LoRa Basics (Spreading factor, BW, SNR, Bit Rate).
  - [July 03: Antenna Basics](docs/lectures/2024-0703-Antenna.pdf): Radiation mechanism, equivalent circuit, Radiation pattern, polarization, types of antenna, antenna tuning. 
  - [July 10: RaspberryPi for Space](docs/lectures/2024-0710-RasPi-RadHard.pdf): Considerations for building elecrotnic systems for space eg. Radiation hardening. 


- **DATASHEETS/APP NOTES**
  - [Datasheet SX127X](docs/Datasheet-SX1276-7-8-9_W_APP_V7.pdf)
  - [Application Note AN1200-22: LoRa Basics](docs/AN1200_22_Semtech_LoRa_Basics_v2_STD.pdf): This application note covers the basics of LoRa Modulation including spread-spectrum communication and LoRa spread spectrum. 
  - [Ai Thinker's LoRa Radio Module RA-02](AiThinkerRA02.md) is RF radio module based on the Semtech's SX127X transceiver chip. This module will be used for all the satellite communication Lab exercises as well as the [tinyGS](https://tinygs.com) ground station. This page provides the basic information about the module.
    - [Datasheet RA-02: LoRa modeule](docs/datasheet-LoRaModule-RA02-v1_1.pdf): Ai Thinker's LoRa Radio Module RA-02
    - [Datasheet ESP32 SoC](docs/Datasheet-ESP32.pdf)
    - [Datasheet ESP32 WROOM32E Module](docs/Datasheet-ESP32-WROOM32E.pdf)
    - [Engineering Reference Manual ESP32](docs/esp32_technical_reference_manual_en.pdf)
  - LoRa Library for ESP32 firmware development:
    - [LoRa Library GitHub](https://github.com/sandeepmistry/arduino-LoRa)
    - [LoRa Arduino Library Reference](https://www.arduino.cc/reference/en/libraries/lora)

- **LITERATURE**
  - Rappaport, "*Wireless Communication Principles*", PHI, 2002 ([Link](https://www.github.com/scl/fi/22fosc0i4s3rnj66rd5xm/Rappaport-WirelessCommunicationsPrinciples-Prentice-Hall-PTR-2002.pdf?rlkey=33d77z1wx5twk8jr50xmafttp&dl=0) : Chap5: Modulation techniques for Mobile Radio 5.4 Digital Modulation technique (p-220) 5.10 SPread spectrum Modulation Technique 
  - Xiong, "*Digital Modulation Techniques*", Artech, 2006 ([Link](https://www.github.com/scl/fi/5lhdmeyicf5vny3vprobe/Xiong-DigitalModulationTechniques-2e-Artech-2006.pdf?rlkey=e5tjkqvkcur387ouheymkfq8c&dl=0))

  - Siwiak, Bahreini, "*Radiowave Propagation and Antennas*", Artech, 2007 ([Link](https://www.github.com/scl/fi/stcjy2n63mio0aqya6neo/Siwiak-Bahreini-RadiowavePropagation-Artech-2007.pdf?rlkey=5xg6rb5dffnr539q9qga2x6hs&dl=0) ( - Chap4: Radio Frequency Spectrum - p 99, - Chap5: Comm using Earth-Orbiting Satellites.)
  - Balanis, C, "Antenna Thoery" Wiley, 2005 ([Link](https://www.github.com/scl/fi/6a3rakx1g605hhrpsnbjx/Balanis-AntennaTheory-4thEd-2016.pdf?rlkey=d0khyp7zjqsrzitr59etz74r2&dl=0))
  - NASA CubeSat Launch Initiative (NCSLI), _CubeSat 101: Basic Concepts and Processes for First-Time CubeSat Developers_, Oct 2017 ([PDF](docs/NASA_CSLI_CubeSAT_101_508.pdf))
## Lab 5: Introduction Signal Processing using Python

- You can use [lab1-fft.py](Labs/python/lab1-fft.py) and [lab2-fsk.py](Labs/python/lab2-fsk.py) as reference for the following exercises:
- Write a python program to create a _cosine wave_ of frequency `2MHz` with `256` samples per cycle.
- Plot it with proper annonation and axis labeling. 
- Compute the `FFT` of the above signal and plot it.
  - You will notice the FFT resolution is very limited for a single cycle.
- Create another a signal of frequency `3MHz`, add it to above signal and do `FFT` for the resultant signal.
- Simulate [lab2-fsk.py](Labs/python/lab2-fsk.py) and anlayze the plot to understand FSK modulation.
  - Change the code such that the modulation frequency for `1` is `4MHz` and for `0` it is `3MHz`.
- Change the above code to simulate ASK modulation.
- Add demodulation to the above code and plot the time-domain waveform, as well as the FFT of the demodulated signal.
- Add a moving average filter to remove the high-frequency component from the demodulated signal.

## Lab 4: I2C-based OLED Display control.

In this Lab students learnt to use a I2C-based OLED display to display data on it.


## Lab 3: Dimming LED using PWM

In this exercise we are going to use the ESP32 to control the light intensity of an external LED using PWM signal.

- From the [LED Datasheet](docs/Datasheet-LED-XLMR01DE.pdf) tabulate the following data:
  - Maximum Forward current (If)
  - Typical Forward Voltage (Vf)
  - Dominant Wavelength (lambdaD)
  - Estimate the color (RGB) from the above wavelength
  - Typical Cacpacitance (pF)
  - Operating temperature range
- From the [ESP32 Datasheet](docs/Datasheet-ESP32.pdf) find and tabulate:
  - the maximum output voltage of the GPIO pins, and
  - the maximum current that the GPIO can source from supply to the load.
- Calculate the value of the resistance to pass _half of the Maximum_ forward current (If) when ON.
  - Make sure this current can be sourced by the output port.
- Find the closest *E12* standardized resistors value available in the market to use for the above limiter.
  - See this [guide](https://eepower.com/resistor-guide/resistor-standards-and-codes/resistor-values/#) on resistor standardization.
- Calculate the maximum frequency you can switch the LED such that, the RC time-constant of the LED-cap-resitor is at least 1/25 of the switching period.
- Find out what is the minimum frequency you can switch the LED.
- Decide on a frequency which is safely in between the minimum and maximum.
- Write a program for ESP32:
  - Assign an output port for the LED
  - Assign an input port for 2-step dimmer control.
    - 1: Full intensity, 0: 25-percent intensity.
  - Write a program to control the LED intensity using Pulse-Width Modulation (PWM).
    
## Lab 2: Intro to GPIO programming.

In this Lab exercise, students learn to configure a GPIO as an output and control an LED with it.

## Lab 1: Intro to ESP32 Programming 

- Install and configure Arduino IDE
- Introduction to ESP32 development kit.
- Write and execute a C-code to blink an LED on the dev board.


# Lab Info

## Requirements

- Download and install the latest version (**2.3.2+**) [Arduino IDE](https://www.arduino.cc/en/software). Majority of the Lab activity will be writing `C Programming Language` for the ESP 32 platform which we will develop using the Arduino IDE.
  - [Installing the ESP32 boards](https://randomnerdtutorials.com/installing-esp32-arduino-ide-2-0/)
- Download and install [4NEC2](https://www.qsl.net/4nec2/), antenna modeling and simulation softwware. The antenna design and simulation will be done using this sofware.
- Install [Windows Subsystem for Linux (WSL)](https://github.com/silicon-vlsi-org/eda-wsl2) with **Ubuntu 22.04 Linux Distro** (**OMIT** instruction related to EDA tools). During the tenure of the course, we will learn many fundamental signal processing concepts that is best practiced using the Python programming/scripting language. We will WSL for that purpose. Python language is not a prereq, the basic programming structures will be provided to you.
  - After updating your linux distro, install the following packages:
  - `sudo apt install pip -y`
  - `pip install numpy scipy matplotlib`
- Create a [GitHub](https://github.com) account if you don't have one already. We will use it for multiple purpose: for submission Lab assignment, documenting your Labs and final projec and keeping a revision control repository of all your work during the course work.

## Lab Resources

- [Ai Thinker's LoRa Radio Module RA-02](AiThinkerRA02.md) is RF radio module based on the Semtech's SX127X transceiver chip. This module will be used for all the satellite communication Lab exercises as well as the [tinyGS](https://tinygs.com) ground station. This page provides the basic information about the module.
  - [Datasheet RA-02](docs/datasheet-LoRaModule-RA02-v1_1.pdf): Ai Thinker's LoRa Radio Module RA-02
  - [Datasheet ESP32 SoC](docs/Datasheet-ESP32.pdf)
  - [Datasheet ESP32 WROOM32E Module](docs/Datasheet-ESP32-WROOM32E.pdf)
  - [Engineering Reference Manual ESP32](docs/esp32_technical_reference_manual_en.pdf)
- The [SX1276/77/78/79](https://www.semtech.com/products/wireless-rf/lora-connect/sx1276) transceiver chipset features the LoRa® long range modem that provides ultra-long range spread spectrum communication
  - [Datasheet SX127X](docs/Datasheet-SX1276-7-8-9_W_APP_V7.pdf)
  - [Application Note AN1200-22](docs/AN1200_22_Semtech_LoRa_Basics_v2_STD.pdf): This application note covers the basics of LoRa Modulation including spread-spectrum communication and LoRa spread spectrum. 
  - [Application Note AN1200-13](docs/AN1200_13_SX17x_Modem_DesignerGuide.pdf): This is an application note for LoRa modem design covering basic priciples of LoRa Design (Modulation, RX Senisitivty, SNR, SF, BW, etc.) to advancd LoRa design (FEC, HW, etc) and how to use the LoRa calculator to optimize Radio design.
- LoRa Library for ESP32 firmware development:
  - [LoRa Library GitHub](https://github.com/sandeepmistry/arduino-LoRa)
  - [LoRa Arduino Library Reference](https://www.arduino.cc/reference/en/libraries/lora)

# Course Venue & Timings

- 📆 **DURATION**: June 25th till July 12th (3 weeks)
- ⏲️ **TIMINGS**:
  - Theory Sessions 🕙 **10:00am - 1:00pm**
  - Hands-on practical Sessions 🕝 **2:30pm - 5:30pm**
- 🏛️ **VENUE**(Old Building):
  - Theory & Practical Sessions: **Room 04-10** (Advanced VLSI Training Lab)
    - **NOTE** The venue for **June 25th ONLY** is **Training Hall-2, 2nd Floor, New Building**.
- 👨‍🏫 **RESOURCE PERSONS**:
  - [Dr. Saroj Rout](https://sroutk.github.io) and [Prof. Prasant Swain](https://silicon.ac.in/wp-content/uploads/2022/04/Prasant-Kumar-Swain.pdf), *ECE*, *Silicon University*
  - [Dr. (Prof.) Chinmoy Saha](https://www.iist.ac.in/avionics/chinmoysaha) and [Dr. (Prof.) Priyadarshanam](https://www.iist.ac.in/avionics/priyadarshnam), *Dept. of Avionics, Indian Institute of Space Science and Technology*
  - [Adnaan M](https://www.linkedin.com/in/adnaan-m-262a261b2/), Founder, *ToSpace, Karur, Tamil Nadu*.
 
# Course Details

- 📖 **PREREQUISITES**:
  - 1st Year Engineering Math Courses.
  - All programming the embedded systems will be done using 'C language'. So a general revision will help.
 
-  **COURSE OUTCOME**:
   - A good understanding of CubeSat, a small satellite format.
   - Good understanding of satellite communication.
   - Proficient in RF communication systems using LoRa protocol.
   - A good understanding of antenna design, simulation and implementation.
   - Setting up a satelitte ground station using the open source platform TinyGS.
 
- **COURSE DETAILS**
  - Introduction to small satellite format CubeSats.
    - CubeSat Dispenser Systems
    - Launch Vehicles (LVs) or, Rockets.
    - Development Process Overview: Development, Funding, Design, Regulation, GS, etc
    - Mission Models and Requirement Sources for Launch
    - Licensing and Flight Certification.
  - Basics of Satellite Communication
    - Introduction to Communication and signal processing.
    - Introduction to LoRa protocol.
    - Introduction to spread-spectrum communication protocol.
    - Setting up a LoRa communication system using ESP32 platform.
  - Introduction to Antenna Design
    - Types of Antenna and their Radiation Mechanism.
    - Design and simulation of wire and dipole antennas.
    - Practical antenna tuning using VNA.
  - Setting up Ground Station using the TinyGS open-source platform.
    - Programming ESP32 platform using Platform I/O
    - Setting up a TinyGS ground station using an ESP32 platform.
    - Design and tune an antenna for the ground station.
    - A group of three will design a implement their ground station. The ground stations will be judged based on figure of merit based on the density of satellites and the strength of the signal received. The final winner will present a poster during the upcoming NES-2024 workshop.



