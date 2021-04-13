#  code
```python
import cv2
import numpy as np
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

face_cascade = cv2.CascadeClassifier('D:\Program Files (x86)\python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

help="""
    h: show help
    l: auxiliary lines on/off
    r: reference point on/off
    esc: end this program
"""
showline = True
showpoint = True
showplot = False

while (True):
    ret,img=cap.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    if showline:
        cv2.line(img, (0, 260), (280, 260), (126, 139, 146), 2)
        cv2.line(img, (360, 260), (640, 260), (126, 139, 146), 2)
        cv2.line(img, (320, 0), (320, 220), (126, 139, 146), 2)
        cv2.line(img, (320, 300), (320, 480), (126, 139, 146), 2)
        cv2.rectangle(img, (280, 220), (360, 300), (126, 139, 146), 2)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        a = int(x + w / 2)
        b = int(y + h / 2)

        pos = mc.player.getTilePos()
        
        if a < 280:
            pos.x-=1
        elif a > 360:
            pos.x+=1
        if b < 220:
            pos.z+=1
        elif b > 300:
            pos.z-=1
        mc.player.setTilePos(pos.x, pos.y, pos.z)

        if showpoint:
            cv2.line(img, (a, b - 5), (a, b + 5), (46, 50, 52), 2)
            cv2.line(img, (a - 5, b), (a + 5, b), (46, 50, 52), 2)
        if showplot:
            print(a, b)
        time.sleep(1)

    cv2.imshow('img',img)
    k = cv2.waitKey(20)
    if k == 27:
        break                   # if press the 'esc' key, end this program
    elif k == 104:
        print(help)             # if press the 'h' key, print the help
    elif k == 108:              # if press the 'l' key, auxiliary lines on or off
        showline = not showline
    elif k == 114:              # if press the 'r' key, reference point on or off
        showpoint = not showpoint
    elif k == 112:              # if press the 'p' key, show plot
        showplot = not showplot
cap.release()
cv2.destroyAllWindows()
```
