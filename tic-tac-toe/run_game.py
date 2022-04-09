from tic_tac_toe import *
score = {'Player 1' : 0, 'Player 2' : 0, 'Tie' : 0}
for i in range(0,10000):
    #print(i)
    a = Game(Strategies('custom'),Strategies('random'))
    score[a.game()] += 1
print(score)
