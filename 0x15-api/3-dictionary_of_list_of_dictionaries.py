#!/usr/bin/python3
'''returns information about TODO list progress by employee id.'''
import json
import requests
from sys import argv


if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    with open('todo_all_employees.json', 'w', newline='') as f:
        res = {}
        for user in users:
            id = str(user.get('id'))
            tasks = [i for i in data if i.get('userId') == int(id)]
            expo = {id: []}
            l = expo.get(id)
            for task in tasks:
                l.append({"task": task.get('title'), "completed": task.
                          get('completed'), "username": user.get('username')})
            res.update(expo.copy())
            expo.clear()
        f.write(json.dumps(res))
        f.close()
