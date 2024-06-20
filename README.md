# Course Venue & Timings
🛰️ This is the portal for Summer Internship 2024 on Introduction to CubeSat and Satellite Communication. 📡

- 📆 **DURATION**: June 25th till July 12th (3 weeks)
- ⏲️ **TIMINGS**:
  - Theory Sessions 🕙 **10:00am - 1:00pm**
  - Hands-on practical Sessions 🕝 **2:30pm - 5:30pm**
- 🏛️ **VENUE**(Old Building):
  - Theory & Practical Sessions: **Room 04-10** (Advanced VLSI Training Lab)

# Lab Info

## Requirements

- Download and install the latest version (2.3.2+) [Arduino IDE](https://www.arduino.cc/en/software). Majority of the Lab activity will be writing `C Programming Language` for the ESP 32 platform which we will develop using the Arduino IDE.
- Download and install [4NEC2](https://www.qsl.net/4nec2/), antenna modeling and simulation softwware. The antenna design and simulation will be done using this sofware.
- Install [Windows Subsystem for Linux (WSL)](https://github.com/silicon-vlsi-org/eda-wsl2) with Ubuntu 22.04 Linux Distro. In this instruction page, **OMIT** the installation of EDA tools. During the tenure of the course, we will learn many fundamental signal processing concepts that is best practiced using the Python programming/scripting language. We will WSL for that purpose. Python language is not a prereq, the basic programming structures will be provided to you. 

## Lab Resources

- [Ai Thinker's LoRa Radio Module RA-02](AiThinkerRA02.md) is RF radio module based on the Semtech's SX127X transceiver chip. This module will be used for all the satellite communication Lab exercises as well as the [tinyGS](https://tinygs.com) ground station. This page provides the basic information about the module.
  - [Datasheet RA-02](docs/datasheet-LoRaModule-RA02-v1_1.pdf): Ai Thinker's LoRa Radio Module RA-02
- The [SX1276/77/78/79](https://www.semtech.com/products/wireless-rf/lora-connect/sx1276) transceiver chipset features the LoRa® long range modem that provides ultra-long range spread spectrum communication
  - [Datasheet SX127X](docs/Datasheet-SX1276-7-8-9_W_APP_V7.pdf)
  - [Application Note AN1200-22](docs/AN1200_22_Semtech_LoRa_Basics_v2_STD.pdf): This application note covers the basics of LoRa Modulation including spread-spectrum communication and LoRa spread spectrum. 
  - [Application Note AN1200-13](docs/AN1200_13_SX17x_Modem_DesignerGuide.pdf): This is an application note for LoRa modem design covering basic priciples of LoRa Design (Modulation, RX Senisitivty, SNR, SF, BW, etc.) to advancd LoRa design (FEC, HW, etc) and how to use the LoRa calculator to optimize Radio design.
- LoRa Library for ESP32 firmware development:
  - [LoRa Library GitHub](https://github.com/sandeepmistry/arduino-LoRa)
  - [LoRa Arduino Library Reference](https://www.arduino.cc/reference/en/libraries/lora)


# Course Details

- 📖 **PREREQUISITES**:
  - 1st Year Engineering Math Courses.
  - All programming the embedded systems will be done using 'C language'. So a general revision will help.

- 👨‍🏫 **RESOURCE PERSONS**:
  - [Dr. Saroj Rout](https://sroutk.github.io) and [Prof. Prasant Swain](https://silicon.ac.in/wp-content/uploads/2022/04/Prasant-Kumar-Swain.pdf), *ECE*, *Silicon University*
  - [Dr. (Prof.) Chinmoy Saha](https://www.iist.ac.in/avionics/chinmoysaha) and [Dr. (Prof.) Priyadarshanam](https://www.iist.ac.in/avionics/priyadarshnam), *Dept. of Avionics, Indian Institute of Space Science and Technology*
  - [Adnaan M](https://www.linkedin.com/in/adnaan-m-262a261b2/), Founder, *ToSpace, Karur, Tamil Nadu*.
 
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



