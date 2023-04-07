#type: ignore
import sys
from c_four import *
from c_four_minimax import *

sys.path.append(sys.path[0] + '/strats')
from strat_custom import *
from strat_input import manual as manual
from strat_random import *
from strat_lastminute import *


outcomes = {'Tie':0, 'mini' : 0, 'last' : 0}
mini_wins = {'1':0,'2':0}
fails = 0
# a = Game(str_minimax,str_custom)
# a.game(log = True)
# print("SPACE")


for i in range(0,2):
    minimax_ply_2 = minimaxHeuristic(1,2)
    minimax_ply_4 = minimaxHeuristic(2,4)

    if i%2 == 0:
        minimax_ply_2.player = 1
        minimax_ply_4.player = 2
        a = Game(minimax_ply_2,minimax_ply_4)
    else:
        minimax_ply_4.player = 1
        minimax_ply_2.player = 2
        a = Game(minimax_ply_4,minimax_ply_2)
    
    print("i is ", i)
    print(a.game(log=True))
    

# for i in range(0,10):
#     #str_custom = custom()
#     str_random = random()
#     str_manual = manual()
#     if i%2 == 0:
#         str_lastminute = lastMinute(1)
#         str_minimax_2 = minimaxHeuristic(2,3)
#         a = Game(str_lastminute, str_minimax_2)
#         order = {'Tie':'Tie', 2: 'mini', 1:'last'}
#     else:
#         str_lastminute2 = lastMinute(2)
#         str_minimax = minimaxHeuristic(1,3)
#         a = Game(str_minimax,str_lastminute2)
#         order = {'Tie':'Tie', 1: 'mini', 2:'last'}
#     turn_winner = a.game()

#     if turn_winner != 'Tie':
#         print("game " + str(i) + " winner is " + order[int(turn_winner)])
#     if turn_winner == "Tie":
#         outcomes['Tie'] += 1
#     else:
#         player_winner = order[int(turn_winner)]
#         outcomes[player_winner] += 1
#         if player_winner == 'mini':
#             mini_wins[str(i%2 + 1)] += 1

# print(outcomes)
# print(mini_wins)
# print(fails)