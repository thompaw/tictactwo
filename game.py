

def display_board():
    for y in range(9):
        for x in range(9):
            if ((x + 1) % 3 == 0) and (x < 8):
                print('x', end='|')
            else:
                print('x', end='')
        print()
        if ((y + 1) % 3 == 0) and (y < 8):
            print('-----------')