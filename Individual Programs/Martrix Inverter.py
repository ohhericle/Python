""" MATRIX INVERTER """

# One place where the usage of tuples is convenient is in the representation of matrices. The values in a 2x2 matrix are labeled as follows:
# [𝑎𝑐𝑏𝑑]
# Code asks the user for a text string including the four numbers, a, b, c, and d, separated by spaces. The split() method on the string to create a list of the four values in order.

# Creates a tuple that represents each row, then create a tuple that contains those two tuples. Should have the form ((a, b), (c, d)). Printed representation.

# The inverse of the matrix above is given by the formula:

# 1𝑎𝑑−𝑏𝑐[𝑑−𝑐−𝑏𝑎]
 
# Multiplying a matrix by a number effectively multiplies each element of the matrix by that number.

# Computes the inverse of the given matrix, again represented as nested tuples.

# Asks user to input four numbers separaed by spaces
numbers = input("Please enter four numbers separated by spaces: ")

# Splits number into a list 
numbers = numbers.split()

# Create new list and convert list to tuple pairs
matrix = []
for i in range(0, len(numbers), 2): # Iterate through elements in list by step of 2
    matrix.append((float(numbers[i]), float(numbers[i+1]))) #Append elements as float
matrix = tuple(matrix) # Convert list to nested tuples

a = (1/((matrix[1][1] * matrix[0][0]) - (matrix[0][1] * matrix[1][0])) ) # Inverse quation to multiply inverse matrix by
inverse_function = matrix[1][1], matrix[0][1]*-1, matrix[1][0]*-1, matrix[0][0] # A single tuple of inverse matrix represented by index values
inverse_function = list(inverse_function) # Tuples are immutable so convert tuple to list to multiply
inverse = []
for j in inverse_function: # For all elements inside inverse list 
    inverse.append(j*a) # Multiply by inverse function
for k in inverse: # For all elements inside new list
    n1 = inverse.pop(0); n2 = inverse.pop(0) # Split items in list into pairs
    inverse.append((n1,n2))
inverse = tuple(inverse) # Converts lists back to tuple


#print output as floats 
print("matrix:", matrix)
print("inverse:",inverse)