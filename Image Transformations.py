#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import os
import numpy as np
os.chdir(r"E:/")


# In[2]:


img = cv.imread('city.jpg')

cv.imshow('City',img)

def translate(img,x,y):
    
    transMat = np.float32([[1,0,x],[0,1,y]])
    
    dimensions = (img.shape[1],img.shape[0])
    
    # this is used to take in the source, function and dimension size to be given
    
    return cv.warpAffine(img,transMat,dimensions)

# -x shifts the source left x turns right
# -y shifts up and y shifts down

translated = translate(img,100,100)

cv.imshow('Translated',translated)

cv.waitKey(0)


# # Rotation

# In[4]:


img = cv.imread('city.jpg')

cv.imshow('City',img)

# Any specific point can also be rotated

def rotate(img,angle,rotPoint=None):
    
    (height,width) = img.shape[:2]
    
    if rotPoint==None:
    
        rotPoint = (width//2,height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)

    dimensions= (width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

# give negative value to turn the angle to opposite direction

rotated = rotate(img,-45)

cv.imshow('Rotated',rotated)

cv.waitKey(0)


# In[ ]:




