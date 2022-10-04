#converting video into gray shape
import cv2 as cv
import numpy as np
cap=cv.VideoCapture("resor/vid.k.mp4")
#indicater
if (cap.isOpened()==False):
    print("error in video")
while (True):
    (ret,frame)=cap.read()
    grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret==True:
        cv.imshow("video",grayframe)
        if cv.waitKey(1)&0xff==ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
