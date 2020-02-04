import unittest
from solver import solve
from board import Board


# This is some starter code to test.
# You can delete this and test however you like.

class TestSolver(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(1,1)
    def test_emptyBoard(self):
    	gameBoard = Board()


if __name__ == "__main__":
    unittest.main()