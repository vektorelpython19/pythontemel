import cv2
import numpy as np
from matplotlib import pyplot as plt 
#RGB değil BGR şeklinde yazmışlar

img = cv2.imread(r"OpenCV\resim.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gri[55,55])
print(gri.shape)


cv2.imshow("resmi ekledim",gri)
cv2.waitKey(0)
cv2.destroyAllWindows()
