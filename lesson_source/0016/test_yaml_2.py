import requests
url = 'http://34.243.20.71:8080/'
url_post_auth = url + 'auth'
url_get_user_status = url + 'user_status'
url_post_user_status = url + 'user_status/set'
register = {"name": "PawelN", "password": "password"}
resp = requests.post(url_post_auth, json=register)
api_key = resp.json()['api_key']
print(api_key)
resp = requests.get(url_get_user_status)
status = resp.json()
my_status = {"api_key": api_key, "status": "super"}
resp = requests.post(url_post_user_status, json=my_status)
print(resp.content)