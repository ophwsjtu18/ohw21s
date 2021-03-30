import numpy as np
import cv2

img = cv2.imread('inter.jpg' , 1)
for x in range(3):
    for y in range(3):
        cv2.line(img , ((x*200),(y*200)),((200+200*x),(200*y)),(0,255,0),3)
        cv2.line(img , ((x*200),(y*200)),((200*x),(200*y+200)),(0,255,0),3)
        cv2.line(img , ((x*200+200),(y*200)),((200+200*x),(200*y+200)),(0,255,0),3)
        cv2.line(img , ((x*200),(y*200+200)),((200+200*x),(200*y+200)),(0,255,0),3)
cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
