from strat_custom import *
from strat_input import *
from strat_random import *
from c_four import *

str_custom = custom()
str_random = random()


outcomes = {'Tie ':0, '1' : 0, '2' : 0}

for i in range(1000):
    a = Game(str_custom,str_random)
    outcomes[a.game()] += 1

outcomes2 = {'Tie':0, '1' : 0, '2':0}
for i in range(1000):
    a = Game(str_random,str_custom)
    outcomes2[a.game()] += 1


print(outcomes)
print(outcomes2)