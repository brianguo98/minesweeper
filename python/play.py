from board import Board
import argparse

def printInitialBoard(n):
    print('  ', end='')
    for rowMarker in range(n):
        print(rowMarker, end='')
        print(' ', end='')
    print('\n')
    for row in range(n):
        print(row, end='')
        print(' ', end='')
        for col in range(n):
            print('X ', end='')
        print('\n')

def getUserInput(n):
	print("Please enter a move: ")
	userRow, userCol = map(int, input().split())
	# validate input
	while (userRow < 0 or userRow >= n
		or userCol < 0 or userCol >= n):
		print("Oops! The row or column you entered is outside of the grid. Your row and column must be between 0 and " + str(n))
		print("Please enter a move: ")
		userRow, userCol = map(int, input().split())
	return userRow, userCol

def playgame(n, num_mines):
	printInitialBoard(n)
	userRow, userCol = getUserInput(n)
	gameBoard = Board(n, num_mines, userRow, userCol)
	move = gameBoard.open(userRow, userCol)
	gameBoard.showSol()
	gameBoard.showplayer(False)
	while(move):
		print('\n')
		gameBoard.showSol()
		gameBoard.showplayer(False)
		userRow, userCol = getUserInput(n)
		move = gameBoard.open(userRow, userCol)
		if gameBoard.checkWin():
			gameBoard.showplayer(True)
			return True
	gameBoard.showplayer(False)
	return False

def printMenu():
	print("Minesweeper 2k20")
	print("All moves should be entered as follows:")
	print("[row] [col]")
	input("Press Enter to begin!")

def main(n, num_mines):
	printMenu()
	choice = 'yes'
	while choice == 'yes':
		if playgame(n, num_mines):
			print("Congrats, you win! Would you like to play again? (yes or no)")
		else:
			print("You've opened a mine :( Better luck next time! Would you like to play again? (yes or no)")
		choice = str.lower(input())
		while choice != 'yes' and choice != 'no':
			print("Please enter 'yes' or 'no'")
			choice = str.lower(input())
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
