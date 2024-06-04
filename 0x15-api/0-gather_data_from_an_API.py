#!/usr/bin/python3
""" Gather data from a REST API """
import requests
import sys

if __name__ == '__main__':
    id = int(sys.argv[1])
    uri = 'https://jsonplaceholder.typicode.com'
    user = requests.get(uri + '/users/' + sys.argv[1]).json()
    Name = user['name']

    tasks = requests.get(uri + '/todos?userId=' + sys.argv[1]).json()
    Total = len(tasks)
    done_tasks = requests.get(uri + '/todos?userId=' + sys.argv[1] +
                              '&completed=true').json()
    Done = len(done_tasks)

    print(f'Employee {Name} is done with tasks({Done}/{Total}):')
    for task in done_tasks:
        print(f'\t {task["title"]}')
