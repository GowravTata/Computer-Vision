#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv
import numpy as np
import os
os.chdir(r"E:/")


# # Grayscale

# In[3]:


img = cv.imread('ca.jpg')
cv.imshow('Cat',img)
# Converting into grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Cat',gray)


cv.waitKey(0)


# # Blurring Image

# In[9]:


img = cv.imread('ca.jpg')
cv.imshow('Cat',img)

# Blur an image, removes the noise in the data like removing extra element due to bad lighting
# Kernel size is the window size that opencv uses, kernel size always should be in odd number and another is BORDER_DEFAULT 
blur= cv.GaussianBlur(img,(69,69),cv.BORDER_DEFAULT)

cv.imshow('Blur',blur)

cv.waitKey(0)


# # Edge Detection

# In[ ]:


# we gonna use canny edge cascade detection
img = cv.imread('ca.jpg')
cv.imshow('Cat',img)
# for this we gonna pass two threshold values
canny = cv.canny(img,125,175)
cv.imshow('Edge',canny)

cv.waitKey(0)


# # Dilate the image

# In[5]:


# we gonna use canny edge cascade detection
img = cv.imread('tree.jpg')
cv.imshow('Tree',img)
# for this we gonna pass two threshold values
canny = cv.Canny(img,125,175)
dilated = cv.dilate(canny,(3,3),iterations=1)

cv.imshow('Dilate',canny)

cv.waitKey(0)


# # Eroding the image

# In[9]:


img = cv.imread('tree.jpg')
cv.imshow('Tree',img)

canny = cv.Canny(img,125,175)
dilated = cv.dilate(canny,(3,3),iterations=1)
eroded = cv.erode(dilated,(3,3),iterations=2)
cv.imshow('Eroded',eroded)

cv.waitKey(0)


# In[6]:


import cv2
 
img = cv.imread('tree.jpg')
 
cv2.circle(img,(100, 0), 25, (0,255,0))
cv2.circle(img,(0, 100), 25, (0,0,255))
 
cv2.circle(img,(100, 100), 50, (255,0,0), 3)
 
cv2.imshow('Test image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Resize

# In[16]:


img = cv.imread('tree.jpg')
# in order to increase the resolution we use cv.INTER_LINEAR or INTER_CUBIC
resized = cv.resize(img,(500,500),interpolation = cv.INTER_LINEAR)

cv.imshow('Resized',resized)

cv.waitKey(0)


# # Cropping

# In[17]:


# as images are arrays, we can slice the image by selecting the certain portion of the image
img = cv.imread('tree.jpg')
cropped = img[200:400,600:800]
cv.imshow('Cropped',cropped)

cv.waitKey(0)


# In[ ]:




