from mcpi.minecraft import Minecraft
import numpy as np
import cv2
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
class House():
    def __init__(self,name,x0,y0,z0,l,h,w):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.z0=z0
        self.l=l
        self.w=w
        self.h=h
        print("I willl build a house named",self.name)
    def buildWall(self):
        print("I will build wall on",self.x0,self.y0,self.z0)
        for y in range(self.h):
            if y%2==0:
                m=46
            else:
                m=1
            
            for i in range(self.l):
                mc.setBlock(self.x0+i,self.y0+y,self.z0,m)
                mc.setBlock(self.x0+i,self.y0+y,self.z0+self.w-1,m)
            for j in range(self.w):
                mc.setBlock(self.x0,self.y0+y,self.z0+j,m)
                mc.setBlock(self.x0+self.l-1,self.y0+y,self.z0+j,m)
    def buildFloor(self):
        for i in range(self.l-2):
            for j in range(self.w-2):
                mc.setBlock(self.x0+i+1,self.y0,self.z0+1+j,17)
    def buildUp(self):
        for i in range(self.l-2):
            for j in range(self.w-2):
                mc.setBlock(self.x0+i+1,self.y0+self.h-1,self.z0+j+1,20)
    def buildDoor(self):
        for j in range(2):
            mc.setBlock(self.x0,self.y0+j+1,self.z0+int(self.w/2)-1,0)
    def buildWindow(self):
        for i in range(2):
            for j in range(2):
                mc.setBlock(self.x0+i+int(self.l/2)-1,self.y0+j+int(self.h/2)-1,self.z0,20)
    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y0<y1<self.y0+self.h:
            return True
        else:
            return False
        
house1=House("Satori",pos.x,pos.y,pos.z,40,20,50)
house2=House("Koishi",pos.x,pos.y+30,pos.z,10,6,15)
house1.buildWall()
house2.buildWall()
house1.buildFloor()
house2.buildFloor()
house1.buildUp()
house2.buildUp()
house1.buildDoor()
house2.buildDoor()
house1.buildWindow()
house2.buildWindow()




houses=[]
houses.append(house1)
houses.append(house2)

while True:
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    for house in houses:
        if(house.isInHome(pos.x,pos.y,pos.z)):
            print("Welcome to",house.name,"home")
'''
def buildHouse(x0,y0,z0,l,w,h):


    #Build Wall
    
    for y in range(6):
        if y%2==0:
            m=46
        else:
            m=1
        
        for i in range(10):
            mc.setBlock(x0+i,y0+y,z0,m)
            mc.setBlock(x0+i,y0+y,z0+14,m)
        for j in range(15):
            mc.setBlock(x0,y0+y,z0+j,m)
            mc.setBlock(x0+9,y0+y,z0+j,m)

    #Build floor in wood
    for i in range(8):
        for j in range(13):
            mc.setBlock(x0+i+1,y0,z0+1+j,17)

    #Build
    for i in range(8):
        for j in range(13):
            mc.setBlock(x0+i+1,y0+5,z0+j+1,20)
    # get door
    for i in range(2):
        for j in range(2):
            mc.setBlock(x0,y0+j+1,z0+i+6,0)
            mc.setBlock(x0+i+3,y0+j+2,z0,20)
'''


