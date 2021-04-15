from mcpi.minecraft import Minecraft
import serial
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

class House():
    def __init__(self,name,x0,y0,z0):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        print("I will build a house named",self.name)
    def buildwall(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
        print('I will build walls on',self.x0,self.y0,self.z0)
        for y in range(h):
            for i in range(w):
                mc.setBlock(self.x0+i,self.y0+y,self.z0,1)
                mc.setBlock(self.x0+i,self.y0+y,self.z0+l,1)
            for i in range(l):
                mc.setBlock(self.x0,self.y0+y,self.z0+i,1)
                mc.setBlock(self.x0+w-1,self.y0+y,self.z0+i,1)
    def buildroof(self):
        for x in range(self.w):
            for z in range (self.l+1):
                mc.setBlock(self.x0+x,self.y0+self.h,self.z0+z,20)
    def buildfloor(self):
        for x in range(self.w):
            for z in range (self.l+1):
                mc.setBlock(self.x0+x,self.y0-1,self.z0+z,35,8)
    def builddoor(self):
        for x in range(2):
            for y in range (3):
                mc.setBlock(self.x0+int(self.w/6)+x,self.y0+int(self.h/5)+y,self.z0,0)
    def buildwindow(self):
        for x in range(int(self.w/4)):
            for y in range (int(self.h/3)):
                mc.setBlock(self.x0+int(2/3*self.w)+x,self.y0+int(self.h/2)+y,self.z0,20)
    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y0<y1<self.y0+self.h:
            return True
        else:
            return False

houses = []
house1 = House('aaa',pos.x,pos.y,pos.z)
house2 = House('bbb',pos.x+20,pos.y,pos.z)
houses.append(house1)
houses.append(house2)
for house in houses:
    house.buildwall(30,15,8)
    house.buildfloor()
    house.buildroof()
    house.buildwindow()
    house.builddoor()

def buildhouse(x0,y0,z0,l,w,h):
    #build wall
    for y in range(h):
        for i in range(w):
            mc.setBlock(x0+i,y0+y,z0,1)
            mc.setBlock(x0+i,y0+y,z0+l,1)
        for i in range(l):
            mc.setBlock(x0,y0+y,z0+i,1)
            mc.setBlock(x0+w-1,y0+y,z0+i,1)
    #build floor
    for x in range(w):
        for z in range (l+1):
            mc.setBlock(x0+x,y0-1,z0+z,35,8)
    #build roof
    for x in range(w):
        for z in range (l+1):
            mc.setBlock(x0+x,y0+h,z0+z,20)
    #build door
    for x in range(2):
        for y in range (3):
            mc.setBlock(x0+1+x,y0+1+y,z0,0)
    #build window
    for x in range(2):
        for y in range (2):
            mc.setBlock(x0+5+x,y0+3+y,z0,20)
    #print(mc.getBlock(pos.x,pos.y-1,pos.z))
#for i in range(3):
    #buildhouse(pos.x,pos.y,pos.z+i*20,w,l,w)
stayed_time=0
while True:
    #print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=-h z=-40 for ls to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            print("Welcome to "+house.name+"'s house")
            mc.postToChat("Welcome to "+house.name+"'s house")

    if pos.x==-30 and pos.z==-40 and pos.y==-h:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=12:
            mc.player.setTilePos(-32,w-1,-45)
            ser = serial.Serial("COM5")
            time.sleep(2)
            song = ['1','1','5','5','h','h','5','4','4','3','3','2','2','1']
            for note in song:
        #a = input('please type your cmd here,q for quit, ~ for remote quit :')
                #print(note);
                note = note + 'a'
                ser.write(note.encode())
                time.sleep(2)
            stayed_time=0
    else:
        stayed_time=0




        
     
