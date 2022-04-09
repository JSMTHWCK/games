import random as rng
import tic_tac_toe
class Strategies:
    def __init__(self,strat_type):
        #methods
        self.types = {'random':self.random, 'custom':self.custom}
        self.strat_type = strat_type
        #turns and indicators
        self.start = True
        self.corners = [0,2,6,8]
        self.edges = [1,3,5,7]
        self.middle = [4]

    def is_end_copy(self,board):
        for i in range(0,3):
            if board[3*i + 0] == board[3*i + 1] == board[3*i + 2] != 0:
                return "Player " + str(board[3*i + 0])
            if board[0 + i] == board[3 + i] == board[6 + i] != 0:
                return "Player " + str(board[0+i])

        if board[0] == board[4] == board[8] != 0:
            return "Player " + str(board[0])
        if board[2] == board[4] == board[6] != 0:
            return "Player " + str(board[2])

        if 0 not in board:
            return 'Tie'
        return False

    def possible_moves(self,board):
        empty_spaces = []
        for i in range(0,len(board)):
            if board[i] == 0:
                empty_spaces.append(i)
        return empty_spaces
        
    def is_almost_end(self,board):
        empty_spaces = self.possible_moves(board)
        p_one = []
        p_two = []
        ends = [p_one,p_two]
        #player 1's turn
        for b in range(1,3):
            for i in empty_spaces:
                tboard = list(board)
                tboard[i] = b
                if self.is_end_copy(tboard) not in ['Tie',False]:
                    ends[b-1].append(i)
        return ends

        #still more left
    def random(self,board):
        poss_moves = self.possible_moves(board)
        a = rng.randint(0,len(poss_moves)-1)
        return poss_moves[a]



    def custom(self,board):
        #for player 1 only
        if self.start == True: #if it's players first turn
            self.p_turn = 1 if board == [0 for i in board] else 2 #player 1 or 2
        if self.p_turn == 1 and self.start == True:
            self.start = False
            return 8 #takes corner
        '''-------------- player 1 turn 1 ended ----------------'''
        if self.p_turn == 1 and len(self.possible_moves(board)) == 9 - 2:
            i = board.index(self.p_turn+1)
            if i in self.middle:
                return 0
            elif i in self.corners:
                if i + board.index(1) == 8:
                    return 2
                else:
                    return 8 - i
            elif i in self.edges:
                return 4
        '''-------------- player 1 turn 2 ended ----------------'''

        if len(self.is_almost_end(board)[0]) != 0:
            return self.is_almost_end(board)[0][0]
        elif len(self.is_almost_end(board)[1]) != 0:
            return self.is_almost_end(board)[1][0]
        for corner in self.corners:
            if board[corner] == 0:
                return corner
