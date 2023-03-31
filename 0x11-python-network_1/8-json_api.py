#!/usr/bin/python3
"""This script communicates with an API and gets a JSON formatted value"""
import requests
from sys import argv


def get_request_status(letter: str):
    payload = {}
    if letter:
        payload["q"] = letter
    else:
        payload["q"] = ""

    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data=payload)

    if isinstance(req, dict):
        resp_dict = req.json()
        if resp_dict:
            print("[{}] {}".format(resp_dict.get("id"), resp_dict.get("name")))
        else:
            print("No result")
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    try:
        get_request_status(argv[1])
    except IndexError:
        get_request_status("")
