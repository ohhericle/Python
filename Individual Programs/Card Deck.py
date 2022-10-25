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
        hand = []
        if len(self.cards) < card_count:
            return "Cannot deal " + str(card_count) + " cards. The deck only has " + str(len(self.cards)) + " cards left!" # No cards left to deal
        for i in range(card_count): 
            hand.append(self.cards.pop(0)) # Pop first item in list into hand 
        return hand
