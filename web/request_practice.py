import requests

payload = {'key1': 'value', 'key2': 'value2'}

# getリクエスト
r = requests.get('http://httpbin.org/get', params=payload)

print(r.status_code)
print(r.text)
print(r.json())

################################################

# postリクエスト
r = requests.post('http://httpbin.org/post', data=payload)

print(r.status_code)
print(r.text)
print(r.json())

