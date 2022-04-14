from tic_tac_toe import *
import custom_strat
from random_strat import random_move
from ben import ben
from elias import elias
from manual import manual_move
from smthwck import jeff
from player import Player
outcomes = {'Jeffrey' : 0, 'ben' : 0, 'Tie' : 0}
past = {}
strat = 1
for i in range(0,2):
    if i%1000 == 0:
        print(i)
    if i%2 == 0:
        a = Game(Player(jeff),Player(ben))
        player_order = {'Tie': 'Tie', 'Player 1': 'Jeffrey', 'Player 2': 'ben'}
    else:
        a = Game(Player(ben),Player(jeff))
        player_order = {'Tie': 'Tie', 'Player 1': "ben", 'Player 2': 'Jeffrey'}
    outcomes[player_order[a.game(log = True)]] += 1
print(outcomes)