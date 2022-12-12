#!/usr/bin/python3
"""Python script that gather data from an API"""

import csv
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    employee = requests.get(user_url + user_id).json()
    username = employee.get("username")
    total_task = requests.get(todos_url, params={"userId": user_id}).json()
    with open(user_id + ".csv", "w")  as cvs_file:
        writer = csv.writer(cvs_file, quoting=csv.QUOTE_ALL)
        for task in total_task:
            writer.writerow([user_id] + [username] + [task.get("completed")] + [task.get("title")])
