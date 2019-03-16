import requests
resp = requests.get('https://ru.wikipedia.org')
print(resp)
# print(resp.text)
print(resp.status_code)
print(resp.headers)
print(resp.url)

