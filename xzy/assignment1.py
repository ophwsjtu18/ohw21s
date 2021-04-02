import numpy as np
import cv2

img = cv2.imread('1111.jpg')
head = img[300:370,220:320]
for j in range(3):
    for i in range(3):        
        img[j*70:j*70+70,i*100:i*100+100] = head       
        
for j in range(3):
    for i in range(3):    
        cv2.rectangle(img,(j*100,i*70),(j*100+100,i*70+70),(0,255,0),3)

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
