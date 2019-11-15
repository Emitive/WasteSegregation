from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/Test/hdpe.jpg')
img = cv2.resize(img,(300, 400))
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret, thresh = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
plt.subplot(221); plt.imshow(grayImg, 'gray')

# temp = grayImg.copy()
# for x in range(0, grayImg.shape[1], 1):
#     for y in range(0, grayImg.shape[0], 1):
#         temp[y][x] -= 127
#         grayImg[y][x] = temp[y][x]

print(grayImg)
# kernel = np.ones((20,10),np.uint8)

# kernel = np.ones((30,50),np.uint8)

# kernel = np.array(([[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
#                     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#                     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#                     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]),np.uint8)

kernel = np.array(([[0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]),np.uint8)
print(kernel)

# plt.subplot(222); plt.imshow(grayImg, 'gray')

# dilation = cv2.dilate(grayImg,kernel,iterations = 1)
# erosion = cv2.erode(grayImg,kernel,iterations = 1)
# plt.subplot(323); plt.imshow(dilation, 'gray')
# plt.subplot(324); plt.imshow(erosion, 'gray')

opening = cv2.morphologyEx(grayImg, cv2.MORPH_OPEN, kernel)
openclosing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

# closing = cv2.morphologyEx(grayImg, cv2.MORPH_CLOSE, kernel)
# openclosing = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

plt.subplot(223); plt.imshow(opening, 'gray')
# plt.subplot(223); plt.imshow(closing, 'gray')
plt.subplot(224); plt.imshow(openclosing, 'gray')



temp = openclosing.copy()
for x in range(0, openclosing.shape[1], 1):
    for y in range(0, openclosing.shape[0], 1):
        if (openclosing[y][x] < 127):
            temp[y][x] = 0
        else:
            temp[y][x] = 255
            

plt.subplot(222); plt.imshow(temp, 'gray')

plt.show()