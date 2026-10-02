# Placeholder pin map. Update after checking which pins your Zero exposes.
A = [0, 1, 2, 3, 4, 5, 6, 7]
B = [8, 9, 10, 11, 12, 13, 14, 15]
ALL = A + B


def scan():
    import time
    from machine import Pin
    pins = {n: Pin(n, Pin.IN, Pin.PULL_UP) for n in ALL}
    result = []
    for a in A:
        pins[a].init(Pin.OUT, value=0)
        time.sleep_us(50)
        lows = {n for n in ALL if n != a and pins[n].value() == 0}
        pins[a].init(Pin.IN, Pin.PULL_UP)
        result.append(lows)
    return result


def analyze(result):
    status = []
    for i, lows in enumerate(result):
        if lows == {B[i]}:
            status.append("OK")
        elif not lows:
            status.append("OPEN")
        elif len(lows) == 1:
            n = next(iter(lows))
            status.append("CROSS %d" % (B.index(n) + 1) if n in B else "SHORT")
        else:
            status.append("SHORT")
    return status