import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

path= r'E:\END TO END ML PROJECT\Eye Detection\Images\2.jpg'

color_image = cv2.imread(path)

gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, 1.3, 8)

for (x, y, w, h) in faces:
    cv2.rectangle(color_image, (x,y), (x+w,y+h), (0,0,255), 4)

cv2.imshow('image', color_image)

cv2.waitKey(0)

cv2.destroyAllWindows()