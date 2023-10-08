#Write  Python  GUI  program  to  add  menu  bar  with  name  of  colors  as  options  to change the background color as per selection from menu option.
import tkinter as tk
def change_background_color(color):
    root.config(bg=color)

root = tk.Tk()
root.title("Color Menu")
# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
# Create a color menu
color_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Colors", menu=color_menu)
# Add color options to the menu
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
for color in colors:
    color_menu.add_command(label=color, command=lambda c=color: change_background_color(c))
# Start the main loop
root.mainloop()