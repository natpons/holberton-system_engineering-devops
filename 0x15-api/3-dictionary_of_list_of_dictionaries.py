#!/usr/bin/python3
"""
task0: Using https://jsonplaceholder.typicode.com/, for a given employee ID,
returns information about his/her TODO list progress
now: Extend your script to export data in the JSON format
"""

import json
import requests


if __name__ == "__main__":
    # Serialization:
    # 1. to form dicts: users_dict(dict of list of dicts),
    # task_dict(list of dicts)
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    users_dict = {}
    username_dict = {}
    for user in users:
        user_id = user.get("id")
        # key: value, for each id - a list of dicts
        users_dict[user_id] = []
        # dict: id : username
        username_dict[user_id] = user.get("username")

    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for task in todo:
        task_dict = {}
        user_id = task.get('userId')
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username_dict.get(user_id)
        # for each userId append list of dicts(task_dict)
        users_dict.get(user_id).append(task_dict)

    # 2. to write obj python to the file JSON
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(users_dict, json_file)
