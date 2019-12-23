#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# blinking function
def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

# to use GPIO pin numbers
GPIO.setmode(GPIO.BCM)
# set up GPIO output channel
GPIO.setup(25, GPIO.OUT)
# blink GPIO25 10 times
for i in range(0, 10):
    blink(25)
GPIO.cleanup()
