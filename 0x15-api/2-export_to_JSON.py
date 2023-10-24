#!/usr/bin/python3
""" a module that returns information about an employee """
import json
import requests
from sys import argv


def progress(payload, params):
    """ a function that returns information about
        todo list progress
    """
    url = f'https://jsonplaceholder.typicode.com/{params}/'
    r = requests.get(url, params=payload)
    return r.json()


if __name__ == '__main__':
    """ code executation """
    user_id = argv[1]
    user = progress({}, f'users/{user_id}')
    todos = progress({'userId': user_id}, 'todos')
    filename = f'{user_id}.json'
    username = user['username']
    result = {user_id: [{
                        'task': todo.get('title'),
                        'completed': todo.get('completed'),
                        'username': username} for todo in todos]}
    with open(filename, 'w') as file:
        json.dump(result, file)
