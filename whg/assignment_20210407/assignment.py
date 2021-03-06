from mcpi.minecraft import Minecraft
import numpy as np
import cv2
import time

mc = Minecraft.create()

pos = mc.player.getPos()
mc.postToChat("Player pos is " + str(pos))

def move(cmd):
    oneStep = 0.5
    pos = mc.player.getPos()
    mc.postToChat(cmd)
    if cmd == 'left':
        mc.player.setPos(pos.x + oneStep, pos.y, pos.z)
    elif cmd == 'right':
        mc.player.setPos(pos.x - oneStep, pos.y, pos.z)
    elif cmd == 'forward':
        mc.player.setPos(pos.x, pos.y, pos.z + oneStep)
    elif cmd == 'backward':
        mc.player.setPos(pos.x, pos.y, pos.z - oneStep)
    elif cmd == 'up':
        mc.player.setPos(pos.x, pos.y + oneStep, pos.z)
    elif cmd == 'down':
        mc.player.setPos(pos.x, pos.y - oneStep, pos.z)
    elif cmd == 'stay':
        pass

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read()
    width = img.shape[0]
    length = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print('alive')
    for (x,y,w,h) in faces:
        if w < length * 0.3:
            continue
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        head = y
        foot = width - head - h
        left = x
        right = length - left - w
        if y + h > int(width * 0.85) and not y < int(width * 0.15):
            move('down')
        elif y < int(width * 0.15) and not y + h > int(width * 0.85):
            move('up')
        elif y < int(width * 0.15) and y + h > int(width * 0.85):
            move('forward')
        elif y > int(width * 0.25) and y + h < int(width * 0.75):
            move('backward')
        elif x + w > int(length * 0.85):
            move('left')
        elif x < int(length * 0.15):
            move('right')
        else:
            move('stay')
    cv2.rectangle(img, (int(length * 0.15), int(width * 0.15)), (int(length * 0.85), int(width * 0.85)), (0,255,0), 2)
    cv2.rectangle(img, (int(length * 0.25), int(width * 0.25)), (int(length * 0.75), int(width * 0.75)), (0,255,0), 2)
    cv2.imshow('img',cv2.flip(img,1))
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()