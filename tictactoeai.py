from random import randint
import time

def drawboard(board):
	# Prints a tic tac toe board
	print "   "
	print " " + board[0] + " | " + board[1] + " | " +  board[2] + " " 
	print "-----------"
	print " " + board[3] + " | " + board[4] + " | " +  board[5] + " " 
	print "-----------"
	print " " + board[6] + " | " + board[7] + " | " +  board[8] + " "


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# def make_move():
# 	ticker = 0

# 	# This game only lasts 10 moves
# 	for i in range(0,10):
# 		print "Where do you want to go? (pick a number between 1 and 9)"
# 		drawboard(board)
# 		move = int(raw_input())-1
# 		ticker += 1
# 		# Alternates between X and 0 and makes sure you cant go the same place twice
# 		if ticker % 2 == 0:
# 			if board[move] == " ":
# 				board[move] = "X"
# 			else: 
# 				print "You can't go there!"	
# 				ticker -= 1
# 		else: 
# 			if board[move] == " ":
# 				board[move] = "O"
# 			else: 
# 				print "You can't go there!"	
# 				ticker -= 1

# 		# Prints the winner	
# 		if winner(board,board[move]):
# 			print "  "
# 			print (board[move] + "'s Win!")
# 			break




def human(board):
	move = int(raw_input())-1
	if board[move] == " ":
		board[move] = "X"
		drawboard(board)
	else:
		print "That space is taken!"
		human(board)
		

def computer(board):

	if board[4] == " ":
		move = 4
	elif board[0] == " ":
		move = 0	
	elif board[2] == " ":
		move = 2	
	elif board[6] == " ":
		move = 6	
	elif board[8] == " ":
		move = 8					
	else:		
		move = randint(0,8)

	time.sleep(.3)
	if board[move] == " ":
		board[move] = "0"
		drawboard(board)
	else:
		computer(board)

def play(board):
	print "Pick a number between 1 and 9"
	for i in range(1,10):
		if i % 2 != 0:
			human(board)
		else:
			computer(board)	

		if winner(board):
			print "  "
			print ("You Win!")
			break	







def winner(board):
	# Checks for matches
	return ((board[0] == board[1] == board[2] and board[0] != " ") or
	(board[3] == board[4] == board[5] and board[3] != " ") or
	(board[6] == board[7] == board[8] and board[6] != " ") or
	(board[0] == board[3] == board[6] and board[0] != " ") or
	(board[1] == board[4] == board[7] and board[1] != " ") or
	(board[2] == board[5] == board[8] and board[2] != " ") or
	(board[0] == board[4] == board[8] and board[0] != " ") or
	(board[0] == board[4] == board[8] and board[0] != " ") or
	(board[2] == board[4] == board[7] and board[2] != " "))

	
if __name__ == "__main__":
	print " "
	print "Welcome to Tic Tac Toe!"
	drawboard(board)
	play(board)

	




