chosenValue = input("Please enter a number between 1 and 6: ")
intValue = int(chosenValue)           # add this line
if (intValue < 1) or (intValue > 6):  # change this line
    print("ERROR: You did not enter a value between 1 and 6.")
else:
    print("You entered: {0}.".format(chosenValue))
    
