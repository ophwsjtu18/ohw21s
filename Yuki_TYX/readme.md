# HW1

![hw1.png](https://i.loli.net/2021/03/24/Pra2Jf7Kspgw6lv.png)

```(python)
import numpy as np
import cv2
img=cv2.imread('pic.jpg')
print(img.shape)

eye=img[450:585,450:550]

for m in range (3):
    for n in range (3):
        img[n*135:n*135+135,m*100:m*100+100]=eye

for p in range (3):
    for q in range (3):
        cv2.rectangle(img,(p*100,q*135),(p*100+100,q*135+135),(0,255,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows
cv2.imwrite('hw1.png',img)
```
