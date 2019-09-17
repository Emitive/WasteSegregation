from imageai.Detection import ObjectDetection
import os
from cv2 import cv2


execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "data/pic3.jpg"), output_image_path=os.path.join(execution_path , "data/result/imagenew.jpg"), minimum_percentage_probability=30)

image = cv2.imread("data/pic3.jpg")
for eachObject in detections:
    if eachObject["name"] == "bottle":
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        x0, y0, x1, y1 = eachObject["box_points"]
        cv2.imshow("xxx", image[y0:y1, x0:x1])
        cv2.waitKey()
        print("--------------------------------")
