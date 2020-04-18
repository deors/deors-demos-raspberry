#!/usr/bin/python

import RPi.GPIO as GPIO
import signal
import sys
import time

# sigint handler
def sigintHandler(sig, frame):
    GPIO.cleanup()
    print
    sys.exit(0)

# register sigint handler
signal.signal(signal.SIGINT, sigintHandler)

# check args
if len(sys.argv) != 2:
    print 'wrong argument list: ./read-button.py pin'
    print 'for example: ./read-button.py 5'
else:
    print 'press Ctrl-C to exit'
    pin = int(sys.argv[1])
    # disable warnings when channel in use
    # for example from previous script run
    GPIO.setwarnings(False)
    # to use GPIO pin numbers
    GPIO.setmode(GPIO.BCM)
    # set up GPIO input channels
    GPIO.setup(pin, GPIO.IN)
    # button control loop
    while True:
        buttonPressed = GPIO.input(pin)
        print('button {} is {}'.format(pin, 'on' if buttonPressed else 'off'))
        time.sleep(0.1)
