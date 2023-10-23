#!/usr/bin/python3
""" a module that returns information about an employee """
import csv
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
    id = int(argv[1])
    emp = progress({'id': id}, 'users')
    todos = progress({'userId': id}, 'todos')
    filename = f'{id}.csv'
    username = emp[0].get('name')
    with open(filename, 'w', newline="") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([id, username, todo.get('completed'),
                                todo.get('title')])
