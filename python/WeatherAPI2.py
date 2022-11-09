import json
import requests

print('Please enter your zip code:')
zip = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=4e54ca6c84e78554467ec14acfadecce' % zip)
data =r.json()
print(data['weather'][0]['description'])
