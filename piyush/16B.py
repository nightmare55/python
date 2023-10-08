#Write Python GUI program to add items in listbox widget and to print and delete the selected items from listbox on button click. Provide three separate buttons to add, print and delete.
import tkinter as tk

from pkg_resources import iter_entry_points

def add_item():
    item = iter_entry_points.get()
    listbox.insert(tk.END, item)

def print_items():
    for item in listbox.get(0, tk.END):
        print(item)

def delete_item():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])

root = tk.Tk()
root.title("Listbox Example")

# Create a listbox widget
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)

# Create a button to add items to the listbox
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack(padx=10, pady=10)

# Create a button to print the items in the listbox
print_button = tk.Button(root, text="Print", command=print_items)
print_button.pack(padx=10, pady=10)

# Create a button to delete the selected item from the listbox
delete_button = tk.Button(root, text="Delete", command=delete_item)
delete_button.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()