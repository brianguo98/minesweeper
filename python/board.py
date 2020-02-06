import random

UNDERLINE = '\033[4m'
END = '\033[0m'

# Minesweeper by Brian Guo
def getAdjacent(row, col, dimension):
        adjacent = []
        surround = [(-1, -1), (-1, 0), (-1, 1),
                    (0,-1),            (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
        for (adjRow, adjCol) in surround:
            # if within bounds of the board
            if (0 <= row+adjRow and row+adjRow < dimension
                and 0 <= col+adjCol and col+adjCol < dimension):
                adjacent.append(((row+adjRow), (col+adjCol)))
        return adjacent

def countAdjacentMines(board, row, col, dimension):
        counter = 0
        for (adjRow, adjCol) in getAdjacent(row, col, dimension):
            # if location is within grid and has a mine
            if board[adjRow][adjCol].isMine:
                counter += 1
        return counter

def printColMarker(dimension):
    for colMarker in range(dimension):
        print(UNDERLINE + str(colMarker) + END, end='')
        if colMarker < 10:
            print('  ', end='')
        else:
            print(' ', end='')

class Cell:
    def __init__(self, state='X', isMine=False):
        self.state = state
        self.isMine = isMine
    def placeMine(self):
        self.isMine = True
        self.state = 'M'

class Board:
    def __init__(self, n, num_mines, firstRow=0, firstCol=0):
        self.num_mines = num_mines
        self.dimension = n
        # player is what the user sees when playing
        self.player = [[Cell() for x in range(n)] for y in range(n)]
        # solution is under the hood
        self.solution = self.setSolBoard([[Cell() for x in range(n)] for y in range(n)], n, num_mines, firstRow, firstCol)

    def setSolBoard(self, board, n, num_mines, firstRow, firstCol):
        # generate 10 mine locations.
        mineLocations = set()
        while len(mineLocations) < num_mines:
            mineRow, mineCol = random.randint(0, n-1), random.randint(0, n-1)
            # repeat random generation if mine already exists or it's the user's first move
            while ((mineRow, mineCol) in mineLocations or
                   (mineRow == firstRow and mineCol == firstCol and n > 1)):
                mineRow, mineCol = random.randint(0, n-1), random.randint(0, n-1)
            mineLocations.add((mineRow, mineCol))
        # place randomly generated mines on solution board
        for mineLoc in mineLocations:
            board[mineLoc[0]][mineLoc[1]].placeMine()
        # set adjacent counts for cells on solution board
        for row in range(n):
            for col in range(n):
                numAdj = countAdjacentMines(board, row, col, n)
                if not board[row][col].isMine:
                    if numAdj == 0:
                        board[row][col].state = '.'
                    else:
                        board[row][col].state = numAdj
        return board

    def autoOpen(self, row, col, visited):
        # DFS recursive function to automatically open neighboring cells
        # base case 1, we've already been to this cell
        if visited[row][col]:
            return
        # base case 2, this cell has mines adjacent to it, can't go any furthur, backtrack
        if self.solution[row][col].state != '.':
            self.player[row][col].state = self.solution[row][col].state
            return
        visited[row][col] = True
        # for every cell adjacent to the current cell
        for (adjRow, adjCol) in getAdjacent(row, col, self.dimension):
            # check that the adjacent cell is not a mine and hasn't been visited yet
            if (not self.solution[adjRow][adjCol].isMine
                and not visited[adjRow][adjCol]):
                # set to corresponding state on solution board
                self.player[adjRow][adjCol] = self.solution[adjRow][adjCol]
                # recursive call
                self.autoOpen(adjRow, adjCol, visited)


    def open(self, row, col):
        # do nothing if cell already opened
        if self.player[row][col].state == 'X':
            if self.solution[row][col].isMine:
                self.player[row][col].placeMine()
                # game over!
                return False
            else:
                # open cell with no adjacent mines and any others around it
                if self.solution[row][col].state == '.':
                    self.player[row][col].state = '.'
                    self.autoOpen(row, col, [[False for x in range(self.dimension)] for y in range(self.dimension)])
                # open cell with adjacent mines
                else:
                    self.player[row][col].state = self.solution[row][col].state
        return True

    def checkWin(self):
        # if number of uncovered cells matches the number of mines, winner winner
        numLeft = 0
        for row in range(0, self.dimension):
            for col in range(0, self.dimension):
                if self.player[row][col].state == 'X' or self.player[row][col].state == 'M':
                    numLeft += 1
        if numLeft == self.num_mines:
            return True
        return False

    def showplayer(self, withMines):
        # it's not always pretty
        print('\n   ', end='')
        printColMarker(self.dimension)
        print('\n')
        for row in range(self.dimension):
            print(UNDERLINE + str(row) + END, end='')
            if row < 10:
                print('  ', end='')
            else:
                print(' ', end='')
            for col in range(self.dimension):
                if withMines and self.solution[row][col].isMine:
                    print('M', end='')
                else:
                    print(self.player[row][col].state, end='')
                print('  ', end='')
            print(UNDERLINE + str(row) + END, end='')
            print('\n')
        print('   ', end='')
        printColMarker(self.dimension)
        print('\n')
