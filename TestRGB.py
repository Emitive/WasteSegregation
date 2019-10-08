from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

testImg = cv2.imread('data/Test/hdpeN.jpg')
img = cv2.cvtColor(testImg, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img, (128,128))

# ---------------------------------------------------------- RGB --------------------------------------------------------------
rgb = []

for i in img:
    for pixel in i:
        rgb.append((pixel[0]/3) + (pixel[1]/3) + (pixel[2]/3))
        
test = img[0][0][0]/3 + img[0][0][1]/3 + img[0][0][2]/3
print('r : ', img[0][0][0]/3, ', g : ', img[0][0][1]/3, ', b : ', img[0][0][2]/3 )
print(test)
for i in rgb:
    print(i, ' : ', rgb[i])



plt.figure(1)
plt.subplot(221), plt.imshow(img)

plt.subplot(222)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.subplot(223)
plt.hist(rgb, bins = 50)

# ------------------------------------------------ Black White ---------------------------------------------------------
plt.figure(2)
plt.subplot(211)
grayImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
plt.imshow(grayImg, 'gray')

plt.subplot(212)
(thresh, bwImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
plt.imshow(bwImg)
# plt.savefig('result/Test/plasticN.png')
plt.show()

