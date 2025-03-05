# Test all the leds connections looping through them back and forth

from machine import Pin
from time import sleep


def createPins(connectors):
    pins = []
    for connector in connectors:
        pins.append(Pin(connector, Pin.OUT))
    return pins


def pinOff(pins):
    for pin in pins:
        pin.off()


def pinOn(pin):
    pin.on()


def light_level(pins, level):
    pinOff(pins)
    sleep(0.5)
    pinOn(pins[level])
    sleep(2)


class Lift:
    def __init__(self, level=0, state=0, stops=[]):
        self.level = level
        self.state = state
        self.stops = stops
        self.organiseStops()

    def __str__(self):
        state_text = {-1: "going down", 0: "stopped", 1: "going up"}
        return f"""
This lift is at level {self.level} and is {state_text[self.state]}
        """

    def organiseStops(self):
        if self.stops == []:
            return
        if self.state == 0:
            return
        levels_higher = [i for i in self.stops if i >= self.level]
        levels_higher.sort()
        levels_lower = [i for i in self.stops if i < self.level]
        levels_lower.sort(reverse=True)
        if self.state == 1:
            self.stops = levels_higher + levels_lower
        else:
            self.stops = levels_lower + levels_higher
        print(f"Stops after organising: {self.stops}")
connectors = [0, 1, 2, 3, 6, 7]
pins = createPins(connectors)

inc = 1
index = 0

lift = Lift(4, 1, [1, 5, 0, 2])
while True:
