import cv2 as cv
import numpy as np
img = cv.imread('lean.jpg')
cv.imshow('Lean',img)

width,height =img.shape[1],img.shape[0]
# we need to give the coordinates of the image we can get those by opening the image in paint and hover over the pixel values
coord = np.float32([[164,5],[281,1],[133,394],[241,397]])
'''This is the order of the defining the co-ordinates, first co-ordinate is the pixel value of the top left, followed by top right
bottom left, bottom right'''
seq = np.float32([[0,0],[width,0],[0,height],[width,height]])
# -- Matrix is to analogise with the coordinates present in image
matrix = cv.getPerspectiveTransform(coord,seq)
# -- Attributes are the source, comparative matrix, dimensions
orient = cv.warpPerspective(img,matrix,(width,height))
cv.imshow('Oriented',orient)

cv.waitKey(0)
