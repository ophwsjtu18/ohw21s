import cv2
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
curpos = mc.player.getTilePos()
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    (x, y, w, h) = faces[0]
    x1 = int((x - 190) / 30)
    y1 = int((y - 190) / 30)
    curpos = mc.player.getTilePos()
    mc.player.setTilePos(curpos.x - x1, curpos.y - y1, curpos.z)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
