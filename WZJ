from mcpi.minecraft import Minecraft
import numpy as np
import math
import time
import cv2


mc=Minecraft.create()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    img = cv2.cvtColor(frame,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #print(x,',',y,',',w,',',h)
   
    pos=mc.player.getPos()
    di=mc.player.getDirection()
    
    l=math.sqrt(di.x*di.x+di.z*di.z)
    dx=di.x/l*0.40
    dz=di.z/l*0.40

    x=pos.x
    y=pos.y
    z=pos.z
    flag = False
    
    if len(faces)==1:
    #left
        if faces[0][0]+faces[0][2]>=580:
            x+=4*dz
            z-=4*dx
            flag = True
        if faces[0][0]+faces[0][2]>=480 and faces[0][0]+faces[0][2]<580:
            x+=2*dz
            z-=2*dx
            flag = True
    #right
        if faces[0][0]>50 and faces[0][0]<=150:
            x-=2*dz
            z+=2*dx
            flag = True
        if faces[0][0]<=50:
            x-=4*dz
            z+=4*dx
            flag = True
    #back
        if faces[0][2]<=170 and faces[0][2]>150:
            x-=2*dx
            z-=2*dz
            flag = True
        if faces[0][2]<=150:
            x-=4*dx
            z-=4*dz
            flag = True
    #front
        if faces[0][2]>=220 and faces[0][2]<240:
            x+=2*dx
            z+=2*dz
            flag = True
        if faces[0][2]>=240 and faces[0][2]<260:
            x+=4*dx
            z+=4*dz
            flag = True
        if faces[0][2]>=260 :
            x+=6*dx
            z+=6*dz
            flag = True
    #up
        if faces[0][1]<=110:
            y+=0.5
            flag = True
    #down
        if faces[0][1]+faces[0][2]>=400:
            y-=0.5
            flag = True

        if flag == True:
            mc.player.setPos(x,y,z)
    



        xx=faces[0][0]+0.5*faces[0][2]
        yy=faces[0][1]+0.5*faces[0][2]
        ww=0.5*faces[0][2]
    
        cv2.rectangle(img,(int(xx-110),int(yy-110)),(int(xx+110),int(yy+110)),(0,255,0),1)
        cv2.rectangle(img,(int(xx-120),int(yy-120)),(int(xx+120),int(yy+120)),(0,255,255),1)
        cv2.rectangle(img,(int(xx-130),int(yy-130)),(int(xx+130),int(yy+130)),(0,0,255),1)
        cv2.rectangle(img,(int(xx-85),int(yy-85)),(int(xx+85),int(yy+85)),(0,255,0),1)
        cv2.rectangle(img,(int(xx-75),int(yy-75)),(int(xx+75),int(yy+75)),(0,255,255),1)
    
    cv2.line(img,(480,0),(480,500),(0,255,0),1)
    cv2.line(img,(150,0),(150,500),(0,255,0),1)
    

    cv2.line(img,(580,0),(580,500),(0,255,255),1)
    cv2.line(img,(50,0),(50,500),(0,255,255),1)

    cv2.line(img,(0,110),(640,110),(0,255,0),1)
    cv2.line(img,(0,400),(640,400),(0,255,0),1)
    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

