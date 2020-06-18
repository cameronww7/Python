from __future__ import print_function
import unittest
from BlackJackGame import Card
from BlackJackGame import Deck
from BlackJackGame import Hand

"""
 Prompt 81-Unittests-library
"""

print("81-Unittests-library")

"""

"""

print("\n81-Unittests-library\n")
print("- - - - - - - - - - ")

# Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class TestBlackJackGame(unittest.TestCase, Deck):
    """
    Note to self: YOU NEED test_ AT THE START OF EVERY FUNCTION TO MAKE IT WORK

    Example:
        def test_one_word(self):
            text = 'python'
            result = cap.cap_text(text)
            self.assertEqual(result, 'Python')
    """


    def test_1_basic(self):
        result = 'MaKe Sure Unit Tests are WORKING'
        self.assertEqual(result, 'MaKe Sure Unit Tests are WORKING')

    def test_2_HandClass(self):
        twoOfHeartsCard = Card('Hearts', 2, 2)
        result = 'True'
        if twoOfHeartsCard.get_Card() != '2 of Hearts':
            result = 'False'
            print("|{}|".format(twoOfHeartsCard))
        self.assertEqual(result, 'True')

    def test_3_DeckClass(self):
        newDeck = Deck(suits, ranks, values)
        result = "True"
        # print("Sstart")
        for index1 in newDeck.deck:
            # print("in here")
            count = 0
            for index2 in newDeck.deck:
                if index1 == index2:
                    count += 1
                    # print("True {} == {}".format(index1, index2))
            if count >= 2:
                result = "False"
                break

        self.assertEqual(result, "True")

    def test_4_hand(self):
        newDeck = Deck(suits, ranks, values)
        result = "True"
        playerHand = Hand()
        dealerHand = Hand()
        newDeck.shuffle()
        #curHand.add_card(newDeck.deal_one_card())
        #curHand.add_card(newDeck.deal_one_card())

        for index in range(0,2):
            playerHand.add_card(newDeck.deal_one_card())
            dealerHand.add_card(newDeck.deal_one_card())

        print(playerHand)
        print(dealerHand)

        playerHand.set_Value()

        self.assertEqual(result, "True")

if __name__ == '__main__':
    unittest.main()

