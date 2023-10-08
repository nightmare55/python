#Write Python GUI program to take accept your birth date and output your age when a button is pressed
from tkinter import *
from datetime import datetime
def calculate_age():
  birth_date = entry.get()
  birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
  today = datetime.now()
  age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
  label.config(text=f"Your age is: {age}")
root = Tk()
root.title("Age Calculator")
label = Label(root, text="Enter your birth date (YYYY-MM-DD):")
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text="Calculate Age", command=calculate_age)
button.pack()
root.mainloop()