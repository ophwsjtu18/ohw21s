from mcpi.minecraft import Minecraft
import cv2
import numpy as np


mc = Minecraft.create()
position = mc.player.getPos()
mc.postToChat("Welcome to mc")
mc.postToChat("player pos is:" + str(position))

def move(action):

    pos = mc.player.getPos()
    mc.postToChat(action)
    if action == 'left':
        mc.player.setPos(pos.x + 0.5, pos.y, pos.z)
        
    elif action == 'right':
        mc.player.setPos(pos.x - 0.5, pos.y, pos.z)
        
    elif action == 'forward':
        mc.player.setPos(pos.x, pos.y, pos.z + 0.5)
        
    elif action == 'back':
        mc.player.setPos(pos.x, pos.y, pos.z - 0.5)
        
    elif action == 'up':
        mc.player.setPos(pos.x, pos.y + 0.5, pos.z)
        
    elif action == 'down':
        mc.player.setPos(pos.x, pos.y - 0.5, pos.z)
        
    else:
        pass

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    img=cv2.flip(img,1)
    img_wd = img.shape[0]
    img_len = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        head = y
        foot = img_wd - head - h
        left = x
        right = img_len - left - w
        if x + w > int(img_len * 0.85):
            move('rightt')
            
        elif x < int(img_len * 0.15):
            move('left')
        
        elif y + h > int(img_wd * 0.85) and not y < int(img_wd * 0.15):
            move('down')
        
        elif y < int(img_wd * 0.15) and not y + h > int(img_wd * 0.85):
            move('up')
        
        elif y < int(img_wd * 0.5) and y + h > int(img_wd * 0.75):
            move('forward')
        
        elif y > int(img_wd * 0.5) and y + h < int(img_wd * 0.75):
            move('back')
        
        else:
            move('pass')
        

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
