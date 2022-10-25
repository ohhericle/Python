""" NUMBER AVERAGER """

# Script that prompts the user for two numbers, a and b. Then, prompt the user to enter a type of average out of the three options below. Make it so the user would just type in a number 1, 2 or 3 for the average (i.e. 1 for arithmetic mean, 2 for geometric mean, or 3 for root-mean-square). This numerical selection is an example of how to give the user a simple response that will get around potential spelling errors and head off user frustration. This design decision makes the user interaction more robust. Output the correct average, based on what the user selected. Format the answer to four decimal places.

# The arithmetic mean:  (𝑎+𝑏)/2 
# The geometric mean:  𝑎𝑏⎯⎯⎯⎯√ 
# The root-mean-square:  𝑎2+𝑏22

import math
#Prompts user for two numbers a & b 
a = float(input("Please provide the first number to average: "))
b = float(input("Please provide the second number to average: "))
print("""Please select the type of average.
    1. The arithmetic mean: (a + b)/2
    2. The geometric mean: sqrt(a * b)
    3. The root-mean-square: sqrt((a^2 + b^2)/2)""")
c = int(input("Enter a number (1, 2 or 3) from the list above:"))

if c == 1:
    d=(a + b) / 2
    print("The arithmetric mean is", format(d,'.4f'))
elif c == 2:
    d=math.sqrt(a * b)
    print("The geometric mean is", format(d,'.4f'))
elif c == 3:
    d=math.sqrt((a**2 + b**2)/2)
    print("The root-mean-square mean is", format(d,'.4f'))
else:
    print("Invalid selection.")