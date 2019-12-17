import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)
    camera.start_preview()
    time.sleep(1)
    for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
        print('captured image %s' % filename)
        if i == 10:
            break
        time.sleep(1)
    camera.stop_preview()
