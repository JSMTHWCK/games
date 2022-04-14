from helpers import *
import random as rng
def random_move(board):
    poss_moves = possible_moves(board)
    a = rng.randint(0,len(poss_moves)-1)
    return poss_moves[a]

