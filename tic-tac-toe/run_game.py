from tic_tac_toe import *
import custom_strat
from random_strat import random_move
import ben
from elias import elias
from manual import manual_move
from smthwck import jeff
from player import Player
score = {'Player 1' : 0, 'Player 2' : 0, 'Tie' : 0}
score2 = {'Player 1' : 0, 'Player 2':0, 'Tie':0}
past = {}
strat = 1
for i in range(0,50000):
    if i%1000 == 0:
        print(i)
    a = Game(Player(jeff),Player(elias))
    b = Game(Player(elias),Player(jeff))
    score[a.game()] += 1
    score2[b.game()] += 1
print('where player 1 is jeffrey ', score)
print('where player 1 is random ', score2)
