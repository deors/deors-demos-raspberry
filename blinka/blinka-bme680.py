#!/usr/bin/python3

import time
import board
import busio
import adafruit_bme680

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
sensor.sea_level_pressure = 1013.25

while True:
    print("Temperature  : %0.1f C" % sensor.temperature)
    print("Humidity     : %0.1f %%" % sensor.humidity)
    print("Pressure     : %0.1f hPa" % sensor.pressure)
    print("Altitude     : %0.2f meters" % sensor.altitude)
    print("Gas detector : %0.2f ohms" % sensor.gas)
    print()
    time.sleep(2)
