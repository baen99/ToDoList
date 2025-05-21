"""
Read from and write into SQLite database storing the tasks instead of simple .json file
"""

import sqlite3


DB_NAME = "todo.db"
#DB_NAME = "test.db"

class DataBase:
    """
    Object representing an SQLite database
    """
    def __init__(self, name=DB_NAME):
        """
        Set up table of todo tasks in database
        """
        self.name = name
        # establish connection or create database if not exists
        self.con = sqlite3.connect(self.name)
        self.cursor = self.con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Tasks (" \
                            "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                            "name TEXT NOT NULL UNIQUE," \
                            "done BOOLEAN NOT NULL CHECK (done IN (0,1))" \
                                                    ")"
                        )
        self.con.commit()
    

    def get_tasks(self):
        query = self.cursor.execute("SELECT * FROM Tasks")
        result = query.fetchall() # list of all rows in table
        return result
    

    def add_task(self, taskname):
        self.cursor.execute("INSERT INTO Tasks (name, done) VALUES (?,?)", (taskname, False))
        self.con.commit()


    def toggle_task(self, taskname):
        query = self.cursor.execute("SELECT done FROM Tasks WHERE name = ?", (taskname,))
        result = query.fetchall()
        # for completeness check if result in not None which shouldn't happen with GUI
        if result:
            current_status = bool(result[0][0])
            inverse_status = not current_status
            self.cursor.execute("UPDATE Tasks SET done = ? WHERE name = ?", (inverse_status, taskname))
            self.con.commit()


    def delete_task(self, taskname):
        self.cursor.execute("DELETE FROM Tasks WHERE name = ?", (taskname,))
        self.con.commit()


    def __del__(self):
        """
        Destructor to close connection when there are no more references to the DataBase object.
        Obsolete when using DataBase as context manager.
        """
        #print("Destructor called")
        self.con.close()


    # ------ Context Manager Methods -----------
    def __enter__(self):
        """
        Run when entering context manager with block.
        Return value is assigned to the variable after the as statement
        """
        #print("__enter__ called")
        return self
    

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Run when exiting context manager with block.
        Run in any case, even when exceptions occur within the with block.
        Additional arguments describe an exception if occurring inside the with block (gets handled by backend logic).
        """
        #print("__exit__ called")
        self.con.close()

