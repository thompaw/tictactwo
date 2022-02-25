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
        
