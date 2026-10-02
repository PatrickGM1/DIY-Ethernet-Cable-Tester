"""End-to-end test of tester.scan() on a PC, using a fake machine.Pin and a fake cable."""
import sys
import time
import types

time.sleep_us = lambda us: None  # CPython has no sleep_us

wires = set()      # each entry: frozenset({gpio_a, gpio_b}) = a connection
out_low = set()    # GPIOs currently driven low


def component(n):
    seen, todo = {n}, [n]
    while todo:
        x = todo.pop()
        for e in wires:
            if x in e:
                for y in e:
                    if y not in seen:
                        seen.add(y)
                        todo.append(y)
    return seen


class Pin:
    IN, OUT, PULL_UP = 0, 1, 2

    def __init__(self, n, mode=0, pull=None, value=None):
        self.n = n
        self.init(mode, pull, value)

    def init(self, mode=0, pull=None, value=None):
        if mode == Pin.OUT and value == 0:
            out_low.add(self.n)
        else:
            out_low.discard(self.n)

    def value(self):
        return 0 if component(self.n) & out_low else 1


fake = types.ModuleType("machine")
fake.Pin = Pin  # type: ignore
sys.modules["machine"] = fake

from tester import scan, analyze  # noqa: E402


def cable(*extra, drop=(), swap=None):
    w = {frozenset({i, i + 8}) for i in range(8)}
    for d in drop:
        w.discard(frozenset({d, d + 8}))
    if swap:
        a, b = swap
        w.discard(frozenset({a, a + 8}))
        w.discard(frozenset({b, b + 8}))
        w.add(frozenset({a, b + 8}))
        w.add(frozenset({b, a + 8}))
    for e in extra:
        w.add(frozenset(e))
    return w


cases = {
    "good": cable(),
    "swapped 1,2": cable(swap=(0, 1)),
    "open pin 3": cable(drop=(2,)),
    "short pins 5,6 at far end": cable((12, 13)),
}

for name, w in cases.items():
    wires.clear()
    wires.update(w)
    print(name, analyze(scan()))