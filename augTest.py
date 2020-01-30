from PIL import Image
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
path = './HDPE/'
path2 = './HDPENew/'
num = 1
for filename in os.listdir(path):

    colorImage  = Image.open(path + filename)
    # print(str(num) + ' ' + filename)
    # num += 1
    rotated1 = colorImage.rotate(15)
    cv2.imwrite(path2 + '(15)' + filename, np.float32(rotated1))
    rotated2 = colorImage.rotate(105)
    cv2.imwrite(path2 + '(105)' + filename, np.float32(rotated2))
    rotated3 = colorImage.rotate(195)
    cv2.imwrite(path2 + '(195)' + filename, np.float32(rotated3))
    rotated4 = colorImage.rotate(285)
    cv2.imwrite(path2 + '(285)' + filename, np.float32(rotated4))
    
    # colorImage.show()
    # rotated1.show()
    # rotated2.show()
    # rotated3.show()
    # rotated4.show()