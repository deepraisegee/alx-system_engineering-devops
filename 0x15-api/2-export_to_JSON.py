#!/usr/bin/python3
""" Get todo information of a given user id """

import json
import requests
import sys


def main():
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    # get employee data
    user = requests.get(f"{url}/users/{USER_ID}").json()

    # get the todos of the user
    todos = requests.get(f"{url}/todos", params={"userId": USER_ID}).json()

    completed = list(filter(lambda x: x["completed"], todos))

    # export to JSON
    with open(f"{USER_ID}.json", "w") as jsonfile:
        json.dump({USER_ID: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in todos
        ]}, jsonfile)


if __name__ == "__main__":
    main()
