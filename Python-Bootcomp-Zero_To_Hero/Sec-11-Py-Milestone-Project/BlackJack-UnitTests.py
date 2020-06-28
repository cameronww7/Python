from __future__ import print_function
import unittest
from BlackJackGame import Card
from BlackJackGame import Deck
from BlackJackGame import Hand
from BlackJackGame import Chips

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
        print("\n### test_1_basic")
        print("- - - - - - - - - - - - - - ")

        result = 'MaKe Sure Unit Tests are WORKING'
        self.assertEqual(result, 'MaKe Sure Unit Tests are WORKING')

    def test_2_Hand_Class(self):
        print("\n### test_2_HandClass")
        print("- - - - - - - - - - - - - - ")

        twoOfHeartsCard = Card('Hearts', 2, 2)
        result = 'True'
        if twoOfHeartsCard.get_Card() != '2 of Hearts':
            result = 'False'
            print("|{}|".format(twoOfHeartsCard))
        self.assertEqual(result, 'True')

    def test_3_Deck_Class(self):
        print("\n### test_3_DeckClass")
        print("- - - - - - - - - - - - - - ")

        result = "True"

        newDeck = Deck(suits, ranks, values)

        # print("start")
        for index1 in newDeck.deck:
            # print("in here")
            count = 0
            for index2 in newDeck.deck:
                if index1 == index2:
                    count += 1
                    #print("True {} == {}".format(index1, index2))
            if count >= 2:
                result = "False"
                break

        print("EXPECTING -> 52 cards == {} carrds".format(newDeck.get_counter()))
        if newDeck.get_counter() != 52:
            result = "False"

        oneCardDeck = Deck(suits, ranks, values)

        aceOfClubs = str(oneCardDeck.deal_one_card())
        print("EXPECTING -> |Ace of Clubs| == |{}|".format(aceOfClubs))
        if aceOfClubs != "Ace of Clubs":
            result = "False"

        self.assertEqual(result, "True")

    def test_4_hand_Class(self):
        print("\n### test_4_hand")
        print("- - - - - - - - - - - - - - ")

        result = "True"

        nineCard = Card('Diamonds', 'Nine', 9)
        tenCard = Card('Diamonds', 'Ten', 10)

        curHand = Hand()
        curHand.add_card(nineCard)
        curHand.add_card(tenCard)

        curHand.set_Value()

        print("{}curHand Value = {}, {}\n".format(curHand, curHand.get_value(), curHand.get_value_2()))
        print("EXPECTING -> |19| == |{}| and |0| == |{}|".format(curHand.get_value(),curHand.get_value_2()))
        if curHand.get_value() != 19 or curHand.get_value_2() != 0:
            result = "False"

        self.assertEqual(result, "True")

    def test_5_chip_Class(self):
        print("\n### test_5_chip")
        print("- - - - - - - - - - - - - - ")

        result = "True"
        newChips = Chips()

        print("Current Balance: {} , Bet Total : {}".format(newChips.balance(), newChips.get_bet()))

        # Place Bet - Total should be 50g with 50 in Bet
        if not newChips.place_bet(50):
            result = "False"

        print("Place Bet Bal  : {} , Bet Total : {}".format(newChips.balance(), newChips.get_bet()))

        # Win Bet - total should be 150
        if newChips.win_bet() != 150:
            result = "False"

        print("Bal after win  : {} , Bet Total : {}".format(newChips.balance(), newChips.get_bet()))

        # Place a new bet of 150
        if not newChips.place_bet(150):
            result = "False"

        print("Place Bet Bal  : {} , Bet Total : {}".format(newChips.balance(), newChips.get_bet()))
        if newChips.lose_bet() != 0:
            result = "False"

        print("Bal after loss : {} , Bet Total : {}".format(newChips.balance(), newChips.get_bet()))

        self.assertEqual(result, "True")

        print(newChips)

    def test_6_Aces(self):
        print("\n### test_6_Aces")
        print("- - - - - - - - - - - - - - ")

        result = "True"

        aceCard = Card('Diamonds', 'Ace', 11)
        tenCard = Card('Diamonds', 'Ten', 10)

        curHand = Hand()
        curHand.add_card(aceCard)
        curHand.add_card(tenCard)

        curHand.set_Value()
        print("{}curHand Value = {}, {}".format(curHand, curHand.get_value(),curHand.get_value_2()))

        if curHand.get_value_2() != 11:
            result = "False"

    def test_7_clear_hand(self):
        print("\n### test_7_clear_hand")
        print("- - - - - - - - - - - - - - ")
        result = "True"

        aceCard = Card('Diamonds', 'Ace', 11)
        tenCard = Card('Diamonds', 'Ten', 10)

        curHand = Hand()
        curHand.add_card(aceCard)
        curHand.add_card(tenCard)

        curHand.set_Value()
        print("{}curHand Value = {}, {}".format(curHand, curHand.get_value(),curHand.get_value_2()))

        print("\nClearing Hand")
        curHand.clear_hand()
        print("{}curHand Value = {}".format(curHand, curHand.get_value()))

        if curHand.get_value_2() != 0 and curHand.get_value() != 0:
            result = "False"

        self.assertEqual(result, "True")


if __name__ == '__main__':
    unittest.main()

