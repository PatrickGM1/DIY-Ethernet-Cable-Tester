import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(16), 1)


def wheel(pos):
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


while True:
    for pos in range(0, 256, 2):
        np[0] = wheel(pos)
        np.write()
        time.sleep_ms(20)
