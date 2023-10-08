# Write  a  Python  GUI  program  to  create  a  label  and  change  the  label  font  style  (font name, bold, size). Specify separate check button for each style

from tkinter import *
from tkinter import font
import tkinter as tk

# Create the main window
root = Tk()
root.title("Label Font Style")

# Create the label
label = Label(root, text="This is a label")
label.pack()

# Create the check buttons for font name, bold, and size
font_name_var = StringVar()
font_name_checkbutton = Checkbutton(root, text="Font Name", variable=font_name_var)
font_name_checkbutton.pack()

bold_var = BooleanVar()
bold_checkbutton = Checkbutton(root, text="Bold", variable=bold_var)
bold_checkbutton.pack()

size_var = IntVar()
size_scale = Scale(root, from_=10, to=30, variable=size_var)
size_scale.pack()

# Bind the check buttons and scale to the label's font style
def change_font_style():
    font_name = font_name_var.get()
    font_weight = "bold" if bold_var.get() else "normal"
    font_size = size_var.get()
    
    label.config(
        font=(font_name, font_size, font_weight)
    )

# font_name_checkbutton.config(command=change_font_style)
# bold_checkbutton.config(command=change_font_style)
# size_scale.config(command=change_font_style)

update_button = tk.Button(root, text="Update Font", command=change_font_style)
update_button.pack()
# Start the main loop
root.mainloop()