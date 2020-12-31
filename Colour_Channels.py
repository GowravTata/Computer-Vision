# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 15:56:03 2020

@author: Gowrav Tata
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(r'D:/')

img = cv.imread('macaw.jpg')


b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
print(img.shape),print(b.shape),print(g.shape),print(r.shape)
cv.imshow('Macaw',img)


merged = cv.merge([b,g,r])

cv.imshow('Merged Image',merged)



plt.show()

blank =np.zeros(img.shape[:2],dtype='uint8')
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
print(img.shape),print(b.shape),print(g.shape),print(r.shape)
cv.imshow('Macaw',img)


merged = cv.merge([b,g,r])

cv.imshow('Merged Image',merged)

cv.waitKey(0)

plt.show()

