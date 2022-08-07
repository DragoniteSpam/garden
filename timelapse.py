from picamera import PiCamera

# Setup camera: max resolution, frame rate to support the same
def camera_setup():
    global camera, frame_count
    try:
        frame_count = 0
        camera = PiCamera()
        camera.resolution = (2592, 1944)
        camera.framerate = 15
    except:
        print("Could not initialize the camera for the time lapse")

def camera_update():
    global camera, frame_count
    try:
        #Turn on sensor & camera & allow to settle
        camera.start_preview()
        time.sleep(5)
        camera.capture('~/Pictures/pic_%05d.jpg' % (frame_count))
        time.sleep(1)
        camera.stop_preview()
        frame_count = frame_count + 1
    except:
        pass
