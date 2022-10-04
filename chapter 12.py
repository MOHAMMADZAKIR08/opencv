#setting of camera and video
import cv2 as cv 
import numpy as np
cap= cv.VideoCapture(0)
cap.set(10,10)#10 for bribhtness
cap.set(3,720)#3 for width
cap.set(4,10)# 4 for height
while(True):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("frame",frame)
        if cv.waitKey(1)&0xff==ord("q"):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
