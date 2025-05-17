"""
GUI frontend for displaying To-Do list to user graphically using tkinter
"""

import tkinter as tk
from backend_decoupled import TodoList
from errors import *


filepath = "tasklist.json" # TODO: take user input

class TodoApp:
    """
    gui page/window as an instance of a class associated with the TodoList class
    """
    def __init__(self, root):
        self.todo = TodoList(filepath) # a TodoList object is now coupled to the App page object

        self.root = root
        self.root.title("To-Do Liste")

        # -------- UI Components -----------
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)




        self.on_view_tasks()

    
    def on_view_tasks(self):
        self.task_listbox.delete(0, tk.END) # delete all items in current tasklist 
        # populate blank listbox with elements from tasklist
        # TODO: create grid to place checkbox next to task label
        for task in self.todo.view_tasks():
            self.task_listbox.insert(tk.END, task["name"])
            self.task_listbox.insert(tk.END, "test")






if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
