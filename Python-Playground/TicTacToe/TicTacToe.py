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
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("-----------")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("-----------")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("")


def player_choose_side():
    # Step 2: Write a function that can take in a player input and assign their marker as
    # 'X' or 'O'. Think about using while loops to continually ask until you get a correct
    # answer.
    global player1
    global player2

    while True:
        try:
            response = input("First player Enter if you want to be X or O : ")
            break
        except:
            print("Error - Invalid Character - Only Numbers are allowed")

    while response != "X" and response != "O" and response != "x" and response != "o":
        print("< ERROR, Please Enter in either a X or O >")
        while True:
            try:
                response = input("First player Enter if you want to be X or O : ")
                break
            except:
                print("Error - Invalid Character - Only Numbers are allowed")

        response = response.upper()

    player1 = response

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    print("\nPlayer 1 is {}".format(player1))
    print("Player 2 is {}".format(player2))


def place_marker(board, marker, position):
    # Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
    # and a desired position (number 1-9) and assigns it to the board.
    board[position - 1] = marker

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
        if board[index] == board[index + 1] and board[index] == board[index + 2] \
                and board[index] != " " and board[index + 1] != " " and board[index + 2] != " ":
            winnerwinner = board[index]
            print("index:{} | Horizontal Win".format(index))
            varExit = False

        # Check Vertical Win
        if varExit and board[index] == board[index + 3] and board[index] == board[index + 6] \
                and board[index] != " " and board[index + 3] != " " and board[index + 6] != " ":
            winnerwinner = board[index]
            print("index:{} | Vertical Win".format(index))
            varExit = False
        else:
            index = index + 1

        # Break out to stop Out of bound error
        if index == 2:
            break

    # Check Left to Right Diagonal Win
    if varExit and board[0] == board[4] and board[0] == board[8] and board[0] != " " \
            and board[0] != " " and board[4] != " " and board[8] != " ":
        winnerwinner = board[index]
        print("Right Diagonal Win")
        varExit = False

    # Check Right to Left Diagonal Win
    if varExit and board[2] == board[4] and board[2] == board[6] \
            and board[2] != " " and board[4] != " " and board[6] != " ":
        winnerwinner = board[index]
        print("Left Diagonal Win")
        varExit = False

    # Return the mark that one or returns a C for Cats Game
    return winnerwinner


def choose_first():
    # Step 5: Write a function that uses the random module to randomly decide which player
    # goes first. You may want to lookup random.randint() Return a string of which player
    # went first.
    ran = random.randint(0, 1)

    if ran == 0:
        return "X"
    else:
        return "O"


def space_check(board, position):
    # Step 6: Write a function that returns a boolean indicating whether a space on the
    # board is freely available.
    if board[int(position) - 1] == " ":
        return True
    else:
        return False


def full_board_check(board):
    # Step 7: Write a function that checks if the board is full and returns a boolean value.
    # True if full, False otherwise.
    for index in range(0, 9, 1):
        if board[index] == " ":
            return False

    return True


def player_choice(board):
    # Step 8: Write a function that asks for a player's next position (as a number 1-9) and then
    # uses the function from step 6 to check if it's a free position. If it is, then return the
    # position for later use.
    while True:
        try:
            response = int(input("Player Enter the spot you want (1-9): "))
            break
        except:
            print("Error - Invalid Character - Only Numbers are allowed")

    while 9 < int(response) or int(response) < 1:
        print("< ERROR, Please Enter a Spot 1 - 9 >")
        while True:
            try:
                response = int(input("Player Enter the spot you want (1-9): "))
                break
            except:
                print("Error - Invalid Character - Only Numbers are allowed")

    while 9 < int(response) or int(response) < 1 or not space_check(board, int(response)):
        while 9 < int(response) or int(response) < 1:
            print("< ERROR, Please Enter a Spot 1 - 9 >")
            while True:
                try:
                    response = int(input("Player Enter the spot you want (1-9): "))
                    break
                except:
                    print("Error - Invalid Character - Only Numbers are allowed")

        print("< ERROR, Please enter in a Spot that is Empty >")
        while True:
            try:
                response = int(input("Player Enter the spot you want (1-9): "))
                break
            except:
                print("Error - Invalid Character - Only Numbers are allowed")

    return int(response)


