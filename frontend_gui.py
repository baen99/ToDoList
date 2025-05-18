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
        # TODO: embed frame inside a canvas for scrollability with arbitrarily long lists
        self.frame = tk.Frame(root)
        self.frame.pack(pady=15)

        # TODO: button sollte nur einmal clickbar sein oder edit menu muss wieder verschwinden
        self.edit_button = tk.Button(root, text="Liste bearbeiten", command=lambda: self.on_edit_task(), font=("TkDefaultFont",12))
        self.edit_button.pack(pady=15)

        self.save_button = tk.Button(root, text="Speichern & Verlassen")#, command=self.on_save_tasks())
        self.save_button.pack(pady=20)

        # TODO: label to display messages to user?
        # TODO: have tasks as interactive labels (stichwort .bind())?



        

        self.on_view_tasks()

    
    def on_view_tasks(self):
        """
        Destroy all widgets embedded inside self.frame and create a new grid, i.e. resfresh displayed list
        """
        for cell in self.frame.winfo_children():
            cell.destroy()

        tasklist = self.todo.view_tasks() # for consistency call view_tasks method, could also simply access tasklist attribute
        print(tasklist)
        n_tasks = len(tasklist)

        # row 0 with headings
        head_id = tk.Label(self.frame, text="Nr.", font="bold", pady=10, padx=10)
        head_name = tk.Label(self.frame, text="Aufgabe", font="bold", pady=10, padx=10)
        head_status = tk.Label(self.frame, text="Status", font="bold", pady=10, padx=10)

        head_id.grid(column=0, row=0)
        head_name.grid(column=1, row=0)
        head_status.grid(column=2, row=0)

        # have to create vars holding status of checkbox as class attributes
        # that way they are still accessible when calling the mainloop outside of just the method
        self.vars = [tk.BooleanVar() for _ in range(n_tasks)]
        # populate each row with 3 columns for number, name and status of task 
        for row in range(1, n_tasks+1):
             # id column
            id = tk.Label(self.frame, text=str(row), font=("TkDefaultFont",12))
            id.grid(column=0, row=row)

            # name column
            taskname = tasklist[row-1]["name"]
            name = tk.Label(self.frame, text=taskname, font=("TkDefaultFont",12))
            name.grid(column=1, row=row)
            
            # status column
            status = tasklist[row-1]["done"]
            self.vars[row-1].set(status)
            check_done = tk.Checkbutton(
                self.frame,
                height=3,
                width=3,
                variable=self.vars[row-1],
                command=lambda t=taskname: self.on_toggle_task(t) # need to wrap function inside lambda statement in order to
                                                                    # create a function object that is run when the button is clicked
                                                                    # instead of immediately
            )
            check_done.grid(column=2, row=row)
            



    def on_toggle_task(self, taskname):
        """
        can no longer run into TaskNotFoundError since user can only choose between actually existing tasks
        """
        self.todo.toggle_task(taskname)
        self.on_view_tasks()


    def on_edit_task(self):
        self.entry = tk.Entry(self.root)
        self.entry.pack(after=self.edit_button)
        self.add_button = tk.Button(self.root, text="Aufgabe hinzufügen", command=lambda: self.on_add_task())
        self.add_button.pack(after=self.entry)
        self.delete_button = tk.Button(self.root, text="Aufgabe löschen", command=lambda: self.on_delete_task())
        self.delete_button.pack(after=self.add_button)


    def on_add_task(self):
        user_input = self.entry.get()
        try:
            self.todo.add_task(user_input)
            self.on_view_tasks()
        except DuplicateTaskError as e:
            pass
            # TODO: open new window displaying error message to user


    def on_delete_task(self):
        user_input = self.entry.get()
        try:
            self.todo.delete_task(user_input)
            self.on_view_tasks()
        except TaskNotFoundError as e:
            pass
            # TODO: open new window displaying error message to user











        






if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.state("zoomed") # start maximized
    root.resizable(True, True) # allow resizing
    root.mainloop()
