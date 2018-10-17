# Yahtzee dice roller example - with a stack and queue
import random

print("Welcome to the Yahtzee dice roller!")
dice_stack = []
dice_queue = []
roll_number = 1
repeat = 'y'
while (repeat == 'y') or (repeat == 'Y'):
    dice = [0,0,0,0,0]
    print("Rolling the dice...")
    for i in range(0, 5):
        dice[i] = random.randint(1, 6)
    print("You rolled the following dice:")
    dice.sort()
    print(dice)
    print()
    dice_stack.insert(0, (roll_number, dice))
    dice_queue.append((roll_number, dice))
    repeat = input("Would you like to roll again? [Y/n]: ")
    print()
    roll_number = roll_number + 1    
print("Stack:\n{0}".format(dice_stack))
print("Queue:\n{0}".format(dice_queue))
print("bye!")



