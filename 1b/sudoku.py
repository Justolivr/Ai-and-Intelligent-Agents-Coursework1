import csv
import time
import sys
import tkinter as tk
from tkinter import messagebox, filedialog # for file dialog and message boxes.
from datetime import datetime

backTrackCount = 0 # global variable to count the number of backtracks

# takes in board and filename, so that we can read from different files if needed
def read_file(board, filename):

    # open csv file to read
    # populate each value of the csv into the correct position
    # data is stored as a flat row of numbers, seperated by commas
    # assuming the csv has no empty numbers, and all the values are of correct type
    # loop over each row of file
    # once a values read, increment a counter by 1
    # when 9 values are read, a row is done reading
    # go to the next column
    # stop reading when 9 rows are read

    i = j = 0
    with open(filename, newline='') as file:
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


def print_board():

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

# validates the initial board so we dont waste time trying to solve an invalid puzzle
def validate_init_board(board):
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != 0:
                if not check_valid(board, i, j, val):
                    return False
    return True


def check_valid(board, row, column, num):
    # check row contains a number AND i does not equal to the value of the column (stop repeated values)
    for i in range(9):
        if board[row][i] == num and i != column:
            return False
        if board[i][column] == num and i != row:
            return False

    # check column contains a number and j does not equal the value of the row (to stop repeated values)
    
    # checks the top-left cell of 3x3 is valid, and check the area around it
    start_row = (row // 3) * 3
    start_col = (column // 3) * 3

    #
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and (i, j) != (row, column):
                return False

    # return true if all constraints are checked
    return True
# implement the actual solving part


def find_next_empty_space(board):
    # loops through the rows and columns
    for i in range(9):
        for j in range(9):
            # if [i][j] is equal to 0, then return the position that 0 was in
            if (board[i][j] == 0):
                return (i, j)
    return None

def solve_sudoku(board):
    # calling backTrackCount as a global variable so we can increment it
    global backTrackCount
    # we have defined the varialble find to be the next empty space in the board. This is to stop us calling the function twice.
    find = find_next_empty_space(board) 
    if not find:
        return True  # if we cannot find an empty space, then the puzzle has been solved.

    row, column = find # move onto the next value to check

    for num in range(1, 10):
        if check_valid(board, row, column, num): # if we pass the check_valid check, then we change the value of the coordinate to the correct number
            board[row][column] = num

            if solve_sudoku(board): # recursively call the function until we return true
                return True

            # backtrack the number to 0
            board[row][column] = 0
            # increment the backtrack counter
            backTrackCount += 1

    return False



sys.setrecursionlimit(1000)

row, column = (9, 9)
board = [[0 for i in range(column)] for j in range(row)]

read_file(board)
start = time.time()

print("\nInput puzzle\n")
print_board()
print("\n")
print("Validating board...")

if not validate_init_board(board):

    print("Puzzle validated in: %.6f seconds" % (time.time() - start))
    print("This puzzle is invalid and cannot be solved.\n")
else:
    print("\n")
    print("Puzzle validated in: %.6f seconds" % (time.time() - start))
    print("Solve started at %s \n" % datetime.now().time())

    start = time.time()

    if solve_sudoku(board):
        print_board()
        print("\nSolution found in: %.6f seconds" % (time.time() - start))
        print("Solution completed at %s" % datetime.now().time())
    else:
        print("No solution exists.")
        print("Elapsed time: %.6f"  % (time.time() - start))


class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_controls()
    
    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 28), justify='center')
                entry.grid(row=i, column=j, padx=(0 if j % 3 else 4), pady=1)
                self.cells[i][j] = entry
    
    def create_controls(self):
        frame = tk.Frame(self.root)
        frame.grid(row=10, column=0, columnspan=9, pady=10)

        load_btn = tk.Button(frame, text="Load CSV Puzzle", command=self.load_puzzle)
        load_btn.grid(row=0, column=0, padx=10)

        solve_btn = tk.Button(frame, text="Solve Puzzle", command=self.solve_puzzle)
        solve_btn.grid(row=0, column=1, padx=10)

        clear_btn = tk.Button(frame, text="Clear Grid", command=self.clear_grid)
        clear_btn.grid(row=0, column=2, padx=10)

        self.backtrack_label = tk.Label(frame, text="Backtracks: 0")
        self.backtrack_label.grid(row=0, column=3, padx=10)

    def load_puzzle(self):
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            data = []
            with open(file_path, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(int(val))
                if len(data) != 81:
                    raise ValueError("CSV must contain exactly 81 values.")
                
                idx = 0
                for i in range(9):
                    for j in range(9):
                        val = data[idx]
                        idx += 1
                        self.cells[i][j].delete(0, tk.END)
                        if val != 0:
                            self.cells[i][i].insert(0, str(val))
                            messagebox.showinfo("Info", "Puzzle loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {e}")
            return
