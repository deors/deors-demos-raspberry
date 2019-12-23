import RPi.GPIO as GPIO

# cleanup from a possible previous execution
def clean(pin):
    # to use GPIO pin numbers
    GPIO.setmode(GPIO.BCM)
    # set up GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    # cleans up the pin
    GPIO.cleanup()
    return

GPIO.setwarnings(False)

clean(20)
clean(21)
clean(22)
clean(23)
clean(24)
clean(25)
