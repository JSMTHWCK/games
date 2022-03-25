import random as rng

class Strategies:
    def __init__(self,strat_type):
        self.types = {'random':self.random}
        self.strat_type = strat_type
        
    def random(self,board):
        poss_moves = []
        for i in range(0,len(board)):
            if board[i] == 0:
                poss_moves.append(i)
        a = rng.randint(0,len(poss_moves)-1)
        return poss_moves[a]