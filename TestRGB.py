from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy import signal
from scipy import misc

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
plt.savefig('result/Test/hdpeN.png')
# ------------------------------------------------ Black White ---------------------------------------------------------
plt.figure(2)
plt.subplot(221)
grayImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
plt.imshow(grayImg, 'gray')

plt.subplot(222)

#--------------------------------- Treshold --------------------------------
(thresh, bwImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
plt.imshow(bwImg)
#--------------------------------- Edge ------------------------------------
# sobelX = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
# sobelY = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# gradX = signal.convolve2d(grayImg, sobelX, mode='same')
# gradY = signal.convolve2d(grayImg, sobelY, mode='same')
# gradXY = np.sqrt(np.square(gradX) + np.square(gradY))

# plt.imshow(np.absolute(gradXY), cmap='gray')

# plt.subplot(223)
# plt.imshow(np.absolute(gradX), cmap='gray')

# plt.subplot(224)
# plt.imshow(np.absolute(gradY), cmap='gray')

# plt.savefig('result/Test/plasticN.png')

#------------------------------ Canny ---------------------------------
# edges = cv2.Canny(grayImg,100,200)
# plt.imshow(edges, cmap='gray')

plt.show()

