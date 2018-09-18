#
# Parables and Pythons
#
# Lesson 2: Farenheit to Celsius Example
#
# This script reads a value from the user in Fahrenheit and converts it to
# Celsius
#
farenheit = input("Please enter a temperature in Farenheight: ")
celsius = (float(farenheit) - 32.0) * (5.0/9.0)
print("{0}F == {1:.2f}C".format(farenheit, celsius))
print("bye!")
