""" PASCAL'S TRIANGLE """

# Pascal's triangle is a triangle of numbers that is computed as follows. The first row contains a 1.  Each row after that begins and ends with a 1, and every other number is the sum of the two numbers above it. The first six rows of Pascal's triangle are shown below.
# ```
#       1
#      1 1
#     1 2 1
#   1  3 3  1
#  1 4  6  4 1
# 1 5 10 10 5 1
# ```
# Script to compute and print the *n*th row of Pascal's triangle. The input will be the row number as an integer starting with row 1 as the first row.


# Input a row number
row = int(input("Enter a row number: "))

# Set first item in row to 1 
nth_row = [[1]]

for i in range(1,row): # For each new row create new list & append 1 as the beginning number
    nth_row.append([1]) 
    for j in range(1,i): # Iteratre through previous row and add adjacent numbers
        nth_row[i].append(nth_row[i-1][j-1] + nth_row[i-1][j])
    nth_row[i].append(1) # Append 1 to the very end
    
# Print specified row
print(*nth_row[row-1])