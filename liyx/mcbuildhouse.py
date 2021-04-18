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
          self.l=l
          self.w=w
          self.h=h
          print("I will build house",self.name)

      def buildWall(self):
          for i in range(self.h):
              if i%2==0:
                  q=1
              else:
                  q=46

              for x in range(self.w):
                  mc.setBlock(self.x0+x,self.y0+i,self.z0,q)

              for z in range(self.l):
                  mc.setBlock(self.x0,self.y0+i,self.z0+z,q)

              for m in range(self.l):
                  mc.setBlock(self.x0+self.w,self.y0+i,self.z0+m,q)

              for n in range(self.w+1):
                  mc.setBlock(self.x0+n,self.y0+i,self.z0+self.l,q)

          for x in range(self.w+1):
              for z in range(self.l+1):
                  mc.setBlock(self.x0+x,self.y0,self.z0+z,5)

          for x in range(self.w+1):
              for z in range(self.l+1):
                  mc.setBlock(self.x0+x,self.y0+self.h,self.z0+z,20)

      def buildcellingandfloor(self):
          mc.setBlock(self.x0+self.w//2,self.y0+1,self.z0,0)        
          mc.setBlock(self.x0+self.w//2,self.y0+2,self.z0,0)
          mc.setBlock(self.x0+self.w//2+1,self.y0+1,self.z0,0)        
          mc.setBlock(self.x0+self.w//2+1,self.y0+2,self.z0,0)
          mc.setBlock(self.x0+self.w//2+2,self.y0+3,self.z0,20)
          mc.setBlock(self.x0+self.w//2+2,self.y0+4,self.z0,20)
          mc.setBlock(self.x0+self.w//2+3,self.y0+3,self.z0,20)
          mc.setBlock(self.x0+self.w//2+3,self.y0+4,self.z0,20)

      def isInHome(self,x1,y1,z1):
          if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y0<y1<self.y0+self.h:
              return True
          else:
              return False

  houses=[]

  house1=House("peter",pos.x,pos.y,pos.z,15,10,6)
  house2=House("steph",pos.x+30,pos.y,pos.z,20,15,7)

  houses.append(house1)
  houses.append(house2)

  house1.buildWall()
  house2.buildWall()
  house1.buildcellingandfloor()
  house2.buildcellingandfloor()
  def buildhouse(x0,y0,z0,l,w,h):
      # build wall
      for i in range(h):
          if i%2==0:
              q=1
          else:
              q=46

          for x in range(w):
              mc.setBlock(x0+x,y0+i,z0,q)

          for z in range(l):
              mc.setBlock(x0,y0+i,z0+z,q)

          for m in range(l):
              mc.setBlock(x0+w,y0+i,z0+m,q)

          for n in range(w+1):
              mc.setBlock(x0+n,y0+i,z0+l,q)

      for x in range(w+1):
          for z in range(l+1):
              mc.setBlock(x0+x,y0,z0+z,5)

      for x in range(w+1):
          for z in range(l+1):
              mc.setBlock(x0+x,y0+h,z0+z,20)

  #build celling and floor
      mc.setBlock(x0+5,y0+1,z0,0)        
      mc.setBlock(x0+5,y0+2,z0,0)
      mc.setBlock(x0+7,y0+3,z0,20)
      mc.setBlock(x0+7,y0+4,z0,20)
      mc.setBlock(x0+8,y0+3,z0,20)
      mc.setBlock(x0+8,y0+4,z0,20)

  '''buildhouse(pos.x,pos.y,pos.z,0,0,0)
  buildhouse(pos.x+30,pos.y,pos.z+30,0,0,0)
  buildhouse(pos.x+60,pos.y,pos.z+60,0,0,0)'''

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



