# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:09:48 2020

@author: hp
"""

import cv2 as cv
import os
import numpy as np
os.chdir(r"E:/")
img = cv.imread('city.jpg')
cv.imshow('City',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)
# countours are the boundaries of the image
# retr_tree if we want all the hierarchical contours for external use retr_external , retr_list for all the contours
# cv.chain is for contour approximation , just return all the contours
# chain approx simple only gives the two points
# contours is list of all the coordinates of the contours present
# hierarchy represents the hierarchical representation of encapsulation
contours, hierarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are found')

# threshold looks at that image and binarizes it
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are found')

# visualize the contours made on the image
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# threshold looks at that image and binarizes it
#ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
#cv.imshow('Thresh',thresh)
canny  = cv.Canny(img,125,175)
contours, hierarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are found')
# 2 is the thickness, -1 is for all the contours we need
cv.drawContours(blank,contours,-1,(0,0,255),1)

cv.imshow('Contours Drawn',blank)
cv.waitKey(0)