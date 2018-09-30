import random
numSides = int(input("What size dice do you want to use? "))
if (numSides % 2) == 1:
    print("ERROR: you must use an even number!")
else:
    numDice = int(input("How many dice do you want to roll? "))
    for i in range(0,numDice):
        diceVal = random.randint(1,numSides)
        print("Roll: {0}".format(diceVal))
