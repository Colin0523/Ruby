from random import randint
board =  [["O"]*5] 


for i in range(0,4):
    board.append(["O"]*5)


def print_board(board):
    for row in range(len(board)):
    	print " ".join(board[row])

print print_board(board)
            
coin = randint(0,5)
print coin

# Add your code below!
def random_row(board):
    board = randint(0,len(board)-1)
    return board  
def random_col(board):
    board = randint(0,len(board)-1)
    return board  
 
ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
#guess_row = int(raw_input("Guess Row: "))
#guess_col = int(raw_input("Guess Col: "))

print ship_row
print ship_col

print ship_row
print ship_col
board[guess_row][guess_col] = "X"




# Write your code below!
if ship_row == guess_row:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"
print print_board(board)
