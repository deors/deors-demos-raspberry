#!/usr/bin/python

import RPi.GPIO as GPIO
import signal
import sys
import time

# blinking function
def blink(pin):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    return

# sigint handler
def sigintHandler(sig, frame):
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    print
    sys.exit(0)

# register sigint handler
signal.signal(signal.SIGINT, sigintHandler)

# check args
if len(sys.argv) != 2:
    print 'wrong argument list: ./blink-led.py pin'
    print 'for example: ./blink-led.py 20'
else:
    print 'press Ctrl-C to exit'
    pin = int(sys.argv[1])
    # disable warnings when channel in use
    # for example from previous script run
    GPIO.setwarnings(False)
    # to use GPIO pin numbers
    GPIO.setmode(GPIO.BCM)
    # set up GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    # blink led 10 times
    for i in range(0, 10):
        blink(pin)
    GPIO.cleanup()
