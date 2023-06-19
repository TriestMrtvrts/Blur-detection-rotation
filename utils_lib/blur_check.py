import cv2
import os

def check_blury(path, QUALITY_THRESHOLD):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()

    print(os.path.basename(path), fm)

    result = fm < QUALITY_THRESHOLD

    return result