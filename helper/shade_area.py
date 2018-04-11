import numpy as np
from scipy import ndimage
from scipy.ndimage.morphology import binary_dilation

def shade_area(img, imgs, result, window_size, stride, thickness = (8, 8)):
	mask = np.zeros(img.shape[0:2])
	sX, sY = stride
	wX, wY = window_size
	nX, nY = result.shape
	pW, pH = thickness
	
	for i in range(nX):
		for j in range(nY):
			if result[i, j] == 1.0:
				x = i * sX
				y = j * sY
				
				mask[ x:x+wX , y:y+wY ] += imgs[i, j]
				
	mask = (mask != 0.0)
	structure = np.ones(shape = thickness, dtype = bool)
	mask = binary_dilation(mask, structure = structure)
	boxed = np.array(img)
	boxed[mask] = 255, 255, 0
				
	return boxed