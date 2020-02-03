import random

# Minesweeper by Brian Guo

class Cell:
    def __init__(self, state='X', isMine=False):
        self.state = state
        self.isMine = isMine
    def placeMine(self):
        self.isMine = True
        self.state = 'M'

class Board:
    def __init__(self, n, num_mines):
        self.num_mines = num_mines
        self.dimension = n
        self.playerBoard = [[Cell() for x in range(n)] for y in range(n)]
        self.solutionBoard = self.setSolBoard([[Cell() for x in range(n)] for y in range(n)], n, num_mines)

    def setSolBoard(self, board, n, num_mines): 
        sequence = [i for i in range(n*n)]
        mineLocations = set(random.sample(sequence, num_mines))
        counter = 0
        # set randomized mine locations
        for row in range(n):
            for col in range(n):
                if counter in mineLocations:
                    board[row][col].placeMine()
                counter += 1
        # for each cell, calculate adjacent cells and update board
        for row in range(n):
            for col in range(n):
                numAdj = self.countAdjacentMines(board, row, col)
                if not board[row][col].isMine:
                    if numAdj == 0:
                        board[row][col].state = '-'
                    else:
                        board[row][col].state = numAdj
        return board

    def getAdjacentX(self, board, row, col):
        xList = []
        for (adjRow, adjCol) in self.getAdjacent(row, col):
            # if location is within grid and has a mine
            if board[adjRow][adjCol].state == 'X':
                xList.append((adjRow, adjCol))
        return xList

    def countAdjacentMines(self, board, row, col):
        counter = 0
        for (adjRow, adjCol) in self.getAdjacent(row, col):
            # if location is within grid and has a mine
            if board[adjRow][adjCol].isMine:
                counter += 1
        return counter

    def getAdjacent(self, row, col):
        adjacent = []
        surround = [(-1, -1), (-1, 0), (-1, 1),
                    (0,-1),            (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
        for (adjRow, adjCol) in surround:
            if (0 <= row+adjRow and row+adjRow < self.dimension
                and 0 <= col+adjCol and col+adjCol < self.dimension):
                adjacent.append(((row+adjRow), (col+adjCol)))
        return adjacent

    def autoOpen(self, row, col, visited):
        # DFS recursive function to automatically open neighboring cells
        # base case 1, we've already been to this cell
        if visited[row][col]:
            return
        # base case 2, this cell has mines adjacent to it, can't go any furthur, must backtrack
        if self.solutionBoard[row][col].state != '-':
            self.playerBoard[row][col].state = self.solutionBoard[row][col].state
            return
        visited[row][col] = True
        # for every cell adjacent to the current cell
        for (adjRow, adjCol) in self.getAdjacent(row, col):
            # check that the adjacent cell is not a mine and hasn't been visited yet
            if (not self.solutionBoard[adjRow][adjCol].isMine
                and not visited[adjRow][adjCol]):
                # set to corresponding state on solution board
                self.playerBoard[adjRow][adjCol] = self.solutionBoard[adjRow][adjCol]
                # recursive call
                self.autoOpen(adjRow, adjCol, visited)


    def open(self, row, col):
        # do nothing if cell already opened
        if self.playerBoard[row][col].state == 'X':
            if self.solutionBoard[row][col].isMine:
                self.playerBoard[row][col].placeMine()
                # game over!
                return False
            else:
                if self.solutionBoard[row][col].state == '-':
                    self.playerBoard[row][col].state = '-'
                    self.autoOpen(row, col, [[False for x in range(self.dimension)] for y in range(self.dimension)])
                else:
                    self.playerBoard[row][col].state = self.solutionBoard[row][col].state
            return True
        return True

    def showSol(self):
        print('  ', end='')
        for rowMarker in range(self.dimension):
            print(rowMarker, end='')
            print(' ', end='')
        print('\n')
        for row in range(self.dimension):
            print(row, end='')
            print(' ', end='')
            for col in range(self.dimension):
                print(self.solutionBoard[row][col].state, end='')
                print(' ', end='')
            print('\n')

    def checkWin(self):
        # if number of uncovered cells matches the number of mines, winner winner
        numLeft = 0
        for row in range(0, self.dimension):
            for col in range(0, self.dimension):
                if self.playerBoard[row][col].state == 'X' or self.playerBoard[row][col].state == 'M':
                    numLeft += 1
        if numLeft == self.num_mines:
            return True
        return False

    def showPlayerBoard(self, withMines):
        print('  ', end='')
        for rowMarker in range(self.dimension):
            print(rowMarker, end='')
            print(' ', end='')
        print('\n')
        for row in range(self.dimension):
            print(row, end='')
            print(' ', end='')
            for col in range(self.dimension):
                if withMines and self.solutionBoard[row][col].isMine:
                    print('M', end='')
                else:
                    print(self.playerBoard[row][col].state, end='')
                print(' ', end='')
            print('\n')