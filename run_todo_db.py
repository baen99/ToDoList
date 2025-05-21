"""
Main program which runs the whole app
"""

import tkinter as tk
from gui_db import TodoApp


root = tk.Tk()
app = TodoApp(root)
with app.task_manager.db as database:
    root.mainloop()
#print("End")