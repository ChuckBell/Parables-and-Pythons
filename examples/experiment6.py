chosenValue = input("Please enter a number between 1 and 6: ")
intValue = int(chosenValue)
for i in range(0,intValue):
    if (i == 0):
        iterStr = "first"
    elif (i == 1):
        iterStr = "second"
    elif (i == 2):
        iterStr = "third"
    else:
        iterStr = "{0}th".format(i+1)
    print("This is the {0} execution.".format(iterStr))
    
