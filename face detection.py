import cv2
face=cv2.CascadeClassifier("C:/Users/kamal/Desktop/haarcascade_frontalface_default.xml")
img=cv2.imread("C:/Users/kamal/Desktop/group-large-family.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=10)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,165,0),3)
cv2.imshow("legend",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



