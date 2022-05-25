from strat_random import *
from strat_custom import *
from strat_input import *
class Player:
    def __init__(self,strat):
        self.strat = strat
        self.types = {'manual': manual.choose_move,'random':random.choose_move,'custom':custom.choose_move}

