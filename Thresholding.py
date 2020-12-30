# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:51:39 2020

@author: Gowrav Tata
"""
import cv2 as cv
import os
os.chdir(r'E:/')

img  = cv.imread('Cat.jpg')
cv.imshow("Cat",img)
# Thresholding means binarizing an image, where pixels are zero or black
# ---- Simple Thresholding : Convert BGR to gray

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)

cv.imshow('Thresholded image',thresh)

'''Threshold inverse converts all black parts into white, and inverse '''
threshold,thresh_inverse = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresholded  Inverse image',thresh_inverse)

 # the downside of the simple threshold is manually specify the threshold value
# ---- Adaptive Thresholding
'''In the adaptive thresholding  lets the computer find the optimal thresholded value 
last one is the mean of the surrounding pixels, Block size is the neighbourhood size of the kernel 
size, C is the last one, which is an integer removed from the mean, we can even set that to zero'''
adapt = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C ,cv.THRESH_BINARY,13,3)

cv.imshow("Adaptive Threshold",adapt)



cv.waitKey(0)