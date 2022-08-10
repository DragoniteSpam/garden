from picamera import PiCamera
import time

# Setup camera: max resolution, frame rate to support the same
def camera_setup():
    global camera, frame_count, camera_initialized
    try:
        frame_count = 0
        camera = PiCamera()
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        camera_initialized = True
    except:
        print("Could not initialize the camera for the time lapse")
        camera_initialized = False

def camera_update():
    global camera, frame_count, camera_initialized
    if camera_initialized == False:
        return
    try:
        #Turn on sensor & camera & allow to settle
        camera.start_preview()
        time.sleep(5)
        camera.capture('./timelapse/pic_%05d.jpg' % (frame_count))
        time.sleep(1)
        camera.stop_preview()
        frame_count = frame_count + 1
    except Exception as e:
        print("Error running the camera: " + str(e))
        pass
