import easyocr
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = ''

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)

img = cv.imread(IMAGE_PATH)

for detection in result:
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
    img = cv.putText(img, text, top_left, font, 2, (255, 255, 255), 2, cv.LINE_AA)

plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.show()

