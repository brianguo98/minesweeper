from board import Board
import argparse
import re

UNDERLINE = '\033[4m'
END = '\033[0m'

def printInitialBoard(n):
    print('  ', end='')
    for colMarker in range(n):
        print(UNDERLINE + str(colMarker) + END, end='')
        if colMarker < 10:
            print('  ', end='')
        else:
            print(' ', end='')
    print('\n')
    for row in range(n):
        print(UNDERLINE + str(row) + END, end='')
        print(' ', end='')
        for col in range(n):
            print('X', end='')
            print('  ', end='')
        print('\n')

def getUserInput(n):
	# robust input validation. Ensures that game doesn't crash due to wrong input format
	print("Please enter a move: ")
	userIn = input()
	while not re.match('^[0-'+str(n-1)+']\s[0-'+str(n-1)+']$', str(userIn)):
		print("Oops! Something was wrong with your input...")
		print("Please check that your input is in the format [[row] [col]] and your values are between 0 and " + str(n-1))
		print("Please enter a move: ")
		userIn = input()
	userRow, userCol = map(int, userIn.split())
	return userRow, userCol

def playgame(n, num_mines):
	printInitialBoard(n)
	userRow, userCol = getUserInput(n)
	gameBoard = Board(n, num_mines, userRow, userCol)
	move = gameBoard.open(userRow, userCol)
	# gameBoard.showSol()
	while(move):
		print('\n')
		# gameBoard.showSol()
		gameBoard.showplayer(False)
		userRow, userCol = getUserInput(n)
		move = gameBoard.open(userRow, userCol)
		if gameBoard.checkWin():
			print('\n')
			gameBoard.showplayer(True)
			return True
	print('\n')
	gameBoard.showplayer(False)
	return False

def checkValidGame(n, num_mines):
	if n == 0 or num_mines > n*n-1:
		print("Illegal game. Board must be at least 1x1 and num_mines must be at least 1 less than the total number of cells.")
		return False
	return True

def printMenu():
	print("Minesweeper 2k20")
	print("All moves should be entered as follows:")
	print("[row] [col]")
	input("Press Enter to begin!")
	print('\n')

def main(n, num_mines):
	if not checkValidGame(n, num_mines):
		return
	printMenu()
	choice = 'yes'
	while choice == 'yes':
		if playgame(n, num_mines):
			print("\nCongrats, you win! Would you like to play again? (yes or no)")
		else:
			print("\nYou've opened a mine :( Better luck next time! Would you like to play again? (yes or no)")
		choice = str.lower(input())
		while choice != 'yes' and choice != 'no':
			print("Please enter 'yes' or 'no'")
			choice = str.lower(input())
			print('\n')
	print("Thank you for playing Minesweeper 2k20. Have a great day!")	

# DO NOT EDIT--------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', nargs='?', type=int, default=10)
    parser.add_argument('num_mines', nargs='?', type=int, default=10)
    return parser.parse_args() 

if __name__ == "__main__":
    args = parse_args()
    main(args.n, args.num_mines)

# DO NOT EDIT--------------------------------------------
