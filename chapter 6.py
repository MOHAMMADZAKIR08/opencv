import cv2 as cv
import numpy as np
cap=cv.VideoCapture("resor/video.mp4")
#indicater
if (cap.isOpened()==False):
    print("error in video")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("video",frame)
        if cv.waitKey(1)&0xff==ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
