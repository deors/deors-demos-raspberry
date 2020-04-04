#!/usr/bin/python

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.start_preview()
    time.sleep(1)
    camera.start_recording('video00.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()

