# Adapted from here:
# http://web.archive.org/web/20220501075205/https://www.raspberrypi.com/news/raspberry-pi-zero-waters-your-plants-and-records-growth-timelapse/
# http://web.archive.org/web/20210822053232/https://www.explainingcomputers.com/sample_code/Watering.py

from camera import *

camera_setup(show = False, interval = 5)

try:
    while True:
        camera_update()
        camera_wait()
except Exception as e:
    print("Something bad happened:")
    print(str(e))