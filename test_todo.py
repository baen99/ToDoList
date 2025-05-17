"""
Runs todolist module
"""

from todolist_backend import TodoList

#def main():
path = 'tasklist.json' # global path to todo list
path2 = 'example for alternative todo list'
todo = TodoList(path) # create TodoList object
print(todo.tasklist)
todo.view_tasks() # view current tasks
todo.add_task(task_name='Putzen')
todo.view_tasks()
#todo.complete_task('Gym')
#todo.view_tasks()
changed_list = todo.delete_task('Einkauf')
todo.view_tasks()
print(changed_list)
#todo.save_tasks()
#saved_todo = TodoList(path)
#print('saved todo list:')
#saved_todo.view_tasks()





#if __name__ == "__main__":
    #main()