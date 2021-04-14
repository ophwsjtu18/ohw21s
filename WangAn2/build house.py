from mcpi.minecraft import Minecraft
import time
import serial
mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)


            
def buildhouse(x0,y0,z0,l,w,h):#
    for y in range (6):#build wall
        if y%2==1:
            m=46
        else:
            m=100
        for x in range(10):
            
            mc.setBlock(x0+x,y0+y,z0,m)
            mc.setBlock(x0+x,y0+y,z0+14,m)
        for x in range(15):
            mc.setBlock(x0,y0+y,z0+x,m)
            mc.setBlock(x0+9,y0+y,z0+x,m)
            
    for x in range(10):#build floor
        for z in range(15):
             mc.setBlock(x0+x,y0,z0+z,17)
             
    for x in range(10):#roof
        for z in range(15):
             mc.setBlock(x0+x,y0+6,z0+z,20)
             
    mc.setBlock(x0+5,y0+2,z0,0)#door
    mc.setBlock(x0+5,y0+1,z0,183)
    mc.setBlock(x0+4,y0+2,z0,0)#door
    mc.setBlock(x0+4,y0+1,z0,183)
    mc.setBlock(x0+3,y0+2,z0-1,151)
    mc.setBlock(x0+6,y0+2,z0-1,151)
    
    mc.setBlock(x0+9,y0+1,z0+1,20)#window
    mc.setBlock(x0+9,y0+1,z0+2,20)
    mc.setBlock(x0+9,y0+2,z0+1,20)
    mc.setBlock(x0+9,y0+2,z0+2,20)

class House ():#
    def __init__(self,name,x0,y0,z0,l,w,h):
            self.name=name
            self.x0=x0
            self.y0=y0
            self.z0=z0
            self.l=l
            self.w=w
            self.h=h
            print("I will build a house named" ,self.name)
    def buildwall(self):
        print("I will buildwall on",self.x0,self.y0,self.z0)
        for y in range (self.h):#build wall
            if y%2==1:
                m=46
            else:
                m=100
            for x in range(self.l):
                
                mc.setBlock(self.x0+x,self.y0+y,self.z0,m)
                mc.setBlock(self.x0+x,self.y0+y,self.z0+self.w-1,m)
            for x in range(self.w):
                mc.setBlock(self.x0,self.y0+y,self.z0+x,m)
                mc.setBlock(self.x0+self.l-1,self.y0+y,self.z0+x,m)
    def isinhome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y0<y1<self.y0+self.h:
            return True
        else:
            return False
    def floor(self):
        for x in range(self.l):#build floor
            for z in range(self.w):
                mc.setBlock(self.x0+x,self.y0,self.z0+z,17)
    def roof(self):
        for x in range(self.l):#roof
            for z in range(self.w):
                mc.setBlock(self.x0+x,self.y0+self.h,self.z0+z,20)
    def door(self):
        if (self.l%2)==1:
            m=(self.l-1)/2
        else:
            m=self.l/2
        mc.setBlock(self.x0+m,self.y0+2,self.z0,0)#door
        mc.setBlock(self.x0+m,self.y0+1,self.z0,183)
        mc.setBlock(self.x0+m-1,self.y0+2,self.z0,0)#door
        mc.setBlock(self.x0+m-1,self.y0+1,self.z0,183)
    def window(self):
        if (self.w%2)==1:
            m=(self.w-1)/2
        else:
            m=self.w/2
        if (self.h%2)==1:
            n=(self.h-1)/2
        else:
            n=self.h/2
        mc.setBlock(self.x0+self.l-1,self.y0+n,self.z0+m-1,20)#window
        mc.setBlock(self.x0+self.l-1,self.y0+n,self.z0+m,20)
        mc.setBlock(self.x0+self.l-1,self.y0+n-1,self.z0+m-1,20)
        mc.setBlock(self.x0+self.l-1,self.y0+n-1,self.z0+m,20)
        
#buildhouse(pos.x,pos.y,pos.z,1,1,1)
#buildhouse(pos.x+20,pos.y,pos.z,1,1,1)
#buildhouse(pos.x+40,pos.y,pos.z,1,1,1)
houses=[]
house1=House("xu hua shuai",pos.x,pos.y,pos.z,30,30,12)
house2=House("ma yue ran",pos.x+60,pos.y,pos.z,20,7,22)
houses.append(house1)
houses.append(house2)

house1.buildwall()
house1.floor()
house1.roof()
house1.door()
house1.window()

house2.buildwall()
house2.floor()
house2.roof()
house2.door()
house2.window()


while True:
   
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    
    for house in houses:
        if house.isinhome(pos.x,pos.y,pos.z):
            print("Welcome to "+house.name+" home")
            mc.postToChat("Welcome to "+house.name+" home")
            
           
     
