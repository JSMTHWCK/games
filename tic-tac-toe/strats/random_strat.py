
from helpers import *
import random as rng
class RandomMove:
    def choose_move(self,board):
        poss_moves = possible_moves(board)
        a = rng.randint(0,len(poss_moves)-1)
        return poss_moves[a]