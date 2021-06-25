
class SudokuSolver():

    
    def __init__(self, grid):
        self.grid = grid
        self.nums = [1,2,3,4,5,6,7,8,9]
        self.rows = self.most_filled_row()
        self.cols = self.most_filled_col()
        self.solve()
        
        #grid is [ [1,2,3,4,5,6,7,8,9], [0, 0, 0],[]...]

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
        most = [0,0,0,0,0,0,0,0,0]
        index = [0,0,0,0,0,0,0,0,0]
        for i in range(9):
            for value in self.grid[i]:
                if (value != 0):
                    most[i] = most[i]+1


        #sort
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
                    return [x,y]
        return False

    def most_filled_col(self):
        most = [0,0,0,0,0,0,0,0,0]
        index = [0,0,0,0,0,0,0,0,0]
        for i in range(9):
            for j in range(9):
                if (self.grid[j][i] != 0):
                    most[i] = most[i] + 1

        #sort
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

        
    def possible(self,grid,x,y,n):

        #check rows
        for num in grid[x]:
            if (num == n):
                return False

        #check columns
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
                    for col in range(3,6):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
            else:
                for row in range(3):
                    for col in range(6,9):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
                
        elif x <5:
            if y < 3:
                for row in range(3,6):
                    for col in range(3):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

            elif y < 5:
                for row in range(3,6):
                    for col in range(3,6):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
            else:
                for row in range(3,6):
                    for col in range(6,9):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

        else:
            if y < 3:
                for row in range(5,8):
                    for col in range(3):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

            elif y < 5:
                for row in range(5,8):
                    for col in range(3,6):
                        if grid[row][col] == n and (row == x and col == y):
                            return False

            else:
                for row in range(5,8):
                    for col in range(6,9):
                        if grid[row][col] == n and (row == x and col == y):
                            return False
                        
        return True


a = SudokuSolver([[0,0,0,2,6,0,7,0,1], [6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0], [8,2,0,1,0,0,0,4,0], [0,0,4,6,0,2,9,0,0], [0,5,0,0,0,3,0,2,8], [0,0,9,3,0,0,0,7,4], [0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]])
print(a.get_solution())   
        
    
