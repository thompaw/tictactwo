import random


symbol_list = ['X', 'O']
blank_template = [['+', '+', '+'], 
                  ['+', '+', '+'], 
                  ['+', '+', '+']]


def dictToBoard(indict, mark=None):
    endboard = [[0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]]
    # check if open or taken dict
    if mark == None:
        for key in indict.keys():
            xcoord = int(str(key)[0])
            ycoord = int(str(key)[1])
            endboard[xcoord][ycoord] += 1
    else: 
        for key in indict[mark].keys():
            xcoord = int(str(key)[0])
            ycoord = int(str(key)[1])
            endboard[xcoord][ycoord] += 1
    return endboard

class gameBoard:
    def __init__(self, boardin=blank_template):
        # constructor for class, holds board and makes new game if none are inputted
        self.board = boardin

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
        for mark in symbol_list:
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
        pass


    def setUp(self):
        pass

    def artyMove(self):
        # this is the culmination, where the ai picks a spot
        # 1. scan for potential wins and shut down/win where possible
        pass  

        
        
        


class ticTacGame:
    def __init__(self):
        self.gboard = gameBoard()

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
