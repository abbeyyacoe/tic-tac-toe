def drawboard(board):
	# Prints a tic tac toe board
	print "   "
	print " " + board[0] + " | " + board[1] + " | " +  board[2] + " " 
	print "-----------"
	print " " + board[3] + " | " + board[4] + " | " +  board[5] + " " 
	print "-----------"
	print " " + board[6] + " | " + board[7] + " | " +  board[8] + " "


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def make_move():
	ticker = 0

	# This game only lasts 10 moves
	for i in range(0,10):
		print "Where do you want to go? (pick a number between 1 and 9)"
		drawboard(board)
		move = int(raw_input())-1
		ticker += 1
		# Alternates between X and 0 and makes sure you cant go the same place twice
		if ticker % 2 == 0:
			if board[move] == " ":
				board[move] = "X"
			else: 
				print "You can't go there!"	
				ticker -= 1
		else: 
			if board[move] == " ":
				board[move] = "O"
			else: 
				print "You can't go there!"	
				ticker -= 1

		# Prints the winner	
		if winner(board,board[move]):
			print "  "
			print (board[move] + "'s Win!")
			break


def winner(board,letter):
	# Checks for matches
	return ((board[0] == letter and board[1] == letter and board[2] == letter) or
	(board[3] == letter and board[4] == letter and board[5] == letter) or
	(board[6] == letter and board[7] == letter and board[8] == letter) or
	(board[0] == letter and board[3] == letter and board[6] == letter) or
	(board[1] == letter and board[4] == letter and board[7] == letter) or
	(board[2] == letter and board[5] == letter and board[8] == letter) or
	(board[0] == letter and board[4] == letter and board[8] == letter) or
	(board[0] == letter and board[4] == letter and board[8] == letter) or
	(board[2] == letter and board[4] == letter and board[7] == letter))

	
	
if __name__ == "__main__":
	print "  "
	print "Welcome to Tic Tac Toe!"
	print "  "
	make_move()
	




