from imageai.Detection import VideoObjectDetection
import os
from cv2 import cv2


    
execution_path = os.getcwd()

camera = cv2.VideoCapture(0) 

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

def outputVid(name, percent, box):
    _, f = camera.read()
    cv2.cvtColor
    cv2.imshow('s',f)
    cv2.waitKey(1)


video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                output_file_path=os.path.join(execution_path, "data/result/camera_detected_1")
                                , frames_per_second=5, log_progress=True, per_frame_function=outputVid)
print(video_path)

