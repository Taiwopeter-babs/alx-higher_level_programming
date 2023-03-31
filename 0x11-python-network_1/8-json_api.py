#!/usr/bin/python3
"""This script communicates with an API and gets a JSON formatted value"""
import requests
from sys import argv


def get_request_status():
    payload = {}

    if len(argv) > 1:
        payload["q"] = argv[1]
    elif len(argv) == 1:
        payload["q"] = ""

    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=payload)

    if isinstance(req.json(), dict):
        resp_dict = req.json()
        if len(resp_dict) != 0:
            print("[{}] {}".format(resp_dict.get("id"), resp_dict.get("name")))
        else:
            print("No result")
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    get_request_status(argv[1])
