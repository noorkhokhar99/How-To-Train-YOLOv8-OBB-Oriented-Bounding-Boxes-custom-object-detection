from ultralytics import YOLO

# Load a model
model = YOLO("yolov8l.pt")  # load an official model

# Predict with the model
results = model(source=0,show=True,save=True)  # predict on an image