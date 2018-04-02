import numpy as np 

class GrayscaleNormalizer:
	
	def __init__(self, beta = 0.75):
		self.beta = beta
		self.A_kp = None
		self.image_id_k = 1
	
	def __call__(self, image):
	    N,M = image.shape
	    k = self.image_id_k
	    
	    if self.image_id_k == 1:
	        self.A_kp = np.zeros((N,M))
			
	    alpha = self.beta*(k-1)/k
	    a = np.mean(image, axis=0)
		
	    self.A_kp = alpha*self.A_kp + (1-alpha)*np.tile(a,(N,1))
	    self.image_id_k += 1
		
	    image = 128*(image/self.A_kp)
	    return image