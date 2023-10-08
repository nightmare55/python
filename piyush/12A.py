import tkinter as tk
from tkinter import font

def change_font_style(font_name, font_size, is_bold):
    label_font = font.nametofont("label_font")
    label_font.configure(family=font_name, size=font_size, weight="bold" if is_bold else "normal")
    label.config(font=label_font)

def create_menu():
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    font_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Font Style", menu=font_menu)

    font_names = ["Arial", "Times New Roman", "Courier New"]
    font_sizes = [12, 16, 20]
    is_bold = [False, True]

    for name in font_names:
        for size in font_sizes:
            for bold in is_bold:
                label_text = f"{name}, {size}, {'Bold' if bold else 'Normal'}"
                font_menu.add_command(label=label_text, command=lambda n=name, s=size, b=bold: change_font_style(n, s, b))

if __name__== "__main__":
    root = tk.Tk()
    root.title("Font Style Changer")

    label_font = font.Font(family="Arial", size=12)
    label = tk.Label(root, text="Change the Font Style", font=label_font)
    label.pack()

    create_menu()

    root.geometry("400x200")
    root.mainloop()