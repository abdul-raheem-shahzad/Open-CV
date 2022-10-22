# how to capture a webcam in python

# step1 import librabries

import cv2 as cv
import numpy as np

# step2 read the frames from camera 

cap= cv.VideoCapture(0) # wen cam numer 1 will come 
#if i write (1) then 2nd web cam will come

# read until the end 
# step3: display the cam frame by frame

while(cap.isOpened()):
    # capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # to display frames
        cv.imshow('Frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
            break

# relese or cloase windows easliy
cap.release()
cv.destroyAllWindows()
         

