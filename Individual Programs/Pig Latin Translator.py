""" PIG LATIN TRANSLATOR """

# Code that translates a name into (simplified) Pig Latin. Script ask the user for his or her name, which can comprise first, middle, and/or last parts. For each name part, moves the first letter to the end of the part and append the letters "ay". Only the first letter of each word in your output is capitalized. Uses the split() method on the string to create a list of the name parts. Script can handle one, two or three name parts separated by spaces. This will likely involve a loop.

# Asks user to input Name
inputted_name = str(input("Enter your name: " ))

# Split string into list
name = inputted_name.split()

# Create new list for pig latin name 
pig_latin =[ ]

# Traverse through list; For each item: move first letter to the end of the part and append the letters "ay".
for i in name:
    if not i.isalpha():
        print ("Please enter a valid name")
        break
    else:
        if len(i) == 1:
            new_name = i.upper() + "ay"
            pig_latin.append(new_name) 
        else: 
            new_name = i[1:].title() + i[0].lower() + "ay"
            pig_latin.append(new_name)  # Append translated name into new list

# When user inputs more than 3 strings        
if len(name) > 3:
    print ("Name may only have up to three parts")
elif len(name) == len(pig_latin): # Checks if the length of name is the same length as pig latin
    # Combine all items in list into single string separated by space
    pig_latin = ' '.join(pig_latin) 
    
    # Print name in pig latin
    print(pig_latin)