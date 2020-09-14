#!/usr/bin/python3
"""api module to practice getting data"""
import json
import requests


if __name__ == "__main__":
    usrreqs = requests.get('https://jsonplaceholder.typicode.com/users')
    usrdata = usrreqs.json()

    todoreqs = requests.get('https://jsonplaceholder.typicode.com/todos')
    todojson = todoreqs.json()

    data_dic = {}
    for u in usrdata:
        usr_tasks = [todo for todo in todojson
                     if todo.get('userId') == u.get('id')]
        usr_tasks = [{'username': u.get('username'),
                      'task': todo.get('title'),
                      'completed': todo.get('completed')}
                     for todo in usr_tasks]
        data_dic[str(u.get('id'))] = usr_tasks

    with open('todo_all_employees.json', 'w') as json_f:
        json.dump(data_dic, json_f)
