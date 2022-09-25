#!/usr/bin/python3
"""Script that fetches url"""

import urllib.request as request


with request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response:"
          "\n\t- type: {}"
          "\n\t- content: {}"
          "\n\t- utf8 content: {}".format(
                type(data), data, data.decode("utf-8")))
