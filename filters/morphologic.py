import cv2
import numpy as np

def tophat( img, element=(5, 5) ):
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,element)
	return cv2.morphologyEx( img, cv2.MORPH_TOPHAT, kernel )

def blackhat( img, element = (5, 5) ):
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,element)
	return cv2.morphologyEx( img, cv2.MORPH_BLACKHAT, kernel )
	
def gradient( img, element = (5, 5) ):
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,element)
	return sv2.morphologyEx( img, cv2.MORPH_GRADIENT, kernel )

def gradient2( img ):
	
	img = np.uint8(img)
	kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
	kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	
	gradient1 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel1)
	gradient1 = gradient1.reshape(-1)
	gradient2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel2)
	gradient2 = gradient2.reshape(-1)
	
	myfiltered = np.multiply(gradient1, gradient2)
	
	return myfiltered

def gradient3( img ):
	
	img = np.uint8(img)
	
	kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
	kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	kernel3 = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
	
	gradient1 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel1)
	gradient1 = gradient1.reshape(-1)
	gradient2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel2)
	gradient2 = gradient2.reshape(-1)
	gradient3 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel3)
	gradient3 = gradient3.reshape(-1)
	
	myfiltered = np.multiply(gradient1, gradient2)
	myfiltered = np.multiply(gradient3, myfiltered)
	
	return myfiltered
	
def canny_gradient( img ):
	img = np.uint8(img)
	
	blur = cv2.bilateralFilter(img, 10, 20, 20)
	blur = np.uint8(blur)
	
	mycanny = cv2.Canny(blur,100,200)
	mycanny = mycanny.reshape(-1)
	
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
	mygrad = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
	mygrad = mygrad.reshape(-1)
	myfiltered = np.multiply(mygrad,mycanny)
	return myfiltered

def cv2_morphology( img, morphology_type, element ):
	img = np.uint8(img)
	kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, element)
	myfiltered = cv2.morphologyEx(img, morphology_type, kernel)
	myfiltered = myfiltered.reshape(-1)
	return myfiltered