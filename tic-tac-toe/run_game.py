#type: ignore

from tic_tac_toe import *
import sys
from tree_minimax import minimax
from tree_minimax import tic_tac_toe_heuristic
sys.path.append(sys.path[0] + '/strats')
from custom_strat import custom
from random_strat import RandomMove
from ben import Ben
from elias import Elias
from manual import manual_move
from smthwck import jeff
from celeste import Celeste
from christine import christine


score = {'heuristic':0,'minimax':0,'Tie':0}

for i in range(0,20):
    print(i)
    if i%2 == 0:
        a = Game(tic_tac_toe_heuristic(1,2),minimax(2))
        player_order = {'Tie': 'Tie', 'Player 1': 'heuristic', 'Player 2': 'minimax'}
    else:
        a = Game(minimax(1),tic_tac_toe_heuristic(2,2))
        player_order = {'Tie': 'Tie', 'Player 1': "minimax", 'Player 2': 'heuristic'}
    score[player_order[a.game()]] += 1
print(score)

score = {'heuristic':0,'random':0,'Tie':0}

for i in range(0,20):
    print(i)
    if i%2 == 0:
        a = Game(tic_tac_toe_heuristic(1,2),RandomMove())
        player_order = {'Tie': 'Tie', 'Player 1': 'heuristic', 'Player 2': 'random'}
    else:
        a = Game(RandomMove(),tic_tac_toe_heuristic(2,2))
        player_order = {'Tie': 'Tie', 'Player 1': "random", 'Player 2': 'heuristic'}
    score[player_order[a.game()]] += 1
print(score)
