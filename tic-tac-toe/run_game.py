from tic_tac_toe import *
score = {'Player 1' : 0, 'Player 2' : 0, 'Tie' : 0}
score2 = {'Player 1' : 0, 'Player 2':0, 'Tie':0}

for i in range(0,10000):
    #print(i)
    a = Game(Strategies('custom'),Strategies('random'))
    b = Game(Strategies('random'),Strategies('custom'))
    score[a.game()] += 1
    score2[b.game()] += 1

print('where player 1 is custom ', score)
print('where player 2 is custom', score2)
