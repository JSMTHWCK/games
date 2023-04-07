import random as rng
class random:
    def __init__(self,gamenum = None):
        if gamenum != None:
            rng.seed(gamenum)
    def choose_move(self,board):
        open_spaces = [0,1,2,3,4,5,6]
        while True:
            i = rng.choice(open_spaces)
            #print('board:',board)
            #print('open_spaces:', open_spaces)
            #print('i:', i)
            if board[0][i] == 0:
                #print('chosen:', i)
                return i
            open_spaces.remove(i)
