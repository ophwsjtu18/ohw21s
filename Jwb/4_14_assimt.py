from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

class House():
    def __init__(self,name,x,y,z,len,wid,hei):
        self.name=name
        self.x=x
        self.y=y
        self.z=z
        self.len=len
        self.hei=hei
        self.wid=wid
        print("I will build a house named: ",self.name)
        
    
    def buildWall(self):
        print("I will buildWall on: ",self.x,self.y,self.z)
        for j in range(self.hei):
            if (self.y+j)%2==0:
                m=20
            else:   
                m=41
            for i in range(self.len+1): 
                mc.setBlock(self.x+i,self.y+j,self.z,m)
                mc.setBlock(self.x+i,self.y+j,self.z+self.wid,m)
            for k in range(self.wid+1):
                mc.setBlock(self.x,self.y+j,self.z+k,m)
                mc.setBlock(self.x+self.len,self.y+j,self.z+k,m)
        #please add your real block seting code here
        # for.........
        #   mc.setBlock........
    
    #build roof add your code here
    def buildRoof(self):
        print("I will buildRoof on: ",self.x,self.y,self.z)
        for i in range(self.len+1):
            for j in range(self.wid+1):
                mc.setBlock(self.x+i,self.y+self.hei,self.z+j,57)

    #build floor add your code here
    def buildFloor(self):
        print("I will buildFloor on: ",self.x,self.y,self.z)
        for i in range(self.len+1):
            for j in range(self.wid+1):
                mc.setBlock(self.x+i,self.y-1,self.z+j,20)

    
    def buildLight(self):
        print("I will lighten the house: ",self.x,self.y,self.z)
        for j in range(2,self.hei,2):
            for i in range(2,self.len-1): 
                mc.setBlock(self.x+i,self.y+j,self.z+self.wid-2,89)
            for k in range(2,self.wid-2):
                mc.setBlock(self.x+2,self.y+j,self.z+k,89)
                mc.setBlock(self.x+self.len-2,self.y+j,self.z+k,89)

    def buildDoor(self):
        print("I will builDoor on: ",self.x,self.y,self.z)
        for i in range(int(self.hei/2)):
            for j in range(3):
                mc.setBlock(self.x+int(self.len/2)+j,self.y+i,self.z,0)
                      

    def isInHome(self,x1,y1,z1):
        if self.x<x1<self.x+self.len and self.z<z1<self.z+self.wid and self.y<y1<self.y+self.hei:
            return True
        else:
            return False

    def buildHouse(self):
        print("I will build house on: ",self.x,self.y,self.z)    
        House.buildWall(self)
        House.buildRoof(self)
        House.buildFloor(self)
        House.buildLight(self)
        House.buildDoor(self)



houses=[]
house1=House("Peter",pos.x,pos.y,pos.z,22,11,7)
house2=House("Tom",pos.x+37,pos.y,pos.z,11,22,7)
houses.append(house1)
houses.append(house2)
print("house1 name is",house1.name)
print("house2 name is",house2.name)
house1.buildHouse()
house2.buildHouse()




while True:

    pos=mc.player.getTilePos()
    
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            mc.postToChat("welcome to {}'s home".format(house.name))
            time.sleep(2)
   
