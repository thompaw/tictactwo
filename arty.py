import random


symbollist = ['X', 'O']
startboard = [['+', '+', '+'], 
              ['+', '+', '+'], 
              ['+', '+', '+']]

class gameBoard:
    def __init__(self, boardin=startboard):
        # constructor for class, holds board and makes new game if none are inputted
        self.board = boardin

    def newBoard(self):
        # funcion to return a newboard to start a new game. might be inefficient
        newb = gameBoard(boardin=startboard)
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
    
    def checkWin(self):
        for mark in symbollist:
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


class ticTacGame:
    def __init__(self):
        self.gboard = gameBoard().newBoard()

    def playerTurn(self):
        truemove = False
        while not truemove:
            move = input("give position")
            playerx = int(move[0])
            playery = int(move[1])
            if self.gboard.board[playerx][playery] == 'X':
                print('You cannot move on top of arty.')
            elif self.gboard.board[playerx][playery] == 'O':
                print('You already moved there.')
            else:
                self.gboard.board[playerx][playery] = 'O'
                break


    def aiTurn(self):
        arty = Arty(self.gboard)

    def playGame(self):
        gameWon = False
        randx = random.randint(0, 2)
        randy = random.randint(0, 2)
        self.gboard.board[randx][randy] = 'X'
        while not gameWon:
            self.gboard.displayBoard()
            self.playerTurn()
            self.aiTurn()
            res = self.gboard.checkWin()
            if res != 'N':
                gameWon = True
                print(f'{res} Won !')
                self.gboard.displayBoard()
                break

# Game loop here
if __name__ == "__main__":
    ttt = ticTacGame()
    ttt.playGame()
