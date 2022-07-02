import cv2
# creating a classifier object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# reading a image
img = cv2.imread(r" # copy/paste the path of the image you want to process ", 1)
# converting the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# searching the coordinates
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img= cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
# resizing a image
resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
# showing a image function
res=cv2.resize(img, (1200,1200))
cv2.imshow("le", res)
# it will display the picture for 2000 millisecond
cv2.waitKey(0)
cv2.destroyAllWindows()


