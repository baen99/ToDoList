"""
Runs todolist module in CLI interface
"""

#import json
from todolist_backend import TodoList

print("To-Do Liste")
print("=======================")

def show_menu():
    """
    Displays the main menu options to the user.
    """

    print()
    # TODO: edit task
    #print("Please choose an option:")
    print("1. Aufgaben anzeigen")
    print("2. Aufgabe hinzufügen")
    print("3. Aufgabe als erledigt setzen")
    print("4. Aufgabe löschen")
    print("5. Speichern & Verlassen")
    print()


# declare filepath globally
path = input('Dateipfad der To-Do Liste (enter für default): ')
if path == '':
    path = 'tasklist.json' # default path to todo list
#path2 = 'example for alternative todo list'
todo = TodoList(path) # create TodoList object


#def main():
# loop over input options until exit option is chosen
while True:

    show_menu()
    # user input to choose what function is executed
    option = input('Wähle eine Option 1-5: ')
    print()
    # assertion handled by default case in switch
    #assert option in ['1','2','3','4','5'], 'Wähle eine gültige Option (1-5)'

    match option:
        case '1':
            todo.view_tasks()
        case '2':
            task_name = input('Name der Aufgabe: ')
            todo.add_task(task_name)
        case '3':
            task_name = input('Name der Aufgabe: ')
            todo.complete_task(task_name)
        case '4':
            task_name = input('Name der Aufgabe: ')
            todo.delete_task(task_name)
        case '5':
            save_path = input('Dateipfad der Liste (enter für default): ')
            if save_path == '':
                save_path = None
            todo.save_tasks(save_path)
            break
        case _:
            print('Wähle eine gültige Option (1-5).')

print('------------------')
print('Frohes Schaffen!..')






#if __name__ == "__main__":
    #main()