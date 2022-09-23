#!/usr/bin/python3
"""
script that takes in a letter,
sends a POST request to http://0.0.0.0:5000/search_user
with the email as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ""
    data = {'q': letter}
    req = requests.post(url, data=data)

    try:
        json_content = req.json()
        if json_content:
            print('[{}] {}'.format(json_content['id'], json_content['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
