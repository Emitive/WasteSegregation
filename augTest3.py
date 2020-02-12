from PIL import Image
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
path = './Maxbalance/Testset/HDPE/'
path2 = './Maxbalance/Testset/HDPENew/'
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
    # elif (rnd == 5):
    #     rotated1 = colorImage.rotate(345)
    #     cv2.imwrite(path2 + '(345)' + filename, cv2.cvtColor(np.float32(rotated1), cv2.COLOR_BGR2RGB))
    # elif (rnd == 6):
    #     rotated2 = colorImage.rotate(75)
    #     cv2.imwrite(path2 + '(75)' + filename, cv2.cvtColor(np.float32(rotated2), cv2.COLOR_BGR2RGB))
    # elif (rnd == 7):
    #     rotated3 = colorImage.rotate(165)
    #     cv2.imwrite(path2 + '(165)' + filename, cv2.cvtColor(np.float32(rotated3), cv2.COLOR_BGR2RGB))
    # elif (rnd == 8):
    #     rotated4 = colorImage.rotate(255)
    #     cv2.imwrite(path2 + '(255)' + filename, cv2.cvtColor(np.float32(rotated4), cv2.COLOR_BGR2RGB))

    # if(rnd == 1):
    #     rotated1 = colorImage.rotate(5)
    #     cv2.imwrite(path2 + '(5)' + filename, cv2.cvtColor(np.float32(rotated1), cv2.COLOR_BGR2RGB))
    # elif (rnd == 2):
    #     rotated2 = colorImage.rotate(95)
    #     cv2.imwrite(path2 + '(95)' + filename, cv2.cvtColor(np.float32(rotated2), cv2.COLOR_BGR2RGB))
    # elif (rnd == 3):
    #     rotated3 = colorImage.rotate(185)
    #     cv2.imwrite(path2 + '(185)' + filename, cv2.cvtColor(np.float32(rotated3), cv2.COLOR_BGR2RGB))
    # elif (rnd == 4):
    #     rotated4 = colorImage.rotate(275)
    #     cv2.imwrite(path2 + '(275)' + filename, cv2.cvtColor(np.float32(rotated4), cv2.COLOR_BGR2RGB))
    # elif (rnd == 5):
    #     rotated5 = colorImage.rotate(355)
    #     cv2.imwrite(path2 + '(355)' + filename, cv2.cvtColor(np.float32(rotated5), cv2.COLOR_BGR2RGB))
    # elif (rnd == 6):
    #     rotated6 = colorImage.rotate(85)
    #     cv2.imwrite(path2 + '(85)' + filename, cv2.cvtColor(np.float32(rotated6), cv2.COLOR_BGR2RGB))
    # elif (rnd == 7):
    #     rotated7 = colorImage.rotate(175)
    #     cv2.imwrite(path2 + '(175)' + filename, cv2.cvtColor(np.float32(rotated7), cv2.COLOR_BGR2RGB))
    # elif (rnd == 8):
    #     rotated8 = colorImage.rotate(265)
    #     cv2.imwrite(path2 + '(265)' + filename, cv2.cvtColor(np.float32(rotated8), cv2.COLOR_BGR2RGB))
    #     rnd = 0

    rnd += 1
    if(num >= 39):
        break
    # colorImage.show()
    # rotated1.show()
    # rotated2.show()
    # rotated3.show()
    # rotated4.show()
print(num)