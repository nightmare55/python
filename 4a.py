#Write Python GUI program to create background with changing colors
import tkinter as tk
import random

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = '#{:02x}{:02x}{:02x}'.format (r, g, b)
    root.config(bg=color)  # Set the background color of the root window
    root.after(1000, change_color)  # Call the function again after 1000 milliseconds (1 second)

root = tk.Tk()
root.geometry("400x300")
root.title("Color Changing Background")

change_color()  # Start the color changing process

root.mainloop()

