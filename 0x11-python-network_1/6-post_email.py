#!/usr/bin/python3
"""
Script that takes in a URL and an email address
"""


if __name__ == '__main__':
    import requests
    import sys

    payload = {'email': sys.argv[2]}
    rq = requests.post(sys.argv[1], data=payload)
    print(r.text)
