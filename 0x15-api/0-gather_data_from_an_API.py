#!/usr/bin/python3
""" a module that returns information about an employee """
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
    id = argv[1]
    done = 0
    emp = progress({'id': id}, 'users')
    todos = sorted(progress({'userId': id}, 'todos'), key=lambda x: x['title'])
    for i in range(len(todos)):
        if todos[i].get('completed') is True:
            done += 1
    print('Employee {} is done with tasks({}/{}):'.format(emp[0].get('name'),
                                                          done, len(todos)))
    for i in range(len(todos)):
        if todos[i].get('completed'):
            print('\t{}'.format(todos[i].get('title')))
