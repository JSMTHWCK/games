import copy
import random as rng
class lastMinute:
    def __init__(self,player):
        self.player = player

    def next_turn_end(self,board):
        for index in range(0,6):
            for i in range(5,-1,-1):
                new_board = copy.deepcopy(board)
                if new_board[i][index] == 0:
                    new_board[i][index] = self.player
                    if self.is_end(new_board) != False:
                        return index
                new_board = copy.deepcopy(board)
                if new_board[i][index] == 0:
                    new_board[i][index] = [0,2,1][self.player]
                    if self.is_end(new_board) != False:
                        return index


    def is_end(self,board):
        #horizontal
        for row in range(0,6):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                    return str(last_piece)
        #vertical
        for row in range(0,3):
            for col in range(0,7):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                    return str(last_piece)
        #diagonal (\)
        for row in range(0,3):
            for col in range(0,4):
                last_piece = board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                    return str(last_piece)
        #diagonal (/)
        for row in range(5,2,-1):
            for col in range(0,4):
                last_piece == board[row][col]
                if last_piece == 0:
                    continue
                elif last_piece == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                    return str(last_piece)
        for row in board:
            if 0 in row:
                return False
        return 'Tie'

    def choose_move(self,board):
        possible_move = self.next_turn_end(board)
        if possible_move != None:
            return possible_move
        open_spaces = [0,1,2,3,4,5,6]
        while True:
            i = rng.choice(open_spaces)
            #print('board:',board)
            #print('open_spaces:', open_spaces)
            #print('i:', i)
            if board[0][i] == 0:
                #print('chosen:', i)
                return i
            open_spaces.remove(i)
