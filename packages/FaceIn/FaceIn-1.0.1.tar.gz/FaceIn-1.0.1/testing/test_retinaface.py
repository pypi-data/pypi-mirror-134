import cv2
import logging
import time
import platform
import os

os.environ['DEEPFACE_HOME'] = os.getcwd()

from retinaface import RetinaFace
face_model = RetinaFace.build_model()

# default camera starts at 0 by operating system
camera_index = 0

configs = {
    'camera_res'      : (1280, 720 ),   # width & height
    'exposure'        : -6,             # -1,0 = auto, 1...max=frame interval, 
    'autoexposure'    : 1.0,            # depends on camera: 0.25 or 0.75(auto) or 1(auto), -1,0
    'fps'             : 30,             # 15, 30, 40, 90, 120, 180
    'fourcc'          : -1,             # n.a.
    'buffersize'      : -1,             # n.a.
    'output_res'      : (-1, -1),       # Output resolution, -1,-1 no change
    'flip'            : 0,              # 0=norotation 
                                        # 1=ccw90deg 
                                        # 2=rotation180 
                                        # 3=cw90 
                                        # 4=horizontal 
                                        # 5=upright diagonal flip 
                                        # 6=vertical 
                                        # 7=uperleft diagonal flip
    'displayfps'       : 30             # frame rate for display server
}

if configs['displayfps'] >= 0.8*configs['fps']:
    display_interval = 0
else:
    display_interval = 1.0/configs['displayfps']

dps_measure_time = 5.0 # assess performance every 5 secs

window_name      = 'Camera'
font             = cv2.FONT_HERSHEY_SIMPLEX
textLocation0    = (10,20)
textLocation1    = (10,60)
fontScale        = 1
fontColor        = (255,255,255)
lineType         = 2
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE) # or WINDOW_NORMAL

# Setting up logging
logging.basicConfig(level=logging.DEBUG) # options are: DEBUG, INFO, ERROR, WARNING
logger = logging.getLogger("CV2Capture")

# Create camera interface based on computer OS you are running
# plat can be Windows, Linux, MaxOS
plat = platform.system()
if plat == 'Linux' and platform.machine() == "aarch64": # this is jetson nano for me
        from camera.capture.nanocapture import nanoCapture
        camera = nanoCapture(configs, camera_index)
else:
    from camera.capture.cv2capture import cv2Capture
    camera = cv2Capture(configs, camera_num=camera_index, queue_size=2)

logger.log(logging.INFO, "Getting Images")
camera.start()


# Initialize Variables
last_display   = time.perf_counter()
last_fps_time  = time.perf_counter()
measured_dps   = 0
num_frames_received    = 0
num_frames_displayed   = 0
stopped = False

while(not stopped):

    current_time = time.perf_counter()

    # wait for new image
    (img_time, img) = camera.capture.get(block=True, timeout=None)
    num_frames_received += 1
    while not camera.log.empty():
        (level, msg) = camera.log.get_nowait()
        logger.log(level, "{}".format(msg))

    faces = RetinaFace.detect_faces(img, threshold = 0.9, model = face_model, allow_upscaling = True)
    
    for identity in faces:    
        facial_area = identity["facial_area"]
        landmarks = identity["landmarks"]        
        #highlight facial area
        cv2.rectangle(img, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (255, 255, 255), 1)
        
        #highlight the landmarks
        cv2.circle(img, tuple(landmarks["left_eye"]), 1, (0, 0, 255), -1)
        cv2.circle(img, tuple(landmarks["right_eye"]), 1, (0, 0, 255), -1)
        cv2.circle(img, tuple(landmarks["nose"]), 1, (0, 0, 255), -1)
        cv2.circle(img, tuple(landmarks["mouth_left"]), 1, (0, 0, 255), -1)
        cv2.circle(img, tuple(landmarks["mouth_right"]), 1, (0, 0, 255), -1)

    if (current_time - last_fps_time) >= dps_measure_time:
        measured_fps = num_frames_received/dps_measure_time
        logger.log(logging.INFO, "MAIN:Frames received per second:{}".format(measured_fps))
        num_frames_received = 0
        measured_dps = num_frames_displayed/dps_measure_time
        logger.log(logging.INFO, "MAIN:Frames displayed per second:{}".format(measured_dps))
        num_frames_displayed = 0
        last_fps_time = current_time

    if (current_time - last_display) >= display_interval:
        frame_display = img.copy()        
        cv2.putText(frame_display,"Capture FPS:{} [Hz]".format(camera.measured_fps), textLocation0, font, fontScale, fontColor, lineType)
        cv2.putText(frame_display,"Display FPS:{} [Hz]".format(measured_dps),        textLocation1, font, fontScale, fontColor, lineType)
        cv2.imshow(window_name, frame_display)

        if cv2.waitKey(1) & 0xFF == ord('q'): stopped = True
        if cv2.getWindowProperty(window_name, 0) < 0: stopped = True

        last_display = current_time
        num_frames_displayed += 1

# Clean up
camera.stop()
cv2.destroyAllWindows()
