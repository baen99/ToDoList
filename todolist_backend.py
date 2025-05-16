"""
Main module containing functionalities for the TodoList application.
"""

import json
import os


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
        try:
            assert os.path.exists(filepath), f"Dateipfad {filepath} konnte nicht gefunden werden."
        except AssertionError as e:
            print(e)
            # if path is invalid return empty list
            self.tasklist = []
        else:
            self.filepath = filepath

            with open(filepath, 'r') as f:
                self.tasklist = json.load(f)

        

        
    def view_tasks(self):
        """
        Display the current tasks in the to-do list.
        """
        # check for empty tasklist
        if not self.tasklist:
            print("Aktuell keine Aufgaben.")
            return
        
        print("Aktuelle Aufgaben:")
        for t,task in enumerate(self.tasklist):
            status = 'Erledigt' if task['done'] else 'Offen'
            print(f'{t+1}. {task['name']}: {status}')

        return
    

    def add_task(self, task_name):
        """
        Add a new task to an existing To-Do list
        """

        # assert new task doesn't already exist
        task_found = False
        for task in self.tasklist:
            if task['name'] == task_name:
                task_found = True
                break
            else:
                pass

        if task_found:
            print('Aufgabe bereits in To-Do Liste enthalten.')
            return

        new_task = {'id' : len(self.tasklist)+1,
                    'name' : task_name,
                    'done' : False
                    }
        self.tasklist.append(new_task)
        print(f'Aufgabe {task_name} erfolgreich hinzugefügt.')
        return 
    
    
    def complete_task(self, task_name):
        """
        Mark a task as completed
        """

        # assert that completed task exists
        task_found = False
        for task in self.tasklist:
            if task['name'] == task_name:
                completed_task = task
                task_found = True
                break
            else:
                pass

        if not task_found:
            print('Aufgabe nicht gefunden.')
            return
        
        # check if task already done
        if completed_task['done']:
            print('Aufgabe bereits erledigt.')
            return
        
        completed_task['done'] = True

        print(f'Aufgabe {task_name} als erledigt gesetzt.')
        return
    

    def delete_task(self, task_name):
        """
        Delete a task from the To-Do list
        """

        task_found = False
        # iterate over copy of tasklist to avoid conflicts
        for t, task in list(enumerate(self.tasklist)):
            if task['name'] == task_name:
                del self.tasklist[t]
                task_found = True
                break  # Exit loop after deletion to avoid iteration issues

        # Rebuild the tasklist with consistent IDs
        for t, task in enumerate(self.tasklist):
            task['id'] = t + 1

        if not task_found:
            print('Aufgabe nicht gefunden.')
            return
        
        print(f'Aufgabe {task_name} erfolgreich gelöscht.')
        return self.tasklist
    

    def save_tasks(self, filepath=None):
        """
        Saves the altered tasklist to the specified filepath.
        If no filepath is provided, it uses the object's default filepath.
        """
        if filepath is None:
            filepath = self.filepath  # Use the object's self.filepath attribute

        with open(filepath, 'w') as f:
            json.dump(self.tasklist, f, indent=4)

        print(f"To-Do Liste gespeichert unter {filepath}.")
        return






