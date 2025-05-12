"""
Runs todolist module
"""

import json
from todolist import TodoList

#def main():
path = 'tasklist.json' # global path to todo list
todo = TodoList(path) # create TodoList object
#print(todo.tasklist)
todo.view_tasks() # view current tasks



#if __name__ == "__main__":
    #main()