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
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)



# make labels - title and directions (in a frame)
title_frm = ttk.Frame(root)
title_frm.grid(row=0, column=0, columnspan=5)

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
input_txt = tk.StringVar()
input_ent = ttk.Entry(
    root,
    textvariable=input_txt,
)
input_ent.grid(
    row=1, 
    column=0, 
    columnspan=3, 
    sticky=tk.NSEW
)



# make Listbox/Scrollbar Frame - font choose
font_frm = ttk.Frame(root)
font_frm.grid(row=1, column=3, columnspan=2, sticky=tk.NSEW)

# temporary font list
my_fonts = ['alpha', 'beta', 'gamma', 'delta', 'epsilon',
    'eta', 'zeta', 'theta', 'greek', 'letters', 'and', 'such']
font_var = tk.StringVar(value=my_fonts)   

# listbox
font_lbox = tk.Listbox(
    font_frm,
    listvariable=font_var,
    height=5,
    selectmode='browse'
)
font_lbox.pack(
    fill="both",
    expand=True,
    side="left",
)

# slider
font_scr = tk.Scrollbar(
    font_frm,
    orient='vertical',
    command=font_lbox.yview
)
font_scr.pack(
    ipadx=5,
    fill="both",
    side="left"
)
font_lbox['yscrollcommand'] = font_scr.set

# listbox function
def font_selected(event):
    cur_font = font_lbox.get(font_lbox.curselection())
    print(f"You chose {cur_font} as your font.")

font_lbox.bind('<<ListboxSelect>>', font_selected)



# make Text - ascii output
out_txtbox = tk.Text(
    root,
    height=8,
    state='disabled'
)
out_txtbox.grid(row=2, column=0, columnspan=5, sticky=tk.NSEW)



# make copy btn and func
def copy_clicked():
    print("You copied the text!")

copy_btn = ttk.Button(
    root,
    padding=10,
    text="Copy",
    command=copy_clicked
)
copy_btn.grid(row=3, column=2, sticky=tk.NSEW)

# make clear btn and func
def clear_clicked():
    print("You cleared the text!")

clear_btn = ttk.Button(
    root,
    padding=10,
    text="Clear",
    command=clear_clicked
)
clear_btn.grid(row=3, column=0, sticky=tk.NSEW)

# make info btn and func
def info_clicked():
    print("You got info!")

info_btn = ttk.Button(
    root,
    padding=10,
    text="Info",
    command=info_clicked
)
info_btn.grid(row=3, column=4, sticky=tk.NSEW)


root.mainloop()