""" WEIGHTED GRADES """

# Function called weighted_avg that takes a list of grades and a corresponding list of weights and returns the weighted average of the grades rounded to 1 decimal place.

# Function should raise an exception with the message exactly as shown:

# a weight is less than 0 or greater than 100 (message: "A weight is less than 0 or greater than 100")
# the weights do not add to 100 (message: "Weights do not add to 100")
# the number of weights and grades are not equal (message: "The number of weight and grades are not equal")
# a grade is below 0 (grades above 100 would be considered extra credit and are acceptable) (message: "A grade is below 0")
# Do not print the exception just 'raise' it.

# Run your function on grades1 with weights1 and grades2 with weights2 and grades3 with weights3 and grades4 with weights4, defined below. Catch the errors generated in each case as an exception with the useful message for the user as defined above.

# The first 3 test cases should raise an exception!

def weighted_avg (grades, weights):
    
    for w in weights: 
        if w < 0 or w > 100: # If a weight is less than 0 or greater than 100
            raise Exception("A weight is less than 0 or greater than 100")
    if sum(weights) != 100:  # The weights do not add to 100
        raise Exception("Weights do not add to 100")
    if len(weights) != len(grades): # The number of weights and grades are not equal 
        raise Exception("The number of weight and grades are not equal")
    for g in grades: #A grade is below 0
        if g <= 0:
            raise Exception("A grade is below 0")

    weighted_grade = []    # Create empty list to store new grades 
    for g,w in zip(grades, weights): # Aggregate list to tuple pairs
        weighted_grade.append(g*w) # Multiply and append the product to empty list 
        total_grades= sum(weighted_grade) # Add total values inside list 
        final_grade = total_grades / 100 # Divide entire list by 100 to get final weighted grade 
        
    return final_grade # Return final grade 
    

#weighted_avg(grades4, weights4) 