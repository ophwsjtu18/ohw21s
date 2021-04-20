from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

def buildHouse(x0,y0,z0,l, w, h):
    #建造外墙
    for y in range(6):
        if y%2 == 0:
            m =1
        else :
            m = 46
        for x in range(l):
            mc.setBlock(x0+x,y0+h,z0,m)
            mc.setBlock(x0+x,y0+h,z0+15,m)
        for z in range(w):
            mc.setBlock(x0,y0+h,z0+z,m)
            mc.setBlock(x0+10,y0+h,z0+z,m)
    #建造地基
    for x in range(l-1):
        for z in range(w-1):
            mc.setBlock(x0+x+1,y0,z0+z+1,35,2)
    #建造屋顶
    for x in range(l+1):
        for z in range(w+1):
            mc.setBlock(x0+x,y0+h,z0+z,20)
    #挖门
    mc.setBlock(x0+5,y0+2,z0,0)
    mc.setBlock(x0+5,y0+1,z0,0)
    mc.setBlock(x0+5,y0+3,z0,0)
stayed_time=0

class House():
    def __init__(self , name , x0 ,y0 ,z0,l ,w ,h):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.l = l
        self.w = w
        self.h = h
        print('I will build a house named ',self.name)
    def buildWall(self):
        print ('I will build a wall on ',self.x0,self.y0,self.z0)
        #建造外墙
        for y in range(self.h):
            if y%2 == 0:
                m =1
            else :
                m = 46
            for x in range(self.l):
                mc.setBlock(self.x0+x,self.y0+y,self.z0,m)
                mc.setBlock(self.x0+x,self.y0+y,self.z0+self.w,m)
            for z in range(self.w):
                mc.setBlock(self.x0,self.y0+y,self.z0+z,m)
                mc.setBlock(self.x0+self.l,self.y0+y,self.z0+z,m)
        #建造地基
        for x in range(self.l-1):
            for z in range(self.w-1):
                mc.setBlock(self.x0+x+1,self.y0,self.z0+z+1,35,2)
        #建造屋顶
        for x in range(self.l+1):
            for z in range(self.w+1):
                mc.setBlock(self.x0+x,self.y0+self.h,self.z0+z,20)
        #挖门
        mc.setBlock(self.x0+5,self.y0+2,self.z0,0)
        mc.setBlock(self.x0+5,self.y0+1,self.z0,0)
        mc.setBlock(self.x0+5,self.y0+3,self.z0,0)
    def isInHome(self , x1,y1,z1):
        if self.x0 <x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y1<y0<self.y0+self.h:
            return True
        else:
            return False
houses = []
house1 = House('Peter' , pos.x,pos.y,pos.z,10,15,10)
house2 = House('tom' , pos.x+20,pos.y,pos.z,12,12,12)
houses.append(house1)
houses.append(house2)
house1.buildWall()
house2.buildWall()

#buildHouse(pos.x,pos.y,pos.z,1,23,4)
#buildHouse(pos.x+20,pos.y,pos.z,1,23,4)
#buildHouse(pos.x+40,pos.y,pos.z,1,23,4)

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(10)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            print ('welcome to '+house.name+'\'s home')
    if pos.x==-30 and pos.z==-40 and pos.y==-6:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-32,9,-45)
            stayed_time=0
    else:
        stayed_time=0
        
     
