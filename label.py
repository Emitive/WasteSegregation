from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/Test/image (111).jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((25,25),np.uint8)

plt.subplot(321); plt.imshow(grayImg, 'gray')

dilation = cv2.dilate(grayImg,kernel,iterations = 1)
erosion = cv2.erode(grayImg,kernel,iterations = 1)

plt.subplot(323); plt.imshow(dilation, 'gray')
plt.subplot(324); plt.imshow(erosion, 'gray')

opening = cv2.morphologyEx(grayImg, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(grayImg, cv2.MORPH_CLOSE, kernel)

plt.subplot(325); plt.imshow(opening, 'gray')
plt.subplot(326); plt.imshow(closing, 'gray')
plt.show()