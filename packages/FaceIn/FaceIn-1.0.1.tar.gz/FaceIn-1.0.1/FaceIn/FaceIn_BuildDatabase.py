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
import pickle           # To convert to byte stream
import logging          # Logging
from   tqdm import tqdm # Progress bar
import time             # Execution handling
import re               # Regular expression
import os               # To adapt to different operating system

#from datetime     import datetime, timedelta
#from screeninfo   import get_monitors

import numpy as np      # Matrix algebra
import pandas as pd     # Data handling

# Camera
from camera.utils import probeCameras

# OpenCV
import cv2

# Deepface
from deepface import DeepFace
from deepface.extendedmodels import Age
from deepface.commons import functions, distance as dst
from deepface.detectors import FaceDetector

from tensorflow.keras.preprocessing import image

###############################################################################
# Settings
###############################################################################

# Face Recognition
###################################
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
db_path                 = "./database"  # Folder for .jpg files of known faces
model_name              = "ArcFace"     # VGG-Face*, Facenet, OpenFace, DeepFace, DeepID, Dlib or Ensemble
detector_backend        = "retinaface"  # opencv*, ssd, mtcnn, dlib, retinaface
distance_metric         = "cosine"      # cosine*, euclidean, euclidean_l2
enable_face_analysis    = True          # Set this to False to just run face recognition, True*
time_threshold          = 5             # how many second analyzed image will be displayed, 5*
frame_threshold         = 5             # how many frames required to focus on face, 5*
minimum_face_width      = 130           # filter out small faces
datafile                = "./database/bme210_2022Spring.dat"

if __name__ == "__main__":
    """
    Create known Faces
    """

    #
    # Logging
    # #############################################################################################################

    logging.basicConfig(level=logging.DEBUG)
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
    face_model = DeepFace.build_model(model_name)
    logger.log(logging.INFO, "{} is built.".format(model_name))
    input_shape = functions.find_input_shape(face_model)
    input_shape_x = input_shape[0]
    input_shape_y = input_shape[1]
    target_size = (input_shape_y, input_shape_x)
    # tuned thresholds for model and metric pair
    threshold = dst.findThreshold(model_name, distance_metric)

    #
    # Known Face Database
    # #############################################################################################################
    participants = []
    #check passed db folder exists
    if os.path.isdir(db_path) == True:
        for r, d, f in os.walk(db_path): # r=root, d=directories, f = files
            for file in f:
                if ('.jpg' in file):
                    candidate      = file.split("/")[-1].replace(".jpg", "")
                    candidate      = re.sub('[0-9]', '', candidate)
                    if os.path.isdir(db_path + "/" + candidate) == False:
                        # lets move the all files into sub folders
                        os.mkdir(r + "/" + candidate)
                        os.rename(r + "/" + file, r + "/" + candidate + "/" + file )
                        exact_path = r + "/" + candidate + "/" + file
                    else: 
                        exact_path = r + "/" + file
                    exact_path = exact_path.replace("\\", "/")
                    participants.append(exact_path)

    if len(participants) == 0:
        logger.log(logging.WARNING, "There is no image in ({}). Face recognition will not be perfromed.".format(db_path))

    #
    # Facial Features of known Participants
    # #############################################################################################################
    tic = time.perf_counter()
    pbar = tqdm(range(0, len(participants)), desc='Finding embeddings')
    embeddings = []
    #for participant in partcipants:
    for index in pbar:
        participant = participants[index]
        pbar.set_description("Finding embedding for %s" % (participant.split("/")[-1]))
        embedding = []
        
        img_participant = cv2.imread(participant)
        cv2.imshow("Face ondisk",img_participant)
        cv2.waitKey(1)

        face, region = FaceDetector.detect_face(face_detector, detector_backend, img_participant, align = True)

        #resize image to expected shape	
        if face.shape[0] > 0 and face.shape[1] > 0:
            factor_0 = target_size[0] / face.shape[0]
            factor_1 = target_size[1] / face.shape[1]
            factor = min(factor_0, factor_1)
        
            dsize = (int(face.shape[1] * factor), int(face.shape[0] * factor))
            img = cv2.resize(face, dsize)
            
            # Then pad the other side to the target size by adding black pixels
            diff_0 = target_size[0] - img.shape[0]
            diff_1 = target_size[1] - img.shape[1]
            # Put the base image in the middle of the padded image
            img = np.pad(img, ((diff_0 // 2, diff_0 - diff_0 // 2), (diff_1 // 2, diff_1 - diff_1 // 2), (0, 0)), 'constant')
            cv2.imshow("Face",img)
            cv2.waitKey(1)
            
        #double check: if target image is not still the same size with target.
        if img.shape[0:2] != target_size:
            img = cv2.resize(img, target_size)
            cv2.imshow("Face_NO",img)
            cv2.waitKey(1)

        #normalizing the image pixels
        img_Tensor = image.img_to_array(img) 
        img_Tensor = np.expand_dims(img_Tensor, axis = 0)
        img_Tensor /= 255 #normalize input in [0, 1]
        
        # img = functions.preprocess_face(img = participant, target_size = (input_shape_y, input_shape_x), enforce_detection = False, detector_backend = detector_backend)
        img_representation = face_model.predict(img_Tensor)[0,:]

        embedding.append(participant)
        embedding.append(img_representation)
        embeddings.append(embedding)

    toc = time.perf_counter()
    logger.log(logging.INFO,"Embeddings found for given data set in {} seconds.".format(toc-tic))

    with open(datafile, "wb") as file:
        pickle.dump(embeddings, file)

