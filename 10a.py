import tkinter as tk
from tkinter import messagebox

# Function to display an alert message
def show_alert():
    messagebox.showinfo("Alert", "Button Pressed!")

# Create a Tkinter window
window = tk.Tk()
window.title("Alert Demo")

# Create a button that triggers the alert message
button = tk.Button(window, text="Press Me", command=show_alert)
button.pack(padx=20, pady=20)

# Run the Tkinter main loop
window.mainloop()







