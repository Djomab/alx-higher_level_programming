#!/usr/bin/python3
"""
script that takes my GitHub credentials (username and password) and
uses the GitHub API to display my id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]
    basic = HTTPBasicAuth(username, token)
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=basic)
    if req.status_code == 200:
        user = req.json()
        print(user['id'])
    else:
        print('None')
