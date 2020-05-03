# OpenCV\Cascades\haarcascade_frontalface_default.xml
import numpy as np
import cv2
cap = cv2.VideoCapture(1)
yuz_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_frontalface_default.xml")
goz_cascade = cv2.CascadeClassifier(r"OpenCV\Cascades\haarcascade_eye.xml")

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        gozler = goz_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("yuz",frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()