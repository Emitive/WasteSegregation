import os
from cv2 import cv2
import matplotlib.pyplot as plt
from keras.models import Model,load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

path = './Model/'
model = load_model(path + 'InceptionResnetV2__5type+PET+editHDPEOversample.h5')

file_path = "./TestIMG/"

a = int(input('command : '))

while a != 1:
    imgName = (input('IMG : '))
    img = cv2.imread(file_path + imgName)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img/255.
    plt.imshow(img)

    result = model.predict([[img]])
    print(result)

    # print('Color : ' + str(result[0][0]*100) + ', HDPE : ' + str(result[0][1]*100) + ', PET : ' + str(result[0][2]*100) + ', PP : ' + str(result[0][3]*100) + ', PVC : ' + str(result[0][4]*100))
    print('Color : ' + str(result[0][0]*100))
    print('HDPE  : ' + str(result[0][1]*100))
    print('PET   : ' + str(result[0][2]*100))
    print('PP    : ' + str(result[0][3]*100))
    print('PVC   : ' + str(result[0][4]*100))

    # print('HDPE  : ' + str(result[0][0]*100))
    # print('PP    : ' + str(result[0][1]*100))

    # print('PET   : ' + str(result[0][0]*100))
    # print('PVC   : ' + str(result[0][1]*100))

    plt.show()
    
    a = int(input('command : '))


# !wget http://www.ccsmanutech.com/photos/bottle/B105-t.jpg
# file_path = "/content/B105-t.jpg"



