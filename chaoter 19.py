#coordinates of an image and video
#step1 import lib...
from asyncio import events
import cv2 as cv
import numpy as np
#define function
#step 2
def find__cord(event,x,y,flags,params):
    #left mouse button
    if events == cv.EVENT_LBUTTONDOWN:
        print(x,'',y)
        #define or print same image in widow
        font = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img,str(x)+','+str(y),(x,y),font,1,(255,0,125),2)
        # show show text and image it self
        cv.imshow("resor/image",img)
        # for color finding
    if events == cv.EVENT_RBUTTONDOWN:
        print(x,'',y)
        font = cv.FONT_HERSHEY_COMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img,str(b)+','+str(g)+','+str(r),(x,y),font,1,(255,0,125),2)
        cv.imshow("image",img)
        #final funtion to display
        #step 3
if __name__=="__main__":
    #reading image
    img = cv.imread("resor/image.png",1)
    #display image
    cv.imshow("image",img)
    #setting call back funtion
    cv.setMouseCallback("image",find__cord)
    cv.waitKey(0)
    cv.destroyAllWindows()
