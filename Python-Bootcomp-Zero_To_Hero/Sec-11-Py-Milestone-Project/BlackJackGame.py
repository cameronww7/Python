from __future__ import print_function
import random

"""
 Prompt 82-BlackJack-Game
"""

print("82-BlackJack-Game")

"""
Milestone Project 2 - Blackjack Game
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the player's total money.
- You need to alert the player of wins, losses, or busts, etc...

And most importantly:

You must use OOP and classes in some portion of your game. 
You can not just use functions in your game. 
Use classes to help you define the Deck and the Player's hand. 
There are many right ways to do this, so explore it well!

Feel free to expand this game. 
Try including multiple players. 
Try adding in Double-Down and card splits! 
Remember to you are free to use any resources you want and as always HAVE FUN!

Game Play
To play a hand of Blackjack the following steps must be followed:

- Create a deck of 52 cards
- Shuffle the deck
- Ask the Player for their bet
- Make sure that the Player's bet does not exceed their available chips
- Deal two cards to the Dealer and two cards to the Player
- Show only one of the Dealer's cards, the other remains hidden
- Show both of the Player's cards
- Ask the Player if they wish to Hit, and take another card
- If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
- If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
- Determine the winner and adjust the Player's chips accordingly
- Ask the Player if they'd like to play again

Playing Cards
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks 
(2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, 
Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without 
busting. As a starting point in your program, you may want to assign variables to store a list of suits, 
ranks, and then use a dictionary to map ranks to values.

The Game
Imports and Global Variables
Step 1: Import the random module. This will be used to shuffle the deck prior to dealing. Then, declare 
variables to store suits, ranks and values. You can develop your own system, or copy ours below. Finally, 
declare a Boolean value to be used to control while loops. This is a common practice used to control the 
flow of the game.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

"""

print("\n82-BlackJack-Game\n")
print("- - - - - - - - - - ")


class Card:
    """
    This class will function as a card.
    Meaning it will have a Rank and Suite.
    Will be apart of an array of some sort.
    Will output for example "Queen of Hearts" if printed.
    """
    def __init__(self, xSuite, xRank, xValue):
        self.suit = xSuite
        self.rank = xRank
        self.value = xValue

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

    def get_Card(self):
        return "%s of %s" % (self.rank, self.suit)

    def get_Card_Value(self):
        return self.value

    def get_Card_Suite(self):
        return self.suit


class Deck(Card):
    """
    This Class will create an Entire Desk of Cards (Card Class).
    This wil be used to play the game.
    Should keep track of what is dealt to prevent duplicates.
    """
    def __init__(self, xSuite, xRank, xValue):
        suit = xSuite
        rank = xRank
        counter = 0

        self.deck = []  # start with an empty list

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank, xValue.get(rank))
                self.deck.append(card)
                counter += 1

    def __str__(self):
        counter = 1
        for index in self.deck:
            print("%s: %s" % (counter, index))
            counter += 1
        return ""

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one_card(self):
        return self.deck.pop()

class Hand:
    """
    Hand Class is what each player has in this hand
    So at least two objects, First a Player Hand and second the Dealer Hand
    """
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.value2 = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def set_Value(self):
        # I need to loop through the dictionary and add up the value of each card
        # and assign it a total value so
        # add up, Ace + 10 = Blackjack, 10 + 7 = 17
        for index in self.cards:
            # Tracks the Number of Aces

            if index.get_Card_Value() == 11:
                self.value2 += 1
                self.aces -= 1
            elif self.value2 != 0:
                self.value2 += index.get_Card_Value()
                self.aces -= 1
            elif self.aces >= 1:
                self.value2 += index.get_Card_Value()

            self.value += index.get_Card_Value()

        #print(self.value)

    def get_value(self):
        return self.value

    def get_value_2(self):
        return self.value2

    def get_cards(self):
        return self.cards

    def aces_exist(self):
        if self.aces >= 1:
            return True
        else:
            return False

    def add_card(self, xCard):
        # adds 1 card
        self.cards.append(xCard)

        if xCard.get_Card_Value() == 11:
            self.aces += 1

        return True

    def add_cards(self, xCards):
        # adds as many cards are sent in, proply useless
        for card in xCards:
            self.cards.append(card)
        return True

    def adjust_for_ace(self):
        # Provides two values to account for an Ace
        pass

    def clear_hand(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.value2 = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def __str__(self):
        counter = 1
        for index in self.cards:
            print("%s: %s" % (counter, index))
            counter += 1
        return ""


class Chips:
    """
    Chips Class is to hold each players chips
    Needs to Make bets and hold each player total
    """
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def balance(self):
        return self.total

    def place_bet(self, xPlacedBet):
        if xPlacedBet <= self.total:
            print("Bet Placed")
            self.bet = xPlacedBet
            return True
        else:
            print("You do not have that Chip amount")
            return False

    def win_bet(self):
        self.total = self.total + self.bet
        return self.total

    def lose_bet(self):
        self.total = self.total - self.bet
        return self.total

    def __str__(self):
        #print("Stack Total : {}".format(self.total))
        return "Stack Total : {}".format(self.total)

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

newDeck = Deck(suits, ranks, values)
#print(newDeck)
