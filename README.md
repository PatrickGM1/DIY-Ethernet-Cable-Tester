# DIY-Ethernet-Cable-Tester

I am building on a rp2040 zero an Ethernet Cable tester. I will use this readme as a blog post lol, I will put this post on my website when I am done, and I will clean the readme

# Ethernet Cable Tester Parts that I think I will need:

- 1x RP2040 Zero
- 2x [RJ45 breakout board with jack](https://www.otronic.nl/nl/rj45-utp-ethernet-female-breakout-board) (pad pitch still to be confirmed with the shop)
- 2 packs of 10x [1 kOhm resistor, 0.25 W, through-hole](https://www.otronic.nl/nl/10x-weerstand-1k-ohm-1-4-watt-5) (16 needed)
- 1x [SSD1306 128x64 I2C OLED, 0.96 in](https://www.otronic.nl/nl/mini-oled-display-wit-0-96-inch-128x64-i2c)
- 1x [Tactile push button](https://www.otronic.nl/nl/drukknopje-moment-6x6x4-microschakelaar), 6x6x4 mm,
- 1x [Perfboard, 70 x 90 mm, 2.54 mm pitch](https://www.otronic.nl/nl/experimenteer-prototyping-printplaat-7x9cm-groen.html)
- 1x [Male pin header strip, 2.54 mm](https://www.otronic.nl/nl/40-pins-header-male-2-54mm-zwart), 40 pins
- 1x Thin insulated wire
- 1x USB-C cable

For now I checked only [otronic.nl](https://www.otronic.nl), they seem pretty cheap, I wanted to look on the website of a local store, but it is down lmao for the moment

# Pinout

Pinout image: [mischianti.org](https://mischianti.org/wp-content/uploads/2022/09/Waveshare-rp2040-zero-Raspberry-Pi-Pico-alternative-pinout.jpg) (CC BY-NC-ND)

# Wiring diagram

![Wiring diagram](diagram.drawio.svg)

Source: [diagram.drawio](diagram.drawio)

You can also open in [diagrams.net](https://app.diagrams.net).

# Pin map

- Jack A pins 1 to 8: GP0 to GP7
- Jack B pins 1 to 8: GP8 to GP15
- OLED (I2C1): SDA GP26, SCL GP27
- Button: GP28 to GND

# Scripts

- `tester.py` - `scan()` reads the jack pins, `analyze()` turns the readings into OK, OPEN, SHORT or CROSS per wire.
- `test_led.py` - cycles the onboard NeoPixel through a rainbow, quick check the board is alive.
- `test_logic.py` - runs `tester.analyze()` against good/swapped/open/short cable cases, no hardware needed.
