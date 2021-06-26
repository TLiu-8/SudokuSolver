import easyocr
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('Sudoku/sudoku.png')
h, w, c = img.shape


initialWidth = w/18
widthIncrement = w/9
initialHeight = h/18
heightIncrement = h/9
reader = easyocr.Reader(['en'], gpu=False)
for j in range(9):
    for i in range(9):

        blank = np.zeros(img.shape[:2], dtype='uint8')

        mask = cv.circle(
            blank, (int(initialWidth), int(initialHeight)), 66, 255, -1)

        masked = cv.bitwise_and(img, img, mask=mask)
        #cv.imshow('Masked Image', masked)

        result = reader.readtext(masked)

        print(result)

        initialWidth += widthIncrement

        print(i)
    initialWidth = w/18
    initialHeight += heightIncrement

cv.waitKey(0)
