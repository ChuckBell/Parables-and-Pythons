# Yahtzee dice roller example
import random
print("Welcome to the Yahtzee dice roller!")
dice = [0,0,0,0,0]
repeat = 'y'
while (repeat == 'y') or (repeat == 'Y'):
    print("Rolling the dice...")
    for i in range(0, 5):
        dice[i] = random.randint(1, 6)
    print("You rolled the following dice:")
    dice.sort()
    print(dice)
    print()
    repeat = input("Would you like to roll again? [Y/n]: ")
    print()
print("bye!")



