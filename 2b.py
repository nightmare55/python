# #Write Python GUI program to create a digital clock with Tkinter to display the time.
from tkinter import *
from datetime import datetime
root = Tk()
root.title("Digital Clock")
# Create a label to display the time
time_label = Label(root, font=("Arial", 50))
time_label.pack()
# Create a function to update the time
def update_time():
    # Get the current time
    current_time = datetime.now()
    # Format the time
    formatted_time = current_time.strftime("%H:%M:%S")
    # Update the label with the new time
    time_label.config(text=formatted_time)
# Update the time every second
root.after(1000, update_time)
# Start the main loop
root.mainloop()
