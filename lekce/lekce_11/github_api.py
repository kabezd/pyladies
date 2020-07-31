import requests
import json

with open('token.txt') as file_:
    token = file_.read().strip()

headers = {'Authorization': 'token ' + token}

# stažení stránky
page = requests.get('https://api.github.com/user', headers=headers)
# ověření, že dotaz proběhl v pořádku
page.raise_for_status()
#print(page.text)

data = json.loads(page.text)

print(json.dumps(data, ensure_ascii=True, indent=2))