""" PALINDROME """

# Script that prompts the user for a name (this input will be a 1 word string). Using a while loop that counts downwards, print the letters of the name reversed. Uses.lower() and s.upper(), as appropriate, to change the string to lowercase and print it out with only the first letter of the reversed word in uppercase. If the name is the same forward and backwards, print "Palindrome!" on the next line.

#Prompt user for name 
name = str(input("Enter your name: "))
revname = ""
i = len(name) - 1

while i >= 0:
    # save value of name[i]
    revname += name[i]
    i -= 1
#print(revname.title())
print(revname[0].upper() + revname[1:].lower())

# If the name is same forward and backwards print "Palindrome!"
if revname == name:
    print("Palindrome!")
elif revname.lower() == name.lower():
    print("Palindrome!")
elif revname.upper() ==name.upper():
    print("Palindrome!")
else:
    print