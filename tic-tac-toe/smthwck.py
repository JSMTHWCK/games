from helpers import *

def jeff(board):
    corners = [0,2,6,8]
    edges = [1,3,5,7]
    middle = [4]
    almost_end = is_almost_end(board)
    p_turn = 1 if len(possible_moves(board))%2 == 1 else 2
    if p_turn == 1:
        if len(possible_moves(board)) == 9:
            return 8
    if p_turn == 2 and len(possible_moves(board)) == 8:
        if board[4] == 0:
            return 4
        else:
            return 8
    '''-------------- set = 1 ended ----------------'''
    if p_turn == 1 and len(possible_moves(board)) == 9 - 2:
        i = board.index(p_turn+1)
        if i in middle:
            return 0
        elif i in corners:
            if i + board.index(1) == 8:
                return 2
            else:
                return 8 - i
        elif i in edges:
            return 4
            
    if p_turn == 2 and len(possible_moves(board)) == 9 - 3:
        if len(almost_end[0]) == 0:
            for i in possible_moves(board):
                if i in corners:
                    return i
    '''-------------- set = 2 ended ----------------'''
    #print(p_turn)
    if p_turn == 1:
        if len(almost_end[0]) != 0:
            return almost_end[0][0]
        elif len(almost_end[1]) != 0:
            return almost_end[1][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]
    if p_turn == 2:
        if len(almost_end[1]) != 0:
            return almost_end[1][0]
        elif len(almost_end[0]) != 0:
            return almost_end[0][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]