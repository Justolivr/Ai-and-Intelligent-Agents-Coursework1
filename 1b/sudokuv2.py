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


class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver (GUI)")
        global board
        self.cells = [[None] * 9 for _ in range(9)]

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
        load_button = tk.Button(self.root, text="Load Puzzle", command=print("Load Puzzle"))
        load_button.grid(row=10, column=0, columnspan=3,padx=10)

        solve_button = tk.Button(self.root, text="Solve Puzzle", command=print("Solve Puzzle"))
        solve_button.grid(row=10, column=3, columnspan=3, padx=10)

        clear_button = tk.Button(self.root, text="Clear Puzzle", command=print("Clear Puzzle"))
        clear_button.grid(row=10, column=6, columnspan=3, padx=10)

        backtrack_label = tk.Label(self.root, text="Backtracking Steps: 0")
        backtrack_label.grid(row=11, column=6, columnspan=3, padx=10)
    
    def load_puzzle(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        readFile(board)


root = tk.Tk()
app = SudokuApp(root)
root.mainloop()