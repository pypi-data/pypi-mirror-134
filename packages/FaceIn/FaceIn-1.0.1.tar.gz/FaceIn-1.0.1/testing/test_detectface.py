###############################################################################
# Face In 
# Recognizes visitors, records appearance time and display currently signed in
# visitors.
#
# Urs Utiznger
# 2021
###############################################################################

###############################################################################
# Imports
###############################################################################

import platform         # To load correct camera driver
import logging          # Logging
import time             # Execution handling
import os               # To adapt to different operating system

# Camera
from camera.utils import findCamera

# OpenCV
import cv2

# Deepface
from deepface import DeepFace
from deepface.extendedmodels import Age
from deepface.commons import functions, distance as dst
from deepface.detectors import FaceDetector

###############################################################################
# Settings
###############################################################################

# Folder where modesl are stored
# os.environ['DEEPFACE_HOME'] = os.getcwd()

# Face Recognition
###############################################################################
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
detector_backend        = "retinaface"  # opencv*, ssd, mtcnn, dlib, retinaface
freeze_time             = 2         # how many second analyzed image will be displayed, 5*
frame_threshold         = 5         # how many frames required to focus on a face, 5*
minimum_face_width      = 130       # filter out small faces
###############################################################################
# Computation time in ms, rtx notebook
# Retinaface: 233, 224, 225, 229, 172, 216      with glasses,    obstructions, with facemask
# OpenCV:     46,42,44,56,40                    no   glasses, no obstructions
# SSD:        30,21,21,20,21,20,20,20,19        with glasses,    obstructions, no facemask
# MTCNN:      873,1029,973,1265,868,945         with glasses,    obstructions
# DLIB:       352,350,346,346,347               with glasses, no obstructions
###############################################################################

# Camera
###############################################################################
configs = {
    'camera_res'      : (1280, 720 ),   # width & height
    'exposure'        : None,           # -1,0 = auto, 1...max=frame interval, 
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
    'displayfps'       : 5              # frame rate for display server
}

if configs['displayfps'] >= configs['fps']:  display_interval = 0
else:                                        display_interval = 1.0/configs['displayfps']

# Internal Labtop Camera Signature
###############################################################################
widthSig = 640
heightSig = 480
fourccSig = "\x16\x00\x00\x00"

dps_measure_time = 5 # seconds

