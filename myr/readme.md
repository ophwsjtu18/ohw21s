# Big Title  


🥇
![homework Pic](https://github.com/ophwsjtu18/ohw21s/blob/main/myr/result.png)??
## Code
```
import numpy as np  
import cv2  
img = cv2.imread('lianhua.png')  

head=img[250:400,600:800]  

for i in range(3):  
    for j in range(3):  
        img[150*j:150*j+150,200*i:200*i+200]=head  
        cv2.rectangle(img,(200*i,150*j),(200*i+200,150*j+150),(0,255,0),3)  
        
        
        
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
```
## Code 1 
Using virutal keyboard to controll,though i can give the key 'wsad' ,it don't work in minecraft
```
import numpy as np
from pynput.keyboard import Key,Controller
import cv2
import time
key=Controller()
cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    
    
    ret,frame=cap.read()
   
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if(x<150):
            key.press('d')
            time.sleep(0.25)
            key.release('d')
            
        elif(x>380):
            key.press('a')
            time.sleep(0.25)
            key.release('a')
            
        elif(w<100):
            key.press('s')
            time.sleep(0.25)
            key.release('s')
            
        elif(x>150 and x<380 and w>180):
            key.press('w')
            time.sleep(0.25)
            key.release('w')
            
            
            
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```  

#Code 2  
Using teleport ,not moving.
```
from mcpi.minecraft import Minecraft
import numpy as np
import cv2
import time

mc=Minecraft.create()
cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    pos=mc.player.getTilePos()
    
    ret,frame=cap.read()
   
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if(x<150):
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            time.sleep(0.25)
        elif(x>380):
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            time.sleep(0.25)   
        elif(w<100):
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            time.sleep(0.25)
            
        elif(x>150 and x<380 and w>180):
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            time.sleep(0.25)
                   
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()  
```
        
        
      

        
        
        
     




 

 
 
 
