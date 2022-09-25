#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    data = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(data.text)))
    print('\t- content: {}'.format(data.text))
