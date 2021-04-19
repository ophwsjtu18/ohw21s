from mcpi.minecraft import Minecraft

mc=Minecraft.create()

class House():
    def __init__(self,name,x0,y0,z0,l,w,h):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.l = l
        self.w = w
        self.h = h
        print("I will build a house named", self.name)
    def buildWall(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        l = self.l
        w = self.w
        h = self.h
        # Build the wall
        for y in range(h):
            if y % 2 ==0:
                m = 46
            else:
                m = 1
            for x in range(w):
                mc.setBlock(x0+x,y0+y,z0,m)
                mc.setBlock(x0+x,y0+y,z0+l-1,m)
            for z in range(l):
                mc.setBlock(x0,y0+y,z0+z,m)
                mc.setBlock(x0+w-1,y0+y,z0+z,m)
    def buildFloor(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        l = self.l
        w = self.w
        h = self.h
        mc.setBlocks(x0+1,y0,z0+1, x0+w-2, y0, z0 + l-2, 5)
    def buildRoof(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        l = self.l
        w = self.w
        h = self.h
        mc.setBlocks(x0+1,y0+h-1,z0+1, x0+w-2, y0+h-1, z0 + l-2, 20)
    def buildDoor(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        l = self.l
        w = self.w
        h = self.h
        mc.setBlocks(x0,y0+1,z0+int(l/2)-1,x0,y0+3,z0+int(l/2)-1,0)
    def buildWindow(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        l = self.l
        w = self.w
        h = self.h
        mc.setBlocks(x0,y0+4,z0+int(l/2)+2,x0,y0+5,z0+int(l/2)+3,20)
    def buildHouse(self):
        self.buildWall()
        self.buildFloor()
        self.buildRoof()
        self.buildDoor()
        self.buildWindow()
    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.w and self.z0<z1<self.z0+self.l and self.y0<y1<self.y0+self.h:
            return True
        else:
            return False

pos=mc.player.getPos()

print("player pos is",pos)

houses=[]
house1=House("Peter",pos.x,pos.y,pos.z,10,6,15)
house2=House("Tom",pos.x+20,pos.y,pos.z,10,6,15)
houses.append(house1)
houses.append(house2)
house1.buildHouse()
house2.buildHouse()
print("house1 name is",house1.name)
print("house2 name is",house2.name)


while True:
    pos=mc.player.getPos()
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            mc.postToChat("I am in %s's house!"%(house.name))
            break