# Import libraries
from tkinter import Button
import random
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mine = False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None

        # Append the object to to Cell.all list
        Cell.all.append(self)

    # method for creating a button
    def create_btn_object(self, location):
        btn = Button(location, text ="", width = 12, height = 4)

        # Binding the left click with button
        btn.bind('<Button-1>', self.left_click_action)

        # Binding the right click button
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object = btn
    
    # left click method
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
    
    def show_mine(self):
        self.cell_btn_object.configure(bg = "red")

    # right click method
    def right_click_action(self, event):
        print(event)
        print("I am right clicked!")
    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"