#!/usr/bin/python3
"""api module to practice getting data"""
import json
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

    completed = []
    task_titles = []
    for entry in todojson:
        if entry.get('userId') == user_id:
            task_titles.append(entry.get('title'))
            completed.append(entry.get('completed'))
    lst = [{'username': name, 'completed': completed[idx], 'task': ele}
           for idx, ele in enumerate(task_titles)]
    task_json = {user_id: lst}
    with open('{}.json'.format(sys.argv[1]), mode='w') as json_f:
        json.dump(task_json, json_f)
