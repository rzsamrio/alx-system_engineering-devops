#!/usr/bin/python3
""" Export some data to CSV """
import csv
import requests
import sys

if __name__ == '__main__':
    user = (requests.get('https://jsonplaceholder.typicode.com/users/'
            + sys.argv[1])).json()
    Name = user['username']

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                         + sys.argv[1]).json()
    with open(f'{sys.argv[1]}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [str(sys.argv[1]), str(Name), str(task['completed']),
                   str(task['title'])]
            writer.writerow(row)
