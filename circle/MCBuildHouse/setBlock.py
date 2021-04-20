import random

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
We = [
    "Tom",
    "Colin",
    "HW",
    "Mamahaha",
    "Lzm",
    "Cat",
    "Dog",
    "Alice",
    "Kizuna AI",
    "Apple",
    "God",
]


class House:
    def __init__(self, name, length, width, height, pos):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.pos = pos
        self.once = True
        self.build()

    def build(self):
        mc.postToChat("Created %s's house located at: (%s, %s, %s)." % (self.name, self.pos.x, self.pos.y, self.pos.z))
        self.__buildWall__()
        self.__buildFloor__()
        self.__buildRoof__()
        self.__buildDoor__()
        self.__buildWindow__()

    def __buildWall__(self):
        for i in range(1, self.height):
            for j in range(self.length - 1):
                mc.setBlock(self.pos.x + j, self.pos.y + i, self.pos.z, 5)
            for j in range(self.width - 1):
                mc.setBlock(
                    self.pos.x + self.length - 1, self.pos.y + i, self.pos.z + j, 5)
            for j in range(self.length - 1):
                mc.setBlock(
                    self.pos.x + self.length - j - 1,
                    self.pos.y + i,
                    self.pos.z + self.width - 1,
                    5,
                )
            for j in range(self.width - 1):
                mc.setBlock(
                    self.pos.x, self.pos.y + i, self.pos.z + self.width - j - 1, 5
                )

    def __buildFloor__(self):
        for i in range(self.length):  # floor
            for j in range(self.width):
                mc.setBlock(self.pos.x + i, self.pos.y, self.pos.z + j, 100)

    def __buildRoof__(self):
        for i in range(self.length):
            for j in range(self.width):
                mc.setBlock(
                    self.pos.x + i, self.pos.y + self.height - 1, self.pos.z + j, 5
                )

    def __buildDoor__(self):
        for i in range(2):
            for j in range(3):
                mc.setBlock(
                    self.pos.x + self.length / 2 + i, self.pos.y + 1 + j, self.pos.z, 0
                )

    def __buildWindow__(self):
        for i in range(2):
            for j in range(2):
                mc.setBlock(
                    self.pos.x + self.length / 2 + i,
                    self.pos.y + self.height / 2 + j,
                    self.pos.z,
                    101,
                )

    def IsInHome(self, pos):
        if not self.pos.x < pos.x < self.pos.x + self.length - 1:
            return False
        if not self.pos.y < pos.y < self.pos.y + self.height - 1:
            return False
        if not self.pos.z < pos.z < self.pos.z + self.width - 1:
            return False
        return True


Houses = []
for name in We:
    pos = mc.player.getTilePos()
    length = random.randint(10, 15)
    width = random.randint(5, 10)
    height = random.randint(15, 20)
    house = House(name, length, width, height, pos)
    Houses.append(house)
    mc.player.setTilePos(pos.x + 2 * length, pos.y, pos.z + 2 * width)

while True:
    pos = mc.player.getTilePos()
    for house in Houses:
        if house.IsInHome(pos) and house.once:
            mc.postToChat("Welcome to %s's house!" % house.name)
            house.once = False
            break
        elif not house.IsInHome(pos):
            house.once = True
