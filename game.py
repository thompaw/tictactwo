class gameBoard:
    def __init__(self, playermoves, aimoves):
        self.player_movelist = playermoves
        self.ai_movelist = aimoves

    def newBoard(self):
        newb = gameBoard(playermoves=[], aimoves=[])
        return newb

    def displayBoard(self):
        for y in range(3):
            for x in range(3):
                if x < 2:
                    print('x', end='|')
                else:
                    print('x', end='')
            print()
            if y < 2:
                print('-----')
    
    def checkWin(self):
        pass


class ticTacGame:
    def __init__(self):
        pass