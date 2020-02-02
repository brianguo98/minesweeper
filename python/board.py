import random

# Minesweeper


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
        self.cellsRemaining = n*n
        self.dimension = n
        self.playerBoard = [[Cell() for x in range(n)] for y in range(n)]
        self.solutionBoard = self.setSolBoard([[Cell() for x in range(n)] for y in range(n)], self.dimension, num_mines)

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
        # calculate adjacent mines for cells with them
        for row in range(n):
            for col in range(n):
                numAdj = self.countAdjacent(board, row, col)
                if not board[row][col].isMine:
                    if numAdj == 0:
                        board[row][col].state = '-'
                    else:
                        board[row][col].state = numAdj
        return board

    def countAdjacent(self, board, row, col):
        counter = 0
        for (adjRow, adjCol) in self.getAdjacent(row, col):
            if (0 <= adjRow and adjRow < self.dimension
                and 0 <= adjCol and adjCol < self.dimension
                and board[adjRow][adjCol].isMine):
                counter += 1
        return counter

    def getAdjacent(self, row, col):
        adjacent = []
        surround = [(-1, -1), (-1, 0), (-1, 1),
                    (0,-1),            (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
        for (adjRow, adjCol) in surround:
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
            # check that the adjacent cell is in the grid, not a mine, and hasn't been visited yet
            if (0 <= adjRow and adjRow < self.dimension
                and 0 <= adjCol and adjCol < self.dimension
                and not self.solutionBoard[adjRow][adjCol].isMine
                and not visited[adjRow][adjCol]):
                # set to appropriate state
                self.playerBoard[adjRow][adjCol] = self.solutionBoard[adjRow][adjCol]
                # recursive call
                self.autoOpen(adjRow, adjCol, visited)


    def open(self, row, col):
        if self.playerBoard[row][col].state == 'X':
            if self.solutionBoard[row][col].isMine:
                self.playerBoard[row][col].placeMine()
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
        # print('Mines remaining: ' + str(self.minesRemaining))
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
        numLeft = 0
        for row in range(0, self.dimension):
            for col in range(0, self.dimension):
                if self.playerBoard[row][col].state == 'X':
                    numLeft += 1
        if numLeft == self.num_mines:
            return True
        return False

    def showPlayerBoard(self):
        # print('Mines remaining: ' + str(self.minesRemaining))
        print('  ', end='')
        for rowMarker in range(self.dimension):
            print(rowMarker, end='')
            print(' ', end='')
        print('\n')
        for row in range(self.dimension):
            print(row, end='')
            print(' ', end='')
            for col in range(self.dimension):
                print(self.playerBoard[row][col].state, end='')
                print(' ', end='')
            print('\n')