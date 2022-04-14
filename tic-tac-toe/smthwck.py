from helpers import *
past = {}
strat = 1
def jeff(board):
    corners = [0,2,6,8]
    edges = [1,3,5,7]
    middle = [4]
    p_turn = 1 if len(possible_moves(board))%2 == 1 else 2
    if len(past) >= 5:
        lost_game = [k for k,v in past.items() if v == 'Loss']
        if len(lost_game) * 5 < len(past):
            print('strat switched')
            strat = 2

    if p_turn == 1:
        if len(possible_moves(board)) == 9 and strat == 1:
            return 8 #takes corner
        elif len(possible_moves(board)) == 9 and strat == 2:
            return 4
    if p_turn == 2 and len(possible_moves(board)) == 8:
        if board[4] == 0:
            return 4
        else:
            return 8
    '''-------------- set = 1 ended ----------------'''
    if p_turn == 1 and len(possible_moves(board)) == 9 - 2:
        if strat == 1:
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
        if strat == 2:
            a = find_all(2,board)[0] 
            if a < 3:
                if i in edges:
                    return 0
                else:
                   return 8 - i 
            elif a < 6:
                if a == 5:
                    return 8
                elif a == 3:
                    return 6
            
    if p_turn == 2 and len(possible_moves(board)) == 9 - 3:
        if len(is_almost_end(board)[0]) == 0:
            for i in possible_moves(board):
                if i in corners:
                    return i
    '''-------------- set = 2 ended ----------------'''
    #print(p_turn)
    if p_turn == 1:
        if len(is_almost_end(board)[0]) != 0:
            return is_almost_end(board)[0][0]
        elif len(is_almost_end(board)[1]) != 0:
            return is_almost_end(board)[1][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]
    if p_turn == 2:
        if len(is_almost_end(board)[1]) != 0:
            return is_almost_end(board)[1][0]
        elif len(is_almost_end(board)[0]) != 0:
            return is_almost_end(board)[0][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]