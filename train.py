from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="bottles")
trainer.setTrainConfig(object_names_array=["PET","HDPE(1)","HDPE(2)","PVC","Opaque","PP"], batch_size=2, num_experiments=200, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()