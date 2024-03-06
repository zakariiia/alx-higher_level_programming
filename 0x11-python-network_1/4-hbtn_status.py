#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(req.text.__class__))
    print("\t- content: {}".format(req.text))
