#!/usr/bin/python3
#  sends a request to the URL and displays the value of
# the variable X-Request-Id in the response header

'''Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.'''
import sys
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"

    reqEmployee = requests.get(url + sys.argv[1])
    reqTodo = requests.get(url + sys.argv[1] + "todos")

    jsonemp = reqEmployee.json()
    tasks = [key['completed'] for key in reqTodo.json()]
    print("Employee {} is done with tasks ({}/{}):".format(
        jsonemp.get('name'), tasks.count(True), len(tasks)))
    for tasks in reqTodo.json():
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
