import cv2
import numpy as np

def otsu( img, element = (5,5) ):
    img = np.uint8(img)
    blur = cv2.GaussianBlur(img,element,0)
    ret3,myfiltered = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    myfiltered -= 255
    myfiltered = np.abs(myfiltered)
    #myfiltered = np.subtract(myfiltered,255)
    #myfiltered = np.multiply(myfiltered, -1)
    return myfiltered
