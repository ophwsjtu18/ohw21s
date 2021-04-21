from mcpi.minecraft import Minecraft
import time


mc = Minecraft.create()


pos = mc.player.getTilePos()
print("player pos is", pos)


class House():
    def __init__(self,name,x0,y0,z0,l,w,h):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.h = h
        self.w = w
        self.l = l
        mc.postToChat(f'I will built a house named {self.name}on{x0},{y0},{z0}')
    
    def buildWall(self):
            
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x0+x, self.y0, self.z0+z, 5)

        for l in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x0+x, self.y0+self.h, self.z0+z, 41)
        
        
        
        for y in range(self.h):
            for x in range(self.l):
                if x % 2 == 0 and y % 2 == 0:
                    material = 46
                else:
                    material = 41
                mc.setBlock(self.x0+x, self.y0+y, self.z0, material)
                mc.setBlock(self.x0+x, self.y0+y, self.z0+self.w, material)
            for z in range(self.w):
                if z % 2 == 0 and y % 2 == 0:
                    material = 46
                else:
                    material = 41
                mc.setBlock(self.x0, self.y0+y, self.z0+z, material)
                mc.setBlock(self.x0+self.l, self.y0+y, self.z0+z, material)
        
        for y in range(3):
            mc.setBlock(self.x0+int(self.l/2), self.y0+y+1, self.z0, 0)

        for x in range(2):
            for y in range(2):
                mc.setBlock(self.x0+int(self.l/2-1)+x, self.y0+int(self.h/2)+y, self.z0+self.w, 95)
    
    
    
    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y0<y1<self.y0+self.h:
            return True
        else:
            return False



'''
def build_house(x0,y0,z0):

    for x in range(13):
        for z in range(10):
            mc.setBlock(x0+x, y0, z0+z, 5)

    for x in range(13):
        for z in range(10):
            mc.setBlock(x0+x, y0+6, z0+z, 41)

    for y in range(6):
        for x in range(13):
            if x % 2 == 0 and y % 2 == 0:
                material = 46
            else:
                material = 41
            mc.setBlock(x0+x, y0+y, z0, material)
            mc.setBlock(x0+x, y0+y, z0+9, material)
        for z in range(10):
            if z % 2 == 0 and y % 2 == 0:
                material = 46
            else:
                material = 41
            mc.setBlock(x0, y0+y, z0+z, material)
            mc.setBlock(x0+12, y0+y, z0+z, material)

    for y in range(3):
        mc.setBlock(x0+6, y0+y+1, z0, 0)

    for x in range(2):
        for y in range(2):
            mc.setBlock(x0+5+x, y0+2+y, z0+9, 95)


for x in range(3):
    build_house(pos.x+20*x,pos.y,pos.z)
'''

houses=[]
house1=House("peter",pos.x,pos.y,pos.z,10,6,15)
house2=House("tom",pos.x+20,pos.y,pos.z,10,6,15)
houses.append(house1)
houses.append(house2)
print("house1 name is",house1.name)
print("house2 name is",house2.name)
house1.buildWall()
house2.buildWall()


'''
def buildHouse(x0,y0,z0,l,w,h):
    #Build wall

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


buildHouse(pos.x,pos.y,pos.z,10,10,15)
buildHouse(pos.x+20,pos.y,pos.z,10,10,15)
buildHouse(pos.x+40,pos.y,pos.z,10,10,15)

'''
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
        else:
            stayed_time=0


