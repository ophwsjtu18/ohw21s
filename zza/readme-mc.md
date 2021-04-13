import numpy as np
import cv2
from mcpi import minecraft
from mcpi.minecraft import Minecraft
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

mc=Minecraft.create()

while(True):
    ret, img =cap.read()

    faces = face_cascade.detectMultiScale(img, 1.3, 5)

    pos=mc.player.getTilePos()
    cv2.line(img,(0,150),(640,150),(255,0,0),1)
    cv2.line(img,(0,250),(640,250),(255,0,0),1)
    cv2.line(img,(200,0),(200,480),(255,0,0),1)
    cv2.line(img,(300,0),(300,480),(255,0,0),1)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        print(x)
        print(y)
        print(w)
        print(h)
        if x<200 and w>200 and w<250:
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            pos=mc.player.getTilePos()
            mc.postToChat("right")
        elif x>300 and w>200 and w<250:
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            pos=mc.player.getTilePos()
            mc.postToChat("left")
        elif y<150 and w>200 and w<250:
            mc.player.setTilePos(pos.x,pos.y+1,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("up")
        elif y>250 and w>200 and w<250:
            mc.player.setTilePos(pos.x,pos.y-1,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("down")
        elif w>250:
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("ahead")
        elif w<200:
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("back")
        else:
            mc.postToChat("stop")

    cv2.imshow('img',img)
    print(img.shape)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()

video：https://www.bilibili.com/video/BV1KV411H7ag/
