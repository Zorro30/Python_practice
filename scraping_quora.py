import requests

r = requests.get('https://www.quora.com')
print (r.text)