import random
from strategies import *
class Player:
    def __init__(self,p_id,strat):
        self.id = p_id
        self.strat = strat

class Game:
    def __init__(self,strat1,strat2):
        self.player1 = Player(1,strat1)
        self.player2 = Player(2,strat2)
        self.players = [self.player1,self.player2]
        self.turn = 0
        self.board = [0 for i in range(0,9)]


    def is_end(self):
        for i in range(0,3):
            if self.board[3*i + 0] == self.board[3*i + 1] == self.board[3*i + 2] != 0:
                return "Player " + str(self.board[3*i + 0])
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i] != 0:
                return "Player " + str(self.board[0+i])

        if self.board[0] == self.board[4] == self.board[8] != 0:
            return "Player " + str(self.board[0])
        if self.board[2] == self.board[4] == self.board[6] != 0:
            return "Player " + str(self.board[2])

        if 0 not in self.board:
            return 'Tie'
        return False

    def make_move(self,player):
        #p_id comes through as self.player1
        pstrat = player.strat
        a = pstrat.types[pstrat.strat_type](self.board)
        if a == None:
            print(pstrat.strat_type)
            print(pstrat.types)
            print(pstrat.types[pstrat.strat_type](self.board))
            print(pstrat.types['custom'](self.board))
            print(self.board)
        self.board[a] = player.id


    def game(self,log = False):

        while True:

            if log == True:
                print(f'{self.board[0]} {self.board[1]} {self.board[2]}\n{self.board[3]} {self.board[4]} {self.board[5]}\n{self.board[6]} {self.board[7]} {self.board[8]}')
                print('')

            if self.is_end() != False:
                return self.is_end()

            p_turn = self.players[self.turn]
            self.make_move(p_turn)

            self.turn = (self.turn + 1)%2
