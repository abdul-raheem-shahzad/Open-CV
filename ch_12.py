# setting of camera or video

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

cap.set(10, 500) # 10 is the key to set the vbrightness and 50 is the intensity of brughtness
cap.set(3, 10) # 3 for width
cap.set(4,10) # 4 is for height
while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('frame:',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
