import random


def attemptSolve(board):
	openedAtLeastOne = False
	for row in range(board.dimension):
		for col in range(board.dimension):
			# if uncovered cell has at least 1 mine adjacent to it
			if isinstance(board.player[row][col].state, int):
				# get list of unopened cells adjecent to current cell
				adjXList = board.getAdjacentUnopened(board.player, row, col)
				# if the number of already discovered mines and unopened cells equals the number of adjacent mines
				if len(adjXList) + board.countAdjacentMines(board.player, row, col) == board.player[row][col].state:
					# we can mark the uncovered cells as mines with 100% confidence
					for cell in adjXList:
						# print(str(cell[0]) + ' ' + str(cell[1]) + ' marked as a mine')
						board.player[cell[0]][cell[1]].placeMine()
	for row in range(board.dimension):
		for col in range(board.dimension):
			# if uncovered cell has at least 1 mine adjacent to it
			if isinstance(board.player[row][col].state, int):
				# check if all mines around a cell have been discovered already
				if board.countAdjacentMines(board.player, row, col) == board.player[row][col].state:
					# open rest of the uncovered cells around this mine, this is 100% safe
					for (adjRow, adjCol) in board.getAdjacent(row, col):
						if board.player[adjRow][adjCol].state == 'X':
							openedAtLeastOne = True
							board.open(adjRow, adjCol)
				# Otherwise, see if there are cell we can definitively mark as mines
				# else:
					# adjXList = board.getAdjacentUnopened(board.player, row, col)
					# # if the number of already discovered mines and uncovered cells equals the number of adjacent mines
					# if len(adjXList) + board.countAdjacentMines(board.player, row, col) == board.player[row][col].state:
					# 	# we can mark the uncovered cells as mines with 100% confidence
					# 	for cell in adjXList:
					# 		board.player[cell[0]][cell[1]].placeMine()
	# if we didn't open any cells logically, pick a random cell and open it
	if not openedAtLeastOne:
		n = int(board.dimension)
		openRow, openCol = random.randint(0, n-1), random.randint(0, n-1)
		while board.player[openRow][openCol].state != 'X':
			print("in loop")
			openRow, openCol = random.randint(0, n-1), random.randint(0, n-1)
		# if opening this cell causes us to lose, it's over :(
		if not board.open(openRow, openCol):
			return False
	return True # continue playing



# TODO: Takes a board and attempts to solve the board. 
# Return a boolean indicating if the board was successfully solved.
def solve(gameBoard) -> bool:
	# gameBoard.showplayer(False)
	stillAlive = gameBoard.open(0, 0)
	while(stillAlive):
		# print('\n')
		# print("Solution board:")
		# gameBoard.showSol()
		# print("Player board:")
		# gameBoard.showplayer(False)
		stillAlive = attemptSolve(gameBoard)
		if gameBoard.checkWin():
			# gameBoard.showplayer(True)
			# print("YEAH BOIIII")
			return True
	# print("LOSER")
	# gameBoard.showplayer(False)
	return False
 
