from tic_tac_toe import *
import custom_strat
import random_strat
import ben
import elias

score = {'Player 1' : 0, 'Player 2' : 0, 'Tie' : 0}
score2 = {'Player 1' : 0, 'Player 2':0, 'Tie':0}


for i in range(0,1000):
    a = Game(custom_strat.custom(),random_strat.random())
    b = Game(random_strat.random(),custom_strat.custom())
    score[a.game()] += 1
    score2[b.game()] += 1
print('where player 1 is jeffrey ', score)
print('where player 1 is random ', score2)

