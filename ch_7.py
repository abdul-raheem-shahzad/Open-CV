# converting a video to black n white
import cv2 as cv
from cv2 import imshow

cap = cv.VideoCapture('resources/video.mp4')

while (True):
    (ret, frame)=cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary)=cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
    if ret == True:
        cv.imshow('Video',binary)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break

cap.release()
cv.destroyAllWindows()

