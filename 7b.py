#Write python GUI program to generate a random password with upper and lower case letters.
from tkinter import *
import random
import string
root = Tk()
root.title("Random Password Generator")
password_label = Label(root, font=("Arial", 50))
password_label.pack()
def generate_password():
    password = ""
    for i in range(10):
        password += random.choice(string.ascii_letters)
    password_label.config(text=password)
generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()
root.mainloop()