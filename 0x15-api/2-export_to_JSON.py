#!/usr/bin/python3
""" Return data in JSON fromat """
import json
import requests
import sys

if __name__ == '__main__':
    uid = sys.argv[1]

    user = (requests.get('https://jsonplaceholder.typicode.com/users/'
            + sys.argv[1])).json()
    Name = user['username']

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                         + uid).json()
    res = []
    for task in tasks:
        res.append({"task": task['title'], "completed": task['completed'],
                   "username": Name})
    with open(f'{uid}.json', 'w') as file:
        result = {uid: res}
        json.dump(result, file)
