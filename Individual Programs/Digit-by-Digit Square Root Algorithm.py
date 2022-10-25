""" Digit-by-Digit Square Root Algorithm """

# Digit-by-digit algorithm to find the square root of x to a precision of epsilon.
#   1. Begin with a step size of 1 and guess of zero.
#   2. Increase the guess by the step size as long as doing so would not cause the guess^2 to exceed x. Repeat this step (step 2) until the next repetition will cause guess^2 to exceed x.
#   3. If the step size is greater than or equal to epsilon, then divide the step size by 10 and go back to step 2.

# Notice that once a digit has been found, it is not changed again. Code to find the square root of 10 to an epsilon of 8 decimal places.

num = float(input("Enter a number to find the square root: "))

epsilon = 0.00000001

# Set guess to zero ; step size to 1
guess = 0
step = 1

while step >= epsilon: # If step size is greater than or equal to epsilon
    while guess ** 2 < num:# Increase guess by step size as long as guess^2 less than  x 
        guess += step
    guess -= step 
    step = step / 10 # Divide step size by 10
        
        
# Print Square Root to an epsilon of 8 decimals
print("The square root of",num,"is:","{:.8f}".format(guess))


#Continue to run when  step size is greater than epsiion 
#if not that it'll print answer 
#keep guessing until guess ** 2 is greater than the num are trying to find
#incremnt by guess by step 
#so when the expoent greater than the number 
#subtract the step ( to get the lower range of answer )
#and then divide step 