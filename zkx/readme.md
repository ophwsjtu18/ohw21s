#  This is my first readme.md
![pic](https://w.wallhaven.cc/full/rd/wallhaven-rddgwm.jpg "Wallpaper")

| col | 1 | 2 |
| :-------- | --------:| :--: |
| 1 | 0.0 | 0.1 |
| 2 | 1.0 | 1.1 |
| 3 | 2.0 | 2.1 |

## font style

**This text is bold**

*This text is italicized*

___bold and italicized___

~~delete~~
 
 ---
 
## link
[name](https://github.com/ophwsjtu18/ohw21s/tree/main/zkx "title")

[name2][1]

[1]:https://github.com/ophwsjtu18/ohw21s/tree/main/zkx "title2"

[name3][]

[name3]:https://github.com/ophwsjtu18/ohw21s/tree/main/zkx "title3"

---

> Have  
>>you  
>>>heard
>>>>of 
>>>>>matryoshka

---

```python
import numpy as np
import cv2
img = cv2.imread('wallhaven-q6wxvd.png',1)
res=cv2.resize(img,(620,320))

sky=res[100:200,200:300]

for j in range(3):
    for i in range (0,200,10):
        res[j*100:j*100+100,i:i+100]=sky
cv2.imshow('image',res)
```
---

* one
  * 1.1
* two
  * 2.1
  * 2.2
+ three
+ four

---

```sequence
小异常->大异常: 嘿，老大, 看完博客评论了没?
Note right of 大异常: 大异常愣了一下，说：
大异常-->小异常: 呀，差点忘了，马上评论
```

``` flow
st=>start: 开始
e=>end: 结束
com=>operation: 开始评论
cond=>condition: 确认评论？

st->com->cond
cond(yes)->e
cond(no)->com
```
