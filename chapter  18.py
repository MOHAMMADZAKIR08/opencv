# for changing the perspective of image//or change and get image in perfect form
import cv2 as cv
import numpy as np
img = cv.imread("resor/image.png")
print(img.shape)
#defining points
point1 = np.float32([[233,196],[82,471],[522,169],[715,482]])
width,height = 720,720
#or
#width = 
#height = 720
point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(point1,point2)
output_img = cv.warpPerspective(img,matrix,(width,height))
cv.imshow("original",img)
cv.imshow("transformed",output_img)
cv.imwrite("resor/warp_perspective.zakir.png",output_img)
cv.waitKey(0)
cv.destroyAllWindows()