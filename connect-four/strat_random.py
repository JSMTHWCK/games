import random as rng
class random:
    def choose_move(self,board):
        open_spaces = ['0','1','2','3','4','5','6']
        while True:
            a = rng.randint(0,len(open_spaces)-1)
            if board[0][int(open_spaces[a])] == 0:
                return a
            open_spaces.pop(a)
