"""
Main module containing functionalities for the TodoList application.
"""

import json
import os

# TODO: port this to run_todo.py
def show_menu():
    """
    Displays the main menu options to the user.
    """
    print("To-Do List Application")
    print("=======================")
    # TODO: edit task
    #print("Please choose an option:")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save & Exit")

#show_menu()

# todo list as object on which to perform operations
class TodoList():
    """
    Class representing a to-do list.
    """
    def __init__(self, filepath):
        """
        Initializes the TodoList with a given filepath.
        """
        assert os.path.exists(filepath), f"File {filepath} does not exist."

        with open(filepath, 'r') as f:
            self.tasklist = json.load(f)
        
    def view_tasks(self):
        """
        Display the current tasks in the to-do list.
        """
        # check for empty tasklist
        if not self.tasklist:
            print("Currently no tasks.")
            return
        
        print("Current Tasks:")
        for t,task in enumerate(self.tasklist):
            status = 'Erledigt' if task['done'] else 'Offen'
            print(f'{t+1}. {task['name']}: {status}')

        return



