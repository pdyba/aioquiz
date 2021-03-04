import requests
resp = requests.post(
    'http://py.net/auth',
    json={
        "name": "piotrD",
        "password": "p1"
    }
)
resp_2 = requests.post(
    'http://py.net/user_status/set',
    json={
        "api_key": resp.json()['api_key'],
        "status": "piotr"
    }
)
print(resp_2)
resp_3 = requests.get('http://py.net/user_status')
print(resp_3.json()[resp.json()['name']])

resp = requests.get('http://py.net/cat')
with open('cat.jpg', 'wb') as file:
    file.write(resp.content)


resp = requests.get('http://py.net/query_string?co=1&kolwiek=2')
from pprint import pprint as pp
pp(resp.json())