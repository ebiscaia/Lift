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


connectors = [0, 1, 2, 3, 6, 7]
pins = createPins(connectors)

inc = 1
index = 0

while True:
    for pins in [pins_red, pins_green]:
        pinOff(pins)
    sleep(0.5)
    for pins in [pins_red, pins_green]:
        pinOn(pins[index])
    sleep(2)
    index += inc
    if index == 0:
        inc *= -1
    if index == len(pins) - 1:
        inc *= -1
