#!pip install deepface

import cv2
import os
import time
from numba import jit
from deepface import DeepFace
import matplotlib.pyplot as plt

print("Program started successfully")
cap = cv2.VideoCapture(0)

cascade_path = os.path.join(
    cv2.data.haarcascades,
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(cascade_path)
pTime = 0   # for FPS


while True:
    
    success, img = cap.read()# read the video 

    if success == True:
        img = cv2.resize(img, None, None, fx=0.5, fy=0.5)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        
        predictions = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False) 
        
        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        

        #rectangle for faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        
        emotion = predictions[0]['dominant_emotion']

        cv2.putText(img, emotion, (30,30),
            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)

        cv2.imshow("Imagefinal",cv2.putText(img, f'FPS: {int(fps)}',(30,50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255),1) )
            
        k = cv2.waitKey(1) & 0xff
        if k==27:
            break
cap.release()
cv2.destroyAllWindows()


    
  #cv2.waitKey(28)