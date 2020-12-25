#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv


# In[2]:


import os
os.chdir("E:/")


# In[3]:


img = cv.imread('ca.jpg')

# display the image, with a new window
# Cat is the name of the window ,and actual matrix or pixels to be added
cv.imshow('Cat',img)

cv.waitKey(0)


# In[ ]:


img = cv.imread('cat.jpg')

cv.imshow('Cat',img)

cv.waitKey(0)

# when you run this section the a portion of image appears this is due to the higher resolution of the picture which one's PC can display it


# In[ ]:


# OpenCV doesn't have the inbuilt function to compress the image to fit to your screen


# # Reading Videos

# In[3]:


# set a variable to capture everything 
# Here 0 implies as the primary webcam present or connected while passing 1,2,3 takes the input of the other cameras present.
#capture = cv.VideoCapture(0)
capture = cv.VideoCapture('The.Decoy.Bride.2011.720p.BluRay.x264-[YTS.AM].mp4')
while True:
    isTrue,frame = capture.read() # capture.read reads the video frame be radio
    # To display individual frame
    cv.imshow('Video',frame)
    # To stop the video being indefinite , letter 'd' is hit to destroy
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cv.waitKey
# release the instance
capture.release()
cv.destroyAllWindows()


# In[ ]:




