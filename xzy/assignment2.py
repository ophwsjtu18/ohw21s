from mcpi.minecraft import Minecraft
import numpy as np
import cv2
import time
from pynput.keyboard import Key, Controller

mc=Minecraft.create()
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pos=mc.player.getTilePos()
print("player pos is",pos)
keyboard = Controller()

while True:
    xx = 300
    yy = 300
    ret,frame=cap.read()
    frame = cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        
        if x<250 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            pos=mc.player.getTilePos()
            mc.postToChat("right")
            time.sleep(1)
        elif x>350 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            pos=mc.player.getTilePos()
            mc.postToChat("left")
            time.sleep(1)
        elif y<150 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y+1,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("up")
            time.sleep(1)
        elif y>250 and w>70 and w<110:
            mc.player.setTilePos(pos.x,pos.y-1,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("down")
            time.sleep(1)
        elif w>120:
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("ahead")
            time.sleep(1)
        elif w<80:
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            pos=mc.player.getTilePos()
            mc.postToChat("behind")
            time.sleep(1)


        
    cv2.imshow("frame",frame)
    key=cv2.waitKey(20)

    if key==27:
        break     
cv2.destroyAllWindows()
cap.release()




        
