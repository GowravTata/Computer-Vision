import cv2 as cv
img = cv.imread('Images/cruz.jpg')
cv.imshow("Penelope",img)

'''Here the parameters to be passed are 
Source , threshold values, L2gradient
If the threshold values passed are higher, the aperture and detects less edge
'''
canny = cv.Canny(img,100,100,L2gradient = False)
cv.imshow("Detected",canny)

def EdgeDetection(img,thresh1,thresh2):
    img = cv.imread(img)
    canny = cv.Canny(img,thresh1,thresh2,L2gradient = False)
cv.imshow("Edge Detected",canny)

EdgeDetection('cruz.jpg',100,100)

cv.waitKey(0)