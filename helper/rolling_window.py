import numpy as np

def rolling_window(image, window_size, stride):
    '''
    Image is a (X, Y) size array to apply rolling window on
    window_size is a tuple containing (winX, winY)
    stride is a tuple containing (dX, dY)
    
    Returns an array of size (nX, nY, winX, winY)
    where nX, nY are the indices of the window at the position
    '''
    X, Y = image.shape
    winX, winY = window_size
    dX, dY = stride
    
    nX = (X - winX) // dX + 1 
    nY = (Y - winY) // dY + 1
    
    arr = np.zeros(shape = (nX, nY, winX, winY))
    
    for i in range(0, nX):
        for j in range(0, nY):
            x = i * dX
            y = j * dY
            arr[i, j, :, :] = image[ x : x + winX, y : y + winY]
    
    return arr