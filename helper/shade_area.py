import numpy as np

def shade_area(img, imgs, result, window_size, stride, thickness = (8, 8)):
	boxed = np.array(img)
	X, Y = img.shape[0], img.shape[1]
	sX, sY = stride
	wX, wY = window_size
	nX, nY = result.shape
	pW, pH = thickness
	
	for i in range(nX):
		for j in range(nY):
			if result[i, j] == 1.0:
				x = i * sX
				y = j * sY
				
				mask = (imgs[i, j] != 0.0)
				mask2 = np.array(boxed[x:x+wX, y:y+wY])
				
				for offsetX in range(-pW, pW+1):
					for offsetY in range(-pH, pH+1):
						
						minX = max(0, 0 + offsetX)
						maxX = min(wX, wX + offsetX)
						
						minY = max(0, 0 + offsetY)
						maxY = min(wY, wY + offsetY)
						
						m = mask[minX:maxX, minY:maxY]
						
						xpad = np.zeros(shape = (abs(offsetX), maxY-minY), dtype = bool)
						if offsetX > 0:
							m = np.append(m, xpad, axis = 0)
						else:
							m = np.append(xpad, m, axis = 0)
						
						ypad = np.zeros(shape = (wX, abs(offsetY)), dtype = bool)
						if offsetY > 0:
							m = np.append(m, ypad, axis = 1)
						else:
							m = np.append(ypad, m, axis = 1)
						
						mask2[m] = [255, 255, 0]
				
				boxed[x:x+wX, y:y+wY] = mask2
				
	return boxed