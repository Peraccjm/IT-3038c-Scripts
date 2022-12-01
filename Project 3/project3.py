import psutil
import time
import geocoder
import requests
from geopy.geocoders import Nominatim


epoch = time.time()

ctime = time.ctime(epoch)
CPU = psutil.cpu_percent(5)
RAMp = psutil.virtual_memory()[2]
RAMgb = psutil.virtual_memory()[4] / 1000000000
disk = psutil.disk_usage('/') [3]
diskgb = psutil.disk_usage('/')[1] / 1000000000
print()

print("The Current time is :", ctime)
print("The current time since epoch (in seconds) is :", epoch)

print()

print('The CPU usage is: ', CPU)
print('Ram used : ', RAMp,'%' )
print('RAM used in GB :', RAMgb, "GB")
print('Total Disk used on disk C:' , diskgb ,'GB')
print('Disk space used on disk C:' , disk ,'%')
print()

g =geocoder.ip('me')
data1 = g.latlng
print("The current latitude and longitude of this device is: ", data1)

geolocator = Nominatim(user_agent="me")

location = geolocator.reverse(data1)
print("The current location of this device is: " , location)
locationraw = location.raw
locationdata = locationraw['display_name'].split()
zipc = locationdata[12]
zipnew = zipc.rstrip(',')

print()

zip = zipnew
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=4e54ca6c84e78554467ec14acfadecce' % zip)
data =r.json()
print("The weather right now in", zipnew, "is", data['weather'][0]['description'])
ktemp = data['main']['temp']
ftemp = int((ktemp - 273.15) * (9/5) + 32)
print("The tempature in Fahrenheit is:", ftemp)
print("The humidity is:" ,data['main']['humidity'],"%")




print()
print("press enter to close")
t = input()


