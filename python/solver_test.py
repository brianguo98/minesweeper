import unittest
from solver import solve
from solver import flagMines
from solver import openCells
from board import Board
from board import Cell


def checkBoardEqual(testBoard, correctBoard, n):
	for row in range(0,n):
		for col in range(0,n):
			if testBoard.player[row][col].state != correctBoard[row][col]:
				return False
	return True

class TestSolver(unittest.TestCase):
	def test_equals(self):
		self.assertEqual(1,1)
	def test_flagMines(self):

		flagCorners = [[Cell('X'), Cell(2), Cell(1)  , Cell('X'), Cell('X')],
					   [Cell('X'), Cell(2), Cell(1)  , Cell(3)  , Cell('X')],
					   [Cell(1)  , Cell(1), Cell('-'), Cell(1)  , Cell(1)  ], 
					   [Cell(1)  , Cell(1), Cell('X'), Cell('X'), Cell('X')], 
					   [Cell('X'), Cell(1), Cell('X'), Cell('X'), Cell('X')]]
		flagCornersCorrect =  [['M',  2,  1,'M','M'],
					           ['M',  2,  1,  3,'M'],
					            [ 1,  1,'-',  1,  1], 
					            [ 1,  1,'X','X','X'], 
					           ['M',  1,'X','X','X']]
		flagCornersGameBoard = Board(5,4)
		flagCornersGameBoard.player = flagCorners
		self.assertTrue(checkBoardEqual(flagMines(flagCornersGameBoard), flagCornersCorrect, 5))

		noMines    =  [[Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')],
					   [Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')],
					   [Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')], 
					   [Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')], 
					   [Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')]]
		noMinesCorrect =      [['X', 'X', 'X', 'X', 'X'],
					           ['X', 'X', 'X', 'X', 'X'],
					           ['X', 'X', 'X', 'X', 'X'], 
					           ['X', 'X', 'X', 'X', 'X'], 
					           ['X', 'X', 'X', 'X', 'X']]
		noMinesGameBoard = Board(5,4)
		noMinesGameBoard.player = noMines
		self.assertTrue(checkBoardEqual(flagMines(noMinesGameBoard), noMinesCorrect, 5))

		flagMiddle  = [[Cell('X'), Cell('X'), Cell('X'), Cell('X'),  Cell('X')],
					   [Cell('X'),  Cell('X'), Cell('X'), Cell('-'), Cell('-')],
					   [Cell('X'),  Cell(8)  , Cell('X'), Cell(4)  , Cell('-')], 
					   [Cell('X'),  Cell('X'), Cell('X'), Cell('X'), Cell('-')], 
					   [Cell('X'),  Cell('X'), Cell('X'), Cell('X'), Cell('X')]]
		flagMiddleCorrect =   [['X', 'X', 'X', 'X', 'X'],
					           ['M', 'M', 'M', '-', '-'],
					           ['M',   8, 'M',   4, '-'], 
					           ['M', 'M', 'M', 'M', '-'], 
					           ['X', 'X', 'X', 'X', 'X']]
		flagMiddleGameBoard = Board(5,4)
		flagMiddleGameBoard.player = flagMiddle
		self.assertTrue(checkBoardEqual(flagMines(flagMiddleGameBoard), flagMiddleCorrect, 5))

	def test_openCells(self):
		# this board must resort to random choice, therefore openCells() should leave board unchanged and return False
		noLogicalChoice = [[Cell(1)  , Cell('X'), Cell(2)  , Cell('X'), Cell('X')],
					       [Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')],
					       [Cell(1)  , Cell('X'), Cell('X'), Cell('X'), Cell(1)  ], 
					       [Cell('X'), Cell('X'), Cell('X'), Cell('X'), Cell('X')], 
					       [Cell('X'), Cell(4)  , Cell('X'), Cell('X'), Cell(1)  ]]
		noLogicalChoiceCorrect =  [[1  , 'X',   2, 'X','X'],
					           	   ['X', 'X', 'X', 'X','X'],
					               [  1, 'X', 'X', 'X',  1], 
					               ['X', 'X', 'X', 'X','X'], 
					               ['X',   4, 'X', 'X',  1]]
		noLogicalChoiceGameBoard = Board(5,4)
		noLogicalChoiceGameBoard.player = noLogicalChoice
		result = openCells(noLogicalChoiceGameBoard)
		self.assertTrue(checkBoardEqual(result[0], noLogicalChoiceCorrect, 5))
		self.assertFalse(result[1])

		# this test ensures that cells are being appropriately opened
		openMultiple = [[Cell(1)        , Cell(1)  , Cell('-'), Cell(1)        , Cell('M', True)],
					    [Cell('M', True), Cell(1)  , Cell('-'), Cell(1)        , Cell(1)        ],
					    [Cell('X')      , Cell(1)  , Cell('-'), Cell('-')      , Cell('-')      ], 
					    [Cell('X')      , Cell(1)  , Cell(1)  , Cell(1)        , Cell(1)        ], 
					    [Cell('X')      , Cell('X'), Cell('X'), Cell('M', True), Cell(1)  ]]

		solution = 		[[Cell(1)       , Cell(1)  , Cell('-'), Cell(1)        , Cell('M', True)],
					    [Cell('M')      , Cell(1)  , Cell('-'), Cell(1)        , Cell(1)        ],
					    [Cell(1)        , Cell(1)  , Cell('-'), Cell('-')      , Cell('-')      ], 
					    [Cell(1)        , Cell(1)  , Cell(1)  , Cell(1)        , Cell(1)        ], 
					    [Cell('M', True), Cell(1)  , Cell(1)  , Cell('M', True), Cell(1)  ]]
		openMultipleCorrect =  [[  1,   1, '-',   1, 'M'],
					           	['M',   1, '-',   1,   1],
					            [  1,   1, '-', '-', '-'], 
					            [  1,   1,   1,  1,    1], 
					            ['X',   1,   1, 'M',   1]]
		openMultipleGameBoard = Board(5,4)
		openMultipleGameBoard.player = openMultiple
		openMultipleGameBoard.solution = solution
		result = openCells(openMultipleGameBoard)
		self.assertTrue(checkBoardEqual(result[0], openMultipleCorrect, 5))
		self.assertTrue(result[1])


if __name__ == "__main__":
	unittest.main()