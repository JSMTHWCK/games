from tic_tac_toe import *
import sys
from tree_minimax import minimax
sys.path.append(sys.path[0] + '/strats')
from custom_strat import custom
from random_strat import RandomMove as RM
from ben import Ben
from elias import Elias
from manual import manual_move
from smthwck import jeff
from celeste import Celeste
from christine import christine


score = {'Player 1':0,'Player 2':0,'Tie':0}
score2 = {'Player 1' : 0, 'Player 2':0,'Tie':0}

