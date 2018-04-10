import cv2
import numpy as np
#from .filter import GrayscaleNormalizer

from sklearn import linear_model

class bilateral_canny:
	def __init__(self):
		#self.normalizer = GrayscaleNormalizer()
		pass

	def bilateral_canny_img(self, img):
	    img = np.uint8(img)
	    blur = cv2.bilateralFilter(img,10,20,20)
	    blur = np.uint8(blur)
	    myfiltered = cv2.Canny(blur,100,200)
	    #myfiltered = myfiltered.reshape(-1)
	    return myfiltered
    
	def canny_img(self, img):
	    img = np.uint8(img)
	    myfiltered = cv2.Canny(img,100,200)
	    #myfiltered = myfiltered.reshape(-1)
	    return myfiltered
        