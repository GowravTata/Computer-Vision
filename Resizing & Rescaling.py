#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv


# In[2]:


import os
os.chdir(r'E:/')


# In[5]:


'''We usually do resizing and rescaling to prevent computational strain large video needs a lot of data and use lot of processing 
rescaling a video implies modifying its width and height to a particular height'''


# In[ ]:





# In[3]:


img = cv.imread('ca.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.25):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)
resize_image = rescaleFrame(img)
cv.imshow('Image',resize_image)


# In[4]:


def rescaleFrame(frame,scale=0.25):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)


# In[ ]:


# Works only with live-video
def changeRes(width,height):
    # 3 & 4 are the references of the width and height
    capture.set(3,width)
    capture.set(4,height)


# In[6]:


capture = cv.VideoCapture('DecoyBride.mp4')
while True:
    isTrue,frame = capture.read()  
    
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    # display the frame by displaying the resized frame
    cv.imshow('Video',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
cv.waitKey
capture.release()
cv.destroyAllWindows()


# In[ ]:




