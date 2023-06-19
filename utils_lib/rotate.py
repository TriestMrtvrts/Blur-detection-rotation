import cv2
import os

def rotate(path, h, folder='./res'):
    img = cv2.imread(path)
    for i in range(0, h):
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    
    cv2.imwrite(f'{folder}/'+os.path.basename(path), img)