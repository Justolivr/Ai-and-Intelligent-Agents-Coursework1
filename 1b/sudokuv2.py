import csv
import tkinter as tk
from tkinter import messagebox, filedialog # for file dialog and message boxes.
import time

# i've encapsulated all the sudoku functions into a class to make it neater and easier to manage
# this also allows us to create multiple instances of the sudoku solver if needed
class SudokuFunctions:
    def __init__(self):
        # define board dimensions and initialising the board
        self.row = 9
        self.column = 9
        self.board = [[0 for _ in range(self.column)] for _ in range(self.row)]
        self.backTrackCount = 0 # global variable to count the number of backtracks
    
    def read_file(self, filename):
        '''
        open csv file to read
        populate each value of the csv into the correct position
        data is stored as a flat row of numbers, seperated by commas
        assuming the csv has no empty numbers, and all the values are of correct type
        loop over each row of file
        once a values read, increment a counter by 1
        when 9 values are read, a row is done reading
        go to the next column
        stop reading when 9 rows are read

        '''
        i = j = 0
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                for value in line:
                    self.board[i][j] = int(value)
                    j = j + 1
                    if j == 9:
                        j = 0
                        i = i + 1
                        if i == 9:
                            return
    
    def print_board(self):
        '''
        loops through each value of the board
        if j is at the 2nd or 5th index, print a divider after printing the column to ensure the correct format
        if i is at the 2nd or 5th index, print a divider after printing the row to ensure the correct format
        makes the output better resemble an actual board 
        '''
        for i in range(self.row):
            for j in range(self.column):
                if j == 2 or j == 5:
                    # end is used to ensure it doesnt take a new line after printing the column
                    print(str(self.board[i][j]) + " | ", end='')
                else:
                    print(str(self.board[i][j]) + " ", end='')
            if i == 2 or i == 5:
            # take a new line or add a divider based on current row
                print("\n---------------------")
            else:
                print("")
    
    def check_valid(self, num, row, col):
        ''' 
        function to check if a number can be placed in a specific position
        checks the row, column and 3x3 grid to ensure no duplicates

        '''
        for i in range(9):
            # if a number is also found in the same row or column, return false
            if self.board[row][i] == num and col != i: 
                return False
            if self.board[i][col] == num and row != i:
                return False
        # defines the starting row and column of the 3x3 grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        # for each value in the 3x3 grid, if a number is found, return false
        # this is so we are able to follow the rule of sudoku that states no duplicates in a 3x3 grid
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                #  instruction to make sure we don't compare the cell to itself
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False
        return True
    
    def validate_init_board(self):
        '''
        function to validate the initial board, so that we don't waste time trying to solve an invalid puzzle
        we loop through each value of the board
        if the value is not 0 (not empty), we check if its valid in that position
        if any value is found to be invalid, return false (meaning puzzle is invalid)
        '''
        for i in range(9):
            for j in range(9):
                val = self.board[i][j] # gets the value at the current position
                if val != 0: # if the value is not 0 (not empty)
                    self.board[i][j] = 0 # temporarily set it to 0 to avoid self-comparison in check_valid
                    if not self.check_valid(val, i, j):  # check if the value is valid in that position
                        self.board[i][j] = val # restore the value
                        return False # if not valid, return false
                    self.board[i][j] = val # restore the value
        return True
    
    def find_next_empty_space(self):
        '''
        function to find the next empty space (0) in the board
        loops through each value of the board
        if a 0 is found, return the position (row, column)
        if no empty space is found, return None (means board is full)
        '''
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # row, column
        return None

    def solve_sudoku(self):
        '''
        function to solve the entire puzzle using backtracking
        define a variable to find the next empty space
        if no empty space is found, return true (means puzzle is solved)
        else, get the row and column of the empty space
        then, loop through numbers 1-9
        if the number is valid in that position, place it there
        then, recursively call the function to try and solve the rest of the puzzle
        if the recursive call returns true, return true (means puzzle is solved)
        if the recursive call returns false, reset the position to 0 (backtrack) and increment backtrack counter
        if no number is valid in that position, return false (means puzzle is unsolvable)
        '''
        find_space = self.find_next_empty_space() # find the next empty space
        if not find_space:
            return True
        else:
            row, col = find_space # get the row and column of the empty space
        
        for num in range(1, 10): # loop through numbers 1-9
            if self.check_valid(num, row, col): # if the number is valid in that position
                self.board[row][col] = num # place the number there
                
                if self.solve_sudoku(): # recursively call the function to try and solve the rest of the puzzle
                    return True
                
                self.board[row][col] = 0 # if not, reset the position to 0 (backtrack)
                self.backTrackCount += 1 # increment backtrack counter
        return False # if no number is valid in that position, return false (means puzzle is unsolvable)


