#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    headers = {'Authorization': 'token ' + token}
    r = requests.get('https://api.github.com/user', headers=headers)
    req = r.json()
    try:
        print(req['id'])
    except KeyError:
        print(None)
