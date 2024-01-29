#!/usr/bin/python3
"""This py script makes a http request
    to passed url-arg and
    prints the header value
"""
import sys
import urllib.request

if __name__ == "__main__":
    # cmd_arg_url = sys.argv[1]
    # http_req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(sys.argv[1]) as http_res:
        print(dict(http_res.headers).get("X-Request-Id"))
