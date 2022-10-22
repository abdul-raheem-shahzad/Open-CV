# convert webcam into black and white and grey

import cv2 as cv
from cv2 import destroyAllWindows
import numpy as np

cap=cv.VideoCapture(0)

while(True):
    (ret, frame)=cap.read()
    gray_frame =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh, binary)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)
    cv.imshow('orignal cam',frame)
    cv.imshow('grey cam',gray_frame)
    cv.imshow('binary balck and white cam',binary)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()