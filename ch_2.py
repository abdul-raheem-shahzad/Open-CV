#reading an image and displaying it
import cv2 as cv
from cv2 import resize

img=cv.imread("resources/s_image.jpeg")
img=cv.resize(img,(500,600))
cv.imshow("pehli image",img)
cv.waitKey(0)
