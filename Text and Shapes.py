import numpy as np
import cv2 as cv
# 600,600 is the height and width of the image, and 3 is the functionality to give three channels
img = np.zeros((600,600,3),np.uint8)

#-- For colour on the whole image we use img[:]
#img[200:300,100:400] = 0,0,255
# Define the source
#  Parameters are the source image, coordinates of the start and end point , thickness
cv.line(img,(0,0),(600,600),(0,255,255),13)
'''For Drawing more lines use the same syntax and change the co-ordinates of the pixel, and if else we can use polyLine attribute in the Library'''
# Parameters are the source image, coordinates of the start and end point , thickness, use cv.FILLED in order to fill the gap
cv.rectangle(img,(0,0),(250,350),(50,150,250),13,cv.FILLED)
# -- Circle source, center point of the circle, radius, colour and thickness
cv.circle(img,(400,50),30,(255,255,255),4)

# Writing text
# Parameters are text,origin , FONT of the text,scale,colour and thickness
cv.putText(img,"STAR WARS",(100,100),cv.FONT_HERSHEY_COMPLEX,2,(100,100,200),10)

cv.imshow('Blank',img)

cv.waitKey(0)