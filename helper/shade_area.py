import numpy as np

def shade_area(img, result, window_size, stride, line_size = 5):
	boxed = np.array(img)
	X, Y = img.shape
	sX, sY = stride
	wX, wY = window_size
	nX, nY = result.shape
	
	for i in range(nX):
		for j in range(nY):
			if result[i, j] == 1.0:
				x = i * sX
				y = j * sY
				
				boxed[x:x+wX, y:y+wY] = img[x:x+wX, y:y+wY] * 0.75
	
	return boxed