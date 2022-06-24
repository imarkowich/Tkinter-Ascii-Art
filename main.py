# Tkinter Ascii Art
import tkinter as tk
from tkinter import ttk
# from art import *

# make root
root = tk.Tk()
root.title('Tkinter Ascii Art')
root.iconbitmap("./assets/duck.ico")
root.resizable(0, 0)

# root geometry
window_width = 700
window_height = 500
y_offset = 50

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2) - y_offset

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# make labels - title and directions

# make Entry - input text

# make Listbox/Scrollbar - font choose

# make Text - ascii output

# make Button - copy

# make Button - clear

# make Button - info

root.mainloop()