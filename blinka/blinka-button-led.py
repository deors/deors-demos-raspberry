#!/usr/bin/python3

import time
import board
import digitalio

print("press the button!")

led = digitalio.DigitalInOut(board.D23)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D5)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    led.value = button.value # light when button is pressed!
