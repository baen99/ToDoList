#print('test')

#import os
#print(os.path.exists(''))

import tkinter as tk

#
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimal GUI")

        self.label = tk.Label(root, text="Enter something:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Submit", command=self.on_submit)
        self.button.pack()

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

    def on_submit(self):
        user_input = self.entry.get()
        self.output_label.config(text=f"You entered: {user_input}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
#"""
"""
root = tk.Tk()

# 3 x 3 mesh/grid
for row in range(3):
    for col in range(3):
        cell = tk.Button(root, text=f"Cell {row},{col}")
        cell.grid(column=col, row=row, padx=10, pady=10)

root.mainloop()
"""

"""
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=("col1", "col2"), show="headings")
tree.heading("col1", text="Item A")
tree.heading("col2", text="Item B")
tree.pack()

tree.insert("", tk.END, values=("Value A1", "Value B1"))
tree.insert("", tk.END, values=("Value A2", "Value B2"))

root.mainloop()
"""


"""
root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Populate checkbuttons
for row in range(3):
    for col in range(3):
        cell = tk.Checkbutton(frame, text=f"Cell {row},{col}")
        cell.grid(column=col, row=row, padx=10, pady=10)

# Configure scrollregion dynamically
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_configure)

root.mainloop()
"""

"""
import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("PythonExamples.org")

# Create a variable to store the checkbutton state
checkbutton_var = tk.BooleanVar()

# Create the checkbutton widget
checkbutton_1 = tk.Checkbutton(window, text="Option 1", variable=checkbutton_var, command=lambda: check_denied())

# Set the initial checkbutton state
#checkbutton_var.set(True)
def check_denied():
    checkbutton_var.set(False)

# Pack the checkbutton widget
checkbutton_1.grid()

# Start the Tkinter event loop
window.mainloop()
"""
