import numpy as np 

def normalize_grayscale(image, beta=0.75, image_id_k = 1, A_kp=None):
    N,M = image.shape
    k = image_id_k
    
    if image_id_k > 1 and  A_kp is None :
        print("please define A_kp as this is not the first image")
    elif image_id_k == 1:
        A_kp = np.zeros((N,M))
        
    alpha = beta*(k-1)/k
    a = np.mean(image, axis=0)
    A_k = alpha*A_kp + (1-alpha)*np.tile(a,(N,1))
    image = 128*(image/A_k)
    return image, A_k