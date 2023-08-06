import cv2
import logging
import time

from camera.capture.cv2capture import cv2Capture

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


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Capture")

print("Starting Capture")
camera =  camera = cv2Capture(configs,camera_num=0) 
camera.start()

print("Getting Frames")

window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
last_fps_time = time.time()
num_frames = 0
while(cv2.getWindowProperty("CSI Camera", 0) >= 0):
    current_time = time.time()
    (frame_time, frame) = camera.capture.get(block=True, timeout=None)
    num_frames += 1
    while not camera.log.empty():
        (level, msg) = camera.log.get_nowait()
        logger.log(level, "{}".format(msg))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.stop()
cv2.destroyAllWindows()
