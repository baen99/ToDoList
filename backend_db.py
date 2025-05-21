"""
Backend modified for database integration.
Basically just passes the function calls from the GUI frontend
to the corresponding queries in the database layer 
with some validation logic of user input and appropriate exception handling.
Most of the previously needed logic when performing operatoins on the tasklist 
(like appending, indexing, check for duplicates etc...) is now formulated in the queries and handled by SQL.
"""

import sqlite3
from database import DataBase
from errors import *

class TaskManager:
    def __init__(self):
        self.db = DataBase()


    def get_tasks(self):
        return self.db.get_tasks() # list of tuples
    

    def add_task(self, taskname):
        """
        error can occur if task already exists or empty taskname
        """
        assert taskname, "Aufgabenname darf nicht leer sein."
        try:
            self.db.add_task(taskname)
        except sqlite3.IntegrityError:
            raise DuplicateTaskError(taskname) # convert built-in error to custom one
        

    def toggle_task(self, taskname):
        self.db.toggle_task(taskname)


    def delete_task(self, taskname):
        """
        SQL doesn't throw an exception when taskname doesn't exist.
        Still want to display a message to the user in that case
        """
        tasklist = self.get_tasks() # list of tuples
        task_exists = any(taskname in tup for tup in tasklist)
        if not task_exists:
            raise TaskNotFoundError(taskname) 
        self.db.delete_task(taskname)
        


