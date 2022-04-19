from tkinter import Button

class Cell:
    def __init__(self, x, y, is_mine = False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None
    
    # method for creating a button
    def create_btn_object(self, location):
        btn = Button(location, text = f"{self.x}, {self.y}", width = 12, height = 4)

        # Binding the left click with button
        btn.bind('<Button-1>', self.left_click_action)

        # Binding the right click button
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object = btn
    
    # left click method
    def left_click_action(self, event):
        print(event)
        print("I am left clicked!")

    # right click method
    def right_click_action(self, event):
        print(event)
        print("I am right clicked!")