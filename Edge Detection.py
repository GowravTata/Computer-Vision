# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:51:39 2020

@author: Gowrav Tata
"""
import cv2 as cv
import os
os.chdir(r'E:/')

img = cv.imread('city.jpg')

cv.imshow('City',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
'''Gradients are edge like regions.'''
# -- Laplacian

lap  = cv.Laplacian(gray,cv.CV_64F)
'''When converting from black to white and white to black it is considered as a negative slope
As image cannot have negative value, the value it taken as absolute'''

lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)  

# -- Sobel Edge Detection

'''Sobels computes the gradients in both X and Y direction
first is the image source'''
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobel_x,sobel_y)

cv.imshow('Combined',combined_sobel)
cv.imshow("Sobel_X",sobel_x)
cv.imshow("Sobel_Y",sobel_y)
cv.waitKey(0)