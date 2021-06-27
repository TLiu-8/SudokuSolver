# Sudoku.py
# Date: June 26, 2021
# Description: GUI that allows users to upload and solve sudoku puzzles
# Authors: Theodore Liu, Justin Wang, Brian Wu


# PyQt imports
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QColor

# Other imports
import sys
import easyocr
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# Landing Screen
# Basic screen that starts up the program


class LandingScreen(QtWidgets.QMainWindow):

    def __init__(self):
        # Constructor
        # @param: none
        # @return: none

        # loading ui
        super(LandingScreen, self).__init__()
        uic.loadUi('/UI/sudoku.ui', self)
        self.show()

        # button handlers
        self.startButton.clicked.connect(self.startSlot)

    def startSlot(self):
        # start slot
        # starts the main screen
        # @param: none
        # @return: none
        self.ui = MainScreen()
        self.close()


class MainScreen(QtWidgets.QMainWindow):

    def __init__(self):
        # Constructor
        # @param: none
        # @return: none

        # loading ui
        super(MainScreen, self).__init__()
        uic.loadUi('/UI/results.ui', self)
        self.show()

        # shape of image loader
        self.display_height = 225
        self.display_width = 225

        # button handlers
        self.backButton.clicked.connect(self.backSlot)
        self.browseButton.clicked.connect(self.browseSlot)
        self.lcdList = [self.lcdNumber_1, self.lcdNumber_2, self.lcdNumber_3, self.lcdNumber_4,
                        self.lcdNumber_5, self.lcdNumber_6, self.lcdNumber_7, self.lcdNumber_8, self.lcdNumber_9, self.lcdNumber_10, self.lcdNumber_11, self.lcdNumber_12, self.lcdNumber_13,
                        self.lcdNumber_14, self.lcdNumber_15, self.lcdNumber_16, self.lcdNumber_17, self.lcdNumber_18, self.lcdNumber_19, self.lcdNumber_20, self.lcdNumber_21, self.lcdNumber_22,
                        self.lcdNumber_23, self.lcdNumber_24, self.lcdNumber_25, self.lcdNumber_26, self.lcdNumber_27, self.lcdNumber_28, self.lcdNumber_29, self.lcdNumber_30, self.lcdNumber_31, self.lcdNumber_32,
                        self.lcdNumber_33, self.lcdNumber_34, self.lcdNumber_35, self.lcdNumber_36,  self.lcdNumber_37, self.lcdNumber_38, self.lcdNumber_39, self.lcdNumber_40, self.lcdNumber_41,
                        self.lcdNumber_42, self.lcdNumber_43, self.lcdNumber_44, self.lcdNumber_45, self.lcdNumber_46, self.lcdNumber_47, self.lcdNumber_48, self.lcdNumber_49, self.lcdNumber_50,
                        self.lcdNumber_51, self.lcdNumber_52, self.lcdNumber_53, self.lcdNumber_54, self.lcdNumber_55, self.lcdNumber_56, self.lcdNumber_57, self.lcdNumber_58, self.lcdNumber_59,
                        self.lcdNumber_60, self.lcdNumber_61, self.lcdNumber_62, self.lcdNumber_63, self.lcdNumber_64, self.lcdNumber_65, self.lcdNumber_66, self.lcdNumber_67, self.lcdNumber_68,
                        self.lcdNumber_69, self.lcdNumber_70, self.lcdNumber_71, self.lcdNumber_72, self.lcdNumber_73, self.lcdNumber_74, self.lcdNumber_75, self.lcdNumber_76, self.lcdNumber_77, self.lcdNumber_78,
                        self.lcdNumber_79, self.lcdNumber_80, self.lcdNumber_81]

    def backSlot(self):
        # backslot
        # handles going back
        # @param: none
        # @return: none
        self.ui = LandingScreen()
        self.close()

    def browseSlot(self):
        # browseSlot()
        # Description: allows user to select file
        # @param: null
        # @return: null

        fileLoader = QFileDialog()
        # fileLoader.setNameFilter(tr("Images (*.png *.xpm *.jpg)"))
        fileLoader.setFileMode(QFileDialog.ExistingFiles)
        filenames = fileLoader.getOpenFileNames()
        self.paths = filenames[0]
        self.name = self.paths[0]

        img = cv.imread(self.name)
        self.imageLabel.setPixmap(self.convert_cv_qt(img))
        #img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)

        h, w, c = img.shape

        initialWidth = w/18
        radius = w/18
        widthIncrement = w/9
        initialHeight = h/18
        heightIncrement = h/9
        reader = easyocr.Reader(['en'], gpu=False)

        grid = []
        for j in range(9):
            temp = []
            for i in range(9):

                blank = np.zeros(img.shape[:2], dtype='uint8')

                mask = cv.circle(
                    blank, (int(initialWidth), int(initialHeight)), 66, 255, -1)

                masked = cv.bitwise_and(img, img, mask=mask)
                #cv.imshow('Masked Image', masked)

                result = reader.readtext(masked)
                print(result)
                if (result == []):
                    temp.append(0)
                else:
                    temp.append(int(result[0][1]))

                initialWidth += widthIncrement

                # print(i)
            initialWidth = w/18
            initialHeight += heightIncrement
            grid.append(temp)

        a = Solver(grid)

        self.answerSlot(a.get_solution())

    def answerSlot(self, solution):
        # answerSlot
        # displays answer on lcd buttons
        # @param: none
        # @return: none

        counter = 0
        for i in range(9):
            for j in range(9):
                lcdObject = self.lcdList[counter]
                lcdObject.display(solution[i][j])
                counter = counter+1

                # setting up window

    def convert_cv_qt(self, img):
        # conver_cv_qt
        # found from online, allows conversion of cv image into pyqt format
        # @param: none
        # @return: none
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        h, w, c = rgb.shape
        bytes_per_line = c * w

        convert_to_Qt_format = QtGui.QImage(
            rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(
            self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


class Solver():
    # Solver class
    # given a 2-d array representing the sudoku grid, outputs solved grid

    def __init__(self, grid):
        # Constructor
        # @param: none
        # @return: none

        self.grid = grid
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.rows = self.most_filled_row()
        self.cols = self.most_filled_col()

        # calling recursive solve method
        print(self.solve(self.grid))

        # grid is [ [1,2,3,4,5,6,7,8,9], [0, 0, 0],[]...]

    def solve(self, grid):

        # solve
        # @param: 2-d array named grid
        # @return: True or false depending on solvability

        if self.next_empty(self.grid) == False:
            return True  # if all are filled up return true
        else:
            coordinates = self.next_empty(self.grid)
            x = coordinates[0]
            y = coordinates[1]

        for num in self.nums:
            if self.possible(self.grid, x, y, num):  # check if possible
                self.grid[x][y] = num

                if (self.solve(self.grid)):
                    return True

                self.grid[x][y] = 0  # if not possible set back to 0

        return False

    def get_solution(self):
        # get_solution (getter)
        # @param: none
        # @return: solved grid
        return self.grid

    def most_filled_row(self):
        # most_filled_row
        # gets most filled row in the sudoku grid
        # @param: none
        # @return: gets the most filled row (making the searching faster)

        most = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        index = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            for value in self.grid[i]:
                if (value != 0):
                    most[i] = most[i]+1

        # sort
        for j in range(9):
            highest_index = 0
            highest_value = 0
            for i in range(9):
                if (most[i] > highest_value):
                    highest_index = i
                    highest_value = most[i]

            index[j] = highest_index
            most[highest_index] = -1

        return index

    def next_empty(self, grid):
        # next_empty
        # gets next empty square in the sudoku grid
        # @param: goes to next empty square to fill
        # @return: returns the coordinates or False if fully filled

        for x in range(9):
            for y in range(9):
                if grid[x][y] == 0:
                    return [x, y]
        return False

    def most_filled_col(self):
        # most_filled_col
        # gets most filled column in sudoku grid
        # @param: none
        # @return: none

        most = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        index = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            for j in range(9):
                if (self.grid[j][i] != 0):
                    most[i] = most[i] + 1

        # sort
        for j in range(9):
            highest_index = 0
            highest_value = 0
            for i in range(9):
                if (most[i] > highest_value):
                    highest_index = i
                    highest_value = most[i]

            index[j] = highest_index
            most[highest_index] = -1

        return index

    def possible(self, grid, x, y, n):

        # Check row
        for i in range(len(grid[x])):
            if grid[x][i] == n and y != i:
                return False

        # check columns
        for i in range(9):
            if (grid[i][y] == n and x != i):
                return False

        # check the 3x3 squares
        if x < 3:
            if y < 3:
                for row in range(3):
                    for col in range(3):
                        if grid[row][col] == n and (row != x and col != y):
                            return False
            elif y < 6:
                for row in range(3):
                    for col in range(3, 6):
                        if grid[row][col] == n and (row != x and col != y):
                            return False
            else:
                for row in range(3):
                    for col in range(6, 9):
                        if grid[row][col] == n and (row != x and col != y):
                            return False

        elif x < 6:
            if y < 3:
                for row in range(3, 6):
                    for col in range(3):
                        if grid[row][col] == n and (row != x and col != y):
                            return False

            elif y < 6:
                for row in range(3, 6):
                    for col in range(3, 6):
                        if grid[row][col] == n and (row != x and col != y):
                            return False
            else:
                for row in range(3, 6):
                    for col in range(6, 9):
                        if grid[row][col] == n and (row != x and col != y):
                            return False

        else:
            if y < 3:
                for row in range(6, 9):
                    for col in range(3):
                        if grid[row][col] == n and (row != x and col != y):
                            return False

            elif y < 6:
                for row in range(6, 9):
                    for col in range(3, 6):
                        if grid[row][col] == n and (row != x and col != y):
                            return False

            else:
                for row in range(6, 9):
                    for col in range(6, 9):
                        if grid[row][col] == n and (row != x and col != y):
                            return False

        return True


# launcher
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = LandingScreen()
    sys.exit(app.exec_())
