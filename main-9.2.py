# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Ricardo Nevarez
# Creation Date: 2023-05-10
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
    #It looks like line 21 is improperly indented. I've fixed the indentation for this line.
    while cave != '1' and cave != '2':
      print('Which cave will you go into? (1 or 2)')
      cave = input()
    #Caves is not a valid variable, I think you meant to put "cave" here:
    #return caves
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #It looks like you forgot to add parenthesis around this print statement. I have gone ahead and fixed this.
        #print 'Gobbles you down in one bite!'
        print('Gobbles you down in one bite!')


displayIntro()
#Looks like chooseCave is improperly capitalized. I have fixed it:
#caveNumber = choosecave()
caveNumber = chooseCave()
checkCave(caveNumber)

#Looks like there is a typo here - should say "Thanks for playing"
#print("Thanks for planing")
print("Thanks for playing")