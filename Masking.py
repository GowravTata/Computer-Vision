# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:42:33 2020

@author: Gowrav Tata
"""
# Masking allows us to focus on certain parts of image that we are focused on

import cv2 as cv
import numpy as np

import os
os.chdir(r"D:/")
img = cv.imread('Macaw.jpg')
cv.imshow('Macaw',img)
# Mind that the dimensions of the mask should be same as of a image
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)
# Index 1 is the width and index 0 is height, 100 is the radis, 255 is the colour, -1 is the thickness
mas = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Blank',blank)
cv.imshow('Mask',mask)

masked_image = cv.bitwise_or(img,img ,mask=mas)
cv.imshow('Masked Image',masked_image)
cv.waitKey(0)
