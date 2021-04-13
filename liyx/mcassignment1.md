    from mcpi.minecraft import Minecraft
    import time
    import numpy as np
    import cv2

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    dic=0  //dic用0，1，2，3表示人物在平面内的四个方向
    mc=Minecraft.create()

    pos=mc.player.getTilePos()
    print("player pos is",pos)
    mc.player.setDirection(1,0,0) //设置初始方向
    mc.player.setTilePos(-32,9,-45) //设置初始位置

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
                dic=(dic+3)%4
                time.sleep(0.5) //x的大小决定人物左转或者右转，在200-300内保持不动

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
                time.sleep(0.5) //由初始方向决定了0，1，2，3分别是沿着+x，+z,-x,-z方向
            
            if y>200:
                mc.player.setTilePos(pos.x,pos.y-1,pos.z)
                time.sleep(0.5)
            elif y<150:
                mc.player.setTilePos(pos.x,pos.y+1,pos.z)
                time.sleep(0.5) //y决定了人物的上下位置
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
                    time.sleep(0.5) //人脸的大小决定人物向前或向后走
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

        
     


    ![qq](https://github.com/ophwsjtu18/ohw21s/blob/main/liyx/videowindowscannotopen.png)
    ps. 在实际操作过程中因为电脑配置或者什么其他的原因，无法在操作mc的同时加载出电脑的摄像头监视器(相关图片在文件夹里)，所以只能在视频中加批注表现；在用头操作向后的过程中，因为不知道画面后     面有啥，所以出现了穿模的情况
    还有的一点遗憾是在单独操作的过程中不可避免地会改变与当前参数无关的参量，所以导致有的时候mc里的人物跟抽风了一样。。。
