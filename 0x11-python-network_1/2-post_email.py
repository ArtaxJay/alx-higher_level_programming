#!/usr/bin/python3
"""This py script will send a http POST request to the argv-URL
then prints the body of the http response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    cmd_arg_url = sys.argv[1]
    msg_val = {"email": sys.argv[2]}
    parsed = urllib.parse.urlencode(msg_val).encode("ascii")

    http_req = urllib.request.Request(cmd_arg_url, parsed)
    with urllib.request.urlopen(http_req) as http_res:
        print(response.read().decode("utf-8"))
