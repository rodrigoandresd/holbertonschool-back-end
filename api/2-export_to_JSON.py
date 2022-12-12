#!/usr/bin/python3
"""Python script that gather data from an API to export data in the JSON"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    employee = requests.get(user_url + user_id).json()
    username = employee.get("username")
    total_task = requests.get(todos_url, params={"userId": user_id}).json()

    with open(user_id + ".json", "w") as json_file:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in total_task]}, json_file)
