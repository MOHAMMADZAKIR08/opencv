#joining two images 
import cv2 as cv 
import numpy as np

img = cv.imread("resor/image.jpg")
#img = cv.resize(img,(200,300))
#img = cv.resize(img(200,200)) # this line of code work perfect
    
#horizental image
hor_img = np.hstack((img,img))
#vertical image
ver_img = np.vstack((img,img))
cv.imshow("horizental image",hor_img)
cv.imshow("vertical image",ver_img)
cv.waitKey(0)
cv.destroyAllWindows()