#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = urlencode({'eamil': sys.argv[2]}).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
