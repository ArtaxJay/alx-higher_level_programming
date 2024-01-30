#!/usr/bin/python3
"""This script makes a http request to the URL passed to it as an argv.
then prints the body of the http response (utf-8 decoded).
"""


if __name__ == "__main__":
    import urllib.request, urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as http_res:
            print(http_res.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
