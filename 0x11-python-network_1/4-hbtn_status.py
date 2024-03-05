#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    rq = requests.get(url)
    text = rq.text
    print("Body response:")
    print(f"\t- type: {type(text)}")
    print(f"\t- content: {text}")
