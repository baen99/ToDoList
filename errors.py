"""
Define custom to-do related error classes which are more descriptive than simply ValueError
"""

class TodoError(Exception):
    """
    Base class from which all other errors are derived.
    Multiple different derived errors can be caught with one except TodoError statement.
    """
    pass


class TaskNotFoundError(TodoError):
    """
    Raised when task requested by user is not in the current tasklist.
    """
    def __init__(self, task_name):
        self.task_name = task_name
        self.error_message = f"Aufgabe {self.task_name} nicht gefunden."
        super().__init__(self.error_message)


class DuplicateTaskError(TodoError):
    """
    Raised when task requested by user is already in the current tasklist.
    """
    def __init__(self, task_name):
        self.task_name = task_name
        self.error_message = f"Aufgabe {self.task_name} bereits in To-Do Liste enthalten."
        super().__init__(self.error_message)


class TaskAlreadyDoneError(TodoError):
    """
    Raised when task passed to mark_done by user is already done.
    """
    def __init__(self, task_name):
        self.task_name = task_name
        self.error_message = f"Aufgabe {self.task_name} bereits."
        super().__init__(self.error_message)