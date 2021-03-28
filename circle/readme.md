# Circleplus

---
  
    
      
      
## Introduction
I'm a new githuber, welcome to give directions:D  
Here is my profile photo.  

![Circleplus](https://avatars.githubusercontent.com/u/81300841?s=60&v=4)  
*Oh, this profile photo comes from [Alice](https://www.bing.com/search?q=%E7%89%A9%E8%BF%B0%E6%9C%89%E6%A0%96&form=ANNTH1&refig=bc5df75eec314dcb83b8a9db66fc3593).*

## Projects
Not yet.
But I'm interested in **Deep Learning** and **Crawlers**.


## Table test
|table1|table2|table3|
|:-----|:----:|-----:|
|yi|er|san|


## Homework
This is the original picture.
![Original pic](http://i1.hdslb.com/bfs/archive/70bf163cec3d7373d47bf624353fa2c7362158c9.jpg)  

- To show this pic, you may use python with the following code:  
```python
import cv2

img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\test.jpg")  ## The path is your picture's path in your computer.

cv2.imshow('pic', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- Now let's play some tricks.
```python
import cv2

img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\test.jpg")

hd = img[368:488, 1014:1108]
for i in range(3):
    for j in range(3):
        img[120*i:120*i+120, 94*j:94+94*j] = hd
        
cv2.imwrite("C:\\Users\\LENOVO\\Desktop\\test2.jpg", img)
cv.imshow('pic', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
The picture becomes more interesting like this:
![Alice-mihayo](https://github.com/ophwsjtu18/ohw21s/blob/main/circle/test2.jpg)  

- If you would like to draw your picture, here is an example for rectangles:
```python
import cv2

img = cv2.imread("C:\\Users\\LENOVO\\Desktop\\test.jpg")

for i in range(3):
    for j in range(3):
        cv2.rectangle(img, (200*i, 100*j), (200*i+200, 100*j+100), (93, 173, 120), 3)

cv2.imwrite("C:\\Users\\LENOVO\\Desktop\\test3.jpg", img)
cv2.imshow('Alice', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
It should come out like this:
![Alice-mihayo](https://github.com/ophwsjtu18/ohw21s/blob/main/circle/test3.jpg)
