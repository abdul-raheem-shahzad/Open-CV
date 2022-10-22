# convert an image to black and white

import cv2 as cv
from cv2 import threshold
img = cv.imread("resources/s_image.jpeg")
img=cv.resize(img,(500,600))
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

(thresh, binary)=cv.threshold(grey,127,255,cv.THRESH_BINARY)

cv.imshow('orignal:',img)
cv.imshow('grey:',grey)
cv.imshow('black and white:',binary)
cv.waitKey(0)
cv.destroyAllWindows()


