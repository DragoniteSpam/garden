# Adapted from here:
# http://web.archive.org/web/20220501075205/https://www.raspberrypi.com/news/raspberry-pi-zero-waters-your-plants-and-records-growth-timelapse/
# http://web.archive.org/web/20210822053232/https://www.explainingcomputers.com/sample_code/Watering.py

from watering import *
from timelapse import *

camera_setup()
sensor_setup(15, 5)

try:
    while True:
        camera_update()
        sensor_update()
        sensor_wait()
finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
