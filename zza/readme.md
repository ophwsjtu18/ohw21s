import numpy as np
import cv2

warma = cv2.imread('1.jpg')

huo=warma[150:200,415:460]

for i in range(3):
    for j in range(3):
        warma[j*50:j*50+50,i*45:i*45+45]=huo

        b=i*45
        c=j*50
        
        cv2.rectangle(warma,(b,c),(b+10,c+10),(0,255,0),3)


    
cv2.imshow('1',warma)

cv2.waitKey(0)

cv2.destroyAllWindows()



