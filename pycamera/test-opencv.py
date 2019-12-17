from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size = (1920, 1080))

time.sleep(1)

for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port = True):
    image = frame.array

    cv2.imshow("frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord('q'):
        break
