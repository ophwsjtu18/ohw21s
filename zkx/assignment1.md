# picture
<img width="467" alt="屏幕截图 2021-03-27 225207" src="https://user-images.githubusercontent.com/81300130/112724614-2d4ad780-8f4f-11eb-8876-a4b1d625f966.png">

# code
```python
-*- coding=utf-8 -*-
# @Time : 2021/3/25 20:56
# @Author : me
# @File : practice.py
# @Software : PyCharm

import numpy as np
import cv2

img = cv2.imread('wallhaven-q6wxvd.png',1)
res=cv2.resize(img,(620,320))

sky=res[100:200,200:300].copy

color = (0,255,0)
cv2.rectangle(sky,(0,0),(100,100),color,3)

for j in range(3):
    for i in range(0,201,100):
        res[j * 100:j * 100 + 100, i:i + 100] = sky
cv2.imshow('image',res)

cv2.waitKey(0)

cv2.destroyAllWindows()
```
