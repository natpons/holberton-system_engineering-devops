#!/usr/bin/python3

"""
task0: Using https://jsonplaceholder.typicode.com/, for a given employee ID,
returns information about his/her TODO list progress
now: Extend your script to export data in the JSON format:
JSON string representation
"""

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]

    # Body.json():Takes a Response stream and reads it to completion
    # Returns: this object could be anything that can be
    # represented by JSON - an object, an array, a string, a number
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(userId)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    tasks = []

    # Serialization:
    # 1. to form a tasks(list of dicts)
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = user.get('username')
        tasks.append(task_dict)

    # 2. to write obj python(dict json_object) to the file JSON:
    json_object = {}
    # key: value
    json_object[userId] = tasks
    with open('{}.json'.format(userId), 'w') as json_file:
        # dict to be serialized and the file to which the bytes will be written
        json.dump(json_object, json_file)
