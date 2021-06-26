# PyQt imports
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSlot
import sys


class LandingScreen(QtWidgets.QMainWindow):

    def __init__(self):
        super(LandingScreen, self).__init__()
        uic.loadUi('UI/sudoku.ui', self)
        self.show()

        self.startButton.clicked.connect(self.startSlot)

    def startSlot(self):
        self.ui = MainScreen()
        self.close()


class MainScreen(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi('UI/results.ui', self)
        self.show()

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
                        self.lcdNumber_69, self.lcdNumber_70, self.lcdNumber_71, self.lcdNumber_72, self.lcdNumber_74, self.lcdNumber_74, self.lcdNumber_75, self.lcdNumber_76, self.lcdNumber_77,
                        self.lcdNumber_78, self.lcdNumber_79, self.lcdNumber_80, self.lcdNumber_81]

    def backSlot(self):
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

        a = Solver([[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 0], [
            0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]])

        self.answerSlot(a.get_solution())

    def answerSlot(self, solution):
        counter = 0
        for i in range(9):
            for j in range(9):
                lcdObject = self.lcdList[counter]
                lcdObject.display(solution[i][j])
                counter = counter+1

                # setting up window


class Solver():

    def __init__(self, grid):
        self.grid = grid
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.rows = self.most_filled_row()
        self.cols = self.most_filled_col()
        self.solve()

        # grid is [ [1,2,3,4,5,6,7,8,9], [0, 0, 0],[]...]

    def solve(self):
        if self.next_empty(self.grid) == False:
            return True
        else:
            coordinates = self.next_empty(self.grid)
            x = coordinates[0]
            y = coordinates[1]

        for num in self.nums:
            if self.possible(self.grid, x, y, num):
                self.grid[x][y] = num

                if (self.solve()):
                    return True

                self.grid[x][y] = 0

        return False

    def get_solution(self):
        return self.grid

    def most_filled_row(self):
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
        for x in self.rows:
            for y in self.cols:
                if grid[x][y] == 0:
                    return [x, y]
        return False

    def most_filled_col(self):
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

        # check rows
        for num in grid[x]:
            if (num == n):
                return False

        # check columns
        for i in range(8):
            if (grid[i][y] == n):
                return False

        if x < 3:
            if y < 3:
                for row in range(3):
                    for col in range(3):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
            elif y < 5:
                for row in range(3):
                    for col in range(3, 6):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
            else:
                for row in range(3):
                    for col in range(6, 9):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

        elif x < 5:
            if y < 3:
                for row in range(3, 6):
                    for col in range(3):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

            elif y < 5:
                for row in range(3, 6):
                    for col in range(3, 6):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
            else:
                for row in range(3, 6):
                    for col in range(6, 9):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

        else:
            if y < 3:
                for row in range(5, 8):
                    for col in range(3):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

            elif y < 5:
                for row in range(5, 8):
                    for col in range(3, 6):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

            else:
                for row in range(5, 8):
                    for col in range(6, 9):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

        return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = LandingScreen()
    sys.exit(app.exec_())
