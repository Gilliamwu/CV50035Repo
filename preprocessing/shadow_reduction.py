import cv2
import numpy as np

def norm_dilate_median(origin_img):
    result_planes = []
    result_norm_planes = []
    plane = origin_img.astype(np.uint8)
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    cv2.absdiff(plane, bg_img)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img= diff_img
    norm_img = cv2.normalize(diff_img, norm_img, alpha=0, 
                             beta=255, norm_type=cv2.NORM_MINMAX, 
                             dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)

    return result_norm

def adaptiveThreshold(origin_img):
    return cv2.adaptiveThreshold(origin_img.astype(np.uint8) ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)