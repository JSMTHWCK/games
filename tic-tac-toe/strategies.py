import random as rng
from tic-tac-toe import *
class Strategies:
    def __init__(self,strat_type):
        self.types = {'random':self.random, 'custom':self.custom}
        self.strat_type = strat_type
        self.start = True
        self.turn = None
        self.corners = [0,2,6,8]
        self.edges = [1,3,5,7]
        self.middle = [4]

    def possible_moves(self,board):
        empty_spaces = []
        for i in range(0,len(board)):
            if board[i] == 0:
                empty_spaces.append(i)
        return empty_spaces
    def is_almost_end(self,board):
        empty_spaces = possible_moves(board)
        p_one = []
        p_two = []
        ends = [p_one,p_two]
        #player 1's turn
        for b in range(1,3):
            for i in empty_spaces:
                tboard = board
                tboard[i] = b
                a = Game(None,None)
                a.board = tboard
                if a.is_end not in ['Tie',False]:
                    ends[b-1].append(i)
        return ends

        #still more left
    def random(self,board):
        poss_moves = possible_moves(board)
        a = rng.randint(0,len(poss_moves)-1)
        return poss_moves[a]

    def custom(self,board):
        #turn one start
        if self.start = True:
            turn = 0 if board == [0 for i in board] else 1
            self.start = False;
            if turn == 0:
                return 8
            elif turn == 1:
                if board[4] == 0:
                    return 4
                else:
                    return 8
        #turn two player 1
        if len(possible_moves(board)) == 2:
            i = board.index(2)
            if i in self.corners:
                if i != 0:
                    return 0
                else:
                    return 2
            elif i in self.edges:
                return 8 - i + 1
            elif i in middle:
                return 0
        if is_almost_end(board) != [[][]]:
            reutrn is_almost_end(board)
