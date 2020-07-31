import requests

with open('token.txt') as file_:
    token = file_.read().strip()

headers = {'Authorization': 'token ' + token}

page = requests.put('https://api.github.com/user/starred/pyvec/naucse.python.cz', headers=headers)
page.raise_for_status()