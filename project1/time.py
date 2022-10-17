import time

epoch = time.time()

ctime = time.ctime(epoch)

print("The Current time is :", ctime)
print("The current time since epoch (in seconds) is :", epoch)
print
print("press enter to close")
t = input()
