#file diplay
import cv2 as cv
img=cv.imread("resor/image.jpg")
cv.imshow("pehli image",img)
cv.waitKey(0)
cv.destroyAllWindows()