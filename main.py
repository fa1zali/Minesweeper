# Import libraries
from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
# Set the window size
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
# Set the title
root.title("Minesweeper")
# Setting resizing capability to False
root.resizable(False, False)

# Adding a frame at the top
top_frame = Frame(root, width = settings.WIDTH, height = utils.height_prct(25))
top_frame.place(x = 0, y = 0)

# Adding a frame to the left
left_frame = Frame(root, width = utils.width_prct(25), height = utils.height_prct(75))
left_frame.place(x = 0, y = utils.height_prct(25))

# Adding a center frame
center_frame = Frame(root, width=utils.width_prct(75), height=utils.height_prct(75))
center_frame.place(x = utils.width_prct(25), y = utils.height_prct(25))

# Creating buttons on a grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column = x, row = y)

Cell.randomize_mines()

# Keep the window running
root.mainloop()