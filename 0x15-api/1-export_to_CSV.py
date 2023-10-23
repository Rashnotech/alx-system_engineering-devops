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
    user_id = argv[1]
    emp = progress({'id': user_id}, 'users')
    todos = progress({'userId': user_id}, 'todos')
    filename = f'{user_id}.csv'
    username = emp[0].get('username')
    with open(filename, 'w', newline="") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([user_id, username, todo.get('completed'),
                                todo.get('title')])
