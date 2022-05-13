import random as rng
class Player:
    def __init__(self,strat):
        self.strat = strat
        self.types = {'manual': self.manual,'random':self.random}
    def manual(self,board):
        a = input()
        while a not in ['0','1','2','3','4','5','6']:
            print("invalid input, please choose 0 - 6 (indexed at 0)")
            a = input()
        return a     
    def random(self,board):
        open_spaces = ['0','1','2','3','4','5','6']
        while True:
            a = rng.randint(0,len(open_spaces)-1)
            if board[0] == 0:
                return a
            open_spaces.pop(a)
