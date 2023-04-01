#!/usr/bin/python3
""" script to that takes in a URL, sends a
request to the URL and displays the body of the
response (decoded in utf-8) """


if __name__ == '__main__':
    from urllib import request, error
    from sys import argv

    url = argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except error.HTTPError as e:
        print(f"Error code: {e.code}")
