#!/usr/bin/python3
""" post email data into the url """

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]

    data = {'email': email}
    result = requests.post(url, data=data)
    print(f"Your email is: {result.text}")