def replay():
    # Step 9: Write a function that asks the player if they want to play again and returns a
    # boolean True if they do want to play again.
    while True:
        try:
            response = input("Please enter a Y to Play Again and N to Stop: ")
            response = response.upper()
            break
        except:
            print("Error - Invalid Character - Only Letters are allowed")

    while response != "Y" and response != "N":
        print("< ERROR, Please Enter a Y or  N >")
        response = input("Please enter a Y to Play Again and N to Stop: ")
        response = response.upper()

    if response == "Y":
        return True
    else:
        return False


def display_directions():
    print("\nHello and Welcome to my game of Tic Tac Toe"
          "\nFirst lets get the rules out of the way!"
          "\nDisplayed below is the board, with spots"
          "\nthat are numbers 1 - 9. "
          "\nWhen it is your turn you will enter in "
          "\na number between 1 - 9 to select your slot."
          "\nOnce your turn is over your oppotent will"
          "\nplace his turn, and so on till the game ends."
          "\nat the end you will be prompted to play again")
    spotBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(spotBoard)


def run_unit_tests():
    # Unit Test display_board(board)
    # ----------------------
    # test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    # display_board(test_board)
    # test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # display_board(test_board)

    # Unit Test player_choose_side()
    # ----------------------
    # player_choose_side()
    # print("\nTesting Global Variable Changes")
    # print("Player 1 is {}".format(player1))
    # print("Player 2 is {}".format(player2))

    # Unit Test place_marker(board, marker, position)
    # ----------------------
    # test_board = [' ', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    # test_board = place_marker(test_board, "X", 1)
    # print(test_board)

    # Unit Test win_check(board)
    # ----------------------
    # test_board = ['X', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'O']
    # display_board(test_board)
    # print(win_check(test_board))

    # Unit Test choose_first()
    # ----------------------
    # print(choose_first())

    # Unit Test space_check(board, position)
    # ----------------------
    # test_board = [' ', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'O']
    # print(space_check(test_board, 0))
    # print(space_check(test_board, 1))

    # Unit Test full_board_check(board)
    # ----------------------
    # test_board = ['X', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'O']
    # print(full_board_check(test_board))

    # Unit Test player_choice(board)
    # ----------------------
    # test_board = [' ', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'O']
    # display_board(test_board)
    # print(player_choice(test_board))

    # Unit Test replay()
    # ----------------------
    # print(replay())

    # Unit Test display_directions
    # ----------------------
    # display_directions()

    pass  # end of unit Tests


# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
print('Welcome to Tic Tac Toe!')

run_unit_tests()

while True:
    display_directions()

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player_choose_side()
    game_on = True
    checkWin = "C"

    while game_on:
        print("\nCurrent Board Status")
        display_board(board)

        # Player 1 Starts
        print("Player {} Turn".format(player1))
        player1Spot = player_choice(board)
        place_marker(board, player1, player1Spot)
        display_board(board)

        # Check if Player 1 Won
        # If player 1 Won will stop Player 2 from Playing
        checkWin = win_check(board)
        if checkWin != "C" or full_board_check(board):
            game_on = False
        else:
            # Player 2 Starts
            print("Player {} Turn".format(player2))
            player2Spot = player_choice(board)
            place_marker(board, player2, player2Spot)
            display_board(board)

            # Check if Player 2 Won
            checkWin = win_check(board)
            if checkWin != "C" or full_board_check(board):
                print("checkwin {} | Fullboard {}".format(checkWin, full_board_check(board)))
                game_on = False

    if checkWin == player1:
        print("Player {} WINS".format(player1))
    elif checkWin == player2:
        print("Player {} WINS".format(player2))
    else:
        print("its a Cats Game")

    game_on = replay()
    if not game_on:
        break
