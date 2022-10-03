import random
import os

randnum = random.randint(0,10) 
print (randnum)
print ('Random number game! What is your guess?')
usrguess = int(input())

if usrguess > randnum :
    print('Your guess is too high. Try again next time loser.')
elif usrguess < randnum :
    print('Your guess is too low. Try agin next time loser.')
else :
    print('Good job!! You are good at guessing a number')

print('press enter to close')
u = input()