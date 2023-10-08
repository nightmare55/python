# Write  Python  GUI  program  to  accept  a  number  n  and  check  whether  it  is  Prime, Perfect or Armstrong number or not. Specify three radio buttons.
from tkinter import *
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_perfect(n):
    sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum += i
    return sum == n

def is_armstrong(n):
    s = str(n)
    l = len(s)
    sum = 0
    for dc in s:
        sum += int(dc)**l
    return sum == n

def display_result():
    n = int(entry.get())
    option = var.get()
    result = ""
    if option == 1:
        result = "Prime Number" if is_prime(n) else "Not Prime Number"
    elif option == 2:
        result = "Perfect Number" if is_perfect(n) else "Not Perfect Number"
    elif option == 3:
        result = "Armstrong Number" if is_armstrong(n) else "Not Armstrong Number"
    label.config(text=result)

window = Tk()
window.title("Number Checker")
window.geometry("300x200")
Label(window, text="Enter a number and select an option:").pack()
entry = Entry(window)
entry.pack(padx=10, pady=10)
var = IntVar()
var.set(1)
Radiobutton(window, text="Prime", variable=var, value=1).pack()
Radiobutton(window, text="Perfect", variable=var, value=2).pack()
Radiobutton(window, text="Armstrong", variable=var, value=3).pack()
Button(window, text="Check", command=display_result).pack()
label = Label(window, text="")
label.pack(padx=10, pady=10)
window.mainloop()