from PIL import Image
from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import imageio
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(horizontal_flip=True, rotation_range = 360)
path = './Augment/PET'
for filename in os.listdir(path):
    # print(filename)
    image_path = './Augment/PET/' + filename
    image = np.expand_dims(imageio.imread(image_path), 0)

    save_here = './Keras Augment/PET'

    datagen.fit(image)

    for x, val in zip(datagen.flow(image,                    #image we chose
        save_to_dir=save_here,     #this is where we figure out where to save
        save_prefix='aug',        # it will save the images as 'aug_0912' some number for every new augmented image
        save_format='png'),range(1)) :     # here we define a range because we want 10 augmented images otherwise it will keep looping forever I think
            pass

# path = './Minbalance/Testset/PET/'
# path2 = './Minbalance/Testset/PETNew/'
# num = 0
# rnd = 1
# for filename in os.listdir(path):
#     colorImage  = Image.open(path + filename)
#     # print(str(num) + ' ' + filename)
#     num += 1

#     if(rnd == 1):
#         rotated1 = colorImage.rotate(15)
#         cv2.imwrite(path2 + '(15)' + filename, cv2.cvtColor(np.float32(rotated1), cv2.COLOR_BGR2RGB))
#     elif (rnd == 2):
#         rotated2 = colorImage.rotate(105)
#         cv2.imwrite(path2 + '(105)' + filename, cv2.cvtColor(np.float32(rotated2), cv2.COLOR_BGR2RGB))
#     elif (rnd == 3):
#         rotated3 = colorImage.rotate(195)
#         cv2.imwrite(path2 + '(195)' + filename, cv2.cvtColor(np.float32(rotated3), cv2.COLOR_BGR2RGB))
#     elif (rnd == 4):
#         rotated4 = colorImage.rotate(285)
#         cv2.imwrite(path2 + '(285)' + filename, cv2.cvtColor(np.float32(rotated4), cv2.COLOR_BGR2RGB))
#         rnd = 0
#     rnd += 1
#     if(num >= 27):
#         break
#     # colorImage.show()
#     # rotated1.show()
#     # rotated2.show()
#     # rotated3.show()
#     # rotated4.show()
# print(num)