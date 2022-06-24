# Tkinter Ascii Art
import tkinter as tk
from tkinter import ttk
# from art import *

# make root
root = tk.Tk()
root.title('Tkinter Ascii Art')
root.iconbitmap("./assets/duck.ico")
#root.resizable(0, 0)

# root geometry
window_width = 700
window_height = 500
y_offset = 50

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2) - y_offset

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# root grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)



# make labels - title and directions (in a frame)
title_frm = ttk.Frame(root)
title_frm.grid(row=0, column=2)

# title label
title_lbl = ttk.Label(
    title_frm, 
    font=("Times New Roman", 20),
    text="Ascii Text Generator",
    anchor=tk.CENTER
)
title_lbl.pack(
    expand=True,
    fill="both"
)

# directions label
directions_str = tk.StringVar(
    value="Type some text in the textbox below. "
    "Choose a font from the menu. " 
    "Copy the output with the Button")
directions_lbl = ttk.Label(
    title_frm, 
    font=("Times New Roman", 12),
    textvariable=directions_str,
    anchor=tk.CENTER
)
directions_lbl.pack(
    expand=True,
    fill="both"
)



# make Entry - input text

# make Listbox/Scrollbar - font choose

# make Text - ascii output

# make Button - copy

# make Button - clear

# make Button - info

root.mainloop()