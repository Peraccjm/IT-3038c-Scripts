# Project 3
## Startup Script in Python, peraccjm

### Description

The goal of this script is to retrieve the time in epoch and then convert to a human readable format. Then display both Human readable and epoch. Then it collects system information and displays that information over a 5 second period. The script then determins the latitude and longitude from the devices IP address. It then takes this information to determine the location of the device in the world. It then takes that data that it has found and inputs it into a query for the OpenWeatherMap API to retreave some useful weather information to start your day. Use on Windows only.

### How to run

First install psutil.

  ```pip install psutil```

Then install geocoder

  ```pip install geocoder```

Finally install geopy

  ```pip install geopy```

This can be done in a virtual enviroment or directly on the PC.

Then Run using python on your windows pc. 

### Use Case
Can setup as a start up task to display every time PC is turned on and displays this usefull information when you first login to your PC for Work or School.

### Sources
https://pypi.org/project/psutil/

https://psutil.readthedocs.io/en/latest/

https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/

https://geopy.readthedocs.io/en/stable/#data

https://docs.python.org/3/library/stdtypes.html#dict

https://geocoder.readthedocs.io/

https://www.geeksforgeeks.org/get-zip-code-with-given-location-using-geopy-in-python/
