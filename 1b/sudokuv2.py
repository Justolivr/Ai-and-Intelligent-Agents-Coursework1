import csv
import tkinter as tk
from tkinter import messagebox, filedialog # for file dialog and message boxes.
import time

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