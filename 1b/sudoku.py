import csv

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
    with open("1b/testpuzzle.csv", newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            for value in line:
                board[i][j] = value
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

row, column = (9, 9)
board = [[0 for i in range(column)] for i in range(row)]

readFile(board)
printBoard()

# TODO

def validity(board, row, column, num):
    # check row 
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # check column
    for j in range(9):
        if board[j][column] == num:
            return False
    # checks the top-left cell of 3x3 is valid, and check the area around it
    startRow = (row // 3) * 3
    startCol = (column // 3) * 3

    # 
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if board[i][j] == num:
                return False

    # return true if all constraints are checked
    return True
# implement the actual solving part

def findNextEmptySpace():
    # loops through the rows and columns
    for i in range(9):
        for j in range(9):
            # DEBUG print to check num position
            print(board[i][j])
            # if [i][j] is equal to String, then return 2d coord
            if (board[i][j] == '0'):
                print(i)
                print(j)
                return (i,j)


    # PSEUDO
    # Check the rows and the columns
    # if the next square contains a 0 or an empty space, then return the id of the cell (2d array?)

    # finds the next 0 inside the sudoku board
    return None

# function def was borked and it was throwing an error and it was upsetting me
# up to you whether you want to do it or not

def solveSudoku(board):

    # if we cannot find an empty space, then the puzzle has been solved.
    if not (findNextEmptySpace(board)):
        return True
    else:
        row, column = findNextEmptySpace(board)
    # So we need to go through every row first,
    return True
    

print("\n   V   Solution   V    \n")


# print the completed puzzle here
printBoard()
print(findNextEmptySpace())