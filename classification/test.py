import numpy as np
from keras.models import load_model
from keras.preprocessing import image

# Load the model
model = load_model("model.h5")

# Load the image to classify
img_path = "sample2.png"
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
img_array /= 255.0  # Rescale the image

# Predict the class
prediction = model.predict(img_array)
print("Prediction (0-1) - 0 normal / 1 spaghetti:", prediction[0])
if prediction[0] > 0.5:
    print("Spaghetti print (Failure)")
else:
    print("Normal print (OK)")
