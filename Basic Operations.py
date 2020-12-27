# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:49:16 2020

@author: Gowrav Tata
"""
import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

# Size from 30 to 370, next is colour , 255 is white, thickness is -1 as it has to be fully filled
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),(255),-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# BITWISE AND-- intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND',bitwise_and)

# BITWISE OR -- non intersecting and intersecting regions

bitwiseor = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwiseor)

# BITWISE XOR
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_xor)

# BITWISE NOT -- returns the remaining portion of the blank image
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise XOR',bitwise_not)


cv.waitKey(0)

