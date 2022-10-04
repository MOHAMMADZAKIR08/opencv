#RESIZING
#import cv2 as cv
#img=cv.imread("resor/image.jpg")
#img=cv.resize(img,(600,800))
#cv.imshow("pehli image",img)
#cv.waitKey(0)
#cv.destroyAllWindows()
#for two images


#RESIZING
import cv2 as cv
img=cv.imread("resor/image.jpg")
img1=cv.resize(img,(600,800))
img = cv.imshow("pehli image",img)
cv.imshow("sec image",img1)
cv.waitKey(0)
cv.destroyAllWindows()
#for two images


