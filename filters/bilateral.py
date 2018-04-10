import cv2
import numpy as np
from .filter import GrayscaleNormalizer

from sklearn import linear_model

class bilateral_canny:
	def __init__(self):
		self.normalizer = GrayscaleNormalizer()

	def bilateral_canny_img(self, img):
	    img2 = self.normalizer(img)
	    img2 = np.uint8(img2)
	    blur = cv2.bilateralFilter(img2,10,20,20)
	    blur = np.uint8(blur)
	    myfiltered = cv2.Canny(blur,100,200)
	    #myfiltered = myfiltered.reshape(-1)
	    return myfiltered
    
	def canny_img(self, img):
	    img = np.uint8(img)
	    myfiltered = cv2.Canny(img,100,200)
	    #myfiltered = myfiltered.reshape(-1)
	    return myfiltered
        