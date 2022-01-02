import os, requests, pandas, jwt

url = 'https://presence.pythonanywhere.com/api/login'
data = {'username': 'admin', 'password': 'admin'}

r = requests.post(url, data=data)
raw = r.json()
token = raw['jwt']

ids = jwt.decode(token, 'secret', algorithms='HS256')
print(ids)
