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
# Main function
# ======================================================================
def play_game():

    # Display initial board
    display_board()

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

    # Player selecting where they would like to put their marker
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"
    display_board()

# ======================================================================
# Game over checks
# ======================================================================
def check_if_game_over():
    check_if_win()
    check_if_tie()

# ======================================================================
# Win checks
# ======================================================================
def check_if_win():
    # check rows
    # check columns
    # check diagonals    
    return

# ======================================================================
# Tie checks
# ======================================================================
def check_if_tie():
    return

# ======================================================================
# Switching player handling
# ======================================================================
def switch_player():
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



