#converting video into gray shape
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter("resor/web1 video.avi",cv.VideoWriter_fourcc("M","J","P","G"),10,(frame_width,frame_height),isColor=False)
#indicate
if (cap.isOpened()==False):
    print("error in video")
while (True):
    (ret,frame)=cap.read()
    grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret==True:
        out.write (grayframe)# cv.imshow("gray",grayframe)
        cv.imshow("gray",grayframe)
       
        if cv.waitKey(1)&0xff==ord("q"):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
