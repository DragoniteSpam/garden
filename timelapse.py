from picamera import PiCamera
import time
import datetime

# Setup camera: max resolution, frame rate to support the same
def camera_setup(show):
    global camera, frame_count, camera_initialized, show_camera
    try:
        show_camera = show
        frame_count = 0
        camera = PiCamera()
	# the max resolution for picamera is 2592 x 1944, although the 
	# camera module itself can go up to 3280 x 2464
	# camera.resolution = (2592, 1944)
        camera.resolution = (2560, 1440)
        camera.framerate = 15
        camera_initialized = True
    except:
        print("Could not initialize the camera for the time lapse")
        camera_initialized = False

def camera_update():
    global camera, frame_count, camera_initialized, show_camera
    if camera_initialized == False:
        return
    try:
        #Turn on sensor & camera & allow to settle
        if show_camera:
                camera.start_preview()
        #time.sleep(5)
        camera.capture('./timelapse/pic_%s.jpg' % str(datetime.datetime.now()).replace(":", "_"))
        #time.sleep(1)
        if show_camera:
                camera.stop_preview()
        frame_count = frame_count + 1
    except Exception as e:
        print("Error running the camera: " + str(e))
        pass
