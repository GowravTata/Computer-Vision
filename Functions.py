# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 12:35:29 2020

@author: Gowrav Tata
"""

import cv2 as cv
import numpy as np
import os
os.chdir(r"D:/")
img = cv.imread('tokyo.jpg')
cv.imshow('Tokyo',img)
'''Gray Scale'''
# Converting into grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

'''Blur'''
# Blur an image, removes the noise in the data like removing extra element due to bad lighting
# Kernel size is the window size that opencv uses, kernel size always should be in odd number and another is BORDER_DEFAULT 
blur= cv.GaussianBlur(img,(69,69),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

'''Canny Edge Detection''' 
# we gonna use canny edge cascade detection for this we gonna pass two threshold values
canny = cv.Canny(img,125,175)
cv.imshow('Edge',canny)

'''Dilated'''
canny = cv.Canny(img,125,175)
dilated = cv.dilate(canny,(3,3),iterations=1)

cv.imshow('Dilate',canny)

'''Eroding'''
canny = cv.Canny(img,125,175)
dilated = cv.dilate(canny,(3,3),iterations=1)
eroded = cv.erode(dilated,(3,3),iterations=2)
cv.imshow('Eroded',eroded)


'''Resize'''
# In order to increase the resolution we use cv.INTER_LINEAR or INTER_CUBIC
resized = cv.resize(img,(500,500),interpolation = cv.INTER_LINEAR)

cv.imshow('Resized',resized)

'''Crop'''
# As images are arrays, we can slice the image by selecting the certain portion of the image
cropped = img[200:400,600:800]
cv.imshow('Cropped',cropped)

cv.waitKey(0)