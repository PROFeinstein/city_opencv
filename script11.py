### Import OpenCV & numpy #####

import cv2

import numpy as np

import matplotlib.pyplot as plt




#path = r"/"



img = cv2.imread('robot2.jpg',0)




equalized = cv2.equalizeHist(img)


### plot histogram ######
hist = cv2.calcHist(equalized, [0], None, [256], [0, 256])
plt.plot(hist, color = 'k')
plt.show()




cv2.imshow('main', equalized)
cv2.waitKey(0)



cv2.destroyAllWindows