import json
import os

task1 = {'id':1,
         'name':'Gym',
         'done':True
         }
task2 = {'id':2,
         'name':'Einkauf',
         'done':False
         }
tasks = [task1, task2]

cwd = os.getcwd() # get current working directory

with open(cwd+'/tasklist.json', 'w') as f:
  json.dump(tasks, f)