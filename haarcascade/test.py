import cv2

# for training i used cascade trainer gui

print_failure_cascade = cv2.CascadeClassifier("cascade2.xml")

img = cv2.imread("sample.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform object detection probably have to try tuning these parameters
print_failures = print_failure_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f"Detected {len(print_failures)} print failures.")

# Draw rectangles around detected objects
for x, y, w, h in print_failures:
    resized = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with the detected objects
cv2.imshow("Test:", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# positive: has error
# negative: no error
