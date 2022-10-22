
from msilib.schema import Binary
import cv2 as cv
from cv2 import resize
from cv2 import imread
from cv2 import waitKey
from cv2 import cvtColor
# img = imread("resources/s_image.jpeg")
# img = resize(img,(500,700))
# g_im = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# (thresh,binary) = cv.threshold(g_im,150,255,cv.THRESH_BINARY)
# cv.imshow('practivd',img)
# cv.imshow('practivd_1_grey',g_im)
# cv.imshow('binary)image',binary)
# waitKey(0)
cap = cv.VideoCapture('resources/video.mp4')

if (cap.isOpened()==False):
    print('erro in video loading')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cv.imshow('video',frame)
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
        else:
            break
cap.release()
cv.destroyAllWindows()