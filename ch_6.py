# reading a video
import cv2 as cv
from cv2 import imshow

cap = cv.VideoCapture('resources/video.mp4')

# indicator to check it si working or not
if (cap.isOpened()==False):
    print('error in uploading video')

# reading and playing
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break

cap.release()
cv.destroyAllWindows()

