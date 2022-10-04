#capture web camera inside python

import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
if(cap.isOpened)==False:
    print("there is an error")
while (cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("frame",frame)
        if cv.waitKey(1)&0xff==ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()