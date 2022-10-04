#make images from video
          #OR
#splitvideo into frame or images sequences

import cv2 as cv
import numpy as np
cap = cv.VideoCapture("resor/video.mp4")
frameno = 0
while (True):
    ret,frame = cap.read()
    if ret:
        cv.imwrite(f"resor/framenf/frame_{frameno}.jpg",frame)
    else:
        break
    frameno = frameno +1
cap.release()