#!/usr/bin/python3
"""api module to practice getting data"""
import requests
import sys


if __name__ == "__main__":
    usrreqs = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(sys.argv[1]))
    data = usrreqs.json()
    name = data.get('name')
    user_id = data.get('id')

    todoreqs = requests.get('https://jsonplaceholder.typicode.com/todos')
    todojson = todoreqs.json()

    tasks = 0
    completed = 0
    task_titles = []
    for entry in todojson:
        if entry.get('userId') == user_id:
            tasks += 1
            if entry.get('completed'):
                completed += 1
                title = entry.get('title')
                task_titles.append(title)
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, tasks))
    for t in task_titles:
        print('\t{}'.format(t))
