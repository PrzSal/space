#!/usr/bin/env python3
import random
import sys
import time


again = 'yes'

if len(sys.argv) == 1:
    y = 30
else:
    y = int(sys.argv[1])

while again == 'yes':

    x = random.randint(1,y)
    print(x)
    guess = 100
    count = 1
    while guess != x:
        guess = eval(input("Hero, guess number from 1 to " + str(y) + ": "))
        if guess > x:
            print("the number is too high, try again: ")
            count += 1
        elif guess < x:
            print("the number is too low, try again: ")
            count += 1
	
    
    print("GRATULATIONS, YOU HAVE WON and go to on the bridge to next level")
    break
