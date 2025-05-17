"""
Runs todolist module in CLI interface
"""

from backend_decoupled import TodoList
from errors import *

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
try:
    todo = TodoList(path) # create TodoList object
except FileNotFoundError as e:
    print(e)


# loop over input options until exit option is chosen
while True:

    show_menu()
    # user input to choose what function is executed
    option = input('Wähle eine Option 1-5: ')
    print()

    match option:
        case '1':
            tasklist = todo.view_tasks()
            # check for empty tasklist
            if not tasklist:
                print("Aktuell keine Aufgaben.")

            else:
                print("Aktuelle Aufgaben:")
                for t,task in enumerate(tasklist):
                    status = 'Erledigt' if task['done'] else 'Offen'
                    print(f'{t+1}. {task['name']}: {status}')

        case '2':
            task_name = input('Name der Aufgabe: ')
            try:
                todo.add_task(task_name)
                print(f"Aufgabe {task_name} erfolgreich hinzugefügt.")
            except DuplicateTaskError as e:
                print("Fehler: " + e.error_message)

        case '3':
            task_name = input('Name der Aufgabe: ')
            try:
                todo.complete_task(task_name)
                print(f'Aufgabe {task_name} als erledigt gesetzt.')
            # can catch both error types in complete_Task with one statement since both
            # inherit from base class TodoError
            except TodoError as e:
                print("Fehler: " + e.error_message)

        case '4':
            task_name = input('Name der Aufgabe: ')
            try:
                todo.delete_task(task_name)
                print(f'Aufgabe {task_name} erfolgreich gelöscht.')
            except TaskNotFoundError as e:
                print("Fehler: " + e.error_message)

        case '5':
            save_path = input('Dateipfad der Liste (enter für default): ')
            if save_path == '':
                save_path = None
            filepath = todo.save_tasks(save_path)
            print(f"To-Do Liste gespeichert unter {filepath}.")
            break

        case _:
            print('Wähle eine gültige Option (1-5).')

print('------------------')
print('Frohes Schaffen!..')


