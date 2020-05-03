import cv2
import numpy as np
from matplotlib import pyplot as plt
# RGB 
# BGR

img = cv2.imread(r"OpenCV\kitap.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,treshold = cv2.threshold(gri,12,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
cv2.imshow("eşiklenmiş",th)
cv2.imshow("resmi ekledim",gri)

cv2.waitKey(0)
cv2.destroyAllWindows()