#reading an image and displaying it
import cv2 as cv

img=cv.imread("resources/s_image.jpeg")
cv.imshow("pehli image",img)
cv.waitKey(0)