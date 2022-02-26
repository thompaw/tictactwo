import random


class Arty:
    def __init__(self, board):
        self.b = board

    def scanPotentialWins(self, mark):
        # rows
        moveDict = {}
        for x in range(3):
            for y in range(3):
                if self.b[x][y] != mark:
                    moveDict[(x, y)] += 1
                else: 
                    moveDict[(x, y)] = 0
        # columns
        for y in range(3):
            for x in range(3):
                if self.b[x][y] != mark:
                    moveDict[(x, y)] += 1
                else: 
                    moveDict[(x, y)] = 0
        # front diagonals
        for d in range(3):
            if self.b[d][d] != mark:
                moveDict[(d, d)] += 1
            else:
                moveDict[(d, d)] = 0
        # rear diagonals
        for d in range(2, 0, -1):
            if self.b[d][d] != mark:
                moveDict[(d, d)] += 1
            else:
                moveDict[(d, d)] = 0
        return moveDict

    def setUp(self):
        pass

    def nextMove(self):
        pass

    def artyMove(self):
        # this is the culmination, where the ai picks a spot
        xmoveDict = self.scanPotentialWins('X')
        omoveDict = self.scanPotentialWins('O')


class gameBoard:
    def __init__(self, boardin=[['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]):
        # constructor for class, holds board and makes new game if none are inputted
        self.board = boardin

    def newBoard(self):
        # funcion to return a newboard to start a new game. might be inefficient
        newb = gameBoard(boardin=[['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']])
        return newb

    def displayBoard(self):
        # iterate through one row at a time
        for y in range(3):
            # iterate through columns
            for x in range(3):
                # display the symbol, followed by a divider or a new line
                if x < 2:
                    print(self.board[y][x], end='|')
                else:
                    print(self.board[y][x])
            # can't miss those horizontal lines
            if y < 2:
                print('-----')
    
    def checkWin(self, mark):
        # Check on x axis
        count = 0
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == mark:
                    count += 1
        if count == 3:
            return mark
        # check on y axis
        count = 0
        for y in range(3):
            for x in range(3):
                if self.board[x][y] == mark:
                    count += 1
        if count == 3:
            return mark
        # check diagonals (front/rear)
        count = 0
        for i in range(3):
            if self.board[i][i] == mark:
                count += 1
        if count == 3:
            return mark
        count = 0
        for i in range(2, 0, -1):
            if self.board[i][i] == mark:
                count += 1
        if count == 3:
            return mark

        return 'N'


class ticTacGame:
    def __init__(self):
        g = gameBoard
        self.gboard = g.newBoard()

    def playerTurn(self):
        move = input("give position")
        self.gboard[move[0]][move[1]] = 'O'

    def aiTurn(self):
        arty = Arty(self.gboard)

    def playGame(self):
        gameWon = False
        randx = random.randint(0, 2)
        randy = random.randint(0, 2)
        self.gboard[randx, randy] = 'X'
        while not gameWon:
            self.gboard.displayBoard()
            self.playerTurn()
            self.aiTurn()
            res = self.gboard.checkWin()
            if res != 'N':
                gameWon = True
                print(f'{res} Won !')
                break


