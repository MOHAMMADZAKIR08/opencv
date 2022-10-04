#how to draw lines etc in open cv python 
from pickle import FALSE
from turtle import color
import cv2  as cv
import numpy as np 
img = np.zeros((600,600))#black
img1 = np.ones((600,600))#white
#print("the size of img is :",img.shape)
#adding color to the  canvas
colored_image=np.ones((600,600,3),np.uint8)#for adding color channel
colored_image[ : ]=255,0,500#to color all image
colored_image[100:200,200:300]=255,10,400# color specific part of img
#Adding llines
cv.line(colored_image,(100,250),(300,500),(255,0,222),93)#93 for line thicknes             
#          0R
cv.line(colored_image,(0,0),(colored_image.shape[0],colored_image.shape[1]),(255,0,1))
#Adding rectangle
cv.rectangle(colored_image,(100,250),(300,500),(255,0,222),93)#draw rectangle
cv.rectangle(colored_image,(100,250),(300,500),(255,0,10),cv.FILLED)#filled rectangle
#Adding circle
cv.circle(colored_image,(100,300),60,(255,0.100),3)#draw circle
cv.circle(colored_image,(100,150),60,(255,0,100),cv.FILLED)#filled circle
#Adding text
cv.putText(colored_image,"zakirnitro@gmail.com",(300,500),cv.FONT_HERSHEY_TRIPLEX,2,(255,0,1),9)

cv.imshow("photo",colored_image)
#cv.imshow("photo",img)
cv.waitKey(0)
cv.destroyAllWindows()

