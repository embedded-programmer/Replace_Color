import cv2
import numpy as np

# BGR Color Format
black   =  [0,0,0]
green   =  [0,255,0]
red     =  [0,0,255]
blue    =  [255,0,0]
yellow  =  [0,255,255]
magenta =  [255,0,255]
cyan    =  [255,255,0]
gray    =  [127,127,127]
white   =  [255,255,255]


image = cv2.imread("test.png")  # BGR
cv2.imshow('Test',image)

image[np.where((image==green).all(axis=2))] = cyan
image[np.where((image==yellow).all(axis=2))] = red
image[np.where((image==magenta).all(axis=2))] = gray

cv2.imwrite('result.png',image)
cv2.imshow('Result',image)
