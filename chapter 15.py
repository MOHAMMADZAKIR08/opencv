import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)#video
def hd_resolution():#resolution function
    cap.set(10,100)#brightness
    cap.set(3,1280)    #weidth
    cap.set(4,720)#heigth
def sd_resolution():
    cap.set(10,100)
    cap.set(3,640)
    cap.set(4,480)
def fhd_resolution():
    cap.set(10,100)
    cap.set(3,1920)
    cap.set(4,1080)
#hd_resolution()
fhd_resolution()
#sd_resolution()
while(True):
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("videokkk",frame)
        if cv.waitKey(1)&0xff==ord("q"):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
