#!/usr/bin/python3
"""Python script that gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    employee = requests.get(user_url + user_id).json()
    total_task = requests.get(todos_url, params={"userId": user_id}).json()
    done_task = requests.get(
        todos_url, params={"userId": user_id, "completed": "true"}).json()
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(done_task), len(total_task)))

    for task in done_task:
        print("\t {}".format(task.get("title")))
