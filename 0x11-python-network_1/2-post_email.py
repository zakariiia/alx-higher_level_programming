#!/usr/bin/python3
'''
A Python script that takes in a URL and an email, sends a POST
request
'''


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url, email = sys.argv[1:3]
    val = {"email": email}

    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
