import numpy as np
import cv2

def get_images(inputs, path = '', converter = lambda x : x, nptype = np.float32):
	'''
	path is the directory to load from
	input is a array of files to load from
	converter is a function that coverts from the input array to a string to the file name
	
	Returns a np.array
	'''
	imgs = []
	
	for s in inputs:
		file_path = '{path}\\{img}'.format(path = path, img = converter(s))
		img = cv2.imread(file_path, 0).astype(nptype)
		imgs.append(img)
		
	return np.asarray(imgs)

def get_random_indices(select_range, train_size, test_size, val_size):
	all_selected = np.random.choice(select_range, size = train_size + test_size + val_size, replace = False)
	
	test_start = train_size
	val_start  = test_start + test_size
	
	train_selected = all_selected[0:test_start]
	test_selected  = all_selected[test_start:val_start]
	val_selected   = all_selected[val_start:]
	
	return train_selected, test_selected, val_selected

# concrete data set helpers
def _concrete_file_name_get_positive(n):
    if n >= 10000 and n <= 19378:
        return 'Positive\\{n:05d}_1.jpg'.format(n = n)
    else:
        return 'Positive\\{n:05d}.jpg'.format(n = n)

def _concrete_file_name_get_negative(n):
    return 'Negative\\{n:05d}.jpg'.format(n = n)

# use this
def get_concrete_data(positive_range, negative_range, path = ''):
	x = get_images(positive_range, path, _concrete_file_name_get_positive)
	x = np.append(x, get_images(negative_range, path, _concrete_file_name_get_negative), axis = 0)
	
	y = np.ones(len(positive_range))
	y = np.append(y, np.zeros(len(negative_range)), axis = 0)
	
	return x, y