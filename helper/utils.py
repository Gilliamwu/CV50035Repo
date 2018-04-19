import cv2
import os

def save_image(img, dst, filename):
    if not os.path.exists(dst):
        os.mkdir(dst)  
    cv2.imwrite(os.path.join(dst , filename), img)
    cv2.waitKey(1)