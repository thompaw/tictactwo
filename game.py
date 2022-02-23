import ai

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
        check = mark
        # Check on x axis
        count = 0
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == mark:
                    count += 1
        if count == 3:
            return True
        # check on y axis
        count = 0
        for y in range(3):
            for x in range(3):
                if self.board[x][y] == mark:
                    count += 1
        if count == 3:
            return True
        # check diagonals (front/rear)
        count = 0
        for i in range(3):
            if self.board[i][i] == mark:
                count += 1
        if count == 3:
            return True
        count = 0
        for i in range(2, 0, -1):
            if self.board[i][i] == mark:
                count += 1
        if count == 3:
            return True

        return False


class ticTacGame:
    def __init__(self):
        g = gameBoard
        self.gboard = g.newBoard()

    def playerTurn(self):
        move = input("give position")
        self.gboard[move[0]][move[1]] = 'X'

    def aiTurn(self):
        arty = ai.Arty(self.gboard)

    
    def playGame():
        pass
