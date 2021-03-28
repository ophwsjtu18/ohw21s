+import numpy as np
+import cv2
+img = cv2.imread('sakura.jpg')
+print(img.shape)
+head=img[350:450,250:350]
+for i in range(3):
+    for j in range(3):
+        cv2.rectangle(img,(0+100*i,j*100),(100+100*i,j*100+100),(0,255,0),3)
+        img[0+100*i:100+100*i,j*100:j*100+100]=head
+cv2.imshow('image',img)
+cv2.waitKey(0)
+cv2.destroyAllWindows()
