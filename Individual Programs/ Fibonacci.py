""" FIBONACCI """

# The Fibonacci numbers begin with 1, 1. After the first two numbers, each number is the sum of the previous two. 1 + 1 = 2, so 2 is the third number. Then 1 + 2 = 3, so 3 is the next one, and so on. This script prompts the user for an integer number, then prints all the Fibonacci numbers that are less than or equal to the input, in order.

# Prompt user to enter a number
number = int(input("Enter a number: "))

# Set first number and second number to 1
first, second = 1 , 1

# Checks if Fibonacci number are less than or equal to the input
if number <= 0:   # In the case that number is negative or 0
    print("Error: Please Number Greater Than 0")
else:
    while first <= number:
        print(first,end =" ")
        third = first + second  # Sum of first two numbers
        first = second # Set first number to second number
        second = third # Set second number to sum of number
        