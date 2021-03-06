from helpers import *

class custom:
    def __init__(self):
        self.corners = [0,2,6,8]
        self.edges = [1,3,5,7]
        self.middle = [4]
        self.start = True
    def choose_move(self,board):
        if self.start == True: #if it's players first turn
            self.p_turn = 1 if board == [0 for i in board] else 2 #player 1 or 2
        if self.p_turn == 1 and self.start == True:
            self.start = False
            return 8 #takes corner
        if self.p_turn == 2 and self.start == True:
            self.start = False
            if board[4] == 0:
                return 4
            else:
                return 8
        '''-------------- set = 1 ended ----------------'''
        if self.p_turn == 1 and len(possible_moves(board)) == 9 - 2:
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
        if self.p_turn == 2 and len(possible_moves(board)) == 9 - 3:
            if len(is_almost_end(board)[0]) == 0:
                for i in possible_moves(board):
                    if i in self.corners:
                        return i
        '''-------------- set = 2 ended ----------------'''
      #print(self.p_turn)
        if self.p_turn == 1:
            if len(is_almost_end(board)[0]) != 0:
                return is_almost_end(board)[0][0]
            elif len(is_almost_end(board)[1]) != 0:
                return is_almost_end(board)[1][0]
            for corner in self.corners:
                if board[corner] == 0:
                    return corner
            else:
                return possible_moves(board)[0]
        if self.p_turn == 2:
            if len(is_almost_end(board)[1]) != 0:
                return is_almost_end(board)[1][0]
            elif len(is_almost_end(board)[0]) != 0:
                return is_almost_end(board)[0][0]
            for corner in self.corners:
                if board[corner] == 0:
                    return corner
            else:
                return possible_moves(board)[0]