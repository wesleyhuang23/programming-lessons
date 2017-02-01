#BATTLE SHIP PROJECT PYTHON
#appending 5 'O'
board = []

for i in range(0, 5):
    board.append(['O'] * 5)

#prints [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]

def print_board(board):
    for i in range(0, len(board)):
        print board[i]

print_board(board)

"""prints 
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
"""

#JOIN
#-join on what then method, usually elements in array into a string
board = []

for i in range(0, 5):
    board.append(['O'] * 5)

def print_board(board):
    for i in range(0, len(board)):
        print " ".join(board[i])

print_board(board)

"""
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
"""

#RANDOM ROW AND COL
#-randint: give random number within the givien range includes all high and low
def random_row(board):
    return randint(0, len(board) - 1)
random_row(board)

def random_col(board):
    return randint(0, len(board) - 1)
random_col(board)

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

print ship_row
print ship_col

#if statement with and
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or                guess_col > 4):
            print "Oops, that's not even in the ocean."
            if turn == 3:
                print "Game Over"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            if turn == 3:
                print "Game Over"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"
        # Print (turn + 1) here!
        print "Turn", turn + 1
        print_board(board)
        