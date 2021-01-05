import cv2 as cv
import numpy as np
# Reading the file
img = cv.imread('shape.jpg')
'''
Preprocessing
The input image has to be converted to Canny,
retr_tree if we want all the hierarchical contours for external use retr_external 
retr_list for all the contours
cv.chain is for contour approximation , just return all the contours
 chain approx simple only gives the two points
'''
canny = cv.Canny(img,125,175)
contours, hierarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
'''Parameters are source, source image, input arrays obtained from contours,contourIdx to draw all contours with passed in the
contours object and the last parameter is thickness '''
detected=cv.drawContours(img,contours,-1,(0,0,255),1)
cv.imshow('Detected Contour',detected)
# Saving the image
cv.imwrite('Contours Detected.jpg',detected)
cv.waitKey(0)
        