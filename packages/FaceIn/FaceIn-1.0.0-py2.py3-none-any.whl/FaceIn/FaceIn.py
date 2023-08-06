###############################################################################
# Face In 
# Classroom and Laboratory visual attendance sign in.
# Based on code from https://github.com/serengil/deepface
#
# Urs Utiznger
# 2022 January - initial release
###############################################################################

###############################################################################
# Imports
###############################################################################

import platform         # To load correct camera driver
import logging          # Logging
import time             # Execution handling
import os               # To adapt to different operating system
import pickle           # To convert to byte stream
import re
import tkinter as tk
from datetime import datetime

# Camera
from camera.utils import findCamera, genCapture

# OpenCV
import cv2

# Deepface
from deepface import DeepFace
from deepface.extendedmodels import Age
from deepface.commons import functions, distance
from deepface.detectors import FaceDetector

from tensorflow.keras.preprocessing import image

import numpy as np

###############################################################################
# Settings
###############################################################################

# Folder where modesl are stored
# os.environ['DEEPFACE_HOME'] = os.getcwd()

# Face Recognition
###########################################################################################
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
detector_backend        = "retinaface"  # opencv*, ssd, mtcnn, dlib, retinaface
freeze_time             = 5         # how many second analyzed image will be displayed, 5*
frame_threshold         = 5         # how many frames required to focus on a face, 5*
minimum_face_width      = 180       # filter out small faces
###########################################################################################
# Computation time in ms, rtx notebook          works with   worsk with       works with
#                                               glasses      obstructions     facemasks
# Retinaface: 233, 224, 225, 229, 172, 216      yes          yes              yes
# OpenCV:     46,42,44,56,40                    no           no               no
# SSD:        30,21,21,20,21,20,20,20,19        yes          yes              no
# MTCNN:      3125,873,1029,973,1265,868,945    yes          yes              no
# DLIB:       352,350,346,346,347               yes          no               no
###########################################################################################

model_name              = "ArcFace"     # VGG-Face*, Facenet, OpenFace, DeepFace, DeepID, Dlib, ArcFace or Ensemble
distance_metric         = "cosine"      # cosine*, euclidean, euclidean_l2
datafile                = "./database/bme210_2022Spring.dat"
db_path                 = "./database"  # Folder for .jpg files of known faces
enable_face_analysis    = True          # Enables Age, Gender, Emotion and Race
if os.path.isdir(db_path) == True:  
    logfile = db_path + "/" + "attend.log"
########################################################

# Camera
###################################
configs = {
    'camera_res'      : (1280, 720 ),   # width & height11111111111111
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
    'displayfps'       : 4              # frame rate for display server
}

if configs['displayfps'] >= configs['fps']:  display_interval = 0
else:                                        display_interval = 1.0/configs['displayfps']

# Internal Labtop Camera Signature
###################################
widthSig = 640
heightSig = 480
fourccSig = "\x16\x00\x00\x00"

# Other
#######
dps_measure_time = 5 # seconds

###########################################################################################
# Functions
###########################################################################################

def clamp(val, smallest, largest): return max(smallest, min(val, largest))

