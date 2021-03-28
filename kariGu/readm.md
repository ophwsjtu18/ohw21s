import numpy as np  
import cv2  
img = cv2.imread('3.jpg',1)  

print(img.shape)  
head=img[60:120,90:110]  
for i in range(0,60,20):  
    for k in range(0,180,60):  
        img[k:k+60,i:i+20]=head  
        cv2.rectangle(img,(i,k),(i+20,k+60),(0,255,0),3)  


cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
cv2.imwrite('hw1.png',img)  
![hw1.jpg]()
