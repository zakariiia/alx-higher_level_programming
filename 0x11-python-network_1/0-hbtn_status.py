#!/usr/bin/python3
'''
fetches https://alx-intranet.hbtn.io/status
'''

if __name__ == "__main__":
    import urllib.request

    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as res:
        content = res.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
