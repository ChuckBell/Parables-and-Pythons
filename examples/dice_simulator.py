import random
repeat = 'y'
while (repeat == 'y') or (repeat == 'Y'):
    print("Welcome to the dice simulator!")
    numSides = int(input("What size dice do you want to use? "))
    if (numSides % 2) == 1:
        print("ERROR: you must use an even number!")
    else:
        numDice = int(input("How many dice do you want to roll? "))
        for i in range(0,numDice,2):
            diceVal1 = random.randint(1,numSides)
            print("Roll: {0}".format(diceVal1), end='')
            if (i < numDice-1):
                diceVal2 = random.randint(1,numSides)
                print(", {0}".format(diceVal2))
            else:
                print()
    print()
    repeat = input("Roll again? [Y/N] ")
    print()
print("bye!")