""" COMPUTING FIBONACCI NUMBER """

# Recursive function to compute the nth Fibonacci number. Dunction will call itself and will NOT include explicit loops.

# Function should include a line that looks a lot like the mathematical definition of the nth Fibonacci number.

# It's possible for a recursive function to call itself more than once.

def Fibonacci (num):
    if num < 0: # Checks if num is a positive number
        return "Please enter a positive number"
    elif num <= 1:  # Checks if num is 0 or 1 ; If so returns num 
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2) ### Mathematical definition of the nth Fibonacci number


#num = int(input("Enter number to compute nth Fibonacci number"))
#print(Fibonacci(num)) # Starting from index 0 
