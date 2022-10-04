#saving and image
import cv2 as cv
from cv2 import cvtColor
from cv2 import imwrite
from cv2 import imshow
import numpy as np
img=cv.imread("resor/image.jpg")
#img=cv.resize(img,(600,800))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)
binary=cv.resize(binary,(600,800))#save line
imwrite("resor/image_gray.jpg",gray))#save line

