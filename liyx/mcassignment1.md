    from mcpi.minecraft import Minecraft
    import time
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    dic=0
    mc=Minecraft.create()

    pos=mc.player.getTilePos()
    print("player pos is",pos)
    mc.player.setDirection(1,0,0)
    mc.player.setTilePos(-32,9,-45)

    stayed_time=0
    while True:
        '''print("stay_time"+str(stayed_time))
        time.sleep(0.5)'''
        pos=mc.player.getTilePos()
        '''mc.postToChat("please go to home x=-30 y=-6 z=-40 for 15s to fly")'''
        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
        ret, frame = cap.read()
        faces=face_cascade.detectMultiScale(frame,1.3,5)
        for(x,y,w,h) in faces:
            print(x,y,w,h)
            if x<200:
                dic=(dic+1)%4
                time.sleep(0.5)
            elif x>300:
                dic=(dic-1)%4
                time.sleep(0.5)

            if(dic==0):
                mc.player.setDirection(1,0,0)
                time.sleep(0.5)
            elif(dic==1):
                mc.player.setDirection(0,0,1)
                time.sleep(0.5)
            elif(dic==2):
                mc.player.setDirection(-1,0,0)
                time.sleep(0.5)
            elif(dic==3):
                mc.player.setDirection(0,0,-1)
                time.sleep(0.5)
            
            if y>200:
                mc.player.setTilePos(pos.x,pos.y-1,pos.z)
                time.sleep(0.5)
            elif y<150:
                mc.player.setTilePos(pos.x,pos.y+1,pos.z)
                time.sleep(0.5)
            if w*h>250*250:
                if(dic==0):
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                    time.sleep(0.5)
                elif(dic==1):
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                    time.sleep(0.5)
                elif(dic==2):
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                    time.sleep(0.5)
                elif(dic==3):
                    mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                    time.sleep(0.5)
            elif w*h<200*200:
                if(dic==0):
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                    time.sleep(0.5)
                elif(dic==1):
                    mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                    time.sleep(0.5)
                elif(dic==2):
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                    time.sleep(0.5)
                elif(dic==3):
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                    time.sleep(0.5)
            print(dic)
            '''cv2.imshow('frame',frame)'''
        '''if pos.x==-30 and pos.z==-40 and pos.y==-6:
            mc.postToChat("welcome home")
            stayed_time=stayed_time+1
            if stayed_time>=30:
                mc.player.setTilePos(-32,9,-45)
                stayed_time=0
        else:
            stayed_time=0
        time.sleep(0.5)'''
        '''ret, frame = cap.read()
        faces=face_cascade.detectMultiScale(frame,1.3,5)
        for(x,y,w,h) in faces:
            if x<220:
                dic=(dic+1)%4
            elif x>260:
                dic=(dic-1)%4
            print(dic)
            cv2.imshow('frame',frame)
            print(x,y,w,h)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break'''


    cap.release()
    cv2.destroyAllWindows()

        
     


    ![qq](https://github.com/ophwsjtu18/ohw21s/blob/main/liyx/QQ%E6%88%AA%E5%9B%BE20210410185240.png)
    ps. 在实际操作过程中因为电脑配置或者什么其他的原因，无法在操作mc的同时加载出电脑的摄像头监视器，所以只能在视频中加批注表现；在用头操作向后的过程中，因为不知道画面后面有啥，所以出现了穿     模的情况
    还有的一点遗憾是在单独操作的过程中不可避免地会改变与当前参数无关的参量，所以导致有的时候mc里的人物跟抽风了一样。。。
