import numpy as np
import cv2

img = cv2.imread('inter.jpg',1)
img2 = img[600:800,600:800]
for x in range(3):
    for y in range(3):
        img[(y*200):(200+(y*200)),(x*200):(200+(x*200))]=img2
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
