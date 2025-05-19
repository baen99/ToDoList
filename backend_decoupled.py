"""
Backend To-Do list logic completely decoupled from frontend.
Can be used for arbitrary frontend (CLI/GUI)
"""

import json
import os
import numpy as np
from errors import *



# todo list as object on which to perform operations
class TodoList():
    """
    Class representing a to-do list.
    """
    def __init__(self, filepath):
        """
        Initializes the TodoList with a given filepath.
        """
        # check if path exists
        if not os.path.exists(filepath):
            self.tasklist = []
            raise FileNotFoundError(f"Dateipfad {filepath} konnte nicht gefunden werden. Leere Liste [] angelegt.")
        
        self.filepath = filepath

        with open(filepath, 'r') as f:
                self.tasklist = json.load(f)

        

        
    def view_tasks(self):
        """
        Simply return tasklist, displaying is done in frontend
        """

        return self.tasklist
    

    def add_task(self, task_name):
        """
        Add a new task to an existing To-Do list
        """

        # assert new task doesn't already exist
        if self._task_exists(task_name):
            #raise ValueError(f"Aufgabe bereits in To-Do Liste enthalten.")
            raise DuplicateTaskError(task_name)

        new_task = {'id' : len(self.tasklist)+1,
                    'name' : task_name,
                    'done' : False
                    }
        self.tasklist.append(new_task)
        return 
    

    def _task_exists(self, task_name):
        """
        Private backend function to check if a given task is already in the list
        """
        return any(task["name"] == task_name for task in self.tasklist)
    

    def _task_position(self, task_name):
        """
        Helper function to return index of given task in tasklist
        TODO: How to deal with duplicate tasks? Can't create them
              but can be introduced when reading in filepath to custom list
        TODO: Right now only called when existing task is confirmed, therefore
              list can't be empty and indexing [0] can be done;
              for the future would be nice to pick up the case of empty list
        """
        return np.argwhere(list(task["name"] == task_name for task in self.tasklist)).reshape(-1)[0]
    
    
    def complete_task(self, task_name):
        """
        Mark a task as completed
        """

        # assert that completed task exists
        if not self._task_exists(task_name):
            #raise ValueError("Aufgabe nicht gefunden.")
            raise TaskNotFoundError(task_name)
        
        task_idx = self._task_position(task_name)
        completed_task = self.tasklist[task_idx]
        
        # check if task already done
        if completed_task['done']:
            #raise ValueError("Aufgabe bereits erledigt.")
            raise TaskAlreadyDoneError(task_name)
        
        completed_task['done'] = True

        return
    

    def toggle_task(self, task_name):
        """
        Switch done status between True and False arbitrarily.
        For GUI frontend only (therefore don't have to check for existence of task)
        """
        task_idx = self._task_position(task_name)
        task = self.tasklist[task_idx]
        current_status = task["done"]
        
        # invert current status
        task['done'] = not current_status

        return
    

    def delete_task(self, task_name):
        """
        Delete a task from the To-Do list
        """

         # assert that task exists
        if not self._task_exists(task_name):
            #raise ValueError("Aufgabe nicht gefunden.")
            raise TaskNotFoundError(task_name) 
                  
        
        # build new list and leave out deleted task
        self.tasklist = [task for task in self.tasklist if task["name"] != task_name]
        # Rebuild the tasklist with consistent IDs
        for t, task in enumerate(self.tasklist):
            task['id'] = t + 1

        return
    

    def save_tasks(self, filepath=None):
        """
        Saves the altered tasklist to the specified filepath.
        If no filepath is provided, it uses the object's default filepath.
        """
        if filepath is None:
            # save at default path if filepath attribute wasn't assigned in 
            # __init__() because invalid filepath was passed
            # TODO: check for new default path already existing
            filepath = getattr(self, "filepath", "new_default_path.json")

        with open(filepath, 'w') as f:
            json.dump(self.tasklist, f, indent=4)

        return filepath






