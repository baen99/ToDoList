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
    print("2. Add Task")
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

        self.filepath = filepath

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

        return
    

    def delete_task(self, task_name):
        """
        Delete a task from the To-Do list
        """

        task_found = False
        for t,task in enumerate(self.tasklist):
            if task['name'] == task_name:
                del self.tasklist[t]
                task_found = True

            # make sure ids remain consistent
            self.tasklist[t]['id'] = t+1

        if not task_found:
            print('Aufgabe nicht gefunden.')
            return
        
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






