## code
```
  import numpy as np
  import cv2
  img = cv2.imread('B.jfif',1)
  cv2.namedWindow('image',cv2.WINDOW_NORMAL)   
  head=img[600:700,600:700]

  for i in range(3):
      for j in range(3):
          print(j)
          img[100*i:100*i+100,100*j:100*j+100]=head
        
  for i in range(3):
      for j in range(3):
          cv2.rectangle(img,(j*100,i*100),((j+1)*100,(i+1)*100),(0,255,0),3)
  cv2.imshow('image',img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
```

![picture](https://github.com/Obliviousv/Picture/blob/main/LK4LT%60VVERIQ2BM%5D%5BV%7DH%60QM.png?raw=true)
