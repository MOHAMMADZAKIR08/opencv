
from msilib.schema import Binary
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)

while(True):
    (ret,frame)=cap.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary)=cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)
    cv.imshow("original web camera",frame)
    cv.imshow("Graycamera",gray_frame)
    cv.imshow("Binarycamera",binary)
    if cv.waitKey(0)&0xff==ord("q"):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

     
