class gameBoard:
    def __init__(self, boardin=[['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]):
        self.board = boardin

    def newBoard(self):
        newb = gameBoard(boardin=[['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']])
        return newb

    def displayBoard(self):
        for y in range(3):
            for x in range(3):
                if x < 2:
                    print(self.board[y][x], end='|')
                else:
                    print(self.board[y][x], end='')
            print()
            if y < 2:
                print('-----')
    
    def checkWin(self):
        pass


class ticTacGame:
    def __init__(self):
        pass