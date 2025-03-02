# Test all the leds connections looping through them back and forth

from machine import Pin
from time import sleep

connectors = [0, 1, 2, 3, 6, 7]
pins = []
for connector in connectors:
    pins.append(Pin(connector, Pin.OUT))


def pinOff(pins):
    for pin in pins:
        pin.off()


def pinOn(pin):
    pin.on()


inc = 1
index = 0

while True:
    pinOff(pins)
    sleep(0.5)
    pinOn(pins[index])
    sleep(2)
    index += inc
    if index == 0:
        inc *= -1
    if index == len(pins) - 1:
        inc *= -1
