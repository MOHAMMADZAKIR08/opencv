#black and white image
import cv2 as cv
from cv2 import cvtColor
import numpy as np
img=cv.imread("resor/image.jpg")
img=cv.resize(img,(600,800))
gray_img=cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh_binary)=cv.threshold(gray_img,127,255,cv.THRESH_BINARY)#this code 
cv.imshow("pehli image",img)
cv.imshow("GRAY Image",gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
