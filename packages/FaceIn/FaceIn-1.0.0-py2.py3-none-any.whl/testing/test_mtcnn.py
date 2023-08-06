###############################################################################
# Test MTCNN face detector with camera
#
# Urs Utiznger
# 2020
###############################################################################

###############################################################################
# Imports
###############################################################################
import logging
import time
import platform
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed
# Tensorflow
import tensorflow as tf
# MTCNN
from mtcnn import MTCNN 
# OpenCV
import cv2
# Camera configuration
from camera.configs.dell_internal_configs  import configs

###############################################################################
# Intializing
###############################################################################
# Logging
logging.basicConfig(level=logging.INFO)
#
# Face dtector
detector = MTCNN()
# System dependent camera interface
plat = platform.system()
mach = platform.machine()
# Create camera interface
# Based on computer OS you are running
if plat == 'Windows': 
    from camera.capture.cv2capture import cv2Capture
    camera = cv2Capture(configs)
elif plat == 'Linux':
    if mach == "aarch64":
        from camera.capture.nanocapture import nanoCapture
        camera = nanoCapture(configs)
    elif mach == "armv6l" or platform.machine() == 'armv7l':
        from camera.capture.cv2capture import cv2Capture
        camera = cv2Capture(configs)
        # from picapture import piCapture
        # camera = piCapture()
elif plat == 'MacOS':
    from camera.capture.cv2capture import cv2Capture
    camera = cv2Capture(configs)
else:
    from camera.capture.cv2capture import cv2Capture
    camera = cv2Capture(configs)
# Start camera server
print("Starting Capture")
camera.start()

###############################################################################
# Main Loop
###############################################################################
window_handle = cv2.namedWindow("Camera", cv2.WINDOW_AUTOSIZE)
last_fps_time = time.time()
num_frames = 0
while(cv2.getWindowProperty("Camera", 0) >= 0):
    if camera.new_frame:
        num_frames += 1
        image = cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB)
        result = detector.detect_faces(image)
        if result:
            bounding_box = result[0]['box']
            keypoints = result[0]['keypoints']
            # Mark results on image
            cv2.rectangle(image,
                        (bounding_box[0], bounding_box[1]),
                        (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                        (0,155,255),
                        2)
            cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
            cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
            cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
            cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
            cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)
            # Display results
        cv2.imshow('Camera', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    # Display computation FPS
    current_time = time.time()
    if (current_time - last_fps_time) >= 5.0: # update frame rate every 5 secs
        print("FaceFindFPS: ", num_frames/5.0)
        num_frames = 0
        last_fps_time = current_time
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.stop()
cv2.destroyAllWindows()
