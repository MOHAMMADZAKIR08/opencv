#basic function and manipulation in python
import cv2 as cv
import numpy as np
img=cv.imread("resor/image.jpg")
img=cv.resize(img,(600,800))# resize image
resize_img=cv.resize(img,(100,200)) #resize image
gray_image=gray_frame=cv.cvtColor(img,cv.COLOR_BGR2GRAY)#gray img
blur_image=cv.GaussianBlur(img,(13,13),0)#blur img
edge_detection=cv.Canny(img,48,48)#edge detection
dialated_img=cv.dilate(edge_detection,(53,53),iterations=1)#thicknes of lines in img
mat_kernal=np.ones((3,3),np.uint8)
dialated_img=cv.dilate(edge_detection,(mat_kernal),iterations=1)
ero_img=cv.erode(dialated_img,mat_kernal,iterations=1)#thinner outlines
print("the size of the img is",img.shape)
cropped_img=resize_img[0:200,0:200]#for photo cutting from x to y axis


cv.imshow("original",img)
cv.imshow("gray",gray_image)
cv.imshow("blur",blur_image)
cv.imshow("edge_img",edge_detection)
cv.imshow("dialated",dialated_img)
cv.imshow("ero img",ero_img)
cv.imshow("cropped img",cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()