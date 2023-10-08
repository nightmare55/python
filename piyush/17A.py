#Write Python GUI program that takes input string and change letter to upper case when a button is pressed
import tkinter as tk
from tkinter import ttk

def convert_to_uppercase():
    input_string = input_entry.get()
    output_string = input_string.upper()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_string)

root = tk.Tk()
root.title("Convert to Uppercase")

# Create a label for the input string
input_label = tk.Label(root, text="Input String:")
input_label.pack(padx=10, pady=10)

# Create an entry widget for the input string
input_entry = tk.Entry(root)
input_entry.pack(padx=10, pady=10)

# Create a button to convert the string to uppercase
convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(padx=10, pady=10)

# Create a label for the output string
output_label = tk.Label(root, text="Output String:")
output_label.pack(padx=10, pady=10)

# Create an entry widget for the output string
output_entry = tk.Entry(root)
output_entry.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()