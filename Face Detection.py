# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:51:39 2020

@author: Gowrav Tata
"""
import cv2 as cv
import os
os.chdir(r'D:/')

img = cv.imread('kath.jpg')
cv.imshow('Katherine',img)

gray  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('haar.xml')

faces_rec = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

print(f'Number of faces found are {len(faces_rec)}')

for (x,y,h,w) in faces_rec:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("Detected Faces",img)
cv.waitKey(0)