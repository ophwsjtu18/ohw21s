![image](https://user-images.githubusercontent.com/81301880/112598908-31410180-8e4a-11eb-9e69-54e5bbd4006d.png)
import numpy as np
import cv2
img = cv2.imread('image.jfif')

print(img.shape)
head=img[270:540,1680:1920]
for i in range(3):
    for j in range(3):
        img[i*270:i*270+270,j*240:j*240+240]=head
for i in range(3):
    for j in range(3):
       cv2.rectangle(img,(i*270,j*240),(i*270+270,j*240+240),(0,255,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

