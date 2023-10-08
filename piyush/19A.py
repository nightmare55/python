#Write  a  Python  GUI  program  to  accept  a  number form  user  and  display its multiplication table on button click
import tkinter as tk
def multiplication_table():
    number = int(number_entry.get())
    for i in range(1, 11):
        result = number * i
        output_list.insert(tk.END, f"{number} x {i} = {result}")
root = tk.Tk()
root.title("Multiplication Table")
# Create a label for the input number
number_label = tk.Label(root, text="Enter a number:")
number_label.pack(padx=10, pady=10)
# Create an entry widget for the input number
number_entry = tk.Entry(root)
number_entry.pack(padx=10, pady=10)
# Create a button to generate the multiplication table
generate_button = tk.Button(root, text="Generate Multiplication Table", command=multiplication_table)
generate_button.pack(padx=10, pady=10)
# Create a listbox to display the multiplication table
output_list = tk.Listbox(root)
output_list.pack(padx=10, pady=10)
# Start the main loop
root.mainloop()