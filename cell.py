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
        else:
            if self.sorrounded_cells_mines_length == 0:
                for cell_object in self.sorrounded_cells:
                    cell_object.show_cell()
            self.show_cell()
    
    def get_cell_by_axis(self, x, y):
        # Return a cell object based on x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        self.cell_btn_object.configure(bg = "red")

    @property
    def sorrounded_cells(self):
        cells = [
        self.get_cell_by_axis(self.x-1, self.y-1),
        self.get_cell_by_axis(self.x-1, self.y),
        self.get_cell_by_axis(self.x-1, self.y+1),
        self.get_cell_by_axis(self.x, self.y-1),
        self.get_cell_by_axis(self.x+1, self.y-1),
        self.get_cell_by_axis(self.x+1, self.y),
        self.get_cell_by_axis(self.x+1, self.y+1),
        self.get_cell_by_axis(self.x, self.y+1)
        ]
        cells = [elm for elm in cells if elm is not None]
        return cells

    @property
    def sorrounded_cells_mines_length(self):
        counter = 0
        for cell in self.sorrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        self.cell_btn_object.configure(text=self.sorrounded_cells_mines_length)

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