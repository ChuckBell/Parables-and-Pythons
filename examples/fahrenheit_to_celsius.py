#
# Parables and Pythons
#
# Lesson 2: Fahrenheit to Celsius Example
#
# This script reads a value from the user in Fahrenheit and converts it to
# Celsius
#
fahrenheit = input("Please enter a temperature in Fahrenheit: ")
celsius = (float(fahrenheit) - 32.0) * (5.0/9.0)
print("{0}F == {1:.2f}C".format(fahrenheit, celsius))
print("bye!")
