import psutil
import time

epoch = time.time()

ctime = time.ctime(epoch)
CPU = psutil.cpu_percent(5)
RAMp = psutil.virtual_memory()[2]
RAMgb = psutil.virtual_memory()[4] / 1000000000
disk = psutil.disk_usage('/') [3]
diskgb = psutil.disk_usage('/')[1] / 1000000000

print("The Current time is :", ctime)
print("The current time since epoch (in seconds) is :", epoch)

print()

print('The CPU usage is: ', CPU)
print('Ram used : ', RAMp,'%' )
print('RAM used in GB :', RAMgb, "GB")
print('Total Disk used on disk C:' , diskgb ,'GB')
print('Disk space used on disk C:' , disk ,'%')


print()
print("press enter to close")
t = input()
