from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

time.sleep(2)

class house():
    def __init__(self,name,x,y,z,len,wid,hei):
        self.name=name
        self.x=x
        self.y=y
        self.z=z
        self.len=len
        self.wid=wid
        self.hei=hei
        print("I will build a house named {}".format(self.name))
    def buildHouse(self):
        print("I will buildwall on ({},{},{})\n".format(self.x,self.y,self.z))
        print("The house's length,width and height are {},{} and {}".format(self.len,self.wid,self.hei))

        for y in range(self.hei+1):
            for x in range(self.wid):
                for z in range(self.len):
                    if(x % 2==0 or z % 2==0):
                        mc.setBlock(self.x+x,self.y+y,self.z+z,45) #bricks
                    else:
                        mc.setBlock(self.x+x,self.y+y,self.z+z,46) #TNT
                    if(y==self.hei):
                        mc.setBlock(self.x+x,self.y+y,self.z+z,95,1) #roof
        time.sleep(1)

        for y in range(self.hei):
            for x in range(self.wid-2):
                for z in range(self.len-2):
                    if(y==0):
                        if(x%2==0 or z%2==0):
                            mc.setBlock(self.x+1+x,self.y+y,self.z+1+z,5,2)    #wooden floor
                        else:
                            mc.setBlock(self.x+x+1,self.y+y,self.z+z+1,46) #TNT
                    else:
                        mc.setBlock(self.x+1+x,self.y+y,self.z+1+z,0)
        time.sleep(1)

        #door
        for z in range(2):
            for y in range(2):
                mc.setBlock(self.x,self.y+y+1,self.z+self.len/2-1+z,0)
        time.sleep(2)

        #windows
        for z in range(int(self.len/3)):
            for y in range(int(self.hei/2)):
                mc.setBlock(self.x,self.y+1+y,self.z+1+z,95,1)
                mc.setBlock(self.x,self.y+1+y,self.z+self.len/2+2+z,95,1)
        for x in range(self.wid-2):
            for y in range (self.hei-2):
                if(x==int((self.wid-2)/2)):
                    material=46
                else:
                    material=95
                mc.setBlock(self.x+1+x,self.y+1+y,self.z,material,2)
                mc.setBlock(self.x+1+x,self.y+1+y,self.z+self.len-1,material,2)
        time.sleep(2)

        mc.player.setTilePos(self.x,self.y+1,self.z+self.len/2)

    def isInsideHouse(self):
        mc.player.setTilePos(self.x,self.y+1,self.z+self.len/2)
        pos=mc.player.getTilePos()
        print("player pos is",pos)

        stayed_time=0
        all_time=0
        while True:
            all_time+=1
            mc.postToChat("Stay time: {}s".format(stayed_time))
            print("stay_time"+str(stayed_time))
            time.sleep(0.5)
            pos=mc.player.getTilePos()
            mc.postToChat("please go to somebody's house")
            mc.postToChat("x:"+str(pos.x)+" y:"+str(pos.y)+" z:"+str(pos.z)) 
            if self.x<=pos.x<=(self.x+self.wid) and self.z <=pos.z<= (self.z+self.len) and self.y <=pos.y <= (self.y+self.hei):
                stayed_time=stayed_time+1
                if stayed_time>=10:
                    mc.postToChat("welcome to {}'s home".format(self.name))
                    stayed_time=0
                    return True
            else:
                stayed_time=0
            if(all_time>30):
                return False

house1=house("Peter",-220,11,146,15,8,10)
house2=house("Tom",-260,11,146,14,10,6)
print("house1's name is {}".format(house1.name))
print("house2's name is {}".format(house2.name))
house1.buildHouse()

time.sleep(2)
house2.buildHouse()

flag1=house1.isInsideHouse()
flag2=house2.isInsideHouse()
if flag1:
    print("You are in {}'s house.".format(house1.name))
if flag2:
    print("You are in {}'s house.")
if not flag1 and not flag2:
    print("You are out of the house")