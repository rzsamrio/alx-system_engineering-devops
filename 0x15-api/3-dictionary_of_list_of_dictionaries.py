#!/usr/bin/python3
""" REST API: Acquire and use json data """
import json
import requests
import sys

if __name__ == '__main__':

    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()

    result = {}
    for x, user in enumerate(users):
        uid = str(x + 1)
        path = 'https://jsonplaceholder.typicode.com/todos?userId=' + uid
        tasks = requests.get(path).json()
        res = []
        for task in tasks:
            res.append({"username": user['username'], "task": task['title'],
                       "completed": task['completed']})
        result.update({uid: res})

    with open(f'todo_all_employees.json', 'w') as file:
        json.dump(result, file)
