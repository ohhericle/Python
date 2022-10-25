""" PIG LATIN CONTINUED """ 

# Function is_consonant that takes a character and returns True if it is a consonant.

# Uses function to create a new function to_piglatin that takes a word, moves all starting consonants (all consonants before the first vowel) to the end of the word, then adds ay to the end and returns the result. You may expect that the input to the function will be just one word. (we know this isn't true pig latin - please do not change this basic algorithm). For a single word input the first letter is capitalized and the rest are lower case as shown in the example below.

# Checks if character is a consonant  
def is_consonant(character):
    if character not in "aeiou": # If not a vowel; return True
        return True
    else:
        return False             # If a vowel; return False
    
def to_piglatin (word):
    for char in range(len(word.lower())):         ### Iterate each character in length of word 
        if is_consonant(word[char].lower()) == False: ### Pass in character to is_consonant function ; If character is not a consonant 
            return word[char:].title() + word[:char].lower() + "ay"   ### Print character starting from first vowel + character before consonants + "ay"


#word = str(input("Enter word to translate into pig latin: "))