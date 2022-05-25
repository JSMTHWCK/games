from strat_custom import *
from strat_input import *
from strat_random import *
from c_four import *

str_custom = custom()
str_random = random()


outcomes = {'Tie ':0, '1' : 0, '2' : 0}

a = Game(str_custom,str_random)
for i in range(100):
    a.game(log = True)