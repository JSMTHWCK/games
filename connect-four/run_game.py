from strat_custom import *
from strat_input import manual as manual
from strat_random import *
from c_four import *

str_custom = custom()
str_random = random()


outcomes = {'Tie':0, '1' : 0, '2' : 0}

a = Game(str_random,str_random)
a.game(log=True)