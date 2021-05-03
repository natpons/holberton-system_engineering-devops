#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com/, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]
    # requests.get(url, params={key: value}, args)
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(userId)).json()
    # format GET /comments?postId=1
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    completed_tasks = []

    for task in todo:
        # use get to access to dictionary value by key
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))

    print('Employee {} is done with tasks({}/{})'.
          format(user.get('name'), len(completed_tasks), len(todo)))

    for task in completed_tasks:
        print('\t {}'.format(task))
