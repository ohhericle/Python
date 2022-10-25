""" Nested Functions """

# Three functions as follows:

# sum_digits: a function which takes an int and returns the sum of its (positive value) digits.

# diff_sum_digits: a function that "wraps" sum_digits in that it calls sum_digits from within it. Use the diff_sum_digits function to compute the absolute value of the input number, minus the sum of digits of the input number.

# wraps_diff_sum_digits: a function that "wraps" diff_sum_digits. If diff_sum_digits returns a result that has more than one digit replace the result with the diff_sum_digits of the result. Do this repeatedly until the result has just one digit, then display it.

# Note: The nested functions (all three functions above) will always run through once - even if the inputted number is only one digit!

# To illustrate this with an example:

# The input number is 20 as in: wraps_diff_sum_digits(20)
# wraps_diff_sum_digits calls diff_sum_digits(20) which calls sum_digits(20)
# sum_digits adds the numbers (2+0 = 2) returns a 2, diff_sum_digits subtracts (20-2 = 18) and returns this to wraps_diff_sum_digits
# wraps_diff_sum_digits sees that the number 18 stills has 2 digits and calls diff_sum_digits(18) which calls sum_digits(18)
# sum_digits add the numbers (1+8 = 9) returns a 9, diff_sum_digits subtracts (18-9 = 9) and returns this to wraps_diff_sum_digits
# wraps_diff_sum_digits sees that the number 9 only has 1 digit - stops and returns the value 9.

def sum_digits (x):
    x = abs(x) # Gets absolute value of input 
    x = sum(int(digit) for digit in str(x)) # Converts number to str to iterate through and converts each digit back to integer to calculate sum
    return x

def diff_sum_digits (x):
    x = abs(x) - sum_digits(x) # Subtract input number from the sum of all digits 
    return x

def wraps_diff_sum_digits (x):
    x = diff_sum_digits(x)
    while x >= 10: # Checks to see if number has only one digit 
        x = diff_sum_digits(x) # If greater than one digit ; Pass back into function 
    return x