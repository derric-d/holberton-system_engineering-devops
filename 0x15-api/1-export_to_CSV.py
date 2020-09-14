#!/usr/bin/python3
"""api module to practice getting data"""
import csv
import requests
import sys


if __name__ == "__main__":
    usrreqs = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(sys.argv[1]))
    data = usrreqs.json()
    name = data.get('username')
    user_id = data.get('id')

    todoreqs = requests.get('https://jsonplaceholder.typicode.com/todos')
    todojson = todoreqs.json()

    completed = []
    task_titles = []
    for entry in todojson:
        if entry.get('userId') == user_id:
            task_titles.append(entry.get('title'))
            completed.append(entry.get('completed'))
    with open('{}.csv'.format(sys.argv[1]), mode='w') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for idx, ele in enumerate(task_titles):
            writer.writerow([user_id, name, completed[idx], ele])