if __name__ == "__main__":
    """
    Main FaceIn program
    Some more text here
    Urs Utzinger 2022
    Based on 
    """

    #
    # Logging
    ###############################################################################
    logging.basicConfig(level=logging.DEBUG)
    logger  = logging.getLogger("FaceIn")

    #
    # Face Detector
    ###############################################################################
    # opencv:     OpenCvWrapper.build_model,
    # ssd:        SsdWrapper.build_model,
    # dlib:       DlibWrapper.build_model,
    # mtcnn:      MtcnnWrapper.build_model,
    # retinaface: RetinaFaceWrapper.build_model   
    tic = time.perf_counter() 
    face_detector = FaceDetector.build_model(detector_backend)
    toc = time.perf_counter()
    logger.log(logging.INFO, "Detector backend {} loaded in {}s".format(detector_backend, toc))

    #
    # Camera
    ###############################################################################
    # Scan up to 3 cameras
    camera_index=findCamera(3,fourccSig,widthSig,heightSig)
    # Create camera interface based on computer OS you are running
    plat = platform.system()
    if plat == 'Linux' and platform.machine() == "aarch64": # this is jetson nano for me
            from camera.capture.nanocapture import nanoCapture
            camera = nanoCapture(configs, camera_index)
    else:
        from camera.capture.cv2capture import cv2Capture
        camera = cv2Capture(configs, camera_index)

    logger.log(logging.INFO, "Starting Capture Thread")
    camera.start()
    
    #
    # Initialize Variables for Main Loop
    ###############################################################################

    freeze               = False
    face_detected        = False
    face_included_frames = 0 
    freezed_frame        = 0
    stopped              = False

    window_name          = 'Camera'
    window_handle        = cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE) # or WINDOW_NORMAL

    last_display_time    = time.perf_counter()
    last_fps_time        = time.perf_counter()
    loop_time            = 0
    face_detect_time     = 0
    num_imgs             = 0

    #
    # Main Loop
    ###############################################################################

    while (not stopped):
        # keep track of time
        current_time = time.perf_counter()

        # Obtain Image
        ##############
        (img_time, img) = camera.capture.get(block=True, timeout=None)
        while not camera.log.empty():
            (level, msg) = camera.log.get_nowait()
            logger.log(level, "{}".format(msg))

        # Display
        ##########
        if (current_time - last_display_time) >= display_interval:
            last_display = current_time

            # make copy of current image, 
            # do not change current camera
            display_img = img.copy()
            
            # Detect Faces
            ##############
            if freeze == False:
                tic_facedetect = time.perf_counter()
                faces = FaceDetector.detect_faces(face_detector, detector_backend, img, align = False)
                toc_facedetect = time.perf_counter()
                face_detect_time += (toc_facedetect - tic_facedetect)
                num_imgs += 1                
                # discard small detected faces
                detected_faces = []
                face_index = 0
                for face, (x, y, w, h) in faces:
                    if w > minimum_face_width :
                        detected_face = img[int(y):int(y+h), int(x):int(x+w)]   # crop detected face
                        detected_faces.append((x,y,w,h))
                        face_index += 1
                        cv2.rectangle(display_img, (x,y), (x+w,y+h), (67,67,67), 1)     # draw rectangle to display image
                        cv2.putText(display_img, str(frame_threshold - face_included_frames), (int(x+w/4),int(y+h/1.5)), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2)

                if face_index > 0: face_included_frames += 1

                if face_included_frames >= frame_threshold:
                    freeze = True
                    face_included_frames = 0
                    freeze_start = True
                    detected_faces_final = detected_faces.copy()
                    tic_freeze = time.perf_counter()

                # show current image
                ####################
                cv2.imshow(window_name,display_img)

            # Freeze Detected Face
            ######################
            if freeze == True:
                toc_freeze = time.perf_counter()
                if (toc_freeze - tic_freeze) < freeze_time:
                    # at beginning of freeze update display
                    if freeze_start:
                        freeze_start = False
                        freeze_img = img.copy()
                        for detected_face in detected_faces_final:
                            x = detected_face[0]; y = detected_face[1]
                            w = detected_face[2]; h = detected_face[3]
                            cv2.rectangle(freeze_img, (x,y), (x+w,y+h), (67,67,67), 1) # draw rectangled around faces
                        
                    time_left = (freeze_time- (toc_freeze - tic_freeze))
                    display_img = freeze_img.copy()
                    cv2.rectangle(display_img, (10, 10), (100, 50), (67,67,67), -10)
                    cv2.putText(display_img, "{:.1f}".format(time_left), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

                    # show current image
                    ####################
                    cv2.imshow(window_name,display_img)
                else:
                    # releae freeze
                    face_detected = False
                    face_included_frames = 0
                    freeze = False
                    freezed_frame = 0
                         
        # Check for User input
        if cv2.waitKey(1) & 0xFF == ord('q'): stopped = True
        if cv2.getWindowProperty(window_name, 0) < 0: stopped = True

        # Update performance metrics
        if (current_time - last_fps_time) >= dps_measure_time:
            if num_imgs > 0:
                face_detect_time = face_detect_time/num_imgs
                logger.log(logging.INFO, "Face dection time:{:.1f}ms".format(1000.*face_detect_time))
                face_detect_time = 0
                num_imgs =0 
            last_fps_time = current_time
            logger.log(logging.INFO, "Loop time left:{:.1f}ms".format(1000.*(loop_time-dps_measure_time)))
            loop_time = 0
            
        loop_time += (time.perf_counter()-current_time)

# Clean up and Release handle to window
#######################################
camera.stop()
cv2.destroyAllWindows()
