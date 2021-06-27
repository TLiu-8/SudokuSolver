# SudokuSolver
https://cdn.discordapp.com/attachments/718253662870437888/858537435204681749/unknown.png

## Inspiration
We see grandpas struggling with their sudoku puzzle every morning at the breakfast table. Sometimes they do manage to solve it, however, they aren't sure if it is correct. With SudokuSolver, whether you are stuck on your sudoku puzzle or if you want to check if your solution is correct, our algorithm will produce the accurate solution to your puzzle.

## What it does
SudokuSolver solves Sudoku puzzles using Computer Vision and Python. The user can input an image file of any type (e.g., jpg, pdf, heic) and SudokuSolver will run a backtracking recursive algorithm and output the solved puzzle on its GUI. 

## How we built it
We split up the project into three key tasks. 
1. Create the recursive sudoku solving algorithm
2. Develop optical character recognition code that could parse the image for numbers and blank spaces.
3. Design an interface for users to easily upload and visualize the results.

One person utilized backtracking and starting with the most filled rows and columns to optimize the algorithm's speed. Another person worked on using OpenCV and EasyOCR to detect each grid space and determine whether or not there is a number or a blank space. This result was passed as a 2-D list to the final person who designed the GUI. We used PyQt5 and QtDesigner to create file loading buttons, LCD number displays, etc. 

## Challenges we ran into
One of the challenges we ran into was using OCR to read the numbers from the sudoku board. When we initially used OCR, it would read the numbers but it would also read the grid lines, which we didn't want. To solve this problem, we used the masking feature from OpenCV so that the OCR would analyze each Sudoku box individually to read the number. That way the grid lines wouldn't interfere with our program.

## Accomplishments that we're proud of
- Learning and utilizing OpenCV and other computer vision libraries for the first time
- Producing a sudoku solver that's easier than having to input numbers like most web applications

## What we learned
- The challenges of integrating different libraries to create a complete project and most importantly how to overcome these challenges.

## What's next for SudokuSolver
One of our next steps is to find a way to speed up the calculation time of the algorithm. Currently, the EasyOCR library takes a lot of time to read the number from each grid square. We will find a way to speed up the calculation time and make the process faster by learning ML models like CNNs and more.
We'd also like to add more functionality like real-time video loading, giving the option for users to input numbers directly into the GUI instead of uploading an image, or bringing the project to app development.

https://cdn.discordapp.com/attachments/718253662870437888/858537463484252170/unknown.png
