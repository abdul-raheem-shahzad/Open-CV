#reading an image and displaying it
from turtle import bgcolor
# library importing
import cv2 as cv
from cv2 import resize
from cv2 import cvtColor

# image reading
img=cv.imread("resources/s_image.jpeg")
img=cv.resize(img,(500,600))

# gray image
gray_image=cvtColor(img, cv.COLOR_BGR2GRAY)

#dispay code
cv.imshow("pehli image",img)
cv.imshow("dosri image",gray_image)
cv.waitKey(0)