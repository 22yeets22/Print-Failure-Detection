from ultralytics import YOLO

# I know there's not a lot of code, but I think this was the best way to do it - I have tried other methods too
# see classification folder and haarcascade folder for other methods
# Pretrained model - good table here: https://docs.ultralytics.com/models/
model = YOLO("yolo11s.pt")

# Train
model.train(data="data.yaml", epochs=10, imgsz=640)
model.to("cuda")

results = model.val()  # Get model performance on training dataset

# Quick test - can remove
results = model("sample.png")
for result in results:
    result.show()
