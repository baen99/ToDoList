"""
Some experimental unit tests for the todolist methods
"""

import unittest
import json
import os
from backend_decoupled import TodoList
from errors import *

class TestTodoList(unittest.TestCase):

    def setUp(self):
        """
        Create and save testlist to disk before every test
        """
        empty_tasks = []
        cwd = os.getcwd() # get current working directory
        self.testpath = cwd+'/testlist.json'
        with open(self.testpath, 'w') as f:
            json.dump(empty_tasks, f)
        
        self.testlist = TodoList(filepath=self.testpath)



    def test_add_task(self):
        testname = 'Test'
        self.testlist.add_task(testname)
        self.assertEqual(len(self.testlist.tasklist), 1) # previously empty test list should only contain 1 task after adding
        self.assertEqual(self.testlist.tasklist[0]['id'], 1) # id should be 1
        self.assertEqual(self.testlist.tasklist[0]['name'], testname) # name should be Test
        self.assertFalse(self.testlist.tasklist[0]['done']) # task should not be done yet
        
        # now check if correct exception is thrown
        with self.assertRaises(DuplicateTaskError) as context:
            self.testlist.add_task(testname)
        
        self.assertEqual(context.exception.task_name, testname)
        self.assertEqual(context.exception.error_message, f"Aufgabe {testname} bereits in To-Do Liste enthalten.")


    def test__task_position(self):
        testname = 'Test'
        self.testlist.add_task(testname)  
        idx = self.testlist._task_position(testname)
        #print(idx)
        self.assertEqual(idx, 0)  


    def test__task_exists(self):
        testname = 'Test'
        self.testlist.add_task(testname)   
        self.assertTrue(self.testlist._task_exists(testname))
        self.assertFalse(self.testlist._task_exists("Test2"))


    # TODO: test other functions of TodoList
    
    
       
    def tearDown(self):
        """
        Delete mock list after every test
        """
        os.remove(self.testpath)
    


if __name__ == '__main__':
    unittest.main()
