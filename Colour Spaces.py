# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:58:02 2020

@author: Gowrav Tata
"""

import cv2 as cv
import os
import numpy as np
os.chdir(r'E:/')
import matplotlib.pyplot as plt

'''colour spaces are basically are a space of colours, representing an array of pixel colours
RGB and gray scale are a colour space , HSV and LAV and many more
converting the image from BGR to gray scale'''
img = cv.imread('ca.jpg')
# BGR to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV ( hue, saturation, value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


# OpenCV displays BGR image, and matplotlib displays inversion of colours

# BGR to RGB


rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

# LAB to BGR
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB_BGR',lab_bgr)

# Grey scale to LAB is not possible

cv.waitKey(0)