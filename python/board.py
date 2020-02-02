import random

# Minesweeper


class Cell:
    def __init__(self, isMine=False):
        self.state = 'X'
        self.isMine = isMine
    def placeMine(self):
        self.isMine = True


def placeMines(board, n, num_mines): 
    '''randomly assigns num_mines mines to the n*n board'''
    sequence = [i for i in range(n*n)]
    mineLocations = set(random.sample(sequence, num_mines))
    counter = 0
    for row in range(n):
        for col in range(n):
            if counter in mineLocations:
                board[row][col].placeMine()
            counter += 1
    return board

class Board:
    def __init__(self, n, num_mines):
        self.num_mines = num_mines
        self.cellsRemaining = n
        self.n = n
        self.board = placeMines([[Cell() for x in range(n*n)] for y in range(n*n)], n, num_mines)
    
    def countAdjacent(self, row, col):
        counter = 0
        for (adjRow, adjCol) in self.getAdjacent(row, col):
            if (0 <= adjRow and adjRow < self.n
                and 0 <= adjCol and adjCol < self.n
                and self.board[adjRow][adjCol].isMine):
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

    def open(self, row, col):
        if self.board[row][col].isMine:
            self.board[row][col].state = 'M'
            return (False, False)
        else:
            numAdj = self.countAdjacent(row, col)
            if numAdj == 0:
                self.board[row][col].state = '-'
            else:
                self.board[row][col].state = numAdj
            self.cellsRemaining -= 1
            if self.cellsRemaining == self.num_mines:
                return (True, True)
        return (True, False)

    def show(self):
        # print('Mines remaining: ' + str(self.minesRemaining))
        print('  ', end='')
        for rowMarker in range(self.n):
            print(rowMarker, end='')
            print(' ', end='')
        print('\n')
        for row in range(self.n):
            print(row, end='')
            print(' ', end='')
            for col in range(self.n):
                print(self.board[row][col].state, end='')
                print(' ', end='')
            print('\n')


    # TODO: Write interface
