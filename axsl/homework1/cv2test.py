import cv2


img = cv2.imread("ty.jpg")
head =img[150:210, 190:250]
for i in range(3):
    for j in range(3):
        img[60*j:60*j+60, 60*i:60*i+60] = head

for i in range(3):
    for j in range(3):
        cv2.rectangle(img,(60*j,60*i),(60*j+60,60*i+60),(0,255,0),3)

cv2.imwrite('ty_result.jpg',img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
