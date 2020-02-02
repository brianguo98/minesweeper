from board import Board
import argparse


def getUserInput(n):
	print('Please enter a row and column in the following format:\n[row] [column]')
	userRow, userCol = map(int, input().split())
	# validate input
	while (userRow < 0 or userRow >= n
		or userCol < 0 or userCol >= n):
		print('''
				Oops! The row or column you entered is outside of the grid. Your row and column
				must be between 0 and ''' + str(n))
		userRow, userCol = map(int, input().split())
	return userRow, userCol

def main(n, num_mines):
	print("Welcome to the greatest game ever hacked together by me!")
	gameBoard = Board(n, num_mines)
	gameBoard.showPlaya()
	userRow, userCol = getUserInput(n)
	move = gameBoard.open(userRow, userCol)
	while(move[0]):
		print('\n')
		# gameBoard.showSol()
		gameBoard.showPlaya()
		userRow, userCol = getUserInput(n)
		move = gameBoard.open(userRow, userCol)
		if move[1]:
			print("WINNER")
			break
	gameBoard.showPlaya()
	print("LOSER")

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
