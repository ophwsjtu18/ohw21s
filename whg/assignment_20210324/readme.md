The code:
```python
# assignment.py by Wei Huaguang

import cv2

img = cv2.imread('rika.png')
eye = img[100 : 130, 150 : 200]

for j in range(3):
    for i in range(3):
        img[j * 30 : j * 30 + 30, i * 50 : i * 50 + 50] = eye
        cv2.rectangle(img, (i * 50, j * 30), (i * 50 + 50, j * 30 + 30), (0, 255, 0), 3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Run it: `python assignment.py`  
Then  
![result](https://files.catbox.moe/4w0woa.png)  
it works. :)