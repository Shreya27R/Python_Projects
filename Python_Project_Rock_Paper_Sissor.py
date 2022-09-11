#Python Program for the game Rock paper scissor
#!/usr/bin/env python
import random

import os

import re
while (1 < 2):
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue
    print ("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print ("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print ("Tie! ")
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print ("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beat rock, I win!")
        continue
    else:
        print ("You win!")
