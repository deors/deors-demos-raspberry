#!/usr/bin/python

import RPi.GPIO as GPIO
import random
import signal
import sys
import threading
import time

ON = 1
OFF = 0

HIGHISON = True
HIGHISOFF = False

BUTTON1 = 6
BUTTON2 = 5
RGB_RED = 22
RGB_GREEN = 23
RGB_BLUE = 24
RED = 20
BLUE = 21

class LED():

    def __init__(self, pin, highIsOn = True):
        GPIO.setup(pin, GPIO.OUT)
        self.__loop = False
        self.__threading = None
        self.__pin = pin
        self.__highIsOn = highIsOn
        self.__state = OFF
        self.off()

    def on(self,):
        self.__loop = False
        self.__state = ON
        GPIO.output(self.__pin, GPIO.HIGH if self.__highIsOn else GPIO.LOW)

    def off(self,):
        self.__loop = False
        self.__state = OFF
        GPIO.output(self.__pin, GPIO.LOW if self.__highIsOn else GPIO.HIGH)

    def toggle(self,):
        self.__state = 1 - self.__state
        GPIO.output(self.__pin, self.__state)

    def state(self, state):
        self.__state = state
        GPIO.output(self.__pin, self.__state)

    def blink(self, frequency):
        if self.__threading is not None and self.__threading.isAlive():
            self.__threading.join()
        self.__threading = threading.Thread(target = self.__blink, args=(frequency,))
        self.__threading.start()

    def __blink(self, frequency = 1):
        self.__loop = True
        while self.__loop:
            self.toggle()
            if self.__loop:
                time.sleep(frequency / 2.0)

# led change flags
changing = False
blinking = False

# restore changeabiliy flag
def restoreChanging():
    global changing
    changing = False

# sigint handler
def sigintHandler(sig, frame):
    ledRGBRed.off()
    ledRGBGreen.off()
    ledRGBBlue.off()
    ledRed.off()
    ledBlue.off()
    GPIO.cleanup()
    print
    sys.exit(0)

# register sigint handler
signal.signal(signal.SIGINT, sigintHandler)

# disable warnings when channel in use
# for example from previous script run
GPIO.setwarnings(False)
# to use GPIO pin numbers
GPIO.setmode(GPIO.BCM)
# set up GPIO input channels
GPIO.setup(BUTTON1, GPIO.IN)
GPIO.setup(BUTTON2, GPIO.IN)
# init leds
ledRGBRed = LED(RGB_RED, HIGHISOFF)
ledRGBGreen = LED(RGB_GREEN, HIGHISOFF)
ledRGBBlue = LED(RGB_BLUE, HIGHISOFF)
ledRed = LED(RED)
ledBlue = LED(BLUE)

print 'press Ctrl-C to exit'

# button control loop
while True:
    button1Pressed = GPIO.input(BUTTON1)
    button2Pressed = GPIO.input(BUTTON2)

    #print('buttons state #1 {} #2 {}'.format(
    #      'on' if button1Pressed else 'off',
    #      'on' if button2Pressed else 'off'))

    if button1Pressed and not changing:
        changing = True
        ledRGBRed.state(random.randint(0, 2))
        ledRGBGreen.state(random.randint(0, 2))
        ledRGBBlue.state(random.randint(0, 2))
        # prevent another change for some time
        changeTimer = threading.Timer(0.2, restoreChanging)
        changeTimer.start()

    if button2Pressed:
        ledRed.on()
    else:
        ledRed.off()

    if button2Pressed and not blinking:
        blinking = True
        ledBlue.blink(1)

    if not button2Pressed:
        ledBlue.off()
        blinking = False

    time.sleep(0.01)
