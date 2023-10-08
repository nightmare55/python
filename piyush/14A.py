#Write a Python GUI program to accept dimensions of a cylinder and display the surface area and volume of cylinder.
import math
import tkinter as tk
def calculate_surface_area_and_volume():
    radius = float(radius_entry.get())
    height = float(height_entry.get())
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    volume = math.pi * radius ** 2 * height
    surface_area_label.config(text=f"Surface Area: {surface_area:.2f}")
    volume_label.config(text=f"Volume: {volume:.2f}")
root = tk.Tk()
root.title("Cylinder Surface Area and Volume Calculator")
# Create a frame for the entry widgets
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10)
# Create a label and entry widget for the radius
radius_label = tk.Label(entry_frame, text="Radius:")
radius_label.pack(side=tk.LEFT)
radius_entry = tk.Entry(entry_frame)
radius_entry.pack(side=tk.LEFT, padx=10)
# Create a label and entry widget for the height
height_label = tk.Label(entry_frame, text="Height:")
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(entry_frame)
height_entry.pack(side=tk.LEFT, padx=10)
# Create a button to calculate the surface area and volume
calculate_button = tk.Button(root, text="Calculate", command=calculate_surface_area_and_volume)
calculate_button.pack(padx=10, pady=10)
# Create a label to display the surface area
surface_area_label = tk.Label(root, text="Surface Area:")
surface_area_label.pack(padx=10, pady=10)
# Create a label to display the volume
volume_label = tk.Label(root, text="Volume:")
volume_label.pack(padx=10, pady=10)
# Start the main loop
root.mainloop()
