import cv2
def tophat(img, element=(2,2)):
    img = np.uint8(img)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,element)
    myfiltered = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    return myfiltered