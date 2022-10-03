import random
import os

randnum = random.randint(0,10) 
print (randnum)
print ('Random number game! What is your guess?')
usrguess = int(input())


while randnum != usrguess :
    if usrguess > randnum :
        print('Your guess is too high. Try again.')
        usrguess = int(input())
    elif usrguess < randnum :
        print('Your guess is too low. Try agin.')
        usrguess = int(input())
else :
    print('Good job!! You are good at guessing a number')

print('press enter to close')
u = input()