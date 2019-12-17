import RPi.GPIO as GPIO
# cleanup from a possible previous execution
def clean(pin):
    GPIO.setwarnings(False)
    # to use GPIO pin numbers
    GPIO.setmode(GPIO.BCM)
    # set up GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    # cleans up the pin
    GPIO.cleanup()
    return

clean(23)
clean(24)
clean(25)
