# Working with lists.
myString = "Hello, World!"

# Example 1: print the list one character at a time.
for i in range(0, len(myString)):
    print(myString[i], end='')
print()

# Example 2: print the 3 characters in the middle of the string
num = int(len(myString) / 2)
print(myString[num-1:num+2])

# Example 3: print the first word
print(myString[:5])

# Example 4: print the last word with start to end of string
print(myString[7:])

# Example 5: integer list
myInts = [1,2,3,4,5,6]
print(myInts)
for i in range (0,3):
    print(myInts[i], end=' ')
print()

# Example 6: declaring and assigning values in a list, sorting the list
diceRolls = [0,0,0,0,0]
diceRolls[2] = int(9)
diceRolls[3] = int(4)
print(diceRolls)
diceRolls.sorted()
print(diceRolls)


