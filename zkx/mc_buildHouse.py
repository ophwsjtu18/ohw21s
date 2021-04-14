import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()
print("player pos is", pos)


class House():
    def __init__(self, name, x0, y0, z0, l, w, h):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.l = l
        self.w = w
        self.h = h

    def buildHouse(self):
        print("I will build house on", self.x0, self.y0, self.z0)

        # build my floor in made of wood
        for i in range(self.l+1):
            for j in range(self.w+1):
                mc.setBlock(self.x0 + i, self.y0 - 1, self.z0 + j, 5)

        # build my wall in made of TNT and stone
        for j in range(self.h):
            if j % 2:
                wall = 46
            else:
                wall = 1
            for i in range(self.l):
                mc.setBlock(self.x0 + i, self.y0 + j, self.z0, wall)
            for i in range(self.w):
                mc.setBlock(self.x0, self.y0 + j, self.z0 + i, wall)
            for i in range(self.l):
                mc.setBlock(self.x0 + i, self.y0 + j, self.z0 + 15, wall)
            for i in range(self.w + 1):
                mc.setBlock(self.x0 + 10, self.y0 + j, self.z0 + i, wall)

        # build my roof in made of glass
        for i in range(self.l+1):
            for j in range(self.w+1):
                mc.setBlock(self.x0 + i, self.y0 + 4, self.z0 + j, 20)

        # set the door
        mc.setBlock(self.x0 + self.l/3, self.y0, self.z0, 0)
        mc.setBlock(self.x0 + self.l/3, self.y0 + 1, self.z0, 0)

        # Build window in the middle of tine glass
        mc.setBlock(self.x0, self.y0 + self.h/2, self.z0 + self.w/3, 102)
        mc.setBlock(self.x0, self.y0 + self.h/2-1, self.z0 + self.w/3, 102)
        mc.setBlock(self.x0, self.y0 + self.h/2, self.z0 + self.w/3+1, 102)
        mc.setBlock(self.x0, self.y0 + self.h/2-1, self.z0 + self.w/3+1, 102)

    def isInHome(self, x, y, z):
        if self.x0 < x < self.x0 + self.l and self.y0 < y < self.y0 + self.h and self.z0 < z < self.z0 + self.w:
            return True
        else:
            return False


houses = []
house1 = House("me", pos.x, pos.y, pos.z, 10, 15, 4)
house2 = House("you", pos.x + 20, pos.y, pos.z, 10, 15, 4)
houses.append(house1)
houses.append(house2)
house1.buildHouse()
house2.buildHouse()

while True:
    time.sleep(3)
    pos = mc.player.getTilePos()
    if house1.isInHome(pos.x, pos.y, pos.z):
        mc.postToChat("welcome " + house1.name + "'s home")
        stayed_time = stayed_time + 1
    elif house2.isInHome(pos.x, pos.y, pos.z):
        mc.postToChat("welcome " + house2.name + "'s home")
        stayed_time = stayed_time + 1
    else:
        stayed_time = 0
