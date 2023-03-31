#!/usr/bin/python3
"""This script sends a POST request to the url"""
from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import quote
from sys import argv


def make_post_request(url_str: str, email_arg: str):
    try:
        data = quote(email_arg)
        email = data.encode("ascii")
        req = Request(url_str, data=email)
        with urlopen(req) as response:
            body = response.read()
        print(body.decode("ascii"))
    except URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        elif hasattr(e, "code"):
            print(e.code)


if __name__ == "__main__":
    try:
        make_post_request(argv[1], argv[2])
    except IndexError:
        raise
