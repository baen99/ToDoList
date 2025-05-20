#print('test')

#import os
#print(os.path.exists(''))

import tkinter as tk

"""
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimal GUI")
        self.root.geometry("500x300+400+200")

        self.label = tk.Label(root, text="Enter something:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Submit", command=self.on_submit)
        self.button.pack()

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()


    def on_submit(self):
        user_input = self.entry.get()
        self.output_label.config(text=f"You entered: {user_input}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
"""
"""
root = tk.Tk()

# 3 x 3 mesh/grid
for row in range(3):
    for col in range(3):
        cell = tk.Button(root, text=f"Cell {row},{col}")
        cell.grid(column=col, row=row, padx=10, pady=10)

root.mainloop()
"""

"""
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=("col1", "col2"), show="headings")
tree.heading("col1", text="Item A")
tree.heading("col2", text="Item B")
tree.pack()

tree.insert("", tk.END, values=("Value A1", "Value B1"))
tree.insert("", tk.END, values=("Value A2", "Value B2"))

root.mainloop()
"""


"""
root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Populate checkbuttons
for row in range(3):
    for col in range(3):
        cell = tk.Checkbutton(frame, text=f"Cell {row},{col}")
        cell.grid(column=col, row=row, padx=10, pady=10)

# Configure scrollregion dynamically
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_configure)

root.mainloop()
"""

"""
import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("PythonExamples.org")

# Create a variable to store the checkbutton state
checkbutton_var = tk.BooleanVar()

# Create the checkbutton widget
checkbutton_1 = tk.Checkbutton(window, text="Option 1", variable=checkbutton_var, command=lambda: check_denied())

# Set the initial checkbutton state
#checkbutton_var.set(True)
def check_denied():
    checkbutton_var.set(False)

# Pack the checkbutton widget
checkbutton_1.grid()

# Start the Tkinter event loop
window.mainloop()
"""

#"""
import sqlite3

DB_NAME = "test.db"
# sqlite3.connect() implicitly creates database if it does not exist
con = sqlite3.connect(DB_NAME)
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (" \
                    "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                    "name TEXT NOT NULL UNIQUE," \
                    "done BOOLEAN NOT NULL CHECK (done IN (0,1))" \
                                                ")"
                )
#cursor.execute("DROP TABLE tasks")
con.commit()

test_input = [("Gym",1), ("Einkauf",0)]
#cursor.executemany("INSERT INTO tasks (name, done) VALUES (?,?)", test_input)
try:
    cursor.execute("INSERT INTO tasks (name,done) VALUES (?,?)", (None,2))
except sqlite3.Error as e:
    print(e.__class__.__name__)
#con.commit()

#uery = cursor.execute("DELETE FROM tasks WHERE name = 'Gym'")
#rint(query.fetchall())
#con.commit()

#cursor.execute("INSERT INTO tasks (name,done) VALUES (?,?)", ("Gym", False))
#con.commit()

#cursor.execute("UPDATE tasks SET done = ? WHERE name = ?", (False, "Einkauf"))
#con.commit()

#res = cursor.execute("SELECT name FROM sqlite_master")
res = cursor.execute("SELECT * FROM tasks")
#res = cursor.execute("SELECT done FROM tasks WHERE name = ?", ("Putzen",))
res_list = res.fetchall()
print(res_list)
#print(res_list[0][1])
if not res_list:
    print("Empty!")


con.close()
con.close()
#"""

"""
from database import DataBase
db = DataBase()
print(db.name)
"""