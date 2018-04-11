import numpy as np
from scipy import ndimage
from scipy.ndimage.morphology import binary_dilation
from .rolling_window import rolling_window

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

def generate_shadowed_img(origin, cannyed, model, stride = (106,112), window_size = (227, 227)):
	imgs = rolling_window(cannyed, window_size, stride)
	nx, ny = imgs.shape[0], imgs.shape[1]
	result = model.predict(imgs.reshape(nx * ny, -1)).reshape(nx, ny)
	boxed = shade_area(origin, imgs, result, window_size, stride)
	return boxed

def generate_sub_frames(origin, dst, count, stride = (106,112), window_size = (227, 227)):
	imgs = rolling_window(origin, window_size, stride)
	nx, ny = imgs.shape[0], imgs.shape[1]
	for i in range(nx):
		for j in range(ny):
			count += 1
			sub_img = imgs[i, j]
			filename = "%#06d.jpg" % (count)
			save_image(sub_img, dst, filename)
	return count