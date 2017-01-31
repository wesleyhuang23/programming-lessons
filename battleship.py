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