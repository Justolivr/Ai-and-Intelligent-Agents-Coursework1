import csv
import time
import sys
from datetime import datetime


def readFile(board):

    # open csv file to read
    # populate each value of the csv into the correct position
    # data is stored as a flat row of numbers, seperated by commas
    # assuming the csv has no empty numbers, and all the values are of correct type
    # loop over each row of file
    # once a values read, increment a counter by 1
    # when 9 values are read, a row is done reading
    # go to the next column
    # stop reading when 9 rows are read

    i = 0
    j = 0
    with open("1b/easypuzzlepls.csv", newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            for value in line:
                board[i][j] = int(value)
                j = j + 1
                if j == 9:
                    j = 0
                    i = i + 1
                    if i == 9:
                        return


def printBoard():

    # prints the current state of the board in terminal
    # traverse through the entire state of the board
    # prints a "divider" each time it passes the 2nd/5th indexed row and column (3rd,6th)
    # makes the output better resemble an actual board

    for i in range(row):
        for j in range(column):
            if j == 2 or j == 5:
                # end is used to ensure it doesnt take a new line after printing the value
                # ensures correct format
                print(str(board[i][j]) + " | ", end='')
            else:
                print(str(board[i][j]) + " ", end='')
        if i == 2 or i == 5:
            # take a new line or add a divider based on current row
            print("\n---------------------")
        else:
            print("")


# set up a 2d array
# or a list of lists in this case
# read data and print the initial puzzle


# TODO
def validateInitialBoard(board):
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != 0:
                if not validity(board, i, j, val):
                    return False
    return True


def validity(board, row, column, num):
    # check row contains a number AND i does not equal to the value of the column (stop repeated values)
    for i in range(9):
        if board[row][i] == num and i != column:
            return False

    # check column contains a number and j does not equal the value of the row (to stop repeated values)
    for j in range(9):
        if board[j][column] == num and j != row:
            return False
    # checks the top-left cell of 3x3 is valid, and check the area around it
    startRow = (row // 3) * 3
    startCol = (column // 3) * 3

    #
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if board[i][j] == num and (i, j) != (row, column):
                return False

    # return true if all constraints are checked
    return True
# implement the actual solving part


def findNextEmptySpace(board):
    # loops through the rows and columns
    for i in range(9):
        for j in range(9):
            # if [i][j] is equal to 0, then return the position that 0 was in
            if (board[i][j] == 0):
                return (i, j)

    # PSEUDO
    # Check the rows and the columns
    # if the next square contains a 0 or an empty space, then return the id of the cell (2d array?)

    # finds the next 0 inside the sudoku board
    return None

# function def was borked and it was throwing an error and it was upsetting me
# up to you whether you want to do it or not


def solveSudoku(board):

    # if we cannot find an empty space (e.g. a value with 0), then the puzzle has been solved.
    if not (findNextEmptySpace(board)):
        return True
    else:
        # move onto the next value to check
        row, column = findNextEmptySpace(board)
    # Check every number from 1 to 9
    for num in range(1, 10):
        # if we pass the validity check, then we change the value of the coordinate to the correct number
        if validity(board, row, column, num):
            board[row][column] = num
    # recursively call the function until it returns True
    if (solveSudoku(board)):
        return True
    # else, we backtrack the number to 0
    board[row][column] = 0
    return False


sys.setrecursionlimit(2147483647)

row, column = (9, 9)
board = [[0 for i in range(column)] for j in range(row)]

readFile(board)
start = time.time()

print("\nInput puzzle\n")
printBoard()
print("\n")
print("Validating board...")

if not validateInitialBoard(board):

    print("Puzzle validated in: %s seconds" % (time.time() - start))
    print("This puzzle is invalid and cannot be solved.\n")
else:
    print("\n")
    print("Puzzle validated in: %s seconds" % (time.time() - start))
    print("Solve started at %s \n" % datetime.now().time())

    start = time.time()

    if solveSudoku(board):
        printBoard()
        print("\nSolution found in: %s seconds" % (time.time() - start))
        print("Solution completed at %s" % datetime.now().time())
    else:
        print("No solution exists.")
        print("Elapsed time: %s"  % (time.time() - start))
