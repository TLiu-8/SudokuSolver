import easyocr
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


initialWidth = 66

for i in range(9):

    img = cv.imread('Sudoku/sudoku.png')

    blank = np.zeros(img.shape[:2], dtype='uint8')

    mask = cv.circle(
        blank, (initialWidth, 198), 66, 255, -1)

    masked = cv.bitwise_and(img, img, mask=mask)
    cv.imshow('Masked Image', masked)

    reader = easyocr.Reader(['en'], gpu=False)

    result = reader.readtext(masked)

    print(result)

    initialWidth += 133

    print(i)

cv.waitKey(0)


