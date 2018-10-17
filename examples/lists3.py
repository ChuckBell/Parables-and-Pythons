# Working with lists - part 3
done = False
myList = []
while not done:
    value = input("Please enter a value for the list or "
                  "press ENTER to end the list: ")
    if value:
        myList.append(value)
    else:
        done = True
print("The unsorted list: {0}".format(myList))
myList.sort()
print("The sorted list: {0}".format(myList))
value = input("Enter a value to add to the front of the list: ")
myList.insert(0, value)
print("Updated list: {0}".format(myList))


