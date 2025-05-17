#print('test')

#import os
#print(os.path.exists(''))

import tkinter as tk

"""
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
"""

root = tk.Tk()

# 3 x 3 mesh/grid
for row in range(3):
    for col in range(3):
        cell = tk.Button(root, text=f"Cell {row},{col}")
        cell.grid(column=col, row=row)

root.mainloop()
