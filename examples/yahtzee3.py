# Yahtzee dice roller example - with a function
import random

def roll_dice(num_dice):
    """Roll n 6-sided dice and return as a list"""
    dice = [0,0,0,0,0]
    print("Rolling the dice...")
    for i in range(0, num_dice):
        dice[i] = random.randint(1, 6)
    print("You rolled the following dice:")
    dice.sort()
    return dice
    
print("Welcome to the Yahtzee dice roller!")
dice_rolled = []
roll_number = 1
repeat = 'y'
while (repeat == 'y') or (repeat == 'Y'):
    dice = roll_dice(5)
    print(dice)
    print()
    dice_rolled.append((roll_number, dice))
    repeat = input("Would you like to roll again? [Y/n]: ")
    print()
    roll_number = roll_number + 1    
print("Dice rolled:\n{0}".format(dice_rolled))
print("bye!")



