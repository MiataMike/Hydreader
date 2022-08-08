from cv2 import *
import cv2
import time
import datetime

cam = cv2.VideoCapture(-1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cam.set(cv2.CAP_PROP_FOCUS,0)
s, img = cam.read()
if s:    # frame captured without any errors
#    namedWindow("cam-test")
#    imshow("cam-test",img)
    cv2.waitKey(0)
#    destroyWindow("cam-test")
    cropped = img[:,450:1720]
    rotated = cv2.rotate(cropped,cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("livecam.jpg",rotated) #save image
