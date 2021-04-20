from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

class House():
    def __init__(self,name,x0,y0,z0,l,w,h):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.z0=z0
        print("I will build a house named",self.name)
    def buildWall(self):
        print("I will buildwall on",self.x0,self.y0,self.z0)
        for y in range(6):
                if y%2==0:
                    m=17
                else:
                    m=5
                for x in range(10):
                    mc.setBlock(self.x0+x,self.y0+y,self.z0,m)
                    mc.setBlock(self.x0+x,self.y0+y,self.z0+15,m)
                for z in range(15):
                    mc.setBlock(self.x0,self.y0+y,self.z0+z,m)
                    mc.setBlock(self.x0+10,self.y0+y,self.z0+z,m)
                    
        for x in range(10):
            for z in range(15):
                mc.setBlock(self.x0+x,self.y0+6,self.z0+z,20)
                mc.setBlock(self.x0+x,self.y0,self.z0+z,35)

        #Build door in the middle of x
        mc.setBlock(self.x0+5,self.y0+3,self.z0,0)
        mc.setBlock(self.x0+5,self.y0+2,self.z0,0)

        #Build window in the middle of z
        mc.setBlock(self.x0+10,self.y0+3,self.z0+7,20)
        mc.setBlock(self.x0+10,self.y0+4,self.z0+7,20)
        mc.setBlock(self.x0+10,self.y0+3,self.z0+8,20)
        mc.setBlock(self.x0+10,self.y0+4,self.z0+8,20)
        
    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+l and self.z0<z1<self.z0+w:
            return True
        else:
            return False
        
houses=[]
house1=House("peter",pos.x,pos.y,pos.z,10,6,15)
house2=House("tom",pos.x+20,pos.y,pos.z,10,6,15)
houses.append(house1)
houses.append(house2)
print("house1 name is",house1.name)
print("house2 name is",house2.name)
house1.buildWall()
house2.buildWall()



def buildHouse(x0,y0,z0,l,w,h):
    #Build wall
    for y in range(6):
        if y%2==0:
            m=46
        else:   
            m=1
        for x in range(10): 
            mc.setBlock(x0+x,y0+y,z0,m)
            mc.setBlock(x0+x,y0+y,z0+15,m)
        for z in range(15):
            mc.setBlock(x0,y0+y,z0+z,m)
            mc.setBlock(x0+10,y0+y,z0+z,m)
    #Build floor in wool
    for x in range(10):
        for z in range(15):
            mc.setBlock(x0+x,y0,z0+z,35,2)

    #Build roof in glass
    for x in range(10):
        for z in range(15):
            mc.setBlock(x0+x,y0+6,z0+z,20)

    #Build door in the middle of x
    mc.setBlock(x0+5,y0+1,z0,0)
    mc.setBlock(x0+5,y0+2,z0,0)

    #Build window in the middle of z
    mc.setBlock(x0+10,y0+3,z0+7,20)
    mc.setBlock(x0+10,y0+4,z0+7,20)
    mc.setBlock(x0+10,y0+3,z0+8,20)
    mc.setBlock(x0+10,y0+4,z0+8,20)


'''buildHouse(pos.x,pos.y,pos.z,10,10,15)
buildHouse(pos.x+20,pos.y,pos.z,10,10,15)
buildHouse(pos.x+40,pos.y,pos.z,10,10,15)'''

stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            print("Welcome to "+house.name+" home")
    if pos.x==-30 and pos.z==-40 and pos.y==-6:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-32,9,-45)
            stayed_time=0
    else:
        stayed_time=0
        
     
