#!/usr/bin/python3
"""Python script that gather data from an API to export data in the JSON"""

import json
import requests


if __name__ == "__main__":
    dict_tasks = {}
    employees_d = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    todos_d = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    dict_tasks = {item.get("id"):
                  [{"username": item.get("username"),
                    "task": j.get("title"),
                    "completed": j.get("completed")}
                   for j in todos_d
                   if j.get("userId") == item.get("id")]
                  for item in employees_d}

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dict_tasks, f)
