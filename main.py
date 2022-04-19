# Import libraries
from tkinter import *
import settings

root = Tk()
# Set the window size
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
# Set the title
root.title("Minesweeper")
# Setting resizing capability to False
root.resizable(False, False)

# Adding a frame at the top
top_frame = Frame(root, bg = "teal", width = 1440, height = 180)
top_frame.place(x = 0, y = 0)

# Adding a frame to the left
left_frame = Frame(root, bg = "teal", width = 360, height = 540)
left_frame.place(x = 0, y = 180)

# Keep the window running
root.mainloop()