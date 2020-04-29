from __future__ import print_function
import random

"""
 Tic Tac Toe
"""

print("Tic Tac Toe")

"""
Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

Here are the requirements:

2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
Feel free to use Google to help you figure anything out (but don't just Google 
"Tic Tac Toe in Python" otherwise you won't learn anything!) Keep in mind that this project 
can take anywhere between several hours to several days.

There are 4 Jupyter Notebooks related to this assignment:

This Assignment Notebook
A "Walkthrough Steps Workbook" Notebook
A "Complete Walkthrough Solution" Notebook
An "Advanced Solution" Notebook
I encourage you to just try to start the project on your own without referencing any of 
the notebooks. If you get stuck, check out the next lecture which is a text lecture with 
helpful hints and steps. If you're still stuck after that, then check out the Walkthrough 
Steps Workbook, which breaks up the project in steps for you to solve. Still stuck? Then 
check out the Complete Walkthrough Solution video for more help on approaching the project!

There are parts of this that will be a struggle...and that is good! I have complete faith 
that if you have made it this far through the course you have all the tools and knowledge 
to tackle this project. Remember, it's totally open book, so take your time, do a little 
research, and remember:
"""


player1 = ""
player2 = ""

def display_board(board):
    # Step 1: Write a function that can print out a board. Set up your board as a list,
    # where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3
    # board representation.
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("| {} | {} | {} |".format(board[4], board[5], board[6]))
    print("| {} | {} | {} |".format(board[7], board[8], board[9]))


def player_input():
    # Step 2: Write a function that can take in a player input and assign their marker as
    # 'X' or 'O'. Think about using while loops to continually ask until you get a correct
    # answer.
    global player1
    global player2

    response = input("First player Enter if you want to be X or O : ")
    response = response.upper()

    while response != "X" and response != "O":
        response = input("First player Enter if you want to be X or O : ")
        response = response.upper()

    player1 = response

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"




def place_marker(board, marker, position):
    # Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
    # and a desired position (number 1-9) and assigns it to the board.
    board[position-1] = marker

    return board


def win_check(board):
    # Step 4: Write a function that takes in a board and a mark (X or O) and then checks to
    # see if that mark has won.
    #  0 | 1 | 2
    #  3 | 4 | 5
    #  6 | 7 | 8
    winnerwinner = "C"
    index = 0
    varExit = True

    # Check Horizontal Win & Vertical Win
    while varExit:
        # Check Horizontal Win
        if board[index] == board[index+1] and board[index] == board[index+2]:
            winnerwinner = board[index]
            varExit = False

        # Check Vertical Win
        if varExit and board[index] == board[index+3] and board[index] == board[index+3]:
            winnerwinner = board[index]
            varExit = False
        else:
            index = index + 1

        # Break out to stop Out of bound error
        if index == 2:
            break

    # Check Left to Right Diagonal Win
    if varExit and board[0] == board[4] and board[0] == board[8]:
        winnerwinner = board[index]
        varExit = False

    # Check Right to Left Diagonal Win
    if varExit and board[2] == board[4] and board[2] == board[6]:
        winnerwinner = board[index]
        varExit = False

    # Return the mark that one or returns a C for Cats Game
    return winnerwinner

def choose_first():
    # Step 5: Write a function that uses the random module to randomly decide which player
    # goes first. You may want to lookup random.randint() Return a string of which player
    # went first.
    ran = random.randint(0,1)

    if ran == 0:
        return "X"
    else:
        return "O"

def space_check(board, position):
    # Step 6: Write a function that returns a boolean indicating whether a space on the
    # board is freely available.
    pass


def full_board_check(board):
    # Step 7: Write a function that checks if the board is full and returns a boolean value.
    # True if full, False otherwise.
    pass


def player_choice(board):
    # Step 8: Write a function that asks for a player's next position (as a number 1-9) and then
    # uses the function from step 6 to check if it's a free position. If it is, then return the
    # position for later use.
    pass


def replay():
    # Step 9: Write a function that asks the player if they want to play again and returns a
    # boolean True if they do want to play again.
    pass

def run_unit_tests():
    test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    display_board(test_board)

    # player_input()
    # print(player1)
    # print(player2)

    print(choose_first())


print('Welcome to Tic Tac Toe!')

run_unit_tests()

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

# while True:
# Set the game up here
# pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break
