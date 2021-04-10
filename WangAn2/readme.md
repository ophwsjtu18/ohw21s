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




"""
Created on Thu Jan 30 11:06:23 2014
@author: duan
"""
import numpy as np
import cv2
q=1
from mcpi.minecraft import Minecraft
import time
import serial
from mcpi import minecraft
mc=Minecraft.create()
cap = cv2.VideoCapture(0)
pos=mc.player.getTilePos()
while(True):

    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:      
        print(x)
        print(y)
        print(w)
        print(h)
        if x<200 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            pos=mc.player.getTilePos()
            mc.postToChat("right")
            time.sleep(1)
        elif x>300 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            pos=mc.player.getTilePos()
            mc.postToChat("left")
            time.sleep(1)
        elif y<130 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y+1,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("up")
            time.sleep(1)
        elif y>240 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y-1,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("down")
            time.sleep(1)
        elif w>110:
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("ahead")
            time.sleep(1)
        elif w<70:
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("behind")
            time.sleep(1)



        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
    cv2.imshow('img',frame)
    
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
