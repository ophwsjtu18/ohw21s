import numpy as np
import cv2
from mcpi import minecraft
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

pos=mc.player.getPos()




cap=cv2.VideoCapture(0)

 # When everything done, relea
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
a=0
b=0
while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()
  img = cv2.cvtColor(frame,1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    if x<150:
        a = a+0.3
    else:
         if x>300:
            a = a-0.3
    if y<100:
        b = b+0.3
    else:
        if y>180:
            b = b-0.3
    mc.player.setPos(pos.x+a,pos.y,pos.z+b)
  cv2.imshow('frame',img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
