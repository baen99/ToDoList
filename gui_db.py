"""
GUI frontend for database-supported tasklist
"""

import tkinter as tk
from backend_db import TaskManager
from errors import *


# ------ define some global hyperparameters --------
main_button_width = 20
main_font = ("TkDefaultFont",12)

sub_button_width = 17
sub_font = ("TkDefaultFont",11)

# padding:....


class TodoApp:
    """
    gui page/window as an instance of a class associated with the TaskManager class
    """
    def __init__(self, root):
        self.task_manager = TaskManager() # a TaskManager object is now coupled to the App page object to pass the user commands to the database layer

        self.root = root
        self.root.title("To-Do Liste")
        self.root.state("zoomed") # start maximized
        self.root.resizable(True, True) # allow resizing

        # -------- UI Components -----------

        self.container = tk.Frame(root)

        self.header = tk.Frame(self.container)

        self.canvas = tk.Canvas(self.container, height=400, width=450)

        self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas)
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0,0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.container.pack(pady=15)
        self.header.pack(fill="x")
        #self.frame.pack()
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        
        

        self.edit_button = tk.Button(root, text="Liste bearbeiten", command=lambda: self.on_edit_task(), 
                                     font=main_font, width=main_button_width
                                     )
        self.edit_button.pack(pady=15)
        self.edit_already_clicked = False # boolean value to track if edit menu is toggled or not
        

        self.on_view_tasks()

    
    def on_view_tasks(self):
        """
        Destroy all widgets embedded inside self.frame and create a new grid, i.e. resfresh displayed list
        """
        for cell in self.frame.winfo_children():
            cell.destroy()

        tasklist = self.task_manager.get_tasks() # list of tuples
        n_tasks = len(tasklist)

        # row 0 with headings in non-scrollable header frame
        head_id = tk.Label(self.header, text="Nr.", font="bold", pady=10, padx=10)
        head_name = tk.Label(self.header, text="Aufgabe", font="bold", pady=10, padx=10)
        head_status = tk.Label(self.header, text="Status", font="bold", pady=10, padx=10)

        head_id.grid(column=0, row=0)
        head_name.grid(column=1, row=0)
        head_status.grid(column=2, row=0)

        # TODO: Zeilensprung bei langen tasks oder max stringlength


        # have to create vars holding status of checkbox as class attributes
        # that way they are still accessible when calling the mainloop outside of just the method
        self.vars = [tk.BooleanVar() for _ in range(n_tasks)]
        # populate each row with 3 columns for number, name and status of task 
        for row in range(1, n_tasks+1):
             # id column
            id = tk.Label(self.frame, text=str(row), font=("TkDefaultFont",12))
            id.grid(column=0, row=row)

            # name column
            taskname = tasklist[row-1][1]
            name = tk.Label(self.frame, text=taskname, font=("TkDefaultFont",12), padx=50)
            name.grid(column=1, row=row)
            
            # status column
            status = tasklist[row-1][2]
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
        self.task_manager.toggle_task(taskname)
        self.on_view_tasks()


    def on_edit_task(self):
        """
        edit frame is either created or destroyed if already existing such that there are no multiple edit frames
        """
        if self.edit_already_clicked:
            # already clicked can only be true if edit_frame was created, therefore it exists and can be destroyed
            self.edit_frame.destroy()
            self.edit_already_clicked = False
        else:
            self.edit_frame = tk.Frame(self.root)
            self.edit_frame.pack(after=self.edit_button)

            self.entry = tk.Entry(self.edit_frame, width=sub_button_width, font=sub_font)
            self.entry.pack()

            self.add_button = tk.Button(self.edit_frame, text="Aufgabe hinzufügen", command=lambda: self.on_add_task(),
                                        width=sub_button_width, font=sub_font
                                        )
            self.add_button.pack(after=self.entry)

            self.delete_button = tk.Button(self.edit_frame, text="Aufgabe löschen", command=lambda: self.on_delete_task(),
                                           width=sub_button_width, font=sub_font
                                           )
            self.delete_button.pack(after=self.add_button)

            self.edit_already_clicked = True


    def on_add_task(self):
        user_input = self.entry.get()
        try:
            self.task_manager.add_task(user_input)
            self.on_view_tasks()
        except (DuplicateTaskError, AssertionError) as e:
            self.error_window(e)


    def on_delete_task(self):
        user_input = self.entry.get()
        try:
            self.task_manager.delete_task(user_input)
            self.on_view_tasks()
        except TaskNotFoundError as e:
            self.error_window(e)


    def error_window(self, error):
        """
        New window pops up displaying an error message to the user
        """
        window = tk.Toplevel()
        window.title("Fehlermeldung")
        window.geometry("500x150+400+200")

        # args is tuple of arguments passed to the exception constructor
        # which is the error message in all cases that can occur here
        error_label = tk.Label(window, text=f"Fehler: " + error.args[0], font=("TkDefaultFont",12), pady=20)
        error_label.pack()

        dismiss_button = tk.Button(window, text="Schließen", command=lambda: window.destroy(), font=("TkDefaultFont",12))
        dismiss_button.pack()

        # freeze root in the background until user dismisses error window
        window.transient() # keep on top of root (transient with None)
        window.grab_set() # direct all input and events in application to this window
        window.wait_window() # pause code execution until winodw is destroyed
        #window.mainloop() dont have to call a window's mainloop inside another window's mainloop








if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    #print("Stopped")
