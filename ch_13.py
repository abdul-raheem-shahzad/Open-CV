# basic function and manipulations

import cv2 as cv
from cv2 import imread
import numpy as np
img = cv.imread('resources/s_image.jpeg')

# first function: rezie
resized_img = cv.resize(img,(450,250))

# gray
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blurred image
blurr_img = cv.GaussianBlur(img,(29,29),0)

# edge detection:
edge_img = cv.Canny(img,53,53)

# thicjkness of lines
# edge ko detect kana ka baad us kai thickness change karna
mat_kernal = np.ones((3,3),np.uint8)
dialted_img =cv.dilate(edge_img, (mat_kernal), iterations=3)

# erostion ( thiner outline)
ero_img = cv.erode(dialted_img,mat_kernal,iterations=1)

# cropping
# we will use numpy library not 
print('the size of our image is:',img.shape)
cropped_img = resized_img[0:200,200:300]


cv.imshow("origmal:",img)
# cv.imshow("resized:",resized_img)
# cv.imshow("grey:",gray_img)
#cv.imshow("blurr:",blurr_img)
# cv.imshow("edge:",edge_img)
# cv.imshow("dialted:",dialted_img)
#cv.imshow('erosion',ero_img)
cv.imshow('cropping',cropped_img)
cv.waitKey(0)
cv.destroyAllWindows() 
