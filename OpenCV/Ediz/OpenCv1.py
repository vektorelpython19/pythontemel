import cv2
import numpy as np
from matplotlib import pyplot as plt
# RGB 
# BGR

img = cv2.imread(r"OpenCV\resim.jpg")
print(img.shape)
cv2.imshow("resmi ekledim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()