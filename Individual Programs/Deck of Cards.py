""" DECK OF CARDS """

# # 1. Class called PlayingCard.
# This class has:

# An attribute, "rank" that takes a value of "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", or "A"
# An attribute, "suit" that takes a value of "♠" "♥" "♦" or "♣". (If you don't know how to make these characters you can cut and paste from this block)
# An init method that:
# Accepts as parameters a specific rank (as a string) and suit (as a string).
# Raise a TypeError with "Invalid rank!" or "Invalid suit!" when a rank or suit is not valid.
# The __str__ and __repr__ methods to display the cards correctly (as shown below in the examples)
# 2. Please create a class called Deck. (30 points)
# This class should have:

# An attribute, "cards", that holds a list of PlayingCard objects.

# An init method that:

# By default stores a full deck of 52 playing card (with proper numbers and suits) in the "cards" list. Each cards will be of the class PlayingCard above
# Allows the user to specify a specific suit of the 4 ("♠" "♥" "♦" or "♣"). In this case, the program should only populate the deck with the 13 cards of that suit.
# After the cards object is initialized, call the "shuffle_deck()" function (below).
# A "shuffle_deck()" method that randomly changes the order of cards in the deck.

# Import the random library to 'shuffle' the deck: https://docs.python.org/3.9/library/random.html#random.shuffle
# A "deal_card(card_count)" method that:

# Removes the first card_count cards from the deck and returns them as a list.
# If the deck doesnt have the card_count number of cards left to deal, return the message Cannot deal <x> cards. The deck only has <y> cards left! (do not raise an exception or print inside the method).

import random
from random import shuffle

class PlayingCard: # Class PlayingCard 

    def __init__ (self, rank, suit): # Accepts as parameters a specific rank (as a string) and suit (as a string).
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠", "♥", "♦", "♣"] 
        
        if rank in ranks:
            self.rank = rank # Attribute 
        else:
            # Raise a TypeError with "Invalid rank!"
            raise TypeError("Invalid rank!")
        if suit in suits:
            self.suit = suit # Attribute 
        else:
            # Raise a TypeError with "Invalid suit!"
            raise TypeError("Invalid suit!") 
    
    def __repr__(self): # Repr method to display cards 
        return str(self.rank) + " of " + str(self.suit)

    def __str__(self): # Str method to display cards 
        return str(self.rank) + " of " + str(self.suit)

class Deck: # Class Deck 
    
    def __init__(self, suit = None):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠", "♥", "♦", "♣"] 
        if suit == None:
            self.cards = [PlayingCard(r, s) for r in ranks for s in suits] # Create PlayingCard Object 
        else:
            self.cards = [PlayingCard(r, suit) for r in ranks]
        self.shuffle_deck()

    def shuffle_deck(self): # Method that randomly changes the order of cards in the deck.
        shuffle(self.cards)

    def deal_card(self, card_count): 
        hand = [] # Empty list for cards in hand 
        if len(self.cards) < card_count:
            return "Cannot deal " + str(card_count) + " cards. The deck only has " + str(len(self.cards)) + " cards left!" # No cards left to deal
        for i in range(card_count): 
            hand.append(self.cards.pop(0)) # Pop first item in list into hand 
        return hand