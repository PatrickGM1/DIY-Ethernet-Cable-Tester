import time
import machine, neopixel
from tester import scan, analyze

np = neopixel.NeoPixel(machine.Pin(16), 1)


def led(r, g, b):
    np[0] = (r, g, b)
    np.write()


def run_test():
    status = analyze(scan())
    for i, s in enumerate(status):
        print("pin %d: %s" % (i + 1, s))
    if all(s == "OK" for s in status):
        led(0, 10, 0)
    else:
        led(10, 0, 0)
    return status

last = None
while True:
    status = analyze(scan())
    if status != last:
        for i, s in enumerate(status):
            print("pin %d: %s" % (i + 1, s))
        last = status
    led(0, 10, 0) if all(s == "OK" for s in status) else led(10, 0, 0)
    time.sleep(1)


led(0, 0, 0)