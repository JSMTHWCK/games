from tic_tac_toe import *
import custom_strat
import random_strat
import ben

score = {'Player 1' : 0, 'Player 2' : 0, 'Tie' : 0}
score2 = {'Player 1' : 0, 'Player 2':0, 'Tie':0}


for i in range(0,10000):
    #print(i)
    a = Game(custom_strat.custom(),ben.strat1())
    b = Game(ben.strat1(),custom_strat.custom())
    score[a.game()] += 1
    score2[b.game()] += 1

a = Game(random_strat.random(), custom_strat.custom())
print('where player 1 is jeff ', score)
print('where player 1 is ben ', score2)
