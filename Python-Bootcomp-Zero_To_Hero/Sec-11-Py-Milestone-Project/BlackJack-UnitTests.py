from __future__ import print_function
import unittest
from BlackJack_Game import Deck

"""
 Prompt 81-Unittests-library
"""

print("81-Unittests-library")

"""

"""

print("\n81-Unittests-library\n")
print("- - - - - - - - - - ")


class TestBlackJackGame(unittest.TestCase, Deck):
    """
    Note to self: YOU NEED test_ AT THE START OF EVERY FUNCTION TO MAKE IT WORK

    Example:
        def test_one_word(self):
            text = 'python'
            result = cap.cap_text(text)
            self.assertEqual(result, 'Python')
    """
    def test_one(self):
        result = 'MaKe Sure Unit Tests are WORKING'
        self.assertEqual(result, 'MaKe Sure Unit Tests are WORKING')

    def test_two_word(self):
        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                  'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
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


if __name__ == '__main__':
    unittest.main()

