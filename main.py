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


connectors_red = [0, 1, 2, 3, 6, 7]
connectors_green = [21, 20, 19, 18, 17, 16]
pins_red = createPins(connectors_red)
pins_green = createPins(connectors_green)

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
