"""
GUI frontend for displaying To-Do list to user graphically using tkinter
"""

import tkinter as tk
import copy
from backend_decoupled import TodoList
from errors import *


# ------ define some global hyperparameters --------
filepath = "tasklist.json" # TODO: take user input

main_button_width = 20
main_font = ("TkDefaultFont",12)

sub_button_width = 17
sub_font = ("TkDefaultFont",11)

# padding:....


class TodoApp:
    """
    gui page/window as an instance of a class associated with the TodoList class
    """
    def __init__(self, root):
        self.todo = TodoList(filepath) # a TodoList object is now coupled to the App page object
        # make copy to compare altered list to when closing app
        self.checkpoint = copy.deepcopy(self.todo.tasklist) # need deepcopy to also copy every single object (dict) inside list
                                                            # instead of just shallow .copy() method

        self.root = root
        self.root.title("To-Do Liste")

        # -------- UI Components -----------
        # TODO: embed frame inside a canvas for scrollability with arbitrarily long lists
        self.frame = tk.Frame(root)
        self.frame.pack(pady=15)

        self.edit_button = tk.Button(root, text="Liste bearbeiten", command=lambda: self.on_edit_task(), 
                                     font=main_font, width=main_button_width
                                     )
        self.edit_button.pack(pady=15)
        self.edit_already_clicked = False # boolean value to track if edit menu is toggled or not

        self.save_button = tk.Button(root, text="Liste speichern", command=lambda: self.on_save_tasks(), 
                                     font=main_font, width=main_button_width
                                     )
        self.save_button.pack(pady=20)

        # TODO: have tasks as interactive labels (stichwort .bind())?
        

        self.on_view_tasks()

    
    def on_view_tasks(self):
        """
        Destroy all widgets embedded inside self.frame and create a new grid, i.e. resfresh displayed list
        """
        for cell in self.frame.winfo_children():
            cell.destroy()

        tasklist = self.todo.view_tasks() # for consistency call view_tasks method, could also simply access tasklist attribute
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
            self.todo.add_task(user_input)
            self.on_view_tasks()
        except DuplicateTaskError as e:
            self.error_window(e)


    def on_delete_task(self):
        user_input = self.entry.get()
        try:
            self.todo.delete_task(user_input)
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

        error_label = tk.Label(window, text=f"Fehler: " + error.error_message, font=("TkDefaultFont",12), pady=20)
        error_label.pack()

        dismiss_button = tk.Button(window, text="Schließen", command=lambda: window.destroy(), font=("TkDefaultFont",12))
        dismiss_button.pack()

        # freeze root in the background until user dismisses error window
        window.transient() # keep on top of root (transient with None)
        window.grab_set() # direct all input and events in application to this window
        window.wait_window() # pause code execution until winodw is destroyed
        #window.mainloop() dont have to call a window's mainloop inside another window's mainloop


    def on_save_tasks(self):
        self.todo.save_tasks(filepath=filepath)
        self.checkpoint = copy.deepcopy(self.todo.tasklist) # update checkpoint
        # only display new confirmation label if not already existing
        if hasattr(self, "confirm_label"):
            pass
        else:
            self.confirm_label = tk.Label(self.root, text=f"Liste gespeichert unter {filepath}")
            self.confirm_label.pack(after=self.save_button)


    def handle_close(self):
        """
        Custom handling of window closing event triggered by 
        user clicking close button 'x' in top right corner of window.
        Check if there have been changes made to the initial todo list
        and prompt user to save it.
        """
        if self.todo.tasklist != self.checkpoint:
            window = tk.Toplevel()
            window.title("Warnung")
            window.geometry("500x150+400+200")

            warn_label = tk.Label(window, text="Achtung: Es gibt ungespeicherte Änderungen. Trotzdem schließen?",
                                   font=("TkDefaultFont",12), pady=20
                                   )
            warn_label.pack()

            dialogue_frame = tk.Frame(window)
            dialogue_frame.pack()
            
            close_button = tk.Button(dialogue_frame, text="Ja", command=lambda: self.root.destroy(), font=("TkDefaultFont",12))
            close_button.grid(row=0, column=0)

            dont_close_button = tk.Button(dialogue_frame, text="Nein", command=lambda: window.destroy(), font=("TkDefaultFont",12))
            dont_close_button.grid(row=0, column=1)

            window.transient() 
            window.grab_set()
            window.wait_window() 
        else:
            self.root.destroy()







if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.state("zoomed") # start maximized
    root.resizable(True, True) # allow resizing
    root.protocol("WM_DELETE_WINDOW", lambda: app.handle_close()) # redirect window closing event to custom handler
    root.mainloop()
    #print("Stopped")
