import requests

request= requests.get('http://api.open-notify.org/astros.json/')
data = request.json()
#print(data)

for p in data['people']:
    print(p['name'])

