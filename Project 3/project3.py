import psutil
import time
import geocoder
import requests
from geopy.geocoders import Nominatim


epoch = time.time()

ctime = time.ctime(epoch) #Converts from Epoch to Human readable
CPU = psutil.cpu_percent(5) #Collects CPU usage for 5 seconds
RAMp = psutil.virtual_memory()[2] #Ram Usage Precentage
RAMgb = psutil.virtual_memory()[4] / 1000000000 #Converts from bytes to GB
disk = psutil.disk_usage('/') [3]
diskgb = psutil.disk_usage('/')[1] / 1000000000 #Disk usage in GB
print()

print("The Current time is :", ctime) #Prints the current time
print("The current time since epoch (in seconds) is :", epoch)

print()

print('The CPU usage is: ', CPU)  #Prints all of the system information
print('Ram used : ', RAMp,'%' )
print('RAM used in GB :', RAMgb, "GB")
print('Total Disk used on disk C:' , diskgb ,'GB')
print('Disk space used on disk C:' , disk ,'%')
print()

g =geocoder.ip('me') #This retrieves the Lat and Long
data1 = g.latlng
print("The current latitude and longitude of this device is: ", data1)

geolocator = Nominatim(user_agent="me") #Initializes the Nominatim API

location = geolocator.reverse(data1) #inputs the Lat and Long
print("The current location of this device is: " , location) #Prints location data
locationraw = location.raw
locationdata = locationraw['display_name'].split()
zipc = locationdata[12] #Retreives the Zip code from the list of location data
zipnew = zipc.rstrip(',') #Removes the comma from the end of the zipcode

print()

zip = zipnew
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=4e54ca6c84e78554467ec14acfadecce' % zip) #API request
data =r.json()
print("The weather right now in", zipnew, "is", data['weather'][0]['description']) #Weather Description
ktemp = data['main']['temp'] #Retrieves the temp Kelvin
ftemp = int((ktemp - 273.15) * (9/5) + 32) #Converts from Kelvin to Fahrenheit
print("The tempature in Fahrenheit is:", ftemp) #Prints the temp in F
print("The humidity is:" ,data['main']['humidity'],"%") #Humidity percentage




print()
print("press enter to close") #Closes the window
t = input()


