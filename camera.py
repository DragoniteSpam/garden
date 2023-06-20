from picamera2 import Picamera2, Preview
import time
import datetime

# Setup camera: max resolution, frame rate to support the same
def camera_setup(show):
    global camera, frame_count, camera_initialized, show_camera, capture_config
    try:
        show_camera = show
        frame_count = 0
        camera = Picamera2()
	# the max resolution for:
	#  - the Zero Cam is 2592 x 1944
        #  - the Camera Module 2 is 3280 x 2464
        capture_config = camera.create_still_configuration(main = { "size": camera.sensor_resolution })
        camera.configure(capture_config)
        camera.start(show_preview = False)
        camera_initialized = True
        print("Successfully initialized camera (show preview: " + str(show) + ")")
    except Exception as e:
        print("Could not initialize the camera for the time lapse:")
        print(str(e))
        camera_initialized = False

def camera_update():
    global camera, frame_count, camera_initialized, show_camera
    if camera_initialized == False:
        return
    try:
        # Picam2 changed the camera interface and I don't feel like updating
        # all that old code if I don't have to, but you can have it turn on
        # the preview if you want to here
        #if show_camera:
            # start preview
            # time.sleep(5)

        camera.capture_file('./timelapse/pic_%s.jpg' % str(datetime.datetime.now()).replace(":", "_"))

        # And remember to turn it off when you're done
        #if show_camera:
            # time.sleep(1)
            # stop preview

        frame_count = frame_count + 1

        if (frame_count % 100 == 0):
            print(str(frame_count) + " frames captured")
    except Exception as e:
        print("Error running the camera: " + str(e))
        pass