def image2facetensor(img,face_loc, input_shape):
# takes face roi, resizes and pads to model input shape and creates tensor    
    x = face_loc[0]; y = face_loc[1]
    w = face_loc[2]; h = face_loc[3]
    face = img[y:y+h,x:x+w,:]
    # scale  image to model shape
    factor_0 = input_shape[1] / face.shape[0]
    factor_1 = input_shape[0] / face.shape[1]
    factor = min(factor_0, factor_1)
    dsize = (int(face.shape[1] * factor), int(face.shape[0] * factor))
    face_resized = cv2.resize(face, dsize)
    # center the image and pad with black pixels
    diff_y = input_shape[1] - face_resized.shape[0]
    diff_x = input_shape[0] - face_resized.shape[1]
    face_scaled = np.pad(face_resized, ((diff_y // 2, diff_y - diff_y // 2), (diff_x // 2, diff_x - diff_x // 2), (0, 0)), 'constant')                    
    # prepare the image tensor
    face_tensor = image.img_to_array(face_scaled) 
    face_tensor = np.expand_dims(face_tensor, axis = 0)
    face_tensor /= 255 #normalize input in [0, 1]
    return face_tensor

def matchface(embedding, embeddings, metric):
# compares face_representation to embeddings database
    min_distance = 1000 # very large distances
    min_index = 0
    for indx in range(len(embeddings)): 
        embedding = embeddings[indx]
        if   metric == 'cosine':       d = distance.findCosineDistance(                         face_representation,                        embedding[1])
        elif metric == 'euclidean':    d = distance.findEuclideanDistance(                      face_representation,                        embedding[1])
        elif metric == 'euclidean_l2': d = distance.findEuclideanDistance(distance.l2_normalize(face_representation), distance.l2_normalize(embedding[1]))
        if d < min_distance:
            min_index = indx
            min_distance = d
    return min_index

def overlaymatch(img, candidate_img, pivot_size, face_loc, text, opacity):
# places matched face as overlay onto recorded image
    # resize to match pivot size
    factor_0 = pivot_size / candidate_img.shape[0]
    factor_1 = pivot_size / candidate_img.shape[1]
    factor = min(factor_0, factor_1)
    dsize = (int(candidate_img.shape[1] * factor), int(candidate_img.shape[0] * factor))
    candidate_img = cv2.resize(candidate_img, dsize)
    pivot_size_x = candidate_img.shape[1]
    pivot_size_y = candidate_img.shape[0]
    x = face_loc[0]; y = face_loc[1]
    w = face_loc[2]; h = face_loc[3]
    text_box = np.full((20,pivot_size_x,3),boxBackground,dtype=img.dtype)
    # display candidate onto image
    if y - pivot_size_y >= 0 and x + w + pivot_size_x < width: # top right
        img[y - pivot_size_y:y, x+w:x+w+pivot_size_x] = candidate_img
        img[y:y+20,x+w:x+w+pivot_size_x,:] = img[y:y+20,x+w:x+w+pivot_size_x,:] * (1.-opacity) + text_box * opacity 
        cv2.putText(img, text, (x+w, y+10), font, 0.5*fontScale, fontColor, fontThickness)
        cv2.line(img, (x+int(w/2), y), (x+3*int(w/4), y-int(pivot_size_y/2)), borderColor,1)
        cv2.line(img, (x+3*int(w/4), y-int(pivot_size_y/2)), (x+w, y-int(pivot_size_y/2)), borderColor,1)
    elif y + h + pivot_size < height and x - pivot_size >= 0: # bottom left
        img[y+h:y+h+pivot_size_y, x-pivot_size_x:x] = candidate_img
        img[y+h-20:y+h,x-pivot_size_x:x,:] = img[y+h-20:y+h,x-pivot_size_x:x,:] * (1.-opacity) + text_box * opacity 
        cv2.putText(img, text, (x - pivot_size_x, y+h-10), font, 0.5*fontScale, fontColor, fontThickness)
        cv2.line(img, (x+int(w/2), y+h), (x+int(w/2)-int(w/4), y+h+int(pivot_size_y/2)), borderColor,1)
        cv2.line(img, (x+int(w/2)-int(w/4), y+h+int(pivot_size_y/2)), (x, y+h+int(pivot_size_y/2)), borderColor,1)
    elif y - pivot_size_y >= 0 and x - pivot_size_x >= 0: # top left
        img[y-pivot_size_y:y, x-pivot_size_x:x] = candidate_img
        img[y:y+20,x-pivot_size_x:x,:] = img[y:y+20,x-pivot_size_x:x,:] * (1-opacity) + text_box * opacity  
        cv2.putText(img, text, (x - pivot_size_x, y+10), font, 0.5*fontScale, fontColor, fontThickness)
        cv2.line(img, (x+int(w/2), y), (x+int(w/2)-int(w/4), y-int(pivot_size_y/2)), borderColor,1)
        cv2.line(img, (x+int(w/2)-int(w/4), y-int(pivot_size_y/2)), (x, y-int(pivot_size_y/2)), borderColor,1)
    elif x+w+pivot_size_x < width and y + h + pivot_size_y < height: # bottom right
        img[y+h:y+h+pivot_size_y, x+w:x+w+pivot_size_x] = candidate_img
        img[y+h-20:y+h,x+w:x+w+pivot_size_x,:] = img[y:y+20,x-pivot_size_x:x,:] * (1.-opacity) + text_box * opacity 
        cv2.putText(img, text, (x+w, y+h-10), font, 0.5*fontScale, fontColor, fontThickness)
        cv2.line(img, (x+int(w/2), y+h), (x+int(w/2)+int(w/4), y+h+int(pivot_size_y/2)), borderColor,1)
        cv2.line(img, (x+int(w/2)+int(w/4), y+h+int(pivot_size_y/2)), (x+w, y+h+int(pivot_size_y/2)), borderColor,1)
    return img

def entername():
# ask for user fist and last name
    tkFirstField.delete(0, tk.END)
    tkLastField.delete(0, tk.END)
    tkFrame.tkraise()
    tkFrame.attributes("-topmost", True)
    tkFrame.wait_variable(tkEnterButtonVar)
    tkFrame.attributes("-topmost", False)
    firstName = tkFirstField.get()
    lastName  = tkLastField.get()
    return firstName, lastName

def createknownfaceimage(firstName,lastName,db_path,face_loc,img):
# stores found face as new known face
    full_dirname = db_path + "/" + firstName + "_" + lastName
    if os.path.isdir(full_dirname) == False:
        os.mkdir(full_dirname)
    number_files = len(os.listdir(full_dirname))
    filename = firstName + "_" + lastName + "{:03d}".format(number_files+1) + ".jpg"
    participant = full_dirname + "/" + filename
    x = face_loc[0]; y = face_loc[1]
    w = face_loc[2]; h = face_loc[3]
    height  = img.shape[0]
    width   = img.shape[1]
    extra_h = int(0.5*h)
    extra_w = int(0.4*w)
    y_start = y-extra_h
    y_end   = y+h+extra_h
    x_start = x-extra_w
    x_end   = x+w+extra_w
    y_start = clamp(y_start, 0, height-1)
    x_start = clamp(x_start, 0, width-1)
    y_end   = clamp(y_end, 0, height-1)
    x_end   = clamp(x_end, 0, width-1)
    new_face = img[y_start:y_end, x_start:x_end]
    cv2.imwrite(participant, new_face)

if __name__ == "__main__":
    """
    FaceIn:
    Classroom and laboratory visual attendance sign in.
    Urs Utzinger 2022
    Based on https://github.com/serengil/deepface commons/realtime.py
    """
    
    plat = platform.system()
    if plat == 'Windows': import win32gui

    #
    # Logging
    # #############################################################################################################
    logging.basicConfig(level=logging.ERROR)
    logger  = logging.getLogger("FaceIn")

    #
    # Face Detector
    # #############################################################################################################
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
    # Face Model
    # #############################################################################################################
    # VGG-Face:   VGGFace.loadModel,
    # OpenFace:   OpenFace.loadModel,
    # Facenet:    Facenet.loadModel,
    # Facenet512: Facenet512.loadModel,
    # DeepFace:   FbDeepFace.loadModel,
    # DeepID:     DeepID.loadModel,
    # Dlib:       DlibWrapper.loadModel,
    # ArcFace:    ArcFace.loadModel,
    # Emotion:    Emotion.loadModel,
    # Age:        Age.loadModel,
    # Gender:     Gender.loadModel,
	# Race:       Race.loadModel
    face_model = DeepFace.build_model(model_name)
    logger.log(logging.INFO, "{} is built.".format(model_name))
    # required image shape
    input_shape = functions.find_input_shape(face_model)
    # tuned thresholds for model and metric pair
    distance_threshold = distance.findThreshold(model_name, distance_metric)

    #
    # Known Face Database
    # #############################################################################################################
    # This file was created with FaceIn_AddDirectory.py
    # It contains analsis features of previously seen faces
    with open(datafile, "rb") as file: embeddings = pickle.load(file)

    #
    # Camera
    # #############################################################################################################
    # Scan up to 3 cameras
    camera_index=findCamera(3,fourccSig,widthSig,heightSig)
    # Create camera interface based on computer OS you are running
    camera = genCapture(configs, camera_index)
    logger.log(logging.INFO, "Starting Capture Thread")
    camera.start()
    
    #
    # Name Input Window
    # #############################################################################################################
    tkFrame = tk.Tk()
    tkFrame.configure(background='grey80') 
    tkFrame.title("Face In Name")
    # First and Lastname
    tk.Label(tkFrame, text="First Name",font=("Arial", 16),background='grey80').grid(row=0, column=0)
    tk.Label(tkFrame, text="Last Name",font=("Arial", 16),background='grey80').grid(row=1, column=0)
    tkFirstField=tk.Entry(tkFrame,font=("Arial", 24),background='grey90')
    tkFirstField.grid(row=0,column=1)
    tkLastField=tk.Entry(tkFrame,font=("Arial", 24),background='grey90')
    tkLastField.grid(row=1,column=1)
    # Enter Button
    tkEnterButtonVar = tk.IntVar()
    tkEnterButton    = tk.Button(tkFrame, 
                                 text    = "Submit",
                                 font    = ("Arial", 16),
                                 bg      = 'gray90',
                                 command =lambda:tkEnterButtonVar.set(1))
    tkEnterButton.grid(row=2, columnspan=2, pady=5)

    #
    # Initialize Variables
    # #############################################################################################################
    freeze               = False
    face_detected        = False
    face_included_frames = 0 
    freezed_frame        = 0
    stopped              = False
    acknowledgement      = False
    register             = False
    pivot_size           = 112           # face recognition successful match image

    window_name          = 'Face In'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE) # or WINDOW_NORMAL
    # cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
    height               = camera.height
    width                = camera.width
    font                 = cv2.FONT_HERSHEY_SIMPLEX
    fontScale            = 1
    fontColor            = (255,255,255)
    fontColorDark        = (0,0,0)
    fontThickness        = 1
    lineThickness        = 1
    boxBackground        = (0,180,20)
    boxBackgroundCt      = (100,100,100)
    borderColor          = (0,180,20)
    opacity              = 0.2
 
    last_display_time   = last_fps_time                        = time.perf_counter()
    loop_time           = face_detect_time                     = 0
    num_imgs                                                   = 0
    toc_freeze          = toc_freezestart    = toc_nofreeze    = 0
    tic_freeze          = tic_freezestart    = tic_nofreeze    = 0
    freeze_tictoc       = freezestart_tictoc = facefind_tictoc = 0

    #
    # Main Loop
    # #############################################################################################################

    while (not stopped):
        # keep track of time
        current_time = time.perf_counter()

        # Obtain Image
        ###########################################################################################################
        (img_time, img) = camera.capture.get(block=True, timeout=None)
        while not camera.log.empty():
            (level, msg) = camera.log.get_nowait()
            logger.log(level, "{}".format(msg))

        # Update Display 
        ###########################################################################################################
        if (current_time - last_display_time) >= display_interval:
            last_display = current_time

            
            # Detect Faces
            #######################################################################################################
            if freeze == False:
                tic_nofreeze = time.perf_counter()

                display_img = img.copy()

                tic_facedetect = time.perf_counter()
                faces = FaceDetector.detect_faces(face_detector, detector_backend, img, align = False)
                toc_facedetect = time.perf_counter()
                face_detect_time += (toc_facedetect - tic_facedetect)
                num_imgs += 1
                
                # Determine Foreground Face
                ###########################
                detected_faces = []
                face_index = -1
                largest_width = 0
                foreground_face = 0   
                for face, (x, y, w, h) in faces:
                    face_index += 1
                    # display all faces in the image
                    cv2.rectangle(display_img, (x,y), (x+w,y+h), borderColor, lineThickness)     # draw rectangle to display image
                    if w > minimum_face_width :
                        # find foreground face
                        if w > largest_width:
                            largest_width = w
                            foreground_face_index = face_index
                # mark foreground face
                face, (x, y, w, h) = faces[foreground_face_index]
                cv2.rectangle(display_img, (x,y), (x+w,y+h), borderColor, 3*lineThickness)     # draw rectangle to display image
                cv2.putText(display_img, str(frame_threshold - face_included_frames), (int(x+w/4),int(y+h/1.5)), font, 4*fontScale, fontColor, 2*fontThickness)
                        
                # Make sure we found a face in multiple subsequent frames
                #########################################################
                if face_index > -1: face_included_frames += 1

                # Get Ready for Face Matching
                #############################
                if face_included_frames >= frame_threshold:
                    freeze          = True
                    face_included_frames = 0
                    freeze_start    = True
                    foreground_face = (x, y, w, h)
                    freeze_img      = img.copy() # will draw on this one
                    unaltered_img   = img.copy() # keep unaltered image
                    tic_freezewait  = time.perf_counter()

                # show current image
                ####################
                cv2.imshow(window_name,display_img)
                
                toc_nofreeze = time.perf_counter()
                facefind_tictoc = 1000*(toc_nofreeze - tic_nofreeze)

            # Freeze Detected Face
            #######################################################################################################
            if freeze == True:
                tic_freeze = time.perf_counter()

                toc_freezewait = time.perf_counter()
                if (toc_freezewait - tic_freezewait) < freeze_time:
                    
                    # Keep image frozen
                    ###############################################################################################

                    # Do once at beginning
                    # ####################
                    if freeze_start:
                        tic_freezestart = time.perf_counter()                        
                        freeze_start = False

                        # Check who it is
                        #################
                        # Calc face representation
                        face_tensor=image2facetensor(unaltered_img, foreground_face, input_shape)           
                        face_representation = face_model.predict(face_tensor)[0,:]
                        # Find best match
                        min_index = matchface(face_representation, embeddings, distance_metric)
                        # Candidate
                        participant         = embeddings[min_index][0]
                        candidate           = re.sub('[0-9]', '',participant.split("/")[-1].replace(".jpg", "")) # remove numbers, filesuffix and folder info
                        candidate_firstname = candidate.split("_")[-2]
                        candidate_lastname  = candidate.split("_")[-1]
                        candidate_img = cv2.imread(participant)
                        # Create blank if image not found
                        if candidate_img.shape[0] == 0 or candidate_img.shape[1] == 0: candidate_img = np.zeros((pivot_size,pivot_size,3), np.unit8)
                        # Create image with match overlay
                        freeze_img = overlaymatch(freeze_img, candidate_img, pivot_size, foreground_face, candidate_lastname, opacity)
                        toc_freezestart = time.perf_counter()
                        freezestart_tictoc = 1000*(toc_freezestart - tic_freezestart)

                    # Count down on frozen image
                    ############################
                    time_left = (freeze_time- (toc_freezewait - tic_freezewait))
                    display_img = freeze_img.copy()
                    overlay     = display_img.copy()
                    text_box1   = np.full((40, 90,3),boxBackgroundCt,dtype=img.dtype)
                    text_box2   = np.full((40,740,3),boxBackgroundCt,dtype=img.dtype)
                    display_img[10:50, 10:100,:] = display_img[10:50, 10:100,:] * (1.-opacity) + text_box1 * opacity
                    display_img[55:95, 10:750,:] = display_img[55:95, 10:750,:] * (1.-opacity) + text_box2 * opacity                    
                    cv2.putText(display_img, "{:.1f}".format(time_left), (40, 40), font, fontScale, fontColor, fontThickness)
                    cv2.putText(display_img, "{}".format("Space to approve, Enter to register new"), (40, 90), font, fontScale, fontColorDark, fontThickness)
                            
                    # Show current image
                    ####################
                    cv2.imshow(window_name,display_img)

                    # Did user acknowledged?
                    ###############################################################################################
                    if acknowledgement:
                        acknowledgement = False
                        # stop freeze
                        face_detected = False
                        face_included_frames = 0
                        freeze = False
                        freezed_frame = 0 
                        # yes: add date/time to user records
                        now = datetime.now()
                        with open(logfile, "a") as file: file.write("{}, {}\n".format(candidate, now.strftime("%Y/%m/%d, %H:%M:%S")))
                        
                    # Did user register as new?
                    ###############################################################################################
                    elif register:
                        register = False
                        # ask for user name
                        firstName, lastName = entername()
                        if (len(firstName) + len(lastName)) == 0:
                            firstName = "Jane"
                            lastName  = "Doe"
                        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1) # auto set opncv window to forground
                        if plat == 'Windows': win32gui.SetActiveWindow(win32gui.FindWindow(window_name, None)) # auto activate window
                        createknownfaceimage(firstName, lastName, db_path, foreground_face, unaltered_img)
                        # append face representation to embeddings and save file
                        embedding = [participant, face_representation]
                        embeddings.append(embedding)
                        with open(datafile, "wb") as file: pickle.dump(embeddings, file)
                        # release freeze
                        face_detected = False
                        face_included_frames = 0
                        freeze = False
                        freezed_frame = 0
                    
                # release freeze
                else:
                    face_detected = False
                    face_included_frames = 0
                    freeze = False
                    freezed_frame = 0
                
                toc_freeze = time.perf_counter()
                freeze_tictoc = 1000*(toc_freeze - tic_freeze)
                                
        # Check for User input
        # ##########################################################################################################
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):                             stopped         = True
        if key == ord(' '):                             acknowledgement = True
        if key == ord('\r'):                            register        = True            
        if cv2.getWindowProperty(window_name, 0) < 0:   stopped         = True

        # Update performance metrics
        # ##########################################################################################################
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
                
        print("Freeze: {:.1f}, Freezestart: {:.1f}, no Freeze: {:.1f}".format(freeze_tictoc, freezestart_tictoc,  facefind_tictoc))
        
# Clean up and Release handle to window
# ##################################################################################################################
camera.stop()
cv2.destroyAllWindows()
