#!/usr/bin/python3
""" """

import sys

import requests


USER_ID = sys.argv[1]

# get employee data
user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
user_resp = requests.get(user_url)

EMPLOYEE_NAME = user_resp.json()["name"]

# get the todos of the user
todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
todo_resp = requests.get(todo_url).json()

completed_todos = list(filter(lambda x: x["completed"], todo_resp))
TOTAL_NUMBER_OF_TASKS = len(todo_resp)
NUMBER_OF_DONE_TASKS = len(completed_todos)


print(f"Employee {EMPLOYEE_NAME} is done with"
		f" tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})")
for todo in completed_todos:
    print(f"\t{todo['title']}")



