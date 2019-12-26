#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import time

RED = 20
GREEN = 21
BLUE = 22

# set led state function
def led(pin, mode):
    if mode == '1':
        GPIO.output(pin, GPIO.LOW)
    elif mode == '0':
        GPIO.output(pin, GPIO.HIGH)

    return

# check args
if len(sys.argv) != 4:
    print 'wrong argument list: ./set-rgbled.py red(1/0) green(1/0) blue(1/0)'
    print 'for example: ./set-rgbled.py 1 0 1'
else:
    GPIO.setwarnings(False)
    # to use GPIO pin numbers
    GPIO.setmode(GPIO.BCM)
    # set up GPIO output channel
    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    # set led state
    led(RED, sys.argv[1])
    led(GREEN, sys.argv[2])
    led(BLUE, sys.argv[3])
