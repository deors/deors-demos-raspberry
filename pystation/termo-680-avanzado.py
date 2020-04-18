#!/usr/bin/python3
# -*- coding: utf-8 -*-

import board
import digitalio
import busio
import adafruit_bme680
import time
import signal
import sys
import _thread

# leds
led_ac = digitalio.DigitalInOut(board.D21)
led_ac.direction = digitalio.Direction.OUTPUT

led_cale = digitalio.DigitalInOut(board.D20)
led_cale.direction = digitalio.Direction.OUTPUT

def encender(led):
  led.value = True

def apagar(led):
  led.value = False

def limpiarLeds():
  apagar(led_ac)
  apagar(led_cale)

# sensor bme680
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

sensor.sea_level_pressure = 1013.25 #presión a nivel del mar (referencia)

# teclado
def input_thread(listener):
    input()
    listener.append(True)

# función para procesar sigint (señal de parada)
def sigint_handler(sig, frame):
    limpiarLeds()
    print()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

# main
def main():

  print()
  print("pulsa Enter para terminar")

  limpiarLeds()

  listener = []
  _thread.start_new_thread(input_thread, (listener,))

  while not listener:

    # leemos la situación actual
    temperatura = sensor.temperature
    humedad = sensor.humidity
    presion = sensor.pressure
    altitud = sensor.altitude
    gases = sensor.gas

    # escribimos los valores medidos
    print()
    print("Temperatura : %0.1f C" % temperatura)
    print("Humedad     : %0.1f %%" % humedad)
    print("Presión     : %0.1f hPa" % presion)
    print("Altitud     : %0.2f m" % altitud)
    print("Gases       : %0.2f kΩ" % (gases / 1000))
    print()

    if (temperatura > 25.0): # podemos cambiar la temperatura de corte
      # hace calor
      # necesitamos el aire acondicionado
      encender(led_ac)
      apagar(led_cale)
      print("--> temperatura alta")
    elif (temperatura < 21.0):
      # hace frío
      # necesitamos la calefacción
      encender(led_cale)
      apagar(led_ac)
      print("--> temperatura baja")
    else:
      # ni frío ni calor
      # apagamos todo
      apagar(led_ac)
      apagar(led_cale)
      print("--> temperatura normal")

    time.sleep(1)

  limpiarLeds()

if __name__ == "__main__":
   main()
