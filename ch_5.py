# saving an image or writing image

import cv2 as cv
from cv2 import threshold
from cv2 import imwrite
img = cv.imread("resources/s_image.jpeg")
img=cv.resize(img,(500,600))
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # cvt color means convert color
(thresh, binary)=cv.threshold(grey,127,255,cv.THRESH_BINARY)
imwrite('resources/Imaage_grey.png',grey)
imwrite('resources/Imaage_b_n_w.png',binary)
cv.waitKey(0)
cv.destroyAllWindows()