# ------- Global Variables ---------

# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If Game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it
current_player = "X"


# ======================================================================
# Default board
# ======================================================================
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# ======================================================================
# Main function/Main Game control
# ======================================================================
def play_game():

    # Display initial board
    display_board()

    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Switch to the other player
        switch_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# ======================================================================
# Player turn handling
# ======================================================================
def handle_turn(player):

    print(player + "'s turn.")

    # Player selecting where they would like to put their marker
    position = input("Choose a position from 1-9: ")

    valid = False

    while not valid:
        # Input checking
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        # If the spot has been taken
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player
    display_board()

# ======================================================================
# Game over checks
# ======================================================================
def check_if_game_over():
    check_for_winner()
    check_if_tie()

# ======================================================================
# Win checks
# ======================================================================
def check_for_winner():

    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals    
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

# ======================================================================
# Rows check
# ======================================================================
def check_rows():

    # Set up global variables
    global game_still_going

    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    # Return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

    return

# ======================================================================
# Columns check
# ======================================================================
def check_columns():
    
    # Set up global variables
    global game_still_going

    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    # Return the winner (X or O)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]

    return

# ======================================================================
# Diagonals check
# ======================================================================
def check_diagonals():

    # Set up global variables
    global game_still_going

    # Check if any of the diagonal has all the same value (and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"


    # If any diagonal does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    
    # Return the winner (X or O)
    if diagonals_1:
        return board[0]
    if diagonals_2:
        return board[6]

    return

# ======================================================================
# Tie checks
# ======================================================================
def check_if_tie(): # FIX (Tie is not being recognised as a result)

    global game_still_going

    if "-" not in board:
        game_still_going == False

    return

# ======================================================================
# Switching player handling
# ======================================================================
def switch_player():

    # Set up global varaiables
    global current_player

    # If the current player was X, then change to O
    if current_player == "X":
        current_player = "O"
        # If the current player was O, then change to X
    elif current_player == "O":
        current_player = "X"

    return

play_game()




# board
# display board
# play game
# turn handling
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# switch player



