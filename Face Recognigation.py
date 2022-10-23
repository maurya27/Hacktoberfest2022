#Face recognigation in python
import cv2

img = cv2.imread('testImage.jpg')


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(
   gray,
   scaleFactor = 1.3,   #30% size reduction
   minNeighbors = 3,
   minSize = (20,20)    #faces having size less than this will be ignored
   )


print("No of people =",len(faces))

for (x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("DetectedFaces",img)
