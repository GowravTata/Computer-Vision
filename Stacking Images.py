import cv2 as cv
import numpy as np
img=cv.imread('E:/Keira.jpg')

cv.imshow('keira',img)
# -- Horizontal Stacking

hor_img = np.hstack((img,img))
cv.imshow('Horizontal',hor_img)

# -- Vertical Stacking
ver_img = np.vstack((img,img))
cv.imshow('Vertical',ver_img)


cv.waitKey(0)
