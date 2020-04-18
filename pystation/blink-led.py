#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time

# blinking function
def blink(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    return

# check args
if len(sys.argv) != 2:
    print 'wrong argument list: ./blink-led.py pin'
    print 'for example: ./blink-led.py 20'
else:
    pin = int(sys.argv[1])
    # to use GPIO pin numbers
    GPIO.setmode(GPIO.BCM)
    # set up GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    # blink GPIO20 10 times
    for i in range(0, 10):
        blink(pin)
    GPIO.cleanup()
