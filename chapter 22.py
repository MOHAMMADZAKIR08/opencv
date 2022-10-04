# for face detection 
import cv2 as cv
import numpy as np
face_cascade = cv.CascadeClassifier("resor/haarcascade_frontalface_default.xml")
img = cv.imread("resor/image5.jpg")
img = cv.resize(img,(700,700))
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)#
faces = face_cascade.detectMultiScale(gray_img,1.1,4)
#draw triangle
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,155),2)

cv.imshow("ori",img)
cv.waitKey(0)
cv.destroyAllWindows()