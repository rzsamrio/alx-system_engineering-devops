#!/usr/bin/python3
""" """
import csv
import requests
import sys

if __name__ == '__main__':
	tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]).json()
	with open(f'{sys.argv[1]}.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for task in tasks:
			writer.writerow(task.values())
