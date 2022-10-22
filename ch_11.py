# writing videos from cam
import cv2 as cv
from cv2 import imshow
import numpy as np
from matplotlib.colors import is_color_like
cap = cv.VideoCapture(0)

# writing formats, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height =  int(cap.get(4))
out = cv.VideoWriter("resources/cam_gray_video.avi",cv.VideoWriter_fourcc('M','J','P','G'),10, (frame_width, frame_height),isColor=False)

while (True):
    (ret, frame)=cap.read()
    gray_frame =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    if ret == True:

        out.write(gray_frame)
        cv.imshow('Video',gray_frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()