# my other class to handle the GUI part of the program (this is to separate the logic from the interface
# this was optional on the spec, but I wanted to do it this way to make it neater and easier to manage
# however, it does mean I have changed some functions in sudokuFunctions to be object-oriented
# for example, I have changed the function signatures to use self and access class variables
class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver (GUI)")
        self.cells = [[None] * 9 for _ in range(9)]

        self.solver = SudokuFunctions() # calls the functions class - Encapsulation

        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                grid_entry = tk.Entry(self.root, width=2, font=('Arial', 24), justify='center', state='readonly')
                padx = 0 if j % 3 != 2 else 4
                pady = 0 if i % 3 != 2 else 4
                grid_entry.grid(row = i, column = j, padx=padx, pady=pady)
                self.cells[i][j] = grid_entry
    
    def create_buttons(self):
        load_button = tk.Button(self.root, text="Load Puzzle", command=self.load_puzzle)
        load_button.grid(row=10, column=0, columnspan=3,padx=10)

        solve_button = tk.Button(self.root, text="Solve Puzzle", command=self.solve_puzzle)
        solve_button.grid(row=10, column=3, columnspan=3, padx=10)

        clear_button = tk.Button(self.root, text="Clear Puzzle", command=self.clear_puzzle)
        clear_button.grid(row=10, column=6, columnspan=3, padx=10)

        self.backtrack_label = tk.Label(self.root, text="Backtracking Steps: 0")
        self.backtrack_label.grid(row=11, column=6, columnspan=3, padx=10)

    def update_grid(self):
        for i in range(9):
            for j in range(9):
                entry = self.cells[i][j]
                entry.config(state='normal')
                entry.delete(0, tk.END)
                val = self.solver.board[i][j]
                if val != 0:
                    entry.insert(0, str(val))
                entry.config(state='readonly')

    def load_puzzle(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        self.solver.read_file(file_path)
        self.update_grid()
        self.backtrack_label.config(text=f"Backtracking Steps: {self.solver.backTrackCount}")
    
    def solve_puzzle(self):
        self.solver.backTrackCount = 0
        start_time = time.time()
        if not self.solver.validate_init_board():
            messagebox.showerror("Error", "The initial board is invalid!")
            return
        solved_puzzle = self.solver.solve_sudoku()
        end_time = time.time()-start_time
        self.update_grid()
        self.backtrack_label.config(text=f"Backtracking Steps: {self.solver.backTrackCount}")
        if solved_puzzle:
            messagebox.showinfo("Solved", f"Puzzle solved in {end_time:.4f} seconds with {self.solver.backTrackCount} backtracks.")
        else:
            messagebox.showinfo("Unsolvable", "The puzzle cannot be solved.")
            
    def clear_puzzle(self):
        self.solver.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solver.backTrackCount = 0
        self.update_grid()
        self.backtrack_label.config(text=f"Backtracking Steps: {self.solver.backTrackCount}")
    
        
        
# main part of the program to run the GUI
# setting recursion limit higher to avoid hitting the limit on complex puzzles
import sys
sys.setrecursionlimit(10000)
root = tk.Tk()
app = SudokuApp(root)
root.mainloop()

