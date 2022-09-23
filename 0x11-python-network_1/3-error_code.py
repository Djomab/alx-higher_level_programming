#!/usr/bin/python3
"""
script that takes in a URL,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            data = response.read()
            print(data.decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
