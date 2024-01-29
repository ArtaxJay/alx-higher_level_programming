#!/usr/bin/python3
"""This py script makes a http request to https://alx-intranet.hbtn.io/status
using the py module urllib.request.
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as \
            http_response:
        http_message = http_response.read()
        print("Body response:")
        print("\t- type: {}".format(type(http_message)))
        print("\t- content: {}".format(http_message))
        print("\t- utf8 content: {}".format(http_message.decode('utf-8')))
