# Tkinter Ascii Art
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import art as art
import pyperclip as pc

# make root
root = tk.Tk()
root.title('Tkinter Ascii Art')
root.iconbitmap("./assets/duck.ico")

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
root.rowconfigure(2, weight=4)
root.rowconfigure(3, weight=1)
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
    fill="both",
    padx=50
)

# directions label
directions_str = tk.StringVar(
    value="Type some text in the textbox below. "
    "Choose a font from the menu. " 
    "Copy the output with the Button.")
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



# make Entry/Buttons Frame - input text
in_frm = tk.Frame(root)
in_frm.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)
# in frame grid
in_frm.columnconfigure(0, weight=1)
in_frm.columnconfigure(1, weight=1)
in_frm.columnconfigure(2, weight=1)
in_frm.rowconfigure(0, weight=1)
in_frm.rowconfigure(1, weight=1)

# Entry
input_txt = tk.StringVar(value="teext")
input_ent = ttk.Entry(
    in_frm,
    textvariable=input_txt,
    justify=tk.CENTER
)
input_ent.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)

# copy button and func
def copy_clicked():
    print("You copied the text!") 
    pc.copy(my_text)

copy_btn = ttk.Button(
    in_frm,
    #padding=10,
    text="Copy",
    command=copy_clicked
)
copy_btn.grid(row=1, column=1, sticky=tk.NSEW)

# make clear btn and func
def clear_clicked():
    global input_txt
    input_txt.set("")
    print("You cleared the text!")

clear_btn = ttk.Button(
    in_frm,
    #padding=10,
    text="Clear",
    command=clear_clicked
)
clear_btn.grid(row=1, column=0, sticky=tk.NSEW)

# make info btn and func
def info_clicked():
    print("You got info!")
    log_msg = "Uses Tkinter, Art, and Pyperclip libraries"
    showinfo(
        title="Information",
        message=log_msg
    )

info_btn = ttk.Button(
    in_frm,
    #padding=10,
    text="Info",
    command=info_clicked
)
info_btn.grid(row=1, column=2, sticky=tk.NSEW)



# make Listbox/Scrollbar Frame - font choose
font_frm = ttk.Frame(root)
font_frm.grid(row=1, column=3, columnspan=2, sticky=tk.NSEW)

# font list
ASCII_FONTS = list(set(art.FONT_NAMES) - set(art.NON_ASCII_FONTS))
ASCII_FONTS.sort()
font_var = tk.StringVar(value=ASCII_FONTS) 


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

font_lbox.see(33)

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
cur_font = "bubble"
def font_selected(event):
    global cur_font 
    cur_font = font_lbox.get(font_lbox.curselection())
    #print(f"You chose {cur_font} as your font.")

font_lbox.bind('<<ListboxSelect>>', font_selected)



# make Text Label and Frame - ascii output
out_frm = ttk.Frame(root)
out_frm.grid(row=2, column=0, columnspan=5, sticky=tk.NSEW)

my_text = art.text2art(input_txt.get(), font=cur_font)

out_lbl = ttk.Label(
    out_frm, 
    font=("Consolas", 8),
    text=my_text,
    anchor=tk.CENTER
)
out_lbl.pack(
    fill="both",
    expand=True,
    side="top"
)

def my_after(): 
    global my_text
    my_text = art.text2art(input_txt.get(), font=cur_font)

    out_lbl.config(text=my_text)

    # call again after 100 ms
    root.after(100, my_after)

my_after()



# bottom text
bottom_str = tk.StringVar(
    value="Type some text in the textbox below. "
    "Choose a font from the menu. " 
    "Copy the output with the Button.")
bottom_lbl = ttk.Label(
    root, 
    font=("Times New Roman", 12),
    textvariable=bottom_str,
    anchor=tk.CENTER
)
bottom_lbl.grid(
    row=3,
    column=0,
    columnspan=5,
    sticky=tk.NSEW
)

root.mainloop()