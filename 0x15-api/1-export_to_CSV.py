#!/usr/bin/python3
""" a module that returns information about an employee """
import requests
from sys import argv
import os

def progress(payload, params):
    """ a function that returns information about
        todo list progress
    """
    url = f'https://jsonplaceholder.typicode.com/{params}/'
    r = requests.get(url, params=payload)
    return r.json()


if __name__ == '__main__':
    """ code executation """
    id = argv[1]
    emp = progress({'id': id}, 'users')
    todos = progress({'userId': id}, 'todos')
    filename = f'{id}.csv'
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename, 'w+', encoding='utf-8') as file:
        for i in range(len(todos)):
            file.write('"{}","{}","{}","{}"\n'.format(todos[i].get('userId'),
                                                    emp[0].get('name'),
                                                    todos[i].get('completed'),
                                                    todos[i].get('title')))
