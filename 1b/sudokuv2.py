import csv
import tkinter as tk
from tkinter import messagebox, filedialog # for file dialog and message boxes.
import time

class SudokuFunctions:
    def __init__(self):
        self.row = 9
        self.column = 9
        self.board = [[0 for _ in range(self.column)] for _ in range(self.row)]
        self.backTrackCount = 0 # global variable to count the number of backtracks
    
    def read_file(self, filename):
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
        for i in range(self.row):
            for j in range(self.column):
                if j == 2 or j == 5:
                    # end is used to ensure it doesnt take a new line after printing the value
                    # ensures correct format
                    print(str(self.board[i][j]) + " | ", end='')
                else:
                    print(str(self.board[i][j]) + " ", end='')
            if i == 2 or i == 5:
            # take a new line or add a divider based on current row
                print("\n---------------------")
            else:
                print("")
    
    def check_valid(self, num, row, col):
        for i in range(9):
            if self.board[row][i] == num and col != i:
                return False
            if self.board[i][col] == num and row != i:
                return False
        
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False
        return True
    
    def validate_init_board(self):
        for i in range(9):
            for j in range(9):
                val = self.board[i][j]
                if val != 0:
                    self.board[i][j] = 0
                    if not self.check_valid(val, i, j):
                        self.board[i][j] = val
                        return False
                    self.board[i][j] = val
        return True
    
    def find_next_empty_space(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # row, column
        return None

    def solve_sudoku(self):
        find_space = self.find_next_empty_space()
        if not find_space:
            return True
        else:
            row, col = find_space
        
        for num in range(1, 10):
            if self.check_valid(num, row, col):
                self.board[row][col] = num
                
                if self.solve_sudoku():
                    return True
                
                self.board[row][col] = 0
                self.backTrackCount += 1



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
    
        
        


root = tk.Tk()
app = SudokuApp(root)
root.mainloop()