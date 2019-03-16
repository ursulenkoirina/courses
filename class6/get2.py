import requests
import json
url = 'http://httpbin.org/get'
p = {'spam':'aaaa'}
r = requests.get('http://httpbin.org/get', headers={"User-Agent": "new_app/0.1"}, params=p)
print(r.text)
print(type(r.text))
to_dict = r.json()
print(to_dict)
print(to_dict.get('headers'))
print(to_dict.get('headers').get('User-Agent'))