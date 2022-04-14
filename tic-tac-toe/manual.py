from random import randrange

def manual(self, board):
    print('choose location ')
    x = int(input())
    while board[x] != 0:
        print('invalid move, choose again')
        x = int(input())
    return x