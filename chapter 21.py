#how to detect specific color inside image 
    # OR
#changing color in an image
import cv2 as cv
from cv2 import imshow
import numpy as np

#img = cv.imread("resor/image.png")
#hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
def slider():
  pass
path = "resor/image.png"
cv.namedWindow("Bars")
cv.resizeWindow("Bars",600,300)
cv.createTrackbar("Hue Min","Bars",0,179,slider)
cv.createTrackbar("Hue Max","Bars",179,179,slider)
cv.createTrackbar("Sat Min","Bars",0,255,slider)
cv.createTrackbar("Sat Max","Bars",255,255,slider)
cv.createTrackbar("Val Min","Bars",0,255,slider)
cv.createTrackbar("Val Max","Bars",255,255,slider)
img = cv.imread(path)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#HUE_MIN = cv.getTrackbarPos("HUE MIN","BARS")
#print (HUE_MIN)
while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min","Bars")
    hue_max = cv.getTrackbarPos("Hue Max", "Bars")
    sat_min = cv.getTrackbarPos("Sat Min", "Bars")
    sat_max = cv.getTrackbarPos("Sat Max", "Bars") 
    val_min = cv.getTrackbarPos("Val Min", "Bars")
    val_max = cv.getTrackbarPos("Val Max", "Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])
    mask_img = cv.inRange(hsv_img,lower,upper)
    out_img = cv.bitwise_and(img,img,mask=mask_img)
    #cv.imshow("original",img)
    #cv.imshow("HSV",hsv_img)
    cv.imshow("MASK",mask_img)
    cv.imshow("FINAL output",out_img)
    if cv.waitKey(1)&0xff==ord("q"):
        break
#cv.imshow("ori",img)
#cv.imshow("hsc",hsv_img)
#cv.waitKey(0)
cv.destroyAllWindows()

    




