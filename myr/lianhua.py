import numpy as np
import cv2
img = cv2.imread('lianhua.png')

head=img[250:400,600:800]

for i in range(3):
    for j in range(3):
        img[150*j:150*j+150,200*i:200*i+200]=head
        cv2.rectangle(img,(200*i,150*j),(200*i+200,150*j+150),(0,255,0),3)
        
        
        
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
