import numpy as np
import cv2
cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    #-----------------------------
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Frame',gray)
    #-----------------------------
    # hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # dusuk_renk = np.array([30,150,50])
    # yuksek_renk = np.array([255,255,180])
    # mask = cv2.inRange(hsv,dusuk_renk,yuksek_renk)
    # res = cv2.bitwise_and(frame,frame,mask=mask)
    #-----------------------------
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(frame,-1,kernel)
    blur = cv2.GaussianBlur(frame,(15,15),-2)
    medBlur = cv2.medianBlur(frame,15)
    bilateral = cv2.bilateralFilter(frame,15,75,75)
    cv2.imshow('Frame',frame)
    cv2.imshow('Frame2',smoothed)
    cv2.imshow('Frame3',bilateral)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()