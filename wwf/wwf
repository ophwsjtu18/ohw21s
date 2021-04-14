from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)
def buildHouse (x0,y0,z0,l,w,h):
  for a in range(l):
    for b in range(w):
      mc.setBlock(x0+a,y0,z0+b,5)
      mc.setBlock(x0+a,y0+h,z0+b,95)
  #build wall
  for y in range(h):
    for x in range(l):
      mc.setBlock(x0+x,y0+y,z0,1)
      mc.setBlock(x0+x,y0+y,z0+w,1)
      if y%2 ==0:
        mc.setBlock(x0+x,y0+y,z0,46)
        mc.setBlock(x0+x,y0+y,z0+w,46)
    for z in range(w):
      mc.setBlock(x0,y0+y,z0+z,1)
      mc.setBlock(x0+l,y0+y,z0+z,1)
      if y%2 ==0:
         mc.setBlock(x0,y0+y,z0+z,46)
         mc.setBlock(x0+l,y0+y,z0+z,46)
  for a in range(h-2):
    mc.setBlock(x0+l/2,y0+a,z0,0)
    mc.setBlock(x0+l/2+1,y0+a,z0,0)
  #Build window in the middle of z
    mc.setBlock(x0+l,y0+h/2,z0+w/2,20)
    mc.setBlock(x0+l,y0+h/2+1,z0+w/2,20)
    mc.setBlock(x0+l,y0+h/2,z0+w/2+1,20)
    mc.setBlock(x0+l,y0+h/2+1,z0+w/2+1,20)
class House():
    def __init__(self,name,x0,y0,z0,l,w,h):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.z0=z0
        self.l=l
        self.w=w
        self.h=h
        print("I will build a house name",self.name)
    def buildWall(self,):
        print("I will buildwall on",self.x0,self.y0,self.z0)
        buildHouse(self.x0,self.y0,self.z0,self.l,self.h,self.w)

    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w:
            return True
        else:
            return False
houses=[]        
house1=House("peter",pos.x,pos.y,pos.z,10,6,15)
house2=House("tom",pos.x+20,pos.y,pos.z,10,6,15)
houses.append(house1)
houses.append(house2)
print("house name is",house1.name)
print("house name is",house2.name)
house1.buildWall()
house2.buildWall()



stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for house in houses:
       if house.isInHome(pos.x,pos.y,pos.z):
          print("Welcome to "+house.name+"'s home")
    if pos.x==-30 and pos.z==-40 and pos.y==-6:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-32,9,-45)
            stayed_time=0
    else:
        stayed_time=0
        
