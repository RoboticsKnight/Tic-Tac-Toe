board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


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

    handle_turn()

# ======================================================================
# Player turn handling
# ======================================================================
def handle_turn():

    # Player selecting where they would like to put their marker
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"
    display_board()


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



