from ultralytics import YOLO

# Load trained model (currently has dataset of around 400 labeled images total)
model = YOLO(
    r"C:\Users\lekan.BESTLAPTOP\Visual Studio Code Projects\Print Failure Detection\runs\detect\train8\weights\best.pt"
)

images = [
    "sample1.png",
    "sample2.png",
    "sample3.png",
    "sample4.png",
    "sample5.png",
    "sample6.png",
    "sample7.png",
    "sample8.png",
    "sample9.png",
]  # List of images to test

for i in images:
    results = model(i)
    for result in results:
        result.show()  # Show each image's result
