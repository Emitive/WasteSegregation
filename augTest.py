from PIL import Image
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
path = './Resample/RE/'
path2 = './Resample/RENew/'
num = 1
for filename in os.listdir(path):

    colorImage  = Image.open(path + filename)
    # print(str(num) + ' ' + filename)
    # num += 1
    rotated1 = colorImage.rotate(15)
    cv2.imwrite(path2 + '(15)' + filename, cv2.cvtColor(np.float32(rotated1), cv2.COLOR_BGR2RGB))
    rotated2 = colorImage.rotate(105)
    cv2.imwrite(path2 + '(105)' + filename, cv2.cvtColor(np.float32(rotated2), cv2.COLOR_BGR2RGB))
    rotated3 = colorImage.rotate(195)
    cv2.imwrite(path2 + '(195)' + filename, cv2.cvtColor(np.float32(rotated3), cv2.COLOR_BGR2RGB))
    rotated4 = colorImage.rotate(285)
    cv2.imwrite(path2 + '(285)' + filename, cv2.cvtColor(np.float32(rotated4), cv2.COLOR_BGR2RGB))
    # rotated5 = colorImage.rotate(345)
    # cv2.imwrite(path2 + '(345)' + filename, cv2.cvtColor(np.float32(rotated5), cv2.COLOR_BGR2RGB))
    # rotated6 = colorImage.rotate(75)
    # cv2.imwrite(path2 + '(75)' + filename, cv2.cvtColor(np.float32(rotated6), cv2.COLOR_BGR2RGB))
    # rotated7 = colorImage.rotate(165)
    # cv2.imwrite(path2 + '(165)' + filename, cv2.cvtColor(np.float32(rotated7), cv2.COLOR_BGR2RGB))
    # rotated8 = colorImage.rotate(255)
    # cv2.imwrite(path2 + '(255)' + filename, cv2.cvtColor(np.float32(rotated8), cv2.COLOR_BGR2RGB))
    # rotated9 = colorImage.rotate(90)
    # cv2.imwrite(path2 + '(90)' + filename, cv2.cvtColor(np.float32(rotated9), cv2.COLOR_BGR2RGB))
    # rotated10 = colorImage.rotate(180)
    # cv2.imwrite(path2 + '(180)' + filename, cv2.cvtColor(np.float32(rotated10), cv2.COLOR_BGR2RGB))
    # rotated11 = colorImage.rotate(270)
    # cv2.imwrite(path2 + '(270)' + filename, cv2.cvtColor(np.float32(rotated11), cv2.COLOR_BGR2RGB))
    # rotated12 = colorImage.rotate(5)
    # cv2.imwrite(path2 + '(5)' + filename, cv2.cvtColor(np.float32(rotated12), cv2.COLOR_BGR2RGB))
    # rotated13 = colorImage.rotate(135)
    # cv2.imwrite(path2 + '(95)' + filename, cv2.cvtColor(np.float32(rotated9), cv2.COLOR_BGR2RGB))
    # rotated14 = colorImage.rotate(185)
    # cv2.imwrite(path2 + '(185)' + filename, cv2.cvtColor(np.float32(rotated14), cv2.COLOR_BGR2RGB))
    # rotated15 = colorImage.rotate(275)
    # cv2.imwrite(path2 + '(275)' + filename, cv2.cvtColor(np.float32(rotated15), cv2.COLOR_BGR2RGB))
    # rotated16 = colorImage.rotate(355)
    # cv2.imwrite(path2 + '(355)' + filename, cv2.cvtColor(np.float32(rotated15), cv2.COLOR_BGR2RGB))

    # colorImage.show()
    # rotated1.show()
    # rotated2.show()
    # rotated3.show()
    # rotated4.show()