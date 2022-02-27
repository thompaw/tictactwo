import random


symbollist = ['X', 'O']
blankboard = [['+', '+', '+'], 
              ['+', '+', '+'], 
              ['+', '+', '+']]


def dictToBoard(indict, mark=None):
    endboard = [[0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]]
    # check if open or taken dict
    if mark == None:
        for key in indict[mark].keys():
            xcoord = int(str(key)[0])
            ycoord = int(str(key)[1])
            endboard[xcoord][ycoord] += 1
    else: 
        for key in indict.keys():
            xcoord = int(str(key)[0])
            ycoord = int(str(key)[1])
            endboard[xcoord][ycoord] += 1
    return endboard

class gameBoard:
    def __init__(self, boardin=blankboard):
        # constructor for class, holds board and makes new game if none are inputted
        self.board = boardin

    def newBoard(self):
        # funcion to return a newboard to start a new game. might be inefficient
        newb = gameBoard(boardin=blankboard)
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
        self.board = board
        self.b = self.board.board

    def scanPotentialWins(self):
        openDict = {}
        takenDict = {'X': {}, 'O': {}}
        for mark in symbollist:
            # rows
            for x in range(3):
                for y in range(3):
                    spot = self.b[x][y]
                    if spot != '+':
                        if spot != mark:
                            takenDict[mark][(x, y)] += 1
                    else: 
                        openDict[(x, y)] = 1
            # cols
            for y in range(3):
                for x in range(3):
                    spot = self.b[x][y]
                    if spot != '+':
                        if spot != mark:
                            takenDict[mark][(x, y)] += 1
                    else: 
                        openDict[(x, y)] = 1
            # front diagonal
            for d in range(3):
                spot = self.b[d][d]
                if spot != '+':
                    if spot != mark:
                        takenDict[mark][(d, d)] += 1
                else: 
                    openDict[(d, d)] = 1 
            # rear diagonal
            for rd in range(2, 0, -1):
                spot = self.b[rd][rd]
                if spot != '+':
                    if spot != mark:
                        takenDict[mark][(rd, rd)] += 1
                else: 
                    openDict[(rd, rd)] = 1

        return openDict, takenDict


    def setUp(self):
        pass

    def artyMove(self):
        # this is the culmination, where the ai picks a spot
        # 1. scan for potential wins and shut down/win where possible
        openSpaces, takenspaces = self.scanPotentialWins()
        openboard = dictToBoard(openSpaces)
        takenboard = dictToBoard(takenspaces)
        
        
        


class ticTacGame:
    def __init__(self):
        self.gboard = gameBoard().newBoard()

    def playerTurn(self):
        truemove = False
        while not truemove:
            move = input("give position")
            playerx = int(move[0]) - 1
            playery = int(move[1]) - 1
            if self.gboard.board[playerx][playery] == 'X':
                print('You cannot move on top of arty.')
            elif self.gboard.board[playerx][playery] == 'O':
                print('You already moved there.')
            else:
                self.gboard.board[playerx][playery] = 'O'
                break


    def aiTurn(self):
        arty = Arty(self.gboard)
        arty.artyMove()

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
