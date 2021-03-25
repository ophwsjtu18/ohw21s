# assignment1
## code

``` python
import numpy as np
import cv2
img = cv2.imread('plutus cat.jpg')
print(img.shape)

head=img[501:601,410:510]
print(head.shape)
#cv2.rectangle(head,(2,2),(100,100),(0,255,0),3) #先在head中绘制矩阵然后再拷贝

for i in range(3):
    for j in range(3):
        x=j*100
        y=i*100 
        img[x:x+100,y:y+100]=head

for i in range(3):
    for j in range(3):
        x=j*100
        y=i*100       
        cv2.rectangle(img,(x+2,y+2),(x+100,y+100),(0,255,0),3) #cv.rectangle绘制时边界会向外扩展一部分，所以从(x+2,y+2)作为起始点保证边界宽度为3个像素

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('plutus cat2.jpg',img)
cv2.destroyAllWindows()
```

## picture
![plutus cat]( https://github.com/yyh2000/assignment/blob/main/plutus%20cat2.jpg?raw=true "plutus cat2")
