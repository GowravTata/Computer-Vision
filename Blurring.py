# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:50:04 2020

@author: Gowrav Tata
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(r'D:/')

img = cv.imread('ballo.jpg')
cv.imshow('Img',img)
'''we smooth the image when it has lot of noise caused from camera sensors or by the illumination
generally we make a kernel and it has a size which is known as kernel size
Blur is applied to the middle pixel and it's also its surrounding pixel'''


'''               ----------  Averaging  --------          '''

'''define a kernel window over a specific portion of a image, this window will essentially compute the pixel intensity 
of the middle pixel of the true centre as the average of the surrounding pixel intensities
new pixel will always be the average intensity for the middle pixel
kernel slides on sides and then travels down and follows the pattern'''

average = cv.blur(img,(33,33))
cv.imshow('Average Blur',average)

'''               ----------  Gaussian Blur  --------          '''

'''Each surrounding pixel is given a weight and the average of the product of the weights give the true centre value
we get less blur, but more natural blur compared to average'''

average = cv.blur(img,(7,7 ))
cv.imshow('Average Blur',average)
# Standard deviation for the x is the last parameter
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

'''               ---------- Median Blur  --------          '''
'''Same as mean , but uses median , people tend to use this in advanced computer vision projects '''
average = cv.blur(img,(3,3))
cv.imshow('Average Blur',average)

# Standard deviation for the x is the last parameter
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

# Kernel size will be 3X3 as it a median
median = cv.medianBlur(img,3)
cv.imshow('Median',median)

'''               ---------- Bilateral  --------          '''

'''Applied blur but retains the edges'''

img = cv.imread('ballo.jpg')
cv.imshow('Img',img)

''''sigma colour is the last parameter,  larger value for the sigmacolour more number of colours are present in the 
 neighbourhood ,larger sigma space are pixels are further out of the sigma space'''
bilat = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilat)


cv.waitKey(0)