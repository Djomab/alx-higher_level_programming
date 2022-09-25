#!/usr/bin/python3
"""
Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    json_response = r.json()
    try:
        for i in range(10):
            print(json_response[i].get('sha'), json_response[i].get('commit')
                  .get('author').get('name'), sep=": ")
    except Exception:
        pass
