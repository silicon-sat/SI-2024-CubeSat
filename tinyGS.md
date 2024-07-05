# Resources

- [tinyGS Official Site](https://tinygs.com)
- [tinyGS GitHub](https://github.com/G4lile0/tinyGS)
- [tinyGS Wiki](https://github.com/G4lile0/tinyGS/wiki)
- [tinyGS FAQ](https://github.com/G4lile0/tinyGS/wiki/FAQ)
- [Sooraj Shenoy VU3ZAG's blog](https://soorajshenoys.blogspot.com/2023/01/lora-433mhz-tinygs-satellite-ground.html). [See Circuit Diagram here](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPLXVwBgXXILY6AirUq9ShTVVTN6xoJR0XoF2F4YatzZkGx725gxbevitd35hwaW-gN5zmFXhxZ16sYMLWMtI3AHicCbGBdiQuepzj7F09rUw8RHgCNEeEBdWACViDJuf4WEvP-KMYnK3eSaRneuvUs43CwqN_q3icXc82oeoE3XxNJLL2y_ylKYjQTg/s2864/circuit.jpg).

# Install and Setup 

These instructions are for a Windows workstation.

- Connect your ESP32-LoRa board to your desktop/laptop.
- Follow the instructions on the [web installer](https://installer.tinygs.com/) to install the latest tinyGS firmware.
  - Config detailed in this [GitPage](https://github.com/G4lile0/tinyGS/wiki/Ground-Station-configuration)
  - Noticed that for flashing the board, needed to hold the BOOT button down while connecting the USB cable but not sure. Also mentioned in VU3ZAG's blog. 
- After successful flash, boot it up and it will become a hotspot with SSID **My Tiny GS**.
- Connect to the hotspot and browse to `192.168.4.1` and configure the board.
- **MQTT** and **WiFi** login credentials will be provided to you.
- For the **Board Type** select `433 MHz TTGO LoRa 32 v2` from the dropdown menu.
- Select **TX** to make sure that the test mode can be used.
- Once all info is entered click on the `Apply` button. The ESP32 will reboot and if all went well the ground station should appear on the Tiny GS site.
- Once the ground station is estabilished, you can get a temporary passwordless link to your station by typing `/weblogin` in your telegram BOT. This link will allow you to modify the groundsation parameters.
