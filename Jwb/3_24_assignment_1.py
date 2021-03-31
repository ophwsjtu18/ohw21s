#读一副彩色图片并显示出来彩色
import numpy as py
import cv2

img = cv2.imread('siren.jpg',1)

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
