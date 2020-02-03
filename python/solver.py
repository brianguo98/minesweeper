import random

def markMines(board):
	pass
	

def attemptSolve(board):
	openedAtLeastOne = False
	for row in range(board.dimension):
		for col in range(board.dimension):
			# if cell has at least 1 mine adjacent to it
			if isinstance(board.playerBoard[row][col].state, int):
				# first, check if all mines around a cell have been discovered already
				if board.countAdjacentMines(board.playerBoard, row, col) == board.playerBoard[row][col].state:
					# open rest of the uncovered cells around this mine, this is 100% safe
					for (adjRow, adjCol) in board.getAdjacent(row, col):
						if board.playerBoard[adjRow][adjCol].state == 'X':
							openedAtLeastOne = True
							board.open(adjRow, adjCol)
				# Otherwise, see if there are cell we can definitively mark as mines
				else:
					adjXList = board.getAdjacentX(board.playerBoard, row, col)
					# if the number of already discovered mines and uncovered cells equals the number of adjacent mines
					if len(adjXList) + board.countAdjacentMines(board.playerBoard, row, col) == board.playerBoard[row][col].state:
						# we can mark the uncovered cells as mines with 100% confidence
						for cell in adjXList:
							board.playerBoard[cell[0]][cell[1]].placeMine()
	# if we didn't open any cells during the iteration, pick the first uncovered cell and open it
	if not openedAtLeastOne:
		for row in range(board.dimension):
			for col in range(board.dimension):
				if board.playerBoard[row][col].state == 'X':
					# if opening this cell causes us to lose, it's over
					if not board.open(row, col):
						return False
	return True # continue playing



# TODO: Takes a board and attempts to solve the board. 
# Return a boolean indicating if the board was successfully solved.
def solve(gameBoard) -> bool:
	# gameBoard.showPlayerBoard(False)
	stillAlive = gameBoard.open(0, 0)
	while(stillAlive):
		# print('\n')
		# print("Solution board:")
		# gameBoard.showSol()
		# print("Player board:")
		# gameBoard.showPlayerBoard(False)
		stillAlive = attemptSolve(gameBoard)
		if gameBoard.checkWin():
			# gameBoard.showPlayerBoard(True)
			# print("YEAH BOIIII")
			return True
	# print("LOSER")
	# gameBoard.showPlayerBoard(False)
	return False
 
