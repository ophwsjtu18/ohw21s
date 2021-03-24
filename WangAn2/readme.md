import numpy as np  
import cv2  
img = cv2.imread('22.png',1)  
#heigh weigh  

print(img.shape)  
head=img[170:230,230:300]  
#for i in[0,100,200]:  
for i in range(0,210,70):  
  for k in range(0,130,60):  
    img[k:k+60,i:i+70]=head  
    cv2.rectangle(img,(i,k),(i+70,k+60),(0,255,0),3)  
#weigh heigh  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  

![Alt example](https://github.com/ophwsjtu18/ohw21s/blob/main/WangAn2/%E4%BD%9C%E4%B8%9A.png)  
