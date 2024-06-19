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

- Download and install [Arduino IDE](https://www.arduino.cc/en/software). Majority of the Lab will be writing C code for the ESP 32 platform which will developed in this IDE.
- Download and install [4NEC2](https://www.qsl.net/4nec2/), antenna modeling and simulation softwware. The antenna design and simulation will be done using this sofware.
- Install [Windows Subsystem for Linux (WSL)](https://github.com/silicon-vlsi-org/eda-wsl2). In this instruction, **omit** the installation of EDA tools. There will be few instances during the course where the student has to write a code in Python or other lannguages. We will use WSL for that purpose. 
- 



# Resources

- [LoRa Module Ai Thinker RA-02](AiThinkerRA02.md)
  - [Datasheet](docs/datasheet-LoRaModule-RA02-v1_1.pdf)

- [LoRa Library GitHub](https://github.com/sandeepmistry/arduino-LoRa)
- [LoRa Arduino Library Reference](https://www.arduino.cc/reference/en/libraries/lora)

# Course Details

- 📖 **PREREQUISITES**:
  - 1st Year Engineering Math Courses.
  - All programming the embedded systems will be done using 'C language'. So a general revision will help.

- 👨‍🏫 **RESOURCE PERSONS**:
  - [Dr. Saroj Rout](https://sroutk.github.io) and [Prof. Prasant Swain](https://silicon.ac.in/wp-content/uploads/2022/04/Prasant-Kumar-Swain.pdf), *ECE*, *Silicon University*
  - [Dr. (Prof.) Chinmoy Saha](https://www.iist.ac.in/avionics/chinmoysaha) and [Dr. (Prof.) Priyadarshanam](https://www.iist.ac.in/avionics/priyadarshnam), *Dept. of Avionics, Indian Institute of Space Science and Technology*
 
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



