from PIL import Image
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
path = './Minbalance/Testset/PET/'
path2 = './Minbalance/Testset/PETNew/'
num = 0
rnd = 1
for filename in os.listdir(path):
    colorImage  = Image.open(path + filename)
    # print(str(num) + ' ' + filename)
    num += 1

    if(rnd == 1):
        rotated1 = colorImage.rotate(15)
        cv2.imwrite(path2 + '(15)' + filename, cv2.cvtColor(np.float32(rotated1), cv2.COLOR_BGR2RGB))
    elif (rnd == 2):
        rotated2 = colorImage.rotate(105)
        cv2.imwrite(path2 + '(105)' + filename, cv2.cvtColor(np.float32(rotated2), cv2.COLOR_BGR2RGB))
    elif (rnd == 3):
        rotated3 = colorImage.rotate(195)
        cv2.imwrite(path2 + '(195)' + filename, cv2.cvtColor(np.float32(rotated3), cv2.COLOR_BGR2RGB))
    elif (rnd == 4):
        rotated4 = colorImage.rotate(285)
        cv2.imwrite(path2 + '(285)' + filename, cv2.cvtColor(np.float32(rotated4), cv2.COLOR_BGR2RGB))
        rnd = 0
    rnd += 1
    if(num >= 27):
        break
    # colorImage.show()
    # rotated1.show()
    # rotated2.show()
    # rotated3.show()
    # rotated4.show()
print(num)