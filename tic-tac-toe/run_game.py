from tic_tac_toe import *
import custom_strat
from random_strat import random_move
from ben import ben
from elias import elias
from manual import manual_move
from smthwck import jeff
from player import Player
from celeste import celeste
from christine import christine
'''
outcomes = {'jeff' : 0, 'celeste' : 0, 'Tie' : 0}
past = {}
strat = 1
for i in range(0,200):
    if i%1000 == 0:
        print(i)
    if i%2 == 0:
        a = Game(Player(jeff),Player(strategy_function))
        player_order = {'Tie': 'Tie', 'Player 1': 'jeff', 'Player 2': 'celeste'}
    else:
        a = Game(Player(strategy_function),Player(jeff))
        player_order = {'Tie': 'Tie', 'Player 1': "celeste", 'Player 2': 'jeff'}
    outcomes[player_order[a.game()]] += 1
print(outcomes)
'''

score = {'Player 1':0,'Player 2':0,'Tie':0}
score2 = {'Player 1' : 0, 'Player 2':0,'Tie':0}

for i in range(0,100):
    a = Game(Player(jeff),Player(random_move))
    b = Game(Player(random_move),Player(jeff))

    score[a.game(log = True)] += 1
    score2[b.game(log = True)] += 1


print(score)
print(score2)