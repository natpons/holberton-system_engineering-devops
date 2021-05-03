#!/usr/bin/python3
"""
task0: Using https://jsonplaceholder.typicode.com/, for a given employee ID,
returns information about his/her TODO list progress
now: Extend your script to export data in the CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]
    # requests.get(url, params={key: value}, args)
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(userId)).json()
    # todo list for userId, format GET /comments?postId=1
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()

    with open("{}.csv".format(userId), 'w') as csv_file:
        # https://realpython.com/python-csv/
        employee_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            employee_writer.writerow([userId, user.get('username'),
                                      task.get('completed'),
                                      task.get('title')])
