#!/usr/bin/python3
""" a module that returns information about an employee """
import json
import requests
from sys import argv


def progress(params):
    """ a function that returns information about
        todo list progress
    """
    url = f'https://jsonplaceholder.typicode.com/{params}/'
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    """ code executation """
    users = progress('users')
    todos = progress('todos')
    result = {}
    filename = 'todo_all_employees.json'
    for user in users:
        content = []
        for todo in todos:
            if user['id'] == todo['userId']:
                content.append({
                    'username': user.get('username'),
                    'task': todo.get('title'),
                    'completed': todo.get('completed')})
        result[user.get('id')] = content
    with open(filename, 'w') as file:
        json.dump(result, file)
