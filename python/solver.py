import random
from board import countAdjacentMines
from board import getAdjacent

def getAdjacentUnopened(board, row, col, dimension):
        xList = []
        for (adjRow, adjCol) in getAdjacent(row, col, dimension):
            if board[adjRow][adjCol].state == 'X':
                xList.append((adjRow, adjCol))
        return xList

def flagMines(board):
	for row in range(board.dimension):
		for col in range(board.dimension):
			# if an uncovered cell has at least 1 mine adjacent to it
			if isinstance(board.player[row][col].state, int):
				# get list of unopened cells adjecent to current cell
				adjXList = getAdjacentUnopened(board.player, row, col, board.dimension)
				# if the number of unopened cells plus flagged discovered mines equals the number of adjacent mines
				if len(adjXList) + countAdjacentMines(board.player, row, col, board.dimension) == board.player[row][col].state:
					# we can mark the unopened cells as mines with 100% confidence
					for cell in adjXList:
						board.player[cell[0]][cell[1]].placeMine()
	return board

def openCells(board):
	openedAtLeastOne = False
	for row in range(board.dimension):
		for col in range(board.dimension):
			# if cell is known to have at least 1 mine adjacent to it
			if isinstance(board.player[row][col].state, int):
				# check if number of known adjacent mines matches the number on the cell
				if countAdjacentMines(board.player, row, col, board.dimension) == board.player[row][col].state:
					# if so, we can safely open the remaining unopened cells adjacent to the current cell
					for (adjRow, adjCol) in getAdjacent(row, col, board.dimension):
						if board.player[adjRow][adjCol].state == 'X':
							openedAtLeastOne = True
							board.open(adjRow, adjCol)
	return board, openedAtLeastOne

def openRandom(board):
	n = int(board.dimension)
	openRow, openCol = random.randint(0, n-1), random.randint(0, n-1)
	# keep generating random numbers until you find an unopened cell
	while board.player[openRow][openCol].state != 'X':
		openRow, openCol = random.randint(0, n-1), random.randint(0, n-1)
	# if opening this random cell causes us to lose, game over
	if not board.open(openRow, openCol):
		return board, False
	return board, True

def attemptSolve(board):
	board = flagMines(board)
	board, openedAtLeastOne = openCells(board)
	if not openedAtLeastOne:
		result = openRandom(board)
		board = result[0]
		return result[1]
	return True

# Return a boolean indicating if the board was successfully solved.
def solve(gameBoard) -> bool:
	stillAlive = gameBoard.open(0, 0)
	while(stillAlive):
		if gameBoard.checkWin():
			return True
		stillAlive = attemptSolve(gameBoard)
	return False